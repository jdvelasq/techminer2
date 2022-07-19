"""
Column Indicators
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2 import column_indicators
>>> column_indicators('authors',directory=directory).head() # doctest: +NORMALIZE_WHITESPACE
             OCC  ...  local_citations_per_document
authors           ...                              
Arner DW       7  ...                             4
Buckley RP     6  ...                             4
Zetzsche DA    4  ...                             2
Barberis JN    4  ...                             6
Ryan P         3  ...                             0
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(sorted(column_indicators('authors',directory=directory).columns.to_list()))
['OCC',
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

    return indicators
