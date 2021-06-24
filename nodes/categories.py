from bpy.types import Context
from nodeitems_utils import NodeCategory, NodeItem

from .node_body import SOURCENODES_node_body
from .node_bodygroup import SOURCENODES_node_bodygroup
from .node_model import SOURCENODES_node_model
from .node_sequence import SOURCENODES_node_sequence
from .tree import SOURCENODES_node_tree


class SOURCENODES_node_category(NodeCategory):
    '''Category for Source nodes'''

    @classmethod
    def poll(cls, context: Context):
        '''Whether this category should show up in a given node tree'''
        return context.space_data.tree_type == SOURCENODES_node_tree.__name__


SOURCENODES_node_categories = [
    SOURCENODES_node_category(
        'SOURCENODES_model_nodes',
        'Model Nodes',
        items=[
            NodeItem(SOURCENODES_node_body.__name__),
            NodeItem(SOURCENODES_node_bodygroup.__name__),
            NodeItem(SOURCENODES_node_sequence.__name__),
            NodeItem(SOURCENODES_node_model.__name__),
        ],
    ),
]
