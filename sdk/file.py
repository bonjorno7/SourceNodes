from pathlib import Path

from ..node.nodes import SourceAnimationNode, SourceGeometryNode
from . import fbx, smd


def export_geometry(node: SourceGeometryNode):
    '''Export geometry to a file'''
    objects = []

    if node.input_type == 'OBJECT' and node.input_object:
        name = node.input_object.name
        objects.append(node.input_object)
    elif node.input_type == 'COLLECTION' and node.input_collection:
        name = node.input_collection.name
        objects.extend(node.input_collection.all_objects)

    for object in objects.copy():
        armature = object.find_armature()
        if armature and (armature not in objects):
            objects.append(armature)

    if objects:
        path = Path.home().joinpath('Desktop', name)

        if node.file_type == 'SMD':
            smd.export_geometry(path.with_suffix('.smd'), objects)
        elif node.file_type == 'FBX':
            fbx.export_geometry(path.with_suffix('.fbx'), objects)


def export_animation(node: SourceAnimationNode):
    '''Export animation to a file'''
    if node.input_action:
        path = Path.home().joinpath('Desktop', node.input_action.name)

        if node.file_type == 'SMD':
            smd.export_animation(path.with_suffix('.smd'), node.input_action)
