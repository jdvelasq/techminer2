import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


def corr_map(matrix):

    matrix = matrix.copy()
    matrix = pd.melt(
        matrix,
        var_name="to",
        value_name="value",
        ignore_index=False,
    )
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={matrix.columns[0]: "from"})

    return matrix
