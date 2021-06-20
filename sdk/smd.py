from typing import List

import bpy
from bpy.types import Action, Object


def export_body(objects: List[Object]):
    for object in objects:
        print(object.name)


def export_sequence(object: Object, action: Action):
    print(object.name)
    print(action.name)
