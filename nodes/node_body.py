from bpy.props import EnumProperty, PointerProperty
from bpy.types import Collection, Context, Node, Object, UILayout

from .node_base import SOURCENODES_node_base
from .socket_body import SOURCENODES_socket_body


class SOURCENODES_node_body(Node, SOURCENODES_node_base):
    '''Node which takes geometry from an object or collection'''
    bl_label = 'Body'
    bl_icon = 'OUTLINER_OB_MESH'

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
            stem = self.bl_label

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
            SOURCENODES_socket_body.__name__,
            SOURCENODES_socket_body.bl_label,
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
        layout.operator('sourcenodes.export_body').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.input_type == 'OBJECT' and self.object:
            return self.object.name
        elif self.input_type == 'COLLECTION' and self.collection:
            return self.collection.name
        else:
            return self.bl_label
