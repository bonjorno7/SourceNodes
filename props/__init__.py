import bpy

from .game import SOURCENODES_game
from .prefs import SOURCENODES_prefs

classes = (
    SOURCENODES_game,
    SOURCENODES_prefs,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
