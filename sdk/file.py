from ..node.nodes import SourceBodyNode
from . import fbx, smd


def export_body(node: SourceBodyNode):
    objects = []

    if node.input_type == 'OBJECT' and node.input_object:
        objects.append(node.input_object)
    elif node.input_type == 'COLLECTION' and node.input_collection:
        objects.extend(node.input_collection.all_objects)

    for object in objects.copy():
        armature = object.find_armature()
        if armature and (armature not in objects):
            objects.append(armature)

    if node.file_type == 'SMD':
        smd.export_body(objects)
    elif node.file_type == 'FBX':
        fbx.export_body(objects)
