import bpy

from .export_body import SOURCENODES_OT_export_body
from .export_bodygroup import SOURCENODES_OT_export_bodygroup
from .export_model import SOURCENODES_OT_export_model
from .export_sequence import SOURCENODES_OT_export_sequence
from .list_operator import SOURCENODES_OT_list_operator
from .remove_socket import SOURCENODES_OT_remove_socket

classes = (
    SOURCENODES_OT_list_operator,
    SOURCENODES_OT_remove_socket,
    SOURCENODES_OT_export_body,
    SOURCENODES_OT_export_bodygroup,
    SOURCENODES_OT_export_sequence,
    SOURCENODES_OT_export_model,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
