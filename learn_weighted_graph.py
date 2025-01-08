
"""
Let's create a Weighted graph class and perform DFH(Depth First Search) and BFH(Breadth First Search)
Graph :

A - B,
B - C,
B - D,
C - E,
D - E,
D - F

"""

class WeightedGraph(object):
    """
    Weighted graph body will contain the weight along with the edges in the following format
    Graph = {
        'A' : [('B', 5), ('C', 3)],
        ...
    }
    """
    def __init__(self, weighted=True, directed=False):
        self.weighted = weighted
        self.directed = directed
        self.graph = dict()

    def is_vertex_present(self, vertex):
        return vertex in self.graph.keys()

    def get_edges(self, vertex):
        return self.graph.get(vertex, [])

    def get_vertices(self):
        return list(self.graph.keys())

    def is_edge_associated_with_vertex(self, vertex, edge):
        if not self.is_vertex_present(vertex):
            print("Vertex : {}, not in graph".format(vertex))
            return False

        if self.weighted:
            for single_edge in self.graph[vertex]:
                ed, wt = single_edge
                if edge == ed:
                    return True
            return False
        else:
            return edge in self.get_edges(vertex)

    def add_vertex(self, vertex):
        if self.is_vertex_present(vertex):
            print("Vertex : {}, already present in graph".format(vertex))
            return False

        self.graph[vertex] = list()
        return True

    def add_edges(self, vertex, edge, weight=None):
        # Check if vertex present in graph
        if not self.is_vertex_present(vertex):
            print("Vertex : {}, not in graph, adding".format(vertex))
            self.add_vertex(vertex)

        # Edge is the destination vertex and must also be added to the graph
        if not self.is_vertex_present(edge):
            print("Vertex : {}, not in graph, adding".format(edge))
            self.add_vertex(edge)

        if self.is_edge_associated_with_vertex(vertex, edge):
            print("Edge : {}, already associated with the vertex : {}".format(edge, vertex))
            return False

        if self.weighted:
            self.graph[vertex].append((edge, weight))
            # If not directed graph, then add the inverse connection as well
            if not self.directed:
                self.graph[edge].append((vertex, weight))

        else:
            self.graph[vertex].append(edge)
            # If not directed graph, then add the inverse connection as well
            if not self.directed:
                self.graph[edge].append(vertex)

    def print_graph_body(self):
        print("Graph :", self.graph)

    def dfs_rec(self, node, visited, output_dfs):
        """
        Recursive function for DFS traversal
        :param node:
        :param visited:
        :param output_dfs:
        :return:
        """
        output_dfs.append(node)

        for next_node in self.get_edges(node):
            if self.weighted:
                next_node = next_node[0]

            if not visited[next_node]:
                visited[next_node] = True
                self.dfs_rec(next_node, visited, output_dfs)

    def dfs(self, source):
        """
        Depth First Search
        :param source:
        :return:
        """
        if not self.is_vertex_present(source):
            print("Vertex : {}, not in graph".format(source))
            return None

        visited = {node: False for node in self.get_vertices()}
        output_dfs = list()

        visited[source] = True
        self.dfs_rec(source, visited, output_dfs)
        return output_dfs

    def bfs(self, source):
        """
        Breadth First Search
        :param source:
        :return:
        """
        if not self.is_vertex_present(source):
            print("Vertex : {}, not in graph".format(source))
            return None

        output_bfs = list()
        visited = {node: False for node in self.get_vertices()}
        bfs_queue = list()
        visited[source] = True
        bfs_queue.append(source)

        while bfs_queue:
            node = bfs_queue.pop(0)
            output_bfs.append(node)

            for next_node in self.get_edges(node):
                if self.weighted:
                    next_node = next_node[0]

                print("self.is_edge_associated_with_vertex({}, {}) : {}".format(next_node, node, self.is_edge_associated_with_vertex(next_node, node)))
                if not visited[next_node]:
                    visited[next_node] = True
                    bfs_queue.append(next_node)

        return output_bfs

    def is_cyclic(self):
        """
        We will use Breadth first search to check this
        :return: True/False
        """
        if not self.graph:
            print("Empty graph")
            return False

        source = list(self.graph.keys())[0]
        node_queue = list()
        visited = {node:False for node in self.get_vertices()}
        visited[source] = True
        node_queue.append(source)

        while node_queue:
            node = node_queue.pop(0)
            for next_node in self.get_edges(node):
                if self.weighted:
                    next_node = next_node[0]

                print("self.is_edge_associated_with_vertex({}, {}) : {}".format(next_node, node, self.is_edge_associated_with_vertex(next_node, node)))
                # if not self.is_edge_associated_with_vertex(next_node, node) and visited[next_node]:
                if visited[next_node]:
                    print("Node : {}, next_node : {} : {}".format(node, next_node, self.is_edge_associated_with_vertex(next_node, node)))
                    return True
                elif not visited[next_node]:
                    visited[next_node] = True
                    node_queue.append(next_node)

        return False


if __name__ == "__main__":
    wt_graph = WeightedGraph(weighted=True, directed=True)

    # Add edges, vertex will automatically be added
    # wt_graph.add_edges('A', 'B', weight=5)
    # wt_graph.add_edges('B', 'C', weight=3)
    # wt_graph.add_edges('B', 'D', weight=1)
    # wt_graph.add_edges('C', 'E', weight=2)
    # wt_graph.add_edges('D', 'E', weight=10)
    # wt_graph.add_edges('D', 'F', weight=7)

    wt_graph.add_edges('A', 'B', weight=5)
    wt_graph.add_edges('B', 'C', weight=3)
    wt_graph.add_edges('C', 'D', weight=1)
    wt_graph.add_edges('D', 'E', weight=2)
    wt_graph.add_edges('E', 'F', weight=10)
    wt_graph.add_edges('F', 'A', weight=7)

    # wt_graph.add_edges(0, 1)
    # wt_graph.add_edges(0, 2)
    # wt_graph.add_edges(1, 3)
    # wt_graph.add_edges(1, 4)
    # wt_graph.add_edges(2, 4)

    # print(wt_graph.dfs(0))
    # print(wt_graph.bfs(0))

    wt_graph.print_graph_body()
    print("DFS of graph :", wt_graph.dfs('A'))
    print("BFS of graph :", wt_graph.bfs('A'))
    # {'A': {'B'}, 'B': {'D', 'A', 'C'}, 'C': {'E', 'B'}, 'D': {'E', 'F', 'B'}, 'E': {'C', 'D'}, 'F': {'D'}}

    print("Is Cyclic : ", wt_graph.is_cyclic())