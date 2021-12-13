"""
Column Indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
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


def column_indicators(column, sep="; ", directory="./"):
    """
    Counts the number of terms by record.

    :param dirpath_or_records: path to the directory or the records object
    :param column: column to be used to count the terms
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of terms by record.
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
    report.sort_values(by="num_documents", ascending=False, inplace=True)

    return report
