from pathlib import Path

from ..node.nodes import (SourceAnimationNode, SourceGeometryNode,
                          SourceScriptNode)
from . import fbx, qc, smd


def export_geometry(node: SourceGeometryNode):
    '''Export geometry to a file'''
    objects = []

    if node.input_type == 'OBJECT' and node.object:
        objects.append(node.object)
    elif node.input_type == 'COLLECTION' and node.collection:
        objects.extend(node.collection.all_objects)

    for object in objects.copy():
        armature = object.find_armature()
        if armature and (armature not in objects):
            objects.append(armature)

    if objects:
        path = Path.home().joinpath('Desktop', node.file_name)

        if node.file_type == 'SMD':
            smd.export_geometry(path, objects)
        elif node.file_type == 'FBX':
            fbx.export_geometry(path, objects)


def export_animation(node: SourceAnimationNode):
    '''Export animation to a file'''
    if node.action:
        path = Path.home().joinpath('Desktop', node.file_name)

        if node.file_type == 'SMD':
            smd.export_animation(path, node.action)


def export_script(node: SourceScriptNode):
    '''Export script to a file'''
    if node.name:
        path = Path.home().joinpath('Desktop', node.file_name)

        qc.export_script(path, node.name)
