from typing import Any, Tuple

from bpy.types import UILayout

from .common import get_prefs


def get_list_info(type: str) -> Tuple[str, Any, str, str]:
    '''Get the info necessary to draw a list'''
    prefs = get_prefs()

    if type == 'GAMES':
        list_type = 'SOURCENODES_UL_standard'
        list_name = 'SOURCENODES_UL_games'
        parent = prefs
        items_name = 'game_items'
        index_name = 'game_index'
    else:
        raise Exception('unknown list type')

    return list_type, list_name, parent, items_name, index_name


def draw_list(layout: UILayout, type: str):
    '''Draw a list of the given type'''
    list_type, list_name, parent, items_name, index_name = get_list_info(type)
    items = getattr(parent, items_name)
    operator = 'sourcenodes.list_operator'

    row = layout.row()
    row.template_list(
        listtype_name=list_type,
        list_id=list_name,
        dataptr=parent,
        propname=items_name,
        active_dataptr=parent,
        active_propname=index_name,
    )

    col = row.column(align=True)
    op = col.operator(operator, text='', icon='ADD')
    op.type, op.mode = type, 'ADD'

    sub = col.column(align=True)
    sub.enabled = len(items) > 0
    op = sub.operator(operator, text='', icon='REMOVE')
    op.type, op.mode = type, 'REMOVE'

    col.separator()

    sub = col.column(align=True)
    sub.enabled = len(items) > 0
    op = sub.operator(operator, text='', icon='DUPLICATE')
    op.type, op.mode = type, 'COPY'

    col.separator()

    sub = col.column(align=True)
    sub.enabled = len(items) > 1
    op = sub.operator(operator, text='', icon='TRIA_UP')
    op.type, op.mode = type, 'MOVE_UP'

    sub = col.column(align=True)
    sub.enabled = len(items) > 1
    op = sub.operator(operator, text='', icon='TRIA_DOWN')
    op.type, op.mode = type, 'MOVE_DOWN'
