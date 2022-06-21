"""
Column Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> column_indicators('authors',directory=directory).head()
            num_documents  ...  avg_document_global_citations
authors                    ...                               
Wojcik D                5  ...                              3
Rabbani MR              3  ...                             13
Hornuf L                3  ...                             36
Parker C                2  ...                            114
Yuksel S                2  ...                              7
<BLANKLINE>
[5 rows x 4 columns]

>>> from pprint import pprint
>>> pprint(column_indicators('authors',directory=directory).columns.to_list())
['num_documents',
 'global_citations',
 'local_citations',
 'avg_document_global_citations']


"""

from ._read_records import read_filtered_records


def column_indicators(
    column,
    sep=";",
    directory="./",
):
    """
    Column Indicators
    """

    records = read_filtered_records(directory)
    records = records.assign(num_documents=1)
    records = records[
        [column, "num_documents", "global_citations", "local_citations"]
    ].copy()

    if sep is not None:
        records[column] = records[column].str.split(sep)
        records = records.explode(column)
        records[column] = records[column].str.strip()

    indicators = (
        records.groupby(column, as_index=True)
        .sum()
        .sort_values(by="num_documents", ascending=False)
    )

    indicators = indicators.assign(
        avg_document_global_citations=indicators.global_citations
        / indicators.num_documents
    )
    indicators.avg_document_global_citations = (
        indicators.avg_document_global_citations.round(2)
    )

    indicators = indicators.astype(int)

    return indicators
