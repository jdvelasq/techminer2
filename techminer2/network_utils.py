"""This module contains functions for network analysis that are common to
several modules.


"""
import networkx as nx
import numpy as np


def compute_graph_layout(graph, k, iterations, seed):
    """Computes the layout of a networkx graph."""
    pos = nx.spring_layout(graph, k=k, iterations=iterations, seed=seed)
    for node in graph.nodes():
        graph.nodes[node]["pos"] = pos[node]
    return graph


def compute_node_sizes(node_occ, node_min_size, node_max_size):
    """Computes the node sizes for a networkx graph."""
    node_sizes = np.array(node_occ)
    node_sizes = node_sizes - node_sizes.min() + node_min_size
    if node_sizes.max() > node_max_size:
        node_sizes = node_min_size + (node_sizes - node_min_size) / (
            node_sizes.max() - node_min_size
        ) * (node_max_size - node_min_size)
    return node_sizes


def compute_textfont_sizes(node_occ, textfont_size_min, textfont_size_max):
    """Computes the textfont sizes for a networkx graph."""
    textfont_sizes = np.array(node_occ)
    textfont_sizes = textfont_sizes - textfont_sizes.min() + textfont_size_min
    if textfont_sizes.max() > textfont_size_max:
        textfont_sizes = textfont_size_min + (textfont_sizes - textfont_size_min) / (
            textfont_sizes.max() - textfont_size_min
        ) * (textfont_size_max - textfont_size_min)
    return textfont_sizes


def compute_textposition(node_x, node_y):
    """Computes the text position for a node in a networkx graph."""
    x_mean = np.mean(node_x)
    y_mean = np.mean(node_y)
    textposition = []
    for x_pos, y_pos in zip(node_x, node_y):
        if x_pos >= x_mean and y_pos >= y_mean:
            textposition.append("top right")
        if x_pos <= x_mean and y_pos >= y_mean:
            textposition.append("top left")
        if x_pos <= x_mean and y_pos <= y_mean:
            textposition.append("bottom left")
        if x_pos >= x_mean and y_pos <= y_mean:
            textposition.append("bottom right")
    return textposition


def extract_node_coordinates(graph):
    """Extracts node coordinates from a networkx graph."""
    node_x = []
    node_y = []
    for node in graph.nodes():
        pos_x, pos_y = graph.nodes[node]["pos"]
        node_x.append(pos_x)
        node_y.append(pos_y)
    return node_x, node_y


def extract_node_names(graph):
    """Extracts node names from a networkx graph."""
    node_names = []
    for node in graph.nodes():
        node_names.append(node)
    return node_names


def extract_node_sizes(graph):
    """Extracts node sizes from a networkx graph."""
    node_sizes = []
    for node in graph.nodes():
        node_sizes.append(graph.nodes[node]["size"])
    return node_sizes


def extract_textfont_sizes(graph):
    """Extracts textfont sizes from a networkx graph."""
    textfont_sizes = []
    for node in graph.nodes():
        textfont_sizes.append(graph.nodes[node]["textfont_size"])
    return textfont_sizes
