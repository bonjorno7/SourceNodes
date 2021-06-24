from bpy.types import Context, Node, NodeSocket, UILayout

from .socket_removable import SourceSocketRemovable


class SourceSocketSequence(NodeSocket, SourceSocketRemovable):
    '''Socket to connect a Sequence node to a Model node'''
    bl_label = 'Sequence'

    def draw(self, context: Context, layout: UILayout, node: Node, text: str):
        '''Draw the socket name or properties'''
        layout.label(text=text)
        self.draw_remove_button(layout)

    def draw_color(self, context: Context, node: Node) -> tuple:
        '''The color of this socket on the given node'''
        return (0.9, 0.6, 0.2, 1.0)
