from bpy.props import StringProperty
from bpy.types import Context, Node, UILayout

from .node_base import SOURCENODES_node_base
from .node_dynamic import SOURCENODES_node_dynamic
from .socket_body import SOURCENODES_socket_body
from .socket_bodygroup import SOURCENODES_socket_bodygroup
from .socket_sequence import SOURCENODES_socket_sequence


class SOURCENODES_node_model(
        Node,
        SOURCENODES_node_base,
        SOURCENODES_node_dynamic,
):
    '''Node which combines bodies and sequences into a model'''
    bl_label = 'Model'
    bl_icon = 'PROPERTIES'

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
            stem = self.bl_label

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
            SOURCENODES_socket_body,
            SOURCENODES_socket_bodygroup,
            SOURCENODES_socket_sequence,
        )

        self.handle_virtual_socket(socket_types)
        self.sort_sockets(socket_types)

    def draw_buttons(self, context: Context, layout: UILayout):
        '''Draw node properties'''
        layout.prop(self, 'model_name', text='')
        layout.operator('sourcenodes.export_model').node = repr(self)

    def draw_label(self) -> str:
        '''Draw node label'''
        if self.model_name:
            return self.model_name
        else:
            return self.bl_label
