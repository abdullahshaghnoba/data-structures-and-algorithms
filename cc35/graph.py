class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        """
        Add a vertex to the graph
        Arguments: value
        Returns: The added vertex
        """
        add_vertex = Node(value)
        self.adj_list[add_vertex] = []
        return add_vertex
    
    def add_edge(self,node1, node2, weight=0):
        """
        Adds a new edge between two vertices in the graph
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        """
        if node1 not in self.adj_list:
            return("this node is not in the graph")
        
        if node2 not in self.adj_list:
            return("this node is not in the graph")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def get_vertices(self):
        """
        Arguments: none
        Returns all of the vertices in the graph as a list, Empty collection returned if there are no vertices
        """
        res = self.adj_list.keys()
        vertices = []
        for x in res:
            vertices.append(x.value)
        return vertices
    
    def get_neighbors(self, vertex):
        """
        Arguments: vertex
        Returns a collection of edges connected to the given vertex, Includes the weight of the connection in the returned collection
        Empty collection returned if there are no vertices
        """
        res = self.adj_list[vertex]
        neighbors = []
        for x in res:
            neighbors.append((x.vertex.value,x.weight))
        return  neighbors
    
    def size(self):
        """
        Arguments: none
        Returns the total number of vertices in the graph, 0 if there are none
        """
        return len(self.adj_list.keys())

    def __str__(self):
        output = ''
        for vertex in self.adj_list:
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{vertex}--weight:{edge.weight}--{edge.vertex}: -----/ '
            output += '\n'
        return output

if __name__=='__main__':
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")

    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    # print(graph.get_vertices())
    print(graph.get_neighbors(d))
    # print(graph.size())
    # print(graph)