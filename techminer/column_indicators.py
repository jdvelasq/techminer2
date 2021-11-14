"""
Column indicators
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> column_indicators(directory, 'authors').head(20)
                  num_documents  global_citations  local_citations
authors                                                           
Rabbani MR                   10                69               32
Arner DW                      9               135               47
Buckley RP                    7               132               45
Reyes-Mercado P               7                 0                0
Wojcik D                      7                49               14
Gozman DP                     6                26                8
Ozili PK                      6               151               33
Wonglimpiyarat J              6                52               36
Serrano W                     6                15                3
Schwienbacher A               6                50               19
Khan S                        6                49               22
Faccia A                      5                27                5
Nieves EH                     5                15                3
Mention A-L                   5                35               31
Tan B                         5               105               56
Zetzsche DA                   5                44               25
Hamdan A                      5                18                7
Ashta A                       5                 9                7
Baber H                       5                12                5

"""

from .utils import load_filtered_documents


### def column_indicators(directory=None, column="authors", sep="; ", min_occ=1):
def column_indicators(directory=None, column="authors", sep="; "):
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
    ### report = report[report["num_documents"] >= min_occ]
    ### report.index = report.index.str.replace("/\d+", "", regex=True)

    return report
