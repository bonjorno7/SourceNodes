import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

from .node_body import SourceNodeBody
from .node_bodygroup import SourceNodeBodygroup
from .node_model import SourceNodeModel
from .node_sequence import SourceNodeSequence
from .tree import SourceNodeTree


class SourceNodeCategory(NodeCategory):
    '''Source Node Category'''

    @classmethod
    def poll(cls, context):
        '''Whether this category should show up in a given node tree'''
        return context.space_data.tree_type == SourceNodeTree.__name__


node_categories = [
    SourceNodeCategory(
        'SOURCENODES_NODES',
        'Nodes',
        items=[
            NodeItem(SourceNodeBody.__name__),
            NodeItem(SourceNodeBodygroup.__name__),
            NodeItem(SourceNodeSequence.__name__),
            NodeItem(SourceNodeModel.__name__),
        ],
    ),
]
