from . import (export_body, export_bodygroup, export_model, export_sequence,
               list_operator, remove_socket)

modules = (
    list_operator,
    remove_socket,
    export_body,
    export_bodygroup,
    export_sequence,
    export_model,
)


def register():
    '''Register this module'''
    for module in modules:
        module.register()


def unregister():
    '''Unregister this module'''
    for module in reversed(modules):
        module.unregister()
