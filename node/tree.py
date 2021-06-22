import bpy
from bpy.types import NodeReroute, NodeTree


class SourceNodeTree(NodeTree):
    '''Node based export for Source models'''
    bl_label = 'Source Nodes'
    bl_icon = 'FILE_3D'

    def update(self):
        '''Called when node graph is changed'''
        self.remove_reroute_nodes()
        bpy.app.timers.register(self.mark_invalid_links)

    def remove_reroute_nodes(self):
        '''Remove reroute nodes and attempt to replace their links'''
        for node in self.nodes:
            if isinstance(node, NodeReroute):
                reroute_input = node.inputs[0]
                reroute_output = node.outputs[0]

                if reroute_input.is_linked:
                    input_link = reroute_input.links[0]
                    output_socket = input_link.from_socket

                    for output_link in reroute_output.links:
                        input_socket = output_link.to_socket
                        self.links.new(input_socket, output_socket)

                self.nodes.remove(node)

    def mark_invalid_links(self):
        '''Mark invalid links, must be called from a timer'''
        for link in self.links:
            if type(link.from_socket) != type(link.to_socket):
                link.is_valid = False


classes = (SourceNodeTree,)


def register():
    '''Register this module'''
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    '''Unregister this module'''
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
