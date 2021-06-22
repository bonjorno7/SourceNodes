import bpy
from bpy.types import Context, Node, Operator

from ..sdk.file import export_bodygroup


class SOURCENODES_OT_export_bodygroup(Operator):
    '''Export the bodies in this group'''
    bl_idname = 'sourcenodes.export_bodygroup'
    bl_label = 'Export'
    bl_options = {'REGISTER', 'INTERNAL'}

    node: bpy.props.StringProperty(options={'HIDDEN'})

    def execute(self, context: Context) -> set:
        '''Execute the operator'''
        node: Node = eval(self.node)

        export_bodygroup(node)

        return {'FINISHED'}


classes = (SOURCENODES_OT_export_bodygroup,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
