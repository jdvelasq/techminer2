"""
Lotka's Law
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/lotka.png"
>>> lotka_law(directory=directory).savefig(file_name)

.. image:: images/lotka.png
    :width: 700px
    :align: center


>>> lotka_law(directory=directory, plot=False)
   Num Authors        %  ...  Acum Num Documents % Acum Num Documents
0            1   0.16 %  ...                   5                2.04%
1            2   0.31 %  ...                  11                4.49%
2           35   5.48 %  ...                  49                20.0%
3          601  94.05 %  ...                 245               100.0%
<BLANKLINE>
[4 rows x 9 columns]

"""


import matplotlib.pyplot as plt
import pandas as pd

from .column_indicators import column_indicators
from .utils import *


def _lotka_core_authors(directory="./"):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core authors of the records
    """
    documents = load_filtered_documents(directory)
    documents = documents.copy()

    z = column_indicators(column="authors", sep="; ", directory=directory)[
        "num_documents"
    ]

    authors_dict = {
        author: num_docs for author, num_docs in zip(z.index, z) if not pd.isna(author)
    }

    #
    #  Num Authors x Documents written per Author
    #
    # z = z[["num_documents"]]
    z = z.to_frame(name="num_documents")
    z = z.groupby(["num_documents"]).size()
    w = [str(round(100 * a / sum(z), 2)) + " %" for a in z]
    z = pd.DataFrame(
        {"Num Authors": z.tolist(), "%": w, "Documents written per Author": z.index}
    )
    z = z.sort_values(["Documents written per Author"], ascending=False)
    z["Acum Num Authors"] = z["Num Authors"].cumsum()
    z["% Acum"] = [
        str(round(100 * a / sum(z["Num Authors"]), 2)) + " %"
        for a in z["Acum Num Authors"]
    ]
    m = explode(documents[["authors", "record_no"]], "authors", sep="; ")
    m = m.dropna()
    m["Documents_written"] = m.authors.map(lambda w: authors_dict[w])

    n = []
    for k in z["Documents written per Author"]:
        s = m.query("Documents_written >= " + str(k))
        s = s[["record_no"]]
        s = s.drop_duplicates()
        n.append(len(s))

    k = []
    for index in range(len(n) - 1):
        k.append(n[index + 1] - n[index])
    k = [n[0]] + k
    z["Num Documents"] = k
    z["% Num Documents"] = [str(round(i / max(n) * 100, 2)) + "%" for i in k]
    z["Acum Num Documents"] = n
    z["% Acum Num Documents"] = [str(round(i / max(n) * 100, 2)) + "%" for i in n]

    z = z[
        [
            "Num Authors",
            "%",
            "Acum Num Authors",
            "% Acum",
            "Documents written per Author",
            "Num Documents",
            "% Num Documents",
            "Acum Num Documents",
            "% Acum Num Documents",
        ]
    ]

    return z.reset_index(drop=True)


def lotka_law(
    cmap="Greys",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """

    fig, ax_ = plt.subplots(figsize=figsize)
    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    data = _lotka_core_authors(directory)

    if plot is False:
        return data

    percentage_authors = data["%"].map(lambda w: float(w[:-2])).tolist()
    percentage_authors.reverse()
    documents_written = data["Documents written per Author"].tolist()
    documents_written.reverse()
    total_authors = data["Num Authors"].max()
    theoretical = [total_authors / float(x * x) for x in documents_written]
    total_theoretical = sum(theoretical)
    perc_theoretical_authors = [w / total_theoretical * 100 for w in theoretical]

    ax_.plot(
        documents_written,
        percentage_authors,
        linestyle="-",
        linewidth=2,
        color="k",
    )
    ax_.fill_between(
        documents_written,
        percentage_authors,
        color=color,
        alpha=0.6,
    )

    ax_.plot(
        documents_written,
        perc_theoretical_authors,
        linestyle=":",
        linewidth=4,
        color="k",
    )

    for side in ["top", "right", "left", "bottom"]:
        ax_.spines[side].set_visible(False)

    ax_.grid(axis="y", color="gray", linestyle=":")
    ax_.grid(axis="x", color="gray", linestyle=":")
    ax_.tick_params(axis="x", labelsize=7)
    ax_.tick_params(axis="y", labelsize=7)
    ax_.set_ylabel("% of Authors", fontsize=9)
    ax_.set_xlabel("Documets written per Author", fontsize=9)

    ax_.set_title(
        "Frequency distribution of scientific productivity",
        fontsize=10,
        color="dimgray",
        loc="left",
    )

    fig.set_tight_layout(True)

    return fig
