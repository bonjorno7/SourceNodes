from bpy.types import UILayout


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
