import bpy
from bpy.props import EnumProperty, PointerProperty, StringProperty
from bpy.types import (Action, Collection, Context, Node, NodeTree, Object,
                       UILayout)

from .sockets import SourceAnimationSocket, SourceGeometrySocket
from .tree import SourceNodeTree


class SourceBaseNode:
    '''Base class for Source nodes'''

    @classmethod
    def poll(cls, ntree: NodeTree) -> bool:
        return ntree.bl_idname == SourceNodeTree.__name__


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


class SourceScriptNode(Node, SourceBaseNode):
    '''Node which combines geometry and animation in a script'''
    bl_label = 'Script'
    bl_icon = 'TEXT'

    name: StringProperty(
        name='Name',
        description='Path relative to the models folder',
        default='example/model',
    )

    @property
    def file_name(self) -> str:
        '''The file name for this node'''
        if self.name:
            stem = self.name.split('/')[-1]
        else:
            stem = 'Script'

        return stem + '.qc'

    def init(self, context: Context):
        '''Initialize a new node'''
        self.inputs.new(
            SourceGeometrySocket.__name__,
            SourceGeometrySocket.bl_label,
        )

        self.inputs.new(
            SourceAnimationSocket.__name__,
            SourceAnimationSocket.bl_label,
        )

    def copy(self, node: Node):
        '''Copy values from another node'''
        self.name = node.name

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'name', text='')
        layout.operator('sourcenodes.export_script').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.name:
            return self.name
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
