import bpy
from bpy.types import Context, Operator

from ..sdk.file import export_script


class SOURCENODES_OT_export_script(Operator):
    bl_idname = 'sourcenodes.export_script'
    bl_label = 'Export'
    bl_description = 'Export the given script to a file'
    bl_options = {'REGISTER', 'INTERNAL'}

    node: bpy.props.StringProperty(options={'HIDDEN'})

    def execute(self, context: Context) -> set:
        node = eval(self.node)
        export_script(node)

        return {'FINISHED'}


classes = (SOURCENODES_OT_export_script,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
