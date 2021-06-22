import bpy
from bpy.types import Context, Node, NodeSocket, UILayout


class SourceSocketRemovable:
    '''Socket which can be removed by the user'''

    def draw_remove_button(self, layout: UILayout):
        '''Draw an X next to the socket, which allows the user to remove it'''
        if not self.is_output:
            layout.operator(
                'sourcenodes.remove_socket',
                text='',
                icon='X',
                emboss=False,
            ).socket = repr(self)


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


classes = (
    SourceSocketBody,
    SourceSocketSequence,
)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
