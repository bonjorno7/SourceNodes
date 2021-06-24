import bpy
import nodeitems_utils

from .categories import SOURCENODES_node_categories
from .node_body import SOURCENODES_node_body
from .node_bodygroup import SOURCENODES_node_bodygroup
from .node_model import SOURCENODES_node_model
from .node_sequence import SOURCENODES_node_sequence
from .socket_body import SOURCENODES_socket_body
from .socket_bodygroup import SOURCENODES_socket_bodygroup
from .socket_sequence import SOURCENODES_socket_sequence
from .tree import SOURCENODES_node_tree

classes = (
    SOURCENODES_node_tree,
    SOURCENODES_socket_body,
    SOURCENODES_socket_bodygroup,
    SOURCENODES_socket_sequence,
    SOURCENODES_node_body,
    SOURCENODES_node_bodygroup,
    SOURCENODES_node_sequence,
    SOURCENODES_node_model,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)

    nodeitems_utils.register_node_categories(
        'SOURCENODES',
        SOURCENODES_node_categories,
    )


def unregister():
    '''Unregister this module'''
    nodeitems_utils.unregister_node_categories('SOURCENODES')

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
