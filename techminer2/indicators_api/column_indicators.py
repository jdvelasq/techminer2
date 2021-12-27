"""
Column Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> column_indicators('authors',directory=directory).head()
                num_documents  global_citations  local_citations
authors                                                         
Wojcik D                    5                19                4
Hornuf L                    3               110               24
Rabbani MR                  3                39                3
Gomber P                    2               228               34
Worthington AC              2                 7                1



"""

from .utils import load_filtered_documents


def column_indicators(
    column,
    sep="; ",
    directory="./",
):
    """
    Column Indicators
    """

    report = load_filtered_documents(directory)
    report = report.assign(num_documents=1)
    report = report[
        [column, "num_documents", "global_citations", "local_citations"]
    ].copy()

    if sep is not None:
        report[column] = report[column].str.split(sep)
        report = report.explode(column)

    report = (
        report.groupby(column, as_index=True)
        .sum()
        .sort_values(by="num_documents", ascending=False)
    )

    report = report.astype(int)

    return report
