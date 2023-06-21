# flake8: noqa
"""
Corresponding Author's Organization
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/organizations/corresponding_authors_organization.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.organizations.corresponding_authors_organization(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/organizations/corresponding_authors_organization.html"height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
                           OCC  ...  mp_ratio
organizations                   ...          
Univ of Hong Kong (HKG)      3  ...      1.00
Univ Coll Cork (IRL)         3  ...      0.33
Ahlia Univ (BHR)             3  ...      1.00
Coventry Univ (GBR)          2  ...      1.00
Univ of Westminster (GBR)    2  ...      1.00
<BLANKLINE>
[5 rows x 6 columns]

>>> print(r.prompt_)
Your task is to generate an analysis about the collaboration between organizations \\
according to the data in a scientific bibliography database. Summarize the table \\
below, delimited by triple backticks, where the column 'single publication' is the \\
number of documents in which all the authors belongs to the same organization, and the  \\
column 'multiple publication' is the number of documents in which the authors are \\
from different organizations. The column 'mcp ratio' is the ratio between the columns \\
'multiple publication' and 'single publication'. The higher the ratio, the higher \\
the collaboration between organizations. Use the information in the table to draw \\
conclusions about the level of collaboration between organizations in the dataset. In \\
your analysis, be sure to describe in a clear and concise way, any findings or any \\
patterns you observe, and identify any outliers or anomalies in the data. Limit your \\
description to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
|    | organizations                                                      |   OCC |   global_citations |   local_citations |   single_publication |   multiple_publication |   mp_ratio |
|---:|:-------------------------------------------------------------------|------:|-------------------:|------------------:|---------------------:|-----------------------:|-----------:|
|  0 | Univ of Hong Kong (HKG)                                            |     3 |                185 |                 8 |                    0 |                      3 |       1    |
|  1 | Univ Coll Cork (IRL)                                               |     3 |                 41 |                19 |                    2 |                      1 |       0.33 |
|  2 | Ahlia Univ (BHR)                                                   |     3 |                 19 |                 5 |                    0 |                      3 |       1    |
|  3 | Coventry Univ (GBR)                                                |     2 |                 17 |                 4 |                    0 |                      2 |       1    |
|  4 | Univ of Westminster (GBR)                                          |     2 |                 17 |                 4 |                    0 |                      2 |       1    |
|  5 | Dublin City Univ (IRL)                                             |     2 |                 14 |                 3 |                    1 |                      1 |       0.5  |
|  6 | Politec di Milano (ITA)                                            |     2 |                  2 |                 0 |                    2 |                      0 |       0    |
|  7 | Kingston Bus Sch (GBR)                                             |     1 |                153 |                17 |                    1 |                      0 |       0    |
|  8 | FinTech HK, Hong Kong (HKG)                                        |     1 |                150 |                 0 |                    0 |                      1 |       1    |
|  9 | ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |     1 |                150 |                 0 |                    0 |                      1 |       1    |
| 10 | Duke Univ Sch of Law (USA)                                         |     1 |                 30 |                 0 |                    1 |                      0 |       0    |
| 11 | Heinrich-Heine-Univ (DEU)                                          |     1 |                 24 |                 5 |                    0 |                      1 |       1    |
| 12 | UNSW Sydney, Kensington, Australia (AUS)                           |     1 |                 24 |                 5 |                    0 |                      1 |       1    |
| 13 | Univ of Luxembourg (LUX)                                           |     1 |                 24 |                 5 |                    0 |                      1 |       1    |
| 14 | Univ of Zurich (CHE)                                               |     1 |                 24 |                 5 |                    0 |                      1 |       1    |
| 15 | European Central B (DEU)                                           |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| 16 | Harvard Univ Weatherhead ctr for International Affairs (USA)       |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| 17 | KS Strategic, London, United Kingdom (GBR)                         |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| 18 | Panepistemio Aigaiou, Chios, Greece (GRC)                          |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
| 19 | Sch of Eng (CHE)                                                   |     1 |                 21 |                 8 |                    0 |                      1 |       1    |
```
<BLANKLINE>



# pylint: disable=line-too-long   
"""
import plotly.express as px

from ...classes import CorresponingAuthorOrganization
from ...items import generate_custom_items
from ...metrics import collaboration_indicators_by_field
from ...sorting import sort_indicators_by_metric


# pylint: disable=too-many-arguments
def corresponding_authors_organization(
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Corresponding Author's Organization"""

    indicators = collaboration_indicators_by_field(
        "organizations",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = sort_indicators_by_metric(indicators, "OCC")

    if custom_items is None:
        custom_items = generate_custom_items(
            indicators=indicators,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
        )

    indicators = indicators[indicators.index.isin(custom_items)]

    results = CorresponingAuthorOrganization()
    results.table_ = indicators
    indicators = indicators.reset_index()
    results.plot_ = _make_plot(indicators)
    results.prompt_ = _create_prompt(indicators)
    return results


def _create_prompt(table):
    # pylint: disable=line-too-long
    return (
        "Your task is to generate an analysis about the collaboration between organizations \\\n"
        "according to the data in a scientific bibliography database. Summarize the table \\\n"
        "below, delimited by triple backticks, where the column 'single publication' is the \\\n"
        "number of documents in which all the authors belongs to the same organization, and the  \\\n"
        "column 'multiple publication' is the number of documents in which the authors are \\\n"
        "from different organizations. The column 'mcp ratio' is the ratio between the columns \\\n"
        "'multiple publication' and 'single publication'. The higher the ratio, the higher \\\n"
        "the collaboration between organizations. Use the information in the table to draw \\\n"
        "conclusions about the level of collaboration between organizations in the dataset. In \\\n"
        "your analysis, be sure to describe in a clear and concise way, any findings or any \\\n"
        "patterns you observe, and identify any outliers or anomalies in the data. Limit your \\\n"
        "description to one paragraph with no more than 250 words.\n\n"
        f"Table:\n```\n{table.to_markdown()}\n```\n"
    )


def _make_plot(indicators):
    indicators = indicators.melt(
        id_vars="organizations",
        value_vars=["single_publication", "multiple_publication"],
    )
    indicators = indicators.rename(
        columns={"variable": "publication", "value": "Num Documents"}
    )
    indicators.publication = indicators.publication.map(
        lambda x: x.replace("_", " ").title()
    )
    # indicators.organizations = indicators.countries.map(lambda x: x.title())

    fig = px.bar(
        indicators,
        x="Num Documents",
        y="organizations",
        color="publication",
        title="Corresponding Author's Organization",
        hover_data=["Num Documents"],
        orientation="h",
        color_discrete_map={
            "Single Publication": "#8da4b4",
            "Multiple Publication": "#556f81",
        },
    )
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="gray",
        griddash="dot",
    )

    return fig
