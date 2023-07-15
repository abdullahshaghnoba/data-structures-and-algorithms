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