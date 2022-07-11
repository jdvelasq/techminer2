"""
Lotka's Law
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/lotka_law.html"

>>> lotka_law(directory=directory).write_html(file_name)

.. raw:: html

    <iframe src="_static/lotka_law.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> lotka_law(directory=directory, plot=False)
   Num Authors        %  ...  Acum Num Documents % Acum Num Documents
0            1   0.52 %  ...                   7                7.45%
1            1   0.52 %  ...                   7                7.45%
2            2   1.04 %  ...                   7                7.45%
3            2   1.04 %  ...                  10               10.64%
4            9   4.66 %  ...                  21               22.34%
5          178  92.23 %  ...                  94               100.0%
<BLANKLINE>
[6 rows x 9 columns]


"""
import pandas as pd
import plotly.express as px

from ._read_records import read_records
from .column_indicators import column_indicators


def lotka_law(
    directory="./",
    plot=True,
):
    """Lotka's Law"""

    data = _lotka_core_authors(directory)

    if plot is False:
        return data

    # fig, ax_ = plt.subplots(figsize=figsize)
    # cmap = plt.cm.get_cmap(cmap)
    # color = cmap(0.6)

    percentage_authors = data["%"].map(lambda w: float(w[:-2])).tolist()
    percentage_authors.reverse()
    documents_written = data["Documents written per Author"].tolist()
    documents_written.reverse()
    total_authors = data["Num Authors"].max()
    theoretical = [total_authors / float(x * x) for x in documents_written]
    total_theoretical = sum(theoretical)
    perc_theoretical_authors = [w / total_theoretical * 100 for w in theoretical]

    fig = px.area(
        x=documents_written,
        y=percentage_authors,
        title="Lotka's Law",
        markers=True,
    )

    return fig

    # ax_.plot(
    #     documents_written,
    #     percentage_authors,
    #     linestyle="-",
    #     linewidth=2,
    #     color="k",
    # )
    # ax_.fill_between(
    #     documents_written,
    #     percentage_authors,
    #     color=color,
    #     alpha=0.6,
    # )

    # ax_.plot(
    #     documents_written,
    #     perc_theoretical_authors,
    #     linestyle=":",
    #     linewidth=4,
    #     color="k",
    # )

    # for side in ["top", "right", "left", "bottom"]:
    #     ax_.spines[side].set_visible(False)

    # ax_.grid(axis="y", color="gray", linestyle=":")
    # ax_.grid(axis="x", color="gray", linestyle=":")
    # ax_.tick_params(axis="x", labelsize=7)
    # ax_.tick_params(axis="y", labelsize=7)
    # ax_.set_ylabel("% of Authors", fontsize=9)
    # ax_.set_xlabel("Documets written per Author", fontsize=9)

    # ax_.set_title(
    #     "Frequency distribution of scientific productivity",
    #     fontsize=10,
    #     color="dimgray",
    #     loc="left",
    # )

    # fig.set_tight_layout(True)

    # return fig


def _lotka_core_authors(directory="./", database="documents"):

    records = read_records(directory=directory, database=database, use_filter=False)

    z = column_indicators(column="authors", sep=";", directory=directory)["OCC"]

    authors_dict = {
        author: num_docs for author, num_docs in zip(z.index, z) if not pd.isna(author)
    }

    #
    #  Num Authors x Documents written per Author
    #
    z = z.to_frame(name="OCC")
    z = z.groupby(["OCC"]).size()
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
    # ---- remove explode ------------------------------------------------------------>>>
    m = records[["authors", "record_no"]].copy()
    m["authors"] = m["authors"].str.split(";")
    m = m.explode("authors")
    m["authors"] = m["authors"].str.strip()
    # <<<--------------------------------------------------------------------------------
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
