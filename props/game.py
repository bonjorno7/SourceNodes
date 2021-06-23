from bpy.types import PropertyGroup
from bpy.props import StringProperty


class SOURCENODES_game(PropertyGroup):
    '''Game you can export to'''
    name: StringProperty(
        name='Name',
        description='Name of the game',
        default='Example',
    )
