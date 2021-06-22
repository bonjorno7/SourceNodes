import bpy
from bpy.types import Context, Node, Operator

from ..sdk.file import export_sequence


class SOURCENODES_OT_export_sequence(Operator):
    '''Export the given sequence to a file'''
    bl_idname = 'sourcenodes.export_sequence'
    bl_label = 'Export'
    bl_options = {'REGISTER', 'INTERNAL'}

    node: bpy.props.StringProperty(options={'HIDDEN'})

    def execute(self, context: Context) -> set:
        '''Execute the operator'''
        node: Node = eval(self.node)

        export_sequence(node)

        return {'FINISHED'}


classes = (SOURCENODES_OT_export_sequence,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)