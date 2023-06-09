import json
import os
import random
from os import path

class GraphCreator:
    def __init__(self, file_location=None):
        self.graph_edges = {}
        self.graph_edge_weights = {}
        self.labels = {}

        if file_location is not None:
            self.open_file(file_location)

    def open_file(self, file_location):
        print(f'Opening file {file_location}.')
        with open(file_location, 'r') as file:
            data = file.read()
            graph_data = json.loads(data)
            if 'edges' in graph_data:
                self.graph_edges = graph_data['edges']
            if 'edge-weights' in graph_data:
                self.graph_edge_weights = graph_data['edge-weights']
            if 'labels' in graph_data:
                self.graph_edge_weights = graph_data['labels']
            print('File opened successfully.')

    def save(self, file_location):
        print(f'Writing to file {file_location}.')
        with open(file_location, 'w') as file:
            graph_structure = {'edges': self.graph_edges,
                               'edge-weights': self.graph_edge_weights,
                               'labels': self.labels}
            graph_data = json.dumps(graph_structure)
            file.write(graph_data)
            print('File written successfully.\n')

    def create_vertices(self, vertex_count, maximum_edges=20, maximum_weight=2000, minimum_edges=1):
        self.create_edges(vertex_count, maximum_edges, minimum_edges)
        self.create_edge_weights(maximum_weight)
        label_maximum = max(1000, vertex_count * 5)
        self.create_labels(label_maximum)

    def create_edges(self, vertex_count, maximum_edges, minimum_edges=1):
        print("Creating edges...\n")
        self.graph_edges = {}
        for index in range(vertex_count):
            edges = []
            edge_count = random.randint(minimum_edges, maximum_edges)
            for edge_index in range(edge_count):
                random_vertex = random.randint(0, vertex_count - 1)
                edges.append(random_vertex)
            print(f'\"{index}\": {edges},')
            self.graph_edges[index] = edges
        print("\nEdges created successfully.\n")

    def create_edge_weights(self, maximum_weight=2000):
        print("Creating edge weights...\n")
        self.graph_edge_weights = {}
        for index, graph_edge in self.graph_edges.items():
            length = len(graph_edge)
            weights = []
            for i in range(length):
                random_int = random.randint(0, maximum_weight)
                weights.append(random_int)
            print(f'\"{index}\": {weights},')
            self.graph_edge_weights[index] = weights
        print("\nEdge weights created successfully.\n")

    def create_labels(self, maximum_value=1000, allow_any_value=False):
        if not self.verify_maximum_label_value(maximum_value, allow_any_value):
            return

        print("Creating labels...\n")
        self.labels = {}
        for index in self.graph_edges:
            while True:
                random_int = random.randint(1, maximum_value)
                if (allow_any_value or random_int % 5 == 0) and (random_int not in self.labels.values()):
                    break
            print(f'\"{index}\": {random_int},')
            self.labels[index] = random_int
        print("\nLabels created successfully.\n")

    def verify_maximum_label_value(self, maximum_value, allow_any_value):
        vertex_count = len(self.graph_edges)
        if maximum_value / 5 < vertex_count and not allow_any_value:
            print("Label values are unique and divisible by five. Therefore, "
                  "the maximum must be at least five times the number of vertices.")
            return False
        elif maximum_value < vertex_count:
            print("Label values are unique, so the maximum must be at least the number of vertices.")
            return False
        else:
            return True

parent_directory = os.getcwd()
graph_file = path.join(parent_directory, 'graph-sample.json')
graph = GraphCreator()
graph.create_vertices(1000, 50, 5000, 2)
graph.save(graph_file)
