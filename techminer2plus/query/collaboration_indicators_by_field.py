"""
Collaboration Indicators by Field 
===============================================================================


Examples
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> techminer2plus.query.collaboration_indicators_by_field(
...     "countries",
...     root_dir=root_dir,
... ).head()
                OCC  global_citations  ...  multiple_publication  mp_ratio
countries                              ...                                
United Kingdom    7               199  ...                     3      0.43
Australia         7               199  ...                     3      0.43
United States     6                59  ...                     2      0.33
Ireland           5                55  ...                     1      0.20
China             5                27  ...                     3      0.60
<BLANKLINE>
[5 rows x 6 columns]


>>> print(
...     techminer2plus.query.collaboration_indicators_by_field(
...         "countries",
...         root_dir=root_dir,
...     ).head().to_markdown()
... )
| countries      |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|:---------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
| United Kingdom |     7 |                199 |                34 |                    4 |                      3 |       0.43 |
| Australia      |     7 |                199 |                15 |                    4 |                      3 |       0.43 |
| United States  |     6 |                 59 |                11 |                    4 |                      2 |       0.33 |
| Ireland        |     5 |                 55 |                22 |                    4 |                      1 |       0.2  |
| China          |     5 |                 27 |                 5 |                    2 |                      3 |       0.6  |

# pylint: disable=line-too-long
# noqa: W291 E501
"""


import numpy as np

from ..records import read_records


def collaboration_indicators_by_field(
    field,
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """
    Collaboration indicators.

    Args:
        criterion (str): Criterion to be analyzed.
        directory (str): The working directory.
        database (str):  The database name. It can be 'documents', 'cited_by' or 'references'.
        start_year (int) : The start year for filtering the data.
        end_year (int): The end year for filtering the data.
        **filters: Additional filters to apply to the data.

    Returns:
        A pandas.DataFrame with the collaboration indicators.

    # noqa: E501
    """

    # Read documents from the database
    documents = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # Add a column to represent the number of occurrences of a document
    documents = documents.assign(OCC=1)

    # Add columns to represent single and multiple publications for a document
    documents["single_publication"] = documents[field].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0
    )
    documents["multiple_publication"] = documents[field].map(
        lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0
    )

    # Split multi-topic documents into individual documents with one topic each
    exploded = documents[
        [
            field,
            "OCC",
            "global_citations",
            "local_citations",
            "single_publication",
            "multiple_publication",
            "article",
        ]
    ].copy()

    exploded[field] = exploded[field].str.split(";")
    exploded = exploded.explode(field)
    exploded[field] = exploded[field].str.strip()

    # Compute collaboration indicators for each topic
    indicators = exploded.groupby(field, as_index=False).agg(
        {
            "OCC": np.sum,
            "global_citations": np.sum,
            "local_citations": np.sum,
            "single_publication": np.sum,
            "multiple_publication": np.sum,
        }
    )

    # Compute the multiple publication ratio for each topic
    indicators["mp_ratio"] = (
        indicators["multiple_publication"] / indicators["OCC"]
    )
    indicators["mp_ratio"] = indicators["mp_ratio"].round(2)

    # Sort the topics by number of occurrences, global citations, and local
    # citations
    indicators = indicators.sort_values(
        by=["OCC", "global_citations", "local_citations"],
        ascending=[False, False, False],
    )

    # Set the index to the criterion column
    indicators = indicators.set_index(field)

    return indicators