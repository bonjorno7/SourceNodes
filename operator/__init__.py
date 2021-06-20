from . import export_body, export_sequence

modules = (
    export_body,
    export_sequence,
)


def register():
    '''Register this module'''
    for module in modules:
        module.register()


def unregister():
    '''Unregister this module'''
    for module in reversed(modules):
        module.unregister()
