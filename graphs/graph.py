import math;

class Graph(object):

    def __init__(self):
        self.nodes = {}
        self.connections = []

    def add_node(self, node_key, x = -1, y = -1):
        self.nodes[node_key] = (x, y)

    def connect(self, first_node, second_node, weight=-1):
        if weight < 0:
            weight = self.compute_weight(first_node, second_node)
        self.connections.append((first_node, second_node, weight))

    def compute_weight(self, first_node, second_node):
        xdiff = self.nodes[first_node][0] - self.nodes[second_node][0]
        ydiff = self.nodes[first_node][1] - self.nodes[second_node][1]
        return math.sqrt(xdiff*xdiff + ydiff*ydiff)

    def kruskal_mst(self):
        path = GraphPath(self)
        sorted_connections = sorted(self.connections, key=lambda conn: conn[2])
        for connection in sorted_connections:
            if not path.check_connection_cycle(connection):
                path.add_connection(connection)
        return path

    def get_connections(self, node):
        connections = []
        for connection in self.connections:
            if connection[0] == node or connection[1] == node:
                connections.append(connection)
        return connections

    def show_on_console(self):
        print("I am a graph")
        print("My nodes are " + str(self.nodes))
        print("My connections are " + str(self.connections))

class GraphPath(object):

    def __init__(self, graph):
        self.graph = graph
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def check_connection_cycle(self, connection):
        return self.can_reach(connection[0], connection[1], [])

    def can_reach(self, origin, destiny, checked = []):
        if (origin, destiny) in checked:
            return False
        connections = self.get_connections(origin)
        checked.append((origin, destiny))
        for connection in connections:
            other = connection[1] if connection[0] == origin else connection[0]
            if other == destiny:
                return True
            else:
                if self.can_reach(other, destiny, checked):
                    return True
        return False

    def get_connections(self, node):
        connections = []
        for connection in self.connections:
            if connection[0] == node or connection[1] == node:
                connections.append(connection)
        return connections

    def show_on_console(self):
        print("Path connection is "+ str(self.connections))
