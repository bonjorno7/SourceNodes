import bpy
import nodeitems_utils

from .categories import node_categories
from .node_body import SourceNodeBody
from .node_bodygroup import SourceNodeBodygroup
from .node_model import SourceNodeModel
from .node_sequence import SourceNodeSequence
from .socket_body import SourceSocketBody
from .socket_bodygroup import SourceSocketBodygroup
from .socket_sequence import SourceSocketSequence
from .tree import SourceNodeTree

classes = (
    SourceNodeTree,
    SourceSocketBody,
    SourceSocketBodygroup,
    SourceSocketSequence,
    SourceNodeBody,
    SourceNodeBodygroup,
    SourceNodeSequence,
    SourceNodeModel,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)

    nodeitems_utils.register_node_categories('SOURCENODES', node_categories)


def unregister():
    '''Unregister this module'''
    nodeitems_utils.unregister_node_categories('SOURCENODES')

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
