"""
Co-occurrence Matrix / Chord Diagram
===============================================================================



>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_matrix_chord_diagram.png"
>>> co_occurrence_matrix_chord_diagram(
...     column='author_keywords',
...     min_occ=5,    
...     directory=directory,
... ).savefig(file_name)


.. image:: images/co_occurrence_matrix_chord_diagram.png
    :width: 700px
    :align: center


"""


from .co_occurrence_matrix import co_occurrence_matrix
from .chord_diagram import ChordDiagram


def co_occurrence_matrix_chord_diagram(
    column,
    min_occ=1,
    max_terms=150,
    normalization=None,
    directory="./",
    figsize=(7, 7),
):

    matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        directory=directory,
    )

    max_value = matrix.max().max()

    # ---< network >---------------------------------------------------------------------
    names = matrix.columns.get_level_values(0)
    n_cols = matrix.shape[1]
    edges = []
    for i_row in range(1, n_cols):
        for i_col in range(0, i_row):
            if matrix.iloc[i_row, i_col] > 0:
                edges.append(
                    {
                        "source": names[i_row],
                        "target": names[i_col],
                        "linewidth": 3 * matrix.iloc[i_row, i_col] / max_value,
                    }
                )

    # -----------------------------------------------------------------------------------
    size = {name: 0 for name in names}
    for edge in edges:
        size[edge["source"]] += 1
        size[edge["target"]] += 1
    nodes = [(name, dict(s=size[name])) for name in size.keys()]

    # -----------------------------------------------------------------------------------

    chord_diagram = ChordDiagram()
    for (name, props) in nodes:
        chord_diagram.add_node(name, **props)
    for edge in edges:
        chord_diagram.add_edge(
            edge["source"], edge["target"], linewidth=edge["linewidth"]
        )

    # -----------------------------------------------------------------------------------

    return chord_diagram.plot(
        figsize=figsize,
        R=3,
        dist=0.2,
        n_bezier=100,
    )
