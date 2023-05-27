"""
Indicators by Topic 
===============================================================================


>>> root_dir = "data/regtech/"


>>> from techminer2  import techminer
>>> techminer.indicators.indicators_by_topic(
...     criterion='authors',
...     root_dir=root_dir,
... ).head() # doctest: +NORMALIZE_WHITESPACE
            OCC  ...  local_citations_per_document
authors          ...                              
Arner DW      3  ...                          2.67
Buckley RP    3  ...                          2.67
Lin W         2  ...                          2.00
Brennan R     2  ...                          1.50
Sarea A       2  ...                          2.00
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

from ... import load_utils, record_utils


def indicators_by_topic(
    criterion,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """column indicators"""

    def select_columns(records, criterion):
        return records[[criterion, "global_citations", "local_citations"]]

    def explode_criterion(records, criterion):
        records = records.copy()
        records[criterion] = records[criterion].str.split(";")
        records = records.explode(criterion)
        records[criterion] = records[criterion].str.strip()
        return records

    def compute_basic_indicators(records, criterion):
        indicators = (
            records.groupby(criterion, as_index=True)
            .sum()
            .sort_values(by="OCC", ascending=False)
        )
        indicators = indicators.astype(int)
        indicators = indicators[["OCC", "global_citations", "local_citations"]]
        return indicators

    def compute_global_citations_per_document(indicators):
        indicators = indicators.assign(
            global_citations_per_document=(
                indicators.global_citations / indicators.OCC
            ).round(2)
        )
        return indicators

    def compute_local_citations_per_document(indicators):
        indicators = indicators.assign(
            local_citations_per_document=(
                indicators.local_citations / indicators.OCC
            ).round(2)
        )
        return indicators

    records = record_utils.read_records(
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = select_columns(records, criterion)
    records = explode_criterion(records, criterion)

    records["OCC"] = 1

    indicators = compute_basic_indicators(records, criterion)
    indicators = compute_global_citations_per_document(indicators)
    indicators = compute_local_citations_per_document(indicators)

    stopwords = load_utils.load_stopwords(root_dir=root_dir)
    indicators = indicators.drop(stopwords, axis=0)

    return indicators
