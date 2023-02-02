"""
Impact Indicators by Topic
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2  import techminer
>>> techminer.indicators.impact_indicators_by_topic("countries", directory=directory).head()
           OCC  ...  avg_global_citations
countries       ...                      
Australia    7  ...                 28.43
Bahrain      4  ...                  4.75
Belgium      1  ...                  0.00
China        5  ...                  5.40
France       1  ...                  0.00
<BLANKLINE>
[5 rows x 9 columns]


>>> from pprint import pprint
>>> pprint(sorted(techminer.indicators.impact_indicators_by_topic("countries", directory=directory).columns.to_list()))
['OCC',
 'age',
 'avg_global_citations',
 'first_pb_year',
 'g_index',
 'global_citations',
 'global_citations_per_year',
 'h_index',
 'm_index']

"""

import numpy as np
import pandas as pd

from ..._lib._read_records import read_records


def impact_indicators_by_topic(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):

    """Impact indicators."""

    documents = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if criterion not in [
        "authors",
        "authors_id",
        "countries",
        "organizations",
        "source_title",
        "source_abbr",
    ]:
        raise ValueError(
            'Impact indicators only works with "authors", "authors_id", "countries", "organizations", "source_title" or "source_abbr".'
        )

    columns_to_explode = [
        criterion,
        "global_citations",
        "local_citations",
        "year",
    ]
    detailed_citations = documents[columns_to_explode]
    detailed_citations[criterion] = detailed_citations[criterion].str.split(";")
    detailed_citations = detailed_citations.explode(criterion)
    detailed_citations[criterion] = detailed_citations[criterion].str.strip()
    detailed_citations = detailed_citations.reset_index(drop=True)
    detailed_citations = detailed_citations.assign(
        cumcount_=detailed_citations.sort_values("global_citations", ascending=False)
        .groupby(criterion)
        .cumcount()
        + 1
    )
    detailed_citations = detailed_citations.sort_values(
        [criterion, "global_citations", "cumcount_"], ascending=[True, False, True]
    )
    detailed_citations = detailed_citations.assign(
        cumcount_2=detailed_citations.cumcount_.map(lambda w: w * w)
    )

    detailed_citations["first_pb_year"] = detailed_citations.groupby(criterion)[
        "year"
    ].transform("min")

    detailed_citations["age"] = (
        documents.year.max() - detailed_citations["first_pb_year"] + 1
    )
    ages = detailed_citations.groupby(criterion, as_index=True).agg({"age": np.max})

    global_citations = detailed_citations.groupby(criterion, as_index=True).agg(
        {"global_citations": np.sum}
    )

    first_pb_year = detailed_citations.groupby(criterion, as_index=True).agg(
        {"first_pb_year": np.min}
    )

    occ = detailed_citations.groupby(criterion, as_index=True).size()

    h_indexes = detailed_citations.query("global_citations >= cumcount_")
    h_indexes = h_indexes.groupby(criterion, as_index=True).agg({"cumcount_": np.max})
    h_indexes = h_indexes.rename(columns={"cumcount_": "h_index"})

    g_indexes = detailed_citations.query("global_citations >= cumcount_2")
    g_indexes = g_indexes.groupby(criterion, as_index=True).agg({"cumcount_": np.max})
    g_indexes = g_indexes.rename(columns={"cumcount_": "g_index"})

    indicators = pd.concat(
        [occ, global_citations, first_pb_year, ages, h_indexes, g_indexes],
        axis=1,
        sort=False,
    )

    indicators = indicators.rename(columns={0: "OCC"})
    indicators = indicators.fillna(0)

    indicators = indicators.assign(m_index=indicators.h_index / indicators.age)
    indicators["m_index"] = indicators.m_index.round(decimals=2)

    indicators = indicators.assign(
        global_citations_per_year=indicators.global_citations / indicators.age
    )
    indicators = indicators.assign(
        avg_global_citations=indicators.global_citations / indicators.OCC
    )

    indicators[
        "global_citations_per_year"
    ] = indicators.global_citations_per_year.round(decimals=2)

    indicators["avg_global_citations"] = indicators.avg_global_citations.round(
        decimals=2
    )

    indicators["h_index"] = indicators["h_index"].astype(int)
    indicators["g_index"] = indicators["g_index"].astype(int)
    indicators["age"] = indicators["age"].astype(int)

    # indicators = indicators.sort_values("h_index", ascending=False)
    indicators = indicators.sort_index(axis="index")
    indicators.first_pb_year = indicators.first_pb_year.astype(int)

    return indicators
