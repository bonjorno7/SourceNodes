from . import export_animation, export_geometry, export_script, remove_socket

modules = (
    remove_socket,
    export_geometry,
    export_animation,
    export_script,
)


def register():
    '''Register this module'''
    for module in modules:
        module.register()


def unregister():
    '''Unregister this module'''
    for module in reversed(modules):
        module.unregister()
