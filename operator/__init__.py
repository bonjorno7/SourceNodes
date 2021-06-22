from . import export_body, export_model, export_sequence, remove_socket

modules = (
    remove_socket,
    export_body,
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
