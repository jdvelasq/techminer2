"""
Most frequent authors
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_frequent_authors.png"
>>> most_frequent_authors(directory=directory).savefig(file_name)

.. image:: images/most_frequent_authors.png
    :width: 500px
    :align: center


>>> most_frequent_authors(directory=directory, plot=False).head()
            num_documents  frac_num_documents
authors                                      
Wojcik D                5            3.200000
Rabbani MR              3            0.726190
Hornuf L                3            1.250000
Parker C                2            0.500000
Yuksel S                2            0.416667


>>> most_frequent_authors(directory=directory, use_frac_num_documents=True, plot=False).head()
            num_documents  frac_num_documents
authors                                      
Wojcik D                5                 3.2
Serrano W               2                 2.0
Bernards N              2                 2.0
Omarini AE              2                 2.0
Iman N                  2                 2.0


"""


from .cleveland_dot_chart import cleveland_dot_chart
from .utils import load_filtered_documents


def most_frequent_authors(
    top_n=20,
    use_frac_num_documents=False,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    documents = load_filtered_documents(directory=directory)
    indicators = documents[["authors", "frac_num_documents"]]
    indicators = indicators.assign(authors=indicators.authors.str.split(";"))
    indicators = indicators.explode("authors")
    indicators = indicators.assign(authors=indicators.authors.str.strip())
    indicators = indicators.assign(num_documents=1)
    indicators = indicators.groupby("authors", as_index=False).agg(
        {"num_documents": "sum", "frac_num_documents": "sum"}
    )
    if use_frac_num_documents:
        indicators = indicators.sort_values("frac_num_documents", ascending=False)
    else:
        indicators = indicators.sort_values("num_documents", ascending=False)

    indicators = indicators.set_index("authors")

    if plot is False:
        return indicators[["num_documents", "frac_num_documents"]].head(top_n)

    if use_frac_num_documents:
        indicators = indicators.frac_num_documents
    else:
        indicators = indicators.num_documents

    indicators = indicators.head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most frequent authors",
        xlabel="Num Documents",
        ylabel="Author",
    )
