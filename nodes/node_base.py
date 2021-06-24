from bpy.types import NodeTree

from .tree import SOURCENODES_node_tree


class SOURCENODES_node_base:
    '''Base class for Source nodes'''

    @classmethod
    def poll(cls, ntree: NodeTree) -> bool:
        '''Check whether this node can be placed in the given node tree'''
        return ntree.bl_idname == SOURCENODES_node_tree.bl_idname
