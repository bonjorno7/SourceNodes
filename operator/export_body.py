import bpy
from bpy.types import Context, Node, Operator

from ..sdk.file import export_body


class SOURCENODES_OT_export_body(Operator):
    '''Export the given body to a file'''
    bl_idname = 'sourcenodes.export_body'
    bl_label = 'Export'
    bl_options = {'REGISTER', 'INTERNAL'}

    node: bpy.props.StringProperty(options={'HIDDEN'})

    def execute(self, context: Context) -> set:
        '''Execute the operator'''
        node: Node = eval(self.node)

        export_body(node)

        return {'FINISHED'}
