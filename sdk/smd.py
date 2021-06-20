from typing import List

import bpy
from bpy.types import Object


def export_body(objects: List[Object]):
    for object in objects:
        print(object.name)
