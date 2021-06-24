from bpy.types import NodeTree

from .tree import SourceNodeTree


class SourceNodeBase:
    '''Base class for Source nodes'''

    @classmethod
    def poll(cls, ntree: NodeTree) -> bool:
        '''Check whether this node can be placed in the given node tree'''
        return ntree.bl_idname == SourceNodeTree.bl_idname
