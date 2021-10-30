class Vertex:
    def __init__(self, value=None):
        self.value = value
        self.neighbor = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbor.append(neighbor)

    def set_visited(self):
        self.visited = False

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Graph:
    def __init__(self, num_vertices):
        self.vertices = [Vertex() for i in range(0, num_vertices)]
        self.num_vertices = num_vertices

    def set_vertex(self, vertex_index, value):
        if 0 <= vertex_index and vertex_index < self.num_vertices:
            vertex = self.vertices[vertex_index]
            vertex.set_value(value)
            self.vertices[vertex_index] = vertex
        else:
            raise IndexError(
                vertex_index, " is out of range for a list of ", self.num_vertices, " vertices")

        return [i.get_value() for i in self.vertices]

    def get_vertex_index(self, value):
        for i in range(0, self.num_vertices):
            if value == self.vertices[i].get_value():
                return i

        return -1

    def depth_first_search(self, node):

        node.set_visited = True
        print(vertex.value)
        for neighbor in vertex.neighbor:
            if not neighbor.set_visited:
                self.depth_first_search(neighbor)

    def print_vertices(self):
        print([i.get_value() for i in self.vertices])

    def add_edge(self, source, destination):
        vertex_source = self.get_vertex_index(source)
        vertex_destination = self.get_vertex_index(destination)

        if vertex_source == -1:
            raise ValueError("Invalid Source Vertex")
        elif vertex_destination == -1:
            raise ValueError("Invalid Destination Vertex")

        else:
            self.vertices[vertex_source].add_neighbor(
                self.vertices[vertex_destination])
            self.vertices[vertex_destination].add_neighbor(
                self.vertices[vertex_source])

    def print_graph(self):

        for i in range(len(self.vertices)):
            print(self.vertices[i].get_value(), " --> ", end=" ")
            for j in range(len(self.vertices[i].neighbor)):

                print(self.vertices[i].neighbor[j].get_value(), end=" ")
            print()


g = Graph(5)
g.print_vertices()
g.set_vertex(0, "A")
g.set_vertex(1, "B")
g.set_vertex(2, "C")
g.set_vertex(3, "D")
g.set_vertex(4, "E")
print(g.get_vertex_index("E"))
g.add_edge("A", "B")
g.print_graph()
