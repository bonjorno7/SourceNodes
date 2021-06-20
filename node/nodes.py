import bpy
from bpy.props import EnumProperty, PointerProperty
from bpy.types import Action, Collection, Context, Node, NodeTree, Object, UILayout

from .sockets import SourceBodySocket, SourceSequenceSocket
from .tree import SourceNodeTree


class SourceBaseNode:
    '''Base class for Source nodes'''

    @classmethod
    def poll(cls, ntree: NodeTree) -> bool:
        return ntree.bl_idname == SourceNodeTree.__name__


class SourceBodyNode(Node, SourceBaseNode):
    '''Body which takes geometry from an object or collection'''
    bl_label = 'Body'
    bl_icon = 'CUBE'

    command: EnumProperty(
        name='Command',
        description='Which QC command to use for this body',
        items=[
            ('$body', '$body', 'Use $body in the QC'),
            ('$model', '$model', 'Use $model in the QC'),
        ],
        default='$body',
    )

    input_type: EnumProperty(
        name='Input Type',
        description='Where to get the geometry for this body',
        items=[
            ('OBJECT', 'Object', 'Get geometry from a single object'),
            ('COLLECTION', 'Collection', 'Get geometry from a collection'),
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
        description='What file type to export this body as',
        items=[
            ('SMD', 'SMD', 'Export this body as SMD file'),
            ('FBX', 'FBX', 'Export this body as FBX file'),
        ],
        default='SMD',
    )

    def init(self, context: Context):
        '''Initialize new node'''
        self.outputs.new(SourceBodySocket.__name__, self.bl_label)

    def copy(self, node: Node):
        '''Copy values from other node'''
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
        layout.operator('sourcenodes.export_body').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.input_type == 'OBJECT' and self.input_object:
            return self.input_object.name
        elif self.input_type == 'COLLECTION' and self.input_collection:
            return self.input_collection.name
        else:
            return self.bl_label


class SourceSequenceNode(Node, SourceBaseNode):
    '''Sequence which takes an action from an object'''
    bl_label = 'Sequence'
    bl_icon = 'SEQUENCE'

    command: EnumProperty(
        name='Command',
        description='Which QC command to use for this sequence',
        items=[
            ('$sequence', '$sequence', 'Use $sequence in the QC'),
        ],
        default='$sequence',
    )

    input_object: PointerProperty(
        name='Input Object',
        description='The object to get the action from',
        type=Object,
    )

    input_action: PointerProperty(
        name='Input Action',
        description='The action to export',
        type=Action,
    )

    def init(self, context: Context):
        '''Initialize new node'''
        self.outputs.new(
            SourceSequenceSocket.__name__,
            SourceSequenceSocket.bl_label,
        )

    def copy(self, node: Node):
        '''Copy values from other node'''
        self.command = node.command
        self.input_object = node.input_object
        self.input_action = node.input_action

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'command', text='')
        layout.prop(self, 'input_object', text='')
        layout.prop(self, 'input_action', text='')
        layout.operator('sourcenodes.export_sequence').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.input_action:
            return self.input_action.name
        else:
            return self.bl_label


classes = (
    SourceBodyNode,
    SourceSequenceNode,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
