import bpy
from bpy.types import NodeTree


class SourceNodeTree(NodeTree):
    '''Node based export for Source models'''
    bl_label = 'Source Nodes'
    bl_icon = 'NODETREE'


classes = (SourceNodeTree,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
