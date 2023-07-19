# Code Challenge 35

---

## add_vertex method:
### Add a vertex to the graph
### Arguments: value
### Returns: The added vertex

---

## add_edge method:
### Adds a new edge between two vertices in the graph
### Arguments: 2 vertices to be connected by the edge, weight (optional)
### Returns: nothing

---

## get_vertices method:
### Arguments: none
### Returns all of the vertices in the graph as a list, Empty collection returned if there are no vertices

---

## get_neighbors method:
### Arguments: vertex
### Returns a collection of edges connected to the given vertex, Includes the weight of the connection in the returned collection
### Empty collection returned if there are no vertices

---

## size method:
### Arguments: none
### Returns the total number of vertices in the graph, 0 if there are none

---

## breadth_first method:
### Traverses the graph based on the breadth first algorithm starting from the given node
### arguments: node
### returns: the connected graph vertices to the given node

---

## business_trip method:
### takes a list of vertices and returns the weight from the first vertex to the last one if there is direct connection between each vertex and the one after it.
### Arguments: list of vertices.
### Returns: the weight from the first vertex to the last vertex if there is direct connection between each vertex and the one after it else returns null.

---
## Whiteboard Process for cc35
[Whiteboard Process](./pics/cc35.jpg)

## Whiteboard Process for cc36
[Whiteboard Process](./pics/cc36.jpg)

## Whiteboard Process for cc37
[Whiteboard Process](./pics/cc37.jpg)

---

## Approach & Efficiency

---
## add_vertex method:
### O(1) Time performance --> because we dont depend on the input size.
### O(1) Space performance --> the size of memory taken does not depend on the input size.

## add_edge method:
### O(1) Time performance --> because we dont depend on the input size.
### O(1) Space performance --> the size of memory taken does not depend on the input size.

## get_vertices method:
### O(n) Time performance --> because we depend on the input size in the loop we use.
### O(n) Space performance --> the size of memory taken depends on the input size.

## get_neighbors method:
### O(n) Time performance --> because we depend on the input size in the loop we use.
### O(n) Space performance --> the size of memory taken depends on the input size.

## size method:
### O(n) Time performance --> because we depend on the input size in the loop we use.
### O(1) Space performance --> the size of memory taken does not depend on the input size.

## breadth_first method:
### O(n) Time performance --> because we depend on the input size in the loop we use.
### O(n) Space performance --> the size of memory taken depends on the input size.

## business_trip method:
### O(n*2) Time performance --> because we depend on the input size in the loop we use **nested for loop that iterates over the input**.
### O(n) Space performance --> the size of memory taken depends on the input size.

---


## Solution:

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
        add_vertex = Node(value)
        self.adj_list[add_vertex] = []
        return add_vertex
    
    def add_edge(self,node1, node2, weight=0):
        if node1 not in self.adj_list:
            return("this node is not in the graph")
        
        if node2 not in self.adj_list:
            return("this node is not in the graph")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def get_vertices(self):
        res = self.adj_list.keys()
        vertices = []
        for x in res:
            vertices.append(x.value)
        return vertices
    
    def get_neighbors(self, vertex):
        res = self.adj_list[vertex]
        neighbors = []
        for x in res:
            neighbors.append((x.vertex.value,x.weight))
        return  neighbors
    
    def size(self):
        return len(self.adj_list.keys())

    def breadth_first(self, node):
        
        all_vertices = []
        visiting_queue = [node]
        visited_vertices = {}
        visited_vertices[node.value] = True  
        while len(visiting_queue) > 0:
            front = visiting_queue.pop(0)
            all_vertices.append(front.value)
            for x in self.adj_list[front]:
                if x.vertex.value not in visited_vertices: 
                    visited_vertices[x.vertex.value] = True
                    visiting_queue.append(x.vertex)
        return all_vertices

    def  business_trip(self,list_of_cities):
        
        total_cost = 0
        
        for idx, item in enumerate (list_of_cities): # O(n) time
            neighbors = self.get_neighbors(item) # O(n) space and time
            dict_of_neighbors = {}
            if idx <len(list_of_cities)-1:
                for x in neighbors: # O(n) space and time
                    dict_of_neighbors[x[0]] = x[1]  
                if list_of_cities[idx+1].value in dict_of_neighbors:
                    weight = dict_of_neighbors[list_of_cities[idx+1].value]
                    total_cost += weight
                else:
                    return 'null'
        return total_cost

    def __str__(self):
        output = ''
        for vertex in self.adj_list:
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{vertex}--weight:{edge.weight}--{edge.vertex}: -----/ '
            output += '\n'
        return output
