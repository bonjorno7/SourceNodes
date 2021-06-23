from bpy.props import CollectionProperty, IntProperty
from bpy.types import AddonPreferences, Context, UILayout

from ..utils.common import get_module
from ..utils.ui import draw_list
from .game import SOURCENODES_game


class SOURCENODES_prefs(AddonPreferences):
    '''Preferences for this addon'''
    bl_idname = get_module()

    game_items: CollectionProperty(name='Game Items', type=SOURCENODES_game)
    game_index: IntProperty(name='Game Index')

    def draw(self, context: Context):
        '''Draw the preferences interface'''
        layout: UILayout = self.layout

        layout.label(text='Games')
        draw_list(layout, 'GAMES')
