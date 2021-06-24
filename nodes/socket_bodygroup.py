from bpy.types import Context, Node, NodeSocket, UILayout

from .socket_removable import SOURCENODES_socket_removable


class SOURCENODES_socket_bodygroup(NodeSocket, SOURCENODES_socket_removable):
    '''Socket to connect a Bodygroup node to a Model node'''
    bl_label = 'Bodygroup'

    def draw(self, context: Context, layout: UILayout, node: Node, text: str):
        '''Draw the socket name or properties'''
        layout.label(text=text)
        self.draw_remove_button(layout)

    def draw_color(self, context: Context, node: Node) -> tuple:
        '''The color of this socket on the given node'''
        return (0.2, 0.6, 0.8, 1.0)
