import bpy
from bpy.types import Context, NodeSocket, Operator


class SOURCENODES_OT_remove_socket(Operator):
    '''Remove the given socket from its node'''
    bl_idname = 'sourcenodes.remove_socket'
    bl_label = 'Remove'
    bl_options = {'REGISTER', 'INTERNAL'}

    socket: bpy.props.StringProperty(options={'HIDDEN'})

    def execute(self, context: Context) -> set:
        '''Execute the operator'''
        socket: NodeSocket = eval(self.socket)

        if socket.is_output:
            socket.node.outputs.remove(socket)
        else:
            socket.node.inputs.remove(socket)

        return {'FINISHED'}


classes = (SOURCENODES_OT_remove_socket,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
