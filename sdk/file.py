from pathlib import Path

from ..node.nodes import SourceAnimationNode, SourceGeometryNode
from . import fbx, smd


def export_geometry(node: SourceGeometryNode):
    '''Export geometry to a file'''
    objects = []

    if node.input_type == 'OBJECT' and node.object:
        name = node.object.name
        objects.append(node.object)
    elif node.input_type == 'COLLECTION' and node.collection:
        name = node.collection.name
        objects.extend(node.collection.all_objects)

    for object in objects.copy():
        armature = object.find_armature()
        if armature and (armature not in objects):
            objects.append(armature)

    if objects:
        path = Path.home().joinpath('Desktop', name)

        if node.file_type == 'SMD':
            path = path.with_suffix('.smd')
            smd.export_geometry(path, objects)
        elif node.file_type == 'FBX':
            path = path.with_suffix('.fbx')
            fbx.export_geometry(path, objects)


def export_animation(node: SourceAnimationNode):
    '''Export animation to a file'''
    if node.action:
        path = Path.home().joinpath('Desktop', node.action.name)

        if node.file_type == 'SMD':
            path = path.with_suffix('.smd')
            smd.export_animation(path, node.action)
