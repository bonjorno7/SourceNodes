from typing import List

import bpy
from bpy.types import Object


def export_geometry(objects: List[Object]):
    '''Export geometry to an FBX file'''
    for object in objects:
        print(object.name)
