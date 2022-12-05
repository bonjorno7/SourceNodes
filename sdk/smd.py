from pathlib import Path

from bpy.types import Action, Object


def export_body(path: Path, objects: list[Object]):
    '''Export body to an SMD file'''
    for object in objects:
        print(object.name)


def export_sequence(path: Path, action: Action):
    '''Export sequence to an SMD file'''
    print(action.name)
