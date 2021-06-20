from . import categories, nodes, sockets, tree

modules = (
    tree,
    sockets,
    nodes,
    categories,
)


def register():
    '''Register this module'''
    for module in modules:
        module.register()


def unregister():
    '''Unregister this module'''
    for module in reversed(modules):
        module.unregister()
