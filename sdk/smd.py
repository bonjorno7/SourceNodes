from typing import List

import bpy
from bpy.types import Action, Object


def export_geometry(objects: List[Object]):
    '''Export geometry to an SMD file'''
    for object in objects:
        print(object.name)


def export_animation(object: Object, action: Action):
    '''Export animation to an SMD file'''
    print(object.name)
    print(action.name)
