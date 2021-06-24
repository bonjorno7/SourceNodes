bl_info = {
    'name': 'Source Nodes',
    'author': 'bonjorno7',
    'description': 'Blender node based export for Source models',
    'blender': (2, 80, 0),
    'version': (0, 0, 1),
    'location': 'Editors > Source Nodes',
    'category': 'Import-Export',
    'wiki_url': 'https://github.com/bonjorno7/SourceNodes/wiki',
    'tracker_url': 'https://github.com/bonjorno7/SourceNodes/issues',
}

from . import nodes, ops, props, ui

modules = (
    props,
    nodes,
    ops,
    ui,
)


def register():
    '''Register this module'''
    for module in modules:
        module.register()


def unregister():
    '''Unregister this module'''
    for module in reversed(modules):
        module.unregister()
