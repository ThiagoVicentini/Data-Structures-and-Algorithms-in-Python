class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_value):
        new_node = Node(new_node_value)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_value, node_from_value, node_to_value):
        node_from = None
        node_to = None
        
        for node in self.nodes:
            if node.value == node_from_value:
                node_from = node
            if node.value == node_to_value:
                node_to = node
        
        if node_from == None:
            node_from = Node(node_from_value)
            self.nodes.append(node_from)
        if node_to == None:
            node_to = Node(node_to_value)
            self.nodes.append(node_to)

        new_edge = Edge(new_edge_value, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        edge_list = []

        for edge in self.edges:
            edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))

        return edge_list

    def get_adjacency_list(self):
        adjacency_list = [None]*(len(self.nodes)+1)

        for edge in self.edges:
            if adjacency_list[edge.node_from.value]:
                adjacency_list[edge.node_from.value].append((edge.node_to.value, edge.value))    
            else:
                adjacency_list[edge.node_from.value] = [(edge.node_to.value, edge.value)]
                
        return adjacency_list

    def get_adjacency_matrix(self):
        length = len(self.nodes) + 1
        adjacency_matrix = [[0 for i in range(length)] for j in range(length)]

        for edge in self.edges:
            adjacency_matrix[edge.node_from.value][edge.node_to.value] = edge.value            

        return adjacency_matrix

# Case test
if __name__ == "__main__":
    
    # Setup
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)

    # Testing functions
    print(graph.get_edge_list())            # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print(graph.get_adjacency_list())       # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    
    print(graph.get_adjacency_matrix())     
    
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
  
    #    0   1   2   3   4
    # 0 |0   0   0   0   0  | 
    # 1 |0   0   100 101 102| 
    # 2 |0   0   0   0   0  | 
    # 3 |0   0   0   0   103| 
    # 4 |0   0   0   0   0  | 
    # 