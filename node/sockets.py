import bpy
from bpy.types import Context, Node, NodeSocket, UILayout


class SourceBodySocket(NodeSocket):
    '''Socket to connect a Body to a Body Group or Model'''
    bl_label = 'Body'

    def draw(self, context: Context, layout: UILayout, node: Node, text: str):
        layout.label(text=text)

    def draw_color(self, context: Context, node: Node) -> tuple:
        return (0.4, 0.8, 0.4, 1.0)


classes = (SourceBodySocket,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
