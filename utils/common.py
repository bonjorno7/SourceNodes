import bpy
from bpy.types import AddonPreferences


def get_module():
    '''Get the module name for this addon'''
    return __package__.partition('.')[0]


def get_prefs() -> AddonPreferences:
    '''Get the preferences for this addon'''
    return bpy.context.preferences.addons[get_module()].preferences
