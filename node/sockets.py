import bpy
from bpy.types import Context, Node, NodeSocket, UILayout


class SourceGeometrySocket(NodeSocket):
    '''Socket to connect a Geometry node to a Body Group or Script node'''
    bl_label = 'Geometry'

    def draw(self, context: Context, layout: UILayout, node: Node, text: str):
        '''Draw the socket name or properties'''
        layout.label(text=text)

    def draw_color(self, context: Context, node: Node) -> tuple:
        '''The color of this socket on the given node'''
        return (0.4, 0.8, 0.4, 1.0)


class SourceAnimationSocket(NodeSocket):
    '''Socket to connect an Animation node to a Script node'''
    bl_label = 'Animation'

    def draw(self, context: Context, layout: UILayout, node: Node, text: str):
        '''Draw the socket name or properties'''
        layout.label(text=text)

    def draw_color(self, context: Context, node: Node) -> tuple:
        '''The color of this socket on the given node'''
        return (0.9, 0.6, 0.2, 1.0)


classes = (
    SourceGeometrySocket,
    SourceAnimationSocket,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
