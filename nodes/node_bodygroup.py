from bpy.props import StringProperty
from bpy.types import Context, Node, UILayout

from .node_base import SOURCENODES_node_base
from .node_dynamic import SOURCENODES_node_dynamic
from .socket_body import SOURCENODES_socket_body
from .socket_bodygroup import SOURCENODES_socket_bodygroup


class SOURCENODES_node_bodygroup(
        Node,
        SOURCENODES_node_base,
        SOURCENODES_node_dynamic,
):
    '''Node which takes multiple body inputs'''
    bl_label = 'Bodygroup'
    bl_icon = 'OUTLINER_COLLECTION'

    group_name: StringProperty(
        name='Group Name',
        description='Name for this bodygroup in the QC',
        default='bodygroup',
    )

    @property
    def folder_name(self) -> str:
        '''The folder name for this node'''
        if self.group_name:
            stem = self.group_name
        else:
            stem = self.bl_label

        return stem

    def init(self, context: Context):
        '''Initialize a new node'''
        self.ensure_virtual_socket()

        self.outputs.new(
            SOURCENODES_socket_bodygroup.__name__,
            SOURCENODES_socket_bodygroup.bl_label,
        )

    def copy(self, node: Node):
        '''Copy values from another node'''
        self.group_name = node.group_name

    def update(self):
        '''Called when the node tree is updated'''
        socket_types = (SOURCENODES_socket_body,)

        self.handle_virtual_socket(socket_types)
        self.sort_sockets(socket_types)

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'group_name', text='')
        layout.operator('sourcenodes.export_bodygroup').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.group_name:
            return self.group_name
        else:
            return self.bl_label
