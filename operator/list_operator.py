import bpy
from bpy.types import Context, bpy_prop_collection

from ..utils.ui import get_list_info


class SOURCENODES_OT_list_operator(bpy.types.Operator):
    '''Perform an action on a list'''
    bl_idname = 'sourcenodes.list_operator'
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}
    bl_label = 'List Operator'

    type: bpy.props.EnumProperty(
        name='Type',
        description='List to operate on',
        items=[
            ('GAMES', 'Games', ''),
        ],
        options={'HIDDEN'},
    )

    mode: bpy.props.EnumProperty(
        name='Mode',
        description='Action to perform',
        items=[
            ('ADD', 'Add', ''),
            ('REMOVE', 'Remove', ''),
            ('COPY', 'Copy', ''),
            ('MOVE_UP', 'Move Up', ''),
            ('MOVE_DOWN', 'Move Down', ''),
        ],
        options={'HIDDEN'},
    )

    def add(self, items: bpy_prop_collection, index: int):
        '''Add an item to the list'''
        items.add()
        index = len(items) - 1
        return index

    def remove(self, items: bpy_prop_collection, index: int):
        '''Remove an item from the list'''
        items.remove(index)
        index = min(max(0, index - 1), max(0, len(items) - 1))
        return index

    def copy(self, items: bpy_prop_collection, index: int):
        '''Duplicate an item in the list'''
        items.add()
        old, new = items[index], items[-1]
        for key, value in old.items():
            new[key] = value
        index = len(items) - 1
        return index

    def move_up(self, items: bpy_prop_collection, index: int):
        '''Move an item up in the list'''
        return self.move(items, index, -1)

    def move_down(self, items: bpy_prop_collection, index: int):
        '''Move an item down in the list'''
        return self.move(items, index, 1)

    def move(self, items: bpy_prop_collection, index: int, direction: int):
        '''Move an item in the given direction'''
        neighbor = max(0, index + direction)
        items.move(neighbor, index)
        length = max(0, len(items) - 1)
        index = max(0, min(neighbor, length))
        return index

    def execute(self, context: Context):
        '''Execute the operator'''
        _, _, parent, items_name, index_name = get_list_info(self.type)

        items = getattr(parent, items_name)
        index = getattr(parent, index_name)

        function = {
            'ADD': self.add,
            'REMOVE': self.remove,
            'COPY': self.copy,
            'MOVE_UP': self.move_up,
            'MOVE_DOWN': self.move_down,
        }[self.mode]

        index = function(items, index)
        setattr(parent, index_name, index)

        return {'FINISHED'}


classes = (SOURCENODES_OT_list_operator,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
