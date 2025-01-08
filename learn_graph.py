
"""
Let's create a graph class and perform DFH(Depth First Search) and BFH(Breadth First Search)
Graph :

A - B,
B - C,
B - D,
C - E,
D - E,
D - F

"""


class Graph:
    """
    Graph body consists of a dict with the following format : vertices as keys and edges as set
    {
        'A' : {'B', 'C'}
        ...
    }
    """
    def __init__(self, graph_body=None, directed=False):
        if graph_body is None:
            graph_body = dict()

        self.graph_body = graph_body
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex in self.graph_body.keys():
            print("Edge already exists :", vertex)
            return False

        self.graph_body[vertex] = list()
        return True

    def add_edges(self, vertex, edge):
        if vertex not in self.graph_body.keys():
            print("Vertex not found, adding vertex : ", vertex)
            self.add_vertex(vertex)

        # Add edge as vertex as well
        if edge not in self.graph_body.keys():
            print("Vertex not found, adding vertex : ", edge)
            self.add_vertex(edge)

        if edge in self.graph_body[vertex]:
            print("Edge already added")
            return False

        self.graph_body[vertex].append(edge)
        if not self.directed:
            self.graph_body[edge].append(vertex)

        return True

    def print_graph_body(self):
        print(self.graph_body)

    def get_adjacent_nodes(self, node):
        return self.graph_body.get(node) if self.graph_body.get(node) else []

    def is_node_present(self, node):
        return node in self.graph_body.keys()

    def _dfs_rec(self, node, visited, out_list):
        out_list.append(node)

        for next_node in self.graph_body[node]:
            if not visited[next_node]:
                visited[next_node] = True
                self._dfs_rec(next_node, visited, out_list)

    def dfs(self, start):
        """
        Depth First Search
        :param start:
        :return: list of vertices in dfs order
        """
        # if start not in self.graph_body.keys():
        if not self.is_node_present(start):
            print("Vertex(node) not found in graph : ", start)
            return None

        visited = {node: False for node in self.graph_body}
        out_list = list()
        visited[start] = True
        self._dfs_rec(start, visited, out_list)
        return out_list

    def bfs(self, start):
        """
        Breadth First Search
        :param start:
        :return:
        """
        # if start not in self.graph_body.keys():
        if not self.is_node_present(start):
            print("Vertex(node) not found in graph : ", start)
            return None

        node_queue = list()
        node_queue.append(start)
        visited = {node: False for node in self.graph_body.keys()}
        visited[start] = True
        out_list = list()

        while node_queue:
            node = node_queue.pop(0)
            out_list.append(node)

            for next_node in self.graph_body[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    node_queue.append(next_node)

        return out_list

    def is_cyclic(self):
        """
        Use bfs method to traverse all items and check if reaching a reached node. If yes then cyclic
        :return: True/False
        """
        start = list(self.graph_body.keys())[0]
        node_queue = list()
        visited = {node: False for node in self.graph_body.keys()}
        visited[start] = True
        node_queue.append(start)

        while node_queue:
            node = node_queue.pop(0)

            for next_node in self.graph_body[node]:
                if visited[next_node]:
                    return True
                visited[next_node] = True
                node_queue.append(next_node)

        return False

    def find_all_shortest_path_mapping_for_a_source(self, source):
        if not self.is_node_present(source):
            print("Source not found : {}".format(source))
            return None

        node_queue = list()
        visited = {node: False for node in self.graph_body.keys()}
        destination_source_mapping = {node: None for node in self.graph_body.keys()}
        visited[source] = True
        node_queue.append(source)

        while node_queue:
            node = node_queue.pop(0)
            for next_node in self.get_adjacent_nodes(node):
                if not visited[next_node]:
                    visited[next_node] = True
                    destination_source_mapping[next_node] = node
                    node_queue.append(next_node)

        return destination_source_mapping

    def find_shortest_path(self, source, destination):
        if not self.is_node_present(source) or not self.is_node_present(destination):
            print("Source : {} or Destination : {} not found".format(source, destination))
            return None

        all_mapping_for_a_source = self.find_all_shortest_path_mapping_for_a_source(source)
        if not all_mapping_for_a_source:
            return None

        print("All mapping, source mapping should be None : {}".format(all_mapping_for_a_source))
        if all_mapping_for_a_source.get(source) is not None:
            print("Source mapping should be None, incorrect logic")
            return None

        output_path = list()
        mapping = destination

        while mapping:
            print(mapping)
            output_path.append(mapping)
            mapping = all_mapping_for_a_source[mapping]

        return list(reversed(output_path))


if __name__ == "__main__":
    # Create a graph instance
    my_graph = Graph()

    # Add edges, vertex will automatically be added
    my_graph.add_edges('A', 'B')
    my_graph.add_edges('B', 'C')
    my_graph.add_edges('B', 'D')
    my_graph.add_edges('C', 'E')
    my_graph.add_edges('D', 'E')
    my_graph.add_edges('D', 'F')

    # my_graph.add_edges(0, 1)
    # my_graph.add_edges(0, 2)
    # my_graph.add_edges(1, 3)
    # my_graph.add_edges(1, 4)
    # my_graph.add_edges(2, 4)

    # print(my_graph.dfs(0))
    # print(my_graph.bfs(0))

    my_graph.print_graph_body()

    print(my_graph.dfs('A'))
    print(my_graph.bfs('A'))

    print("Is this graph cyclic : ", my_graph.is_cyclic())

    start_node = 'A'
    end_node = 'E'
    print("Shortest route between {} and {} : {}".format(start_node, end_node,
                                                         my_graph.find_shortest_path(start_node, end_node)))