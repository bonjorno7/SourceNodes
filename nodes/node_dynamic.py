from bpy.types import NodeSocketVirtual


class SOURCENODES_node_dynamic:
    '''Mixin class for dynamic nodes'''

    def ensure_virtual_socket(self) -> NodeSocketVirtual:
        '''Create a virtual input socket if one does not exist'''
        for socket in self.inputs:
            if isinstance(socket, NodeSocketVirtual):
                return socket

        return self.inputs.new(NodeSocketVirtual.__name__, '')

    def handle_virtual_socket(self, socket_types: tuple[type]):
        '''Create new socket for link to virtual socket if there is one'''
        virtual_socket = self.ensure_virtual_socket()

        if virtual_socket.is_linked:
            link = virtual_socket.links[0]
            from_socket = link.from_socket

            self.id_data.links.remove(link)

            if isinstance(from_socket, socket_types):
                to_socket = self.inputs.new(
                    type(from_socket).__name__,
                    type(from_socket).bl_label,
                )

                self.id_data.links.new(to_socket, from_socket)

                from_index = list(self.inputs).index(virtual_socket)
                self.inputs.move(from_index, len(self.inputs) - 1)

    def sort_sockets(self, socket_types: tuple[type]):
        '''Sort input sockets by type, only affect given types'''
        socket_table = {cls: [] for cls in socket_types}

        for socket in self.inputs:
            if isinstance(socket, socket_types):
                socket_table[type(socket)].append(socket)

        for sockets in socket_table.values():
            for socket in sockets:
                from_index = list(self.inputs).index(socket)
                self.inputs.move(from_index, len(self.inputs) - 2)
