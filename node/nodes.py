import bpy
from bpy.props import EnumProperty, PointerProperty
from bpy.types import Action, Collection, Context, Node, NodeTree, Object, UILayout

from .sockets import SourceGeometrySocket, SourceAnimationSocket
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

    input_object: PointerProperty(
        name='Input Object',
        description='The object to get geometry from',
        type=Object,
    )

    input_collection: PointerProperty(
        name='Input Collection',
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
        self.input_object = node.input_object
        self.input_collection = node.input_collection
        self.file_type = node.file_type

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'command', text='')
        layout.prop(self, 'input_type', text='')

        if self.input_type == 'OBJECT':
            layout.prop(self, 'input_object', text='')
        elif self.input_type == 'COLLECTION':
            layout.prop(self, 'input_collection', text='')

        layout.prop(self, 'file_type', text='')
        layout.operator('sourcenodes.export_geometry').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.input_type == 'OBJECT' and self.input_object:
            return self.input_object.name
        elif self.input_type == 'COLLECTION' and self.input_collection:
            return self.input_collection.name
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

    input_action: PointerProperty(
        name='Input Action',
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

    def init(self, context: Context):
        '''Initialize a new node'''
        self.outputs.new(
            SourceAnimationSocket.__name__,
            SourceAnimationSocket.bl_label,
        )

    def copy(self, node: Node):
        '''Copy values from another node'''
        self.command = node.command
        self.input_action = node.input_action
        self.file_type = node.file_type

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'command', text='')
        layout.prop(self, 'input_action', text='')

        layout.prop(self, 'file_type', text='')
        layout.operator('sourcenodes.export_animation').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.input_action:
            return self.input_action.name
        else:
            return self.bl_label


classes = (
    SourceGeometryNode,
    SourceAnimationNode,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
