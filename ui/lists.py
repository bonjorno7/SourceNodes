from typing import Any

from bpy.types import Context, UILayout, UIList


class SOURCENODES_UL_standard(UIList):
    '''List of named items'''

    def draw_item(
        self,
        context: Context,
        layout: UILayout,
        data: Any,
        item: Any,
        icon: int,
        active_data: Any,
        active_property: str,
        index: int,
        flt_flag: int,
    ):
        '''Draw an item in the list'''
        layout.prop(item, 'name', text='', emboss=False, translate=False)
