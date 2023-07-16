from cc35.graph import Graph

def test_graph_one():
    graph = Graph()

    a = graph.add_vertex("A")
    actual = str(graph)
    expected = "A -> \n"
    assert actual == expected

def test_graph_two():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    graph.add_edge(a,b,2)
    actual = str(graph)
    expected = "A -> A--weight:2--B: -----/ \nB -> B--weight:2--A: -----/ \n"
    assert actual == expected

def test_graph_three():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    actual = graph.get_vertices()
    expected =['A', 'B', 'C', 'D']
    assert actual == expected

def test_graph_four():
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
    actual = graph.get_neighbors(d)
    expected =[('B', 4), ('C', 5)]
    assert actual == expected

def test_graph_five():
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
    actual = graph.size()
    expected =4
    assert actual == expected

def test_graph_five():
    graph = Graph()

    a = graph.add_vertex("A")

    graph.add_edge(a,None,2)
    actual = str(graph)
    expected ="A -> \n"
    assert actual == expected
################################################## breadth first tests #########################################################
################################ testing breadth first on a graph where all vertices are connected
def test_graph_six():
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
    actual = graph.breadth_first(a)
    expected =['A', 'B', 'C', 'D']
    assert actual == expected
################################ testing breadth first on a graph where all vertices are not connected (there is an isolated vertex) starting
################################ from a connected vertex
def test_graph_seven():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")


    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.breadth_first(a)
    expected =['A', 'B', 'C', 'D']
    assert actual == expected
################################ testing breadth first on a graph where all vertices are not connected (there is an isolated vertex) starting
################################ from an isolated vertex
def test_graph_eight():
    graph = Graph()

    a = graph.add_vertex("A")
    b = graph.add_vertex("B")
    c = graph.add_vertex("C")
    d = graph.add_vertex("D")
    e = graph.add_vertex("E")

    graph.add_edge(a,b,2)
    graph.add_edge(a,c,3)
    graph.add_edge(c,b,3)
    graph.add_edge(d,b,4)
    graph.add_edge(d,c,5)
    actual = graph.breadth_first(e)
    expected =['E']
    assert actual == expected