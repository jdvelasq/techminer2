"""
Column Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> column_indicators('authors',directory=directory).head() # doctest: +NORMALIZE_WHITESPACE
             num_documents  ...  local_citations_per_document
authors                     ...
Arner DW                 7  ...                             2
Buckley RP               6  ...                             2
Zetzsche DA              4  ...                             2
Barberis JN              4  ...                             3
Ryan P                   3  ...                             1
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(column_indicators('authors',directory=directory).columns.to_list())
['num_documents',
 'local_citations',
 'global_citations',
 'global_citations_per_document',
 'local_citations_per_document']


"""
from ._read_records import read_records


def column_indicators(
    column,
    sep=";",
    directory="./",
    database="documents",
    use_filter=False,
):
    """column indicators"""

    records = read_records(
        directory=directory, database=database, use_filter=use_filter
    )

    records = records.assign(num_documents=1)
    columns = [column, "num_documents"]
    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    if sep is not None:
        records[column] = records[column].str.split(sep)
        records = records.explode(column)
        records[column] = records[column].str.strip()

    indicators = (
        records.groupby(column, as_index=True)
        .sum()
        .sort_values(by="num_documents", ascending=False)
    )

    if "global_citations" in records.columns:
        indicators = indicators.assign(
            global_citations_per_document=(
                indicators.global_citations / indicators.num_documents
            ).round(2)
        )
    if "local_citations" in records.columns:
        indicators = indicators.assign(
            local_citations_per_document=(
                indicators.local_citations / indicators.num_documents
            ).round(2)
        )

    indicators = indicators.astype(int)

    return indicators
