"""
Indicators by Topic --- ChatGPT
===============================================================================


>>> root_dir = "data/regtech/"


>>> from techminer2  import techminer
>>> techminer.indicators.indicators_by_topic(
...     criterion='authors',
...     root_dir=root_dir,
... ).head() # doctest: +NORMALIZE_WHITESPACE
            OCC  ...  local_citations_per_document
authors          ...                              
Arner DW      3  ...                             2
Buckley RP    3  ...                             2
Lin W         2  ...                             2
Brennan R     2  ...                             1
Sarea A       2  ...                             2
<BLANKLINE>
[5 rows x 5 columns]


>>> from pprint import pprint
>>> pprint(sorted(techminer.indicators.indicators_by_topic('authors',
...     root_dir=root_dir).columns.to_list()))
['OCC',
 'global_citations',
 'global_citations_per_document',
 'local_citations',
 'local_citations_per_document']

# noga: W291

"""

from ... import record_utils


def indicators_by_topic(
    criterion,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """column indicators"""

    records = record_utils.read_records(
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = _column_indicators_from_records(criterion, records)

    return indicators


def _column_indicators_from_records(column, records):
    records = records.assign(OCC=1)
    columns = [column, "OCC"]
    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    records[column] = records[column].str.split(";")
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
