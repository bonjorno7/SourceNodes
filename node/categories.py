import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

from .nodes import SourceAnimationNode, SourceGeometryNode, SourceScriptNode
from .tree import SourceNodeTree


class SourceNodeCategory(NodeCategory):
    '''Source Node Category'''

    @classmethod
    def poll(cls, context):
        '''Whether this category should show up in a given node tree'''
        return context.space_data.tree_type == SourceNodeTree.__name__


node_categories = [
    SourceNodeCategory(
        'SOURCE_NODES_ALL',
        'Nodes',
        items=[
            NodeItem(SourceGeometryNode.__name__),
            NodeItem(SourceAnimationNode.__name__),
            NodeItem(SourceScriptNode.__name__),
        ],
    ),
]


def register():
    '''Register this module'''
    nodeitems_utils.register_node_categories('SOURCE_NODES', node_categories)


def unregister():
    '''Unregister this module'''
    nodeitems_utils.unregister_node_categories('SOURCE_NODES')
