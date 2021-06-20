from pathlib import Path
from typing import List

import bpy
from bpy.types import Action, Object


def export_geometry(path: Path, objects: List[Object]):
    '''Export geometry to an SMD file'''
    for object in objects:
        print(object.name)


def export_animation(path: Path, action: Action):
    '''Export animation to an SMD file'''
    print(action.name)
