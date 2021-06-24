from bpy.types import Context, Node, NodeSocket, UILayout

from .socket_removable import SourceSocketRemovable


class SourceSocketBody(NodeSocket, SourceSocketRemovable):
    '''Socket to connect a Body node to a Body Group or Model node'''
    bl_label = 'Body'

    def draw(self, context: Context, layout: UILayout, node: Node, text: str):
        '''Draw the socket name or properties'''
        layout.label(text=text)
        self.draw_remove_button(layout)

    def draw_color(self, context: Context, node: Node) -> tuple:
        '''The color of this socket on the given node'''
        return (0.4, 0.8, 0.4, 1.0)
