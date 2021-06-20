from . import export_body

modules = (export_body,)


def register():
    '''Register this module'''
    for module in modules:
        module.register()


def unregister():
    '''Unregister this module'''
    for module in reversed(modules):
        module.unregister()
