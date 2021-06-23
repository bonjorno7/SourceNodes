import bpy
from bpy.types import Context, Node, Operator

from ..sdk.file import export_model


class SOURCENODES_OT_export_model(Operator):
    '''Export the given model to a file'''
    bl_idname = 'sourcenodes.export_model'
    bl_label = 'Export'
    bl_options = {'REGISTER', 'INTERNAL'}

    node: bpy.props.StringProperty(options={'HIDDEN'})

    def execute(self, context: Context) -> set:
        '''Execute the operator'''
        node: Node = eval(self.node)

        export_model(node)

        return {'FINISHED'}
