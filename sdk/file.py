from pathlib import Path

from ..node.nodes import (SourceNodeBody, SourceNodeBodygroup, SourceNodeModel,
                          SourceNodeSequence)
from . import fbx, qc, smd


def export_body(node: SourceNodeBody):
    '''Export body to a file'''
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
            smd.export_body(path, objects)
        elif node.file_type == 'FBX':
            fbx.export_body(path, objects)


def export_bodygroup(node: SourceNodeBodygroup):
    '''Export the bodies in this group'''
    for socket in node.inputs:
        if socket.is_linked:
            link = socket.links[0]

            if isinstance(link.from_node, SourceNodeBody):
                export_body(link.from_node)


def export_sequence(node: SourceNodeSequence):
    '''Export sequence to a file'''
    if node.action:
        path = Path.home().joinpath('Desktop', node.file_name)

        if node.file_type == 'SMD':
            smd.export_sequence(path, node.action)


def export_model(node: SourceNodeModel):
    '''Export model to a file'''
    if node.model_name:
        path = Path.home().joinpath('Desktop', node.file_name)

        qc.export_model(path, node.model_name)
