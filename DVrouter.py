####################################################
# DVrouter.py
# Name:
# HUID:
#####################################################

from router import Router


class DVrouter(Router):
    """Distance vector routing protocol implementation.

    Add your own class fields and initialization code (e.g. to create forwarding table
    data structures). See the `Router` base class for docstrings of the methods to
    override.
    """

    def __init__(self, addr, heartbeat_time):
        Router.__init__(self, addr)  # Initialize base class - DO NOT REMOVE
        self.heartbeat_time = heartbeat_time
        self.last_time = 0
        # TODO
        #   add your own class fields and initialization code here
        pass

    def handle_packet(self, port, packet):
        """Process incoming packet."""
        # TODO
        if packet.is_traceroute:
            # Hint: this is a normal data packet
            # If the forwarding table contains packet.dst_addr
            #   send packet based on forwarding table, e.g., self.send(port, packet)
            pass
        else:
            # Hint: this is a routing packet generated by your routing protocol
            # If the received distance vector is different
            #   update the local copy of the distance vector
            #   update the distance vector of this router
            #   update the forwarding table
            #   broadcast the distance vector of this router to neighbors
            pass

    def handle_new_link(self, port, endpoint, cost):
        """Handle new link."""
        # TODO
        #   update the distance vector of this router
        #   update the forwarding table
        #   broadcast the distance vector of this router to neighbors
        pass

    def handle_remove_link(self, port):
        """Handle removed link."""
        # TODO
        #   update the distance vector of this router
        #   update the forwarding table
        #   broadcast the distance vector of this router to neighbors
        pass

    def handle_time(self, time_ms):
        """Handle current time."""
        if time_ms - self.last_time >= self.heartbeat_time:
            self.last_time = time_ms
            # TODO
            #   broadcast the distance vector of this router to neighbors
            pass

    def __repr__(self):
        """Representation for debugging in the network visualizer."""
        # TODO
        #   NOTE This method is for your own convenience and will not be graded
        return f"DVrouter(addr={self.addr})"
