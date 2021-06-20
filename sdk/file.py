from ..node.nodes import SourceGeometryNode, SourceAnimationNode
from . import fbx, smd


def export_geometry(node: SourceGeometryNode):
    '''Export geometry to a file'''
    objects = []

    if node.input_type == 'OBJECT' and node.input_object:
        objects.append(node.input_object)
    elif node.input_type == 'COLLECTION' and node.input_collection:
        objects.extend(node.input_collection.all_objects)

    for object in objects.copy():
        armature = object.find_armature()
        if armature and (armature not in objects):
            objects.append(armature)

    if objects:
        if node.file_type == 'SMD':
            smd.export_geometry(objects)
        elif node.file_type == 'FBX':
            fbx.export_geometry(objects)


def export_animation(node: SourceAnimationNode):
    '''Export animation to a file'''
    object = node.input_object
    action = node.input_action

    if object and action:
        smd.export_animation(object, action)
