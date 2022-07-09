"""
Column Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> column_indicators('authors',directory=directory).head() # doctest: +NORMALIZE_WHITESPACE
       authors  ...  local_citations_per_document
0     Arner DW  ...                             2
1   Buckley RP  ...                             2
2  Zetzsche DA  ...                             2
3  Barberis JN  ...                             3
4       Ryan P  ...                             1
<BLANKLINE>
[5 rows x 6 columns]


>>> from pprint import pprint
>>> pprint(sorted(column_indicators('authors',directory=directory).columns.to_list()))
['OCC',
 'authors',
 'global_citations',
 'global_citations_per_document',
 'local_citations',
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

    records = records.assign(OCC=1)
    columns = [column, "OCC"]
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
        .sort_values(by="OCC", ascending=False)
    )

    if "global_citations" in records.columns:
        indicators = indicators.assign(
            global_citations_per_document=(
                indicators.global_citations / indicators.OCC
            ).round(2)
        )
    if "local_citations" in records.columns:
        indicators = indicators.assign(
            local_citations_per_document=(
                indicators.local_citations / indicators.OCC
            ).round(2)
        )

    indicators = indicators.astype(int)
    indicators = indicators.reset_index()

    return indicators
