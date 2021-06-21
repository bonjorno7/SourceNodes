from typing import Tuple

import bpy
from bpy.props import EnumProperty, PointerProperty, StringProperty
from bpy.types import (Action, Collection, Context, Node, NodeSocketVirtual,
                       NodeTree, Object, UILayout)

from .sockets import SourceAnimationSocket, SourceGeometrySocket
from .tree import SourceNodeTree


class SourceBaseNode:
    '''Base class for Source nodes'''

    @classmethod
    def poll(cls, ntree: NodeTree) -> bool:
        '''Check whether this node can be placed in the given node tree'''
        return ntree.bl_idname == SourceNodeTree.bl_idname


class SourceDynamicNode:
    '''Mixin class for dynamic nodes'''

    def remove_unlinked_sockets(self, socket_types: Tuple[type]):
        '''Remove unlinked inputs of the given types'''
        for socket in self.inputs:
            if isinstance(socket, socket_types) and not socket.is_linked:
                self.inputs.remove(socket)

    def ensure_virtual_socket(self) -> NodeSocketVirtual:
        '''Create a virtual input socket if one does not exist'''
        for socket in self.inputs:
            if isinstance(socket, NodeSocketVirtual):
                return socket

        return self.inputs.new(NodeSocketVirtual.__name__, '')

    def handle_virtual_socket(self, socket_types: Tuple[type]):
        '''Create new socket for link to virtual socket if there is one'''
        virtual_socket = self.ensure_virtual_socket()

        if virtual_socket.is_linked:
            link = virtual_socket.links[0]
            from_socket = link.from_socket

            self.id_data.links.remove(link)

            if isinstance(from_socket, socket_types):
                to_socket = self.inputs.new(
                    type(from_socket).__name__,
                    type(from_socket).bl_label,
                )

                self.id_data.links.new(to_socket, from_socket)

                from_index = list(self.inputs).index(virtual_socket)
                self.inputs.move(from_index, len(self.inputs) - 1)

    def sort_sockets(self, socket_types: Tuple[type]):
        '''Sort input sockets by type, only affect given types'''
        socket_table = {cls: [] for cls in socket_types}

        for socket in self.inputs:
            if isinstance(socket, socket_types):
                socket_table[type(socket)].append(socket)

        for sockets in socket_table.values():
            for socket in sockets:
                from_index = list(self.inputs).index(socket)
                self.inputs.move(from_index, len(self.inputs) - 2)


class SourceGeometryNode(Node, SourceBaseNode):
    '''Node which takes geometry from an object or collection'''
    bl_label = 'Geometry'
    bl_icon = 'CUBE'

    command: EnumProperty(
        name='Command',
        description='Which QC command to use for this node',
        items=[
            ('$body', '$body', ''),
            ('$model', '$model', ''),
        ],
        default='$body',
    )

    input_type: EnumProperty(
        name='Input Type',
        description='Where to get the geometry for this node',
        items=[
            ('OBJECT', 'Object', ''),
            ('COLLECTION', 'Collection', ''),
        ],
        default='OBJECT',
    )

    object: PointerProperty(
        name='Object',
        description='The object to get geometry from',
        type=Object,
    )

    collection: PointerProperty(
        name='Collection',
        description='The collection to get geometry from',
        type=Collection,
    )

    file_type: EnumProperty(
        name='File Type',
        description='What file type to export this node as',
        items=[
            ('SMD', 'SMD', ''),
            ('FBX', 'FBX', ''),
        ],
        default='SMD',
    )

    @property
    def file_name(self) -> str:
        '''The file name for this node'''
        if self.input_type == 'OBJECT' and self.object:
            stem = self.object.name
        elif self.input_type == 'COLLECTION' and self.collection:
            stem = self.collection.name
        else:
            stem = 'Geometry'

        if self.file_type == 'SMD':
            suffix = '.smd'
        elif self.file_type == 'FBX':
            suffix = '.fbx'
        else:
            suffix = ''

        return stem + suffix

    def init(self, context: Context):
        '''Initialize a new node'''
        self.outputs.new(
            SourceGeometrySocket.__name__,
            SourceGeometrySocket.bl_label,
        )

    def copy(self, node: Node):
        '''Copy values from another node'''
        self.command = node.command
        self.input_type = node.input_type
        self.object = node.object
        self.collection = node.collection
        self.file_type = node.file_type

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'command', text='')
        layout.prop(self, 'input_type', text='')

        if self.input_type == 'OBJECT':
            layout.prop(self, 'object', text='')
        elif self.input_type == 'COLLECTION':
            layout.prop(self, 'collection', text='')

        layout.prop(self, 'file_type', text='')
        layout.operator('sourcenodes.export_geometry').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.input_type == 'OBJECT' and self.object:
            return self.object.name
        elif self.input_type == 'COLLECTION' and self.collection:
            return self.collection.name
        else:
            return self.bl_label


class SourceAnimationNode(Node, SourceBaseNode):
    '''Node which takes an action from an object'''
    bl_label = 'Animation'
    bl_icon = 'SEQUENCE'

    command: EnumProperty(
        name='Command',
        description='Which QC command to use for this node',
        items=[
            ('$sequence', '$sequence', ''),
        ],
        default='$sequence',
    )

    action: PointerProperty(
        name='Action',
        description='The action to export',
        type=Action,
    )

    file_type: EnumProperty(
        name='File Type',
        description='What file type to export this node as',
        items=[
            ('SMD', 'SMD', ''),
        ],
        default='SMD',
    )

    @property
    def file_name(self) -> str:
        '''The file name for this node'''
        if self.action:
            stem = self.action.name
        else:
            stem = 'Animation'

        if self.file_type == 'SMD':
            suffix = '.smd'
        else:
            suffix = ''

        return stem + suffix

    def init(self, context: Context):
        '''Initialize a new node'''
        self.outputs.new(
            SourceAnimationSocket.__name__,
            SourceAnimationSocket.bl_label,
        )

    def copy(self, node: Node):
        '''Copy values from another node'''
        self.command = node.command
        self.action = node.action
        self.file_type = node.file_type

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'command', text='')
        layout.prop(self, 'action', text='')

        layout.prop(self, 'file_type', text='')
        layout.operator('sourcenodes.export_animation').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.action:
            return self.action.name
        else:
            return self.bl_label


class SourceScriptNode(Node, SourceBaseNode, SourceDynamicNode):
    '''Node which combines geometry and animation in a script'''
    bl_label = 'Script'
    bl_icon = 'TEXT'

    model_name: StringProperty(
        name='Model Name',
        description='Path relative to the models folder',
        default='example/model',
    )

    @property
    def file_name(self) -> str:
        '''The file name for this node'''
        if self.model_name:
            stem = self.model_name.split('/')[-1]
        else:
            stem = 'Script'

        return stem + '.qc'

    def init(self, context: Context):
        '''Initialize a new node'''
        self.ensure_virtual_socket()

    def copy(self, node: Node):
        '''Copy values from another node'''
        self.model_name = node.model_name

    def update(self):
        '''Called when the node tree is updated'''
        socket_types = (
            SourceGeometrySocket,
            SourceAnimationSocket,
        )

        self.remove_unlinked_sockets(socket_types)
        self.handle_virtual_socket(socket_types)
        self.sort_sockets(socket_types)

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'model_name', text='')
        layout.operator('sourcenodes.export_script').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.model_name:
            return self.model_name
        else:
            return self.bl_label


classes = (
    SourceGeometryNode,
    SourceAnimationNode,
    SourceScriptNode,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
