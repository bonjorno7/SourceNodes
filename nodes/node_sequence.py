from bpy.props import EnumProperty, PointerProperty
from bpy.types import Action, Context, Node, UILayout

from .node_base import SourceNodeBase
from .socket_sequence import SourceSocketSequence


class SourceNodeSequence(Node, SourceNodeBase):
    '''Node which takes an action from an object'''
    bl_label = 'Sequence'
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
            stem = self.bl_label

        if self.file_type == 'SMD':
            suffix = '.smd'
        else:
            suffix = ''

        return stem + suffix

    def init(self, context: Context):
        '''Initialize a new node'''
        self.outputs.new(
            SourceSocketSequence.__name__,
            SourceSocketSequence.bl_label,
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
        layout.operator('sourcenodes.export_sequence').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.action:
            return self.action.name
        else:
            return self.bl_label
