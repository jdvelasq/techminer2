"""
Bibliometric Indicators by Year
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2  import techminer
>>> techminer.indicators.indicators_by_year(directory) # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    1        1  ...                  0.0                           0.00
2017    4        5  ...                  3.0                           0.11
2018    3        8  ...                 33.0                           1.67
2019    6       14  ...                 52.0                           0.63
2020   14       28  ...                 81.0                           0.52
2021   10       38  ...                 90.0                           0.30
2022   12       50  ...                 93.0                           0.12
2023    2       52  ...                 93.0                           0.00
<BLANKLINE>
[8 rows x 11 columns]


>>> techminer.indicators.indicators_by_year(directory, database="references").tail() # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2018   89      594  ...                732.0                           0.30
2019   91      685  ...                840.0                           0.30
2020  114      799  ...                985.0                           0.42
2021   80      879  ...               1072.0                           0.54
2022   30      909  ...               1104.0                           1.07
<BLANKLINE>
[5 rows x 11 columns]


>>> techminer.indicators.indicators_by_year(directory, database="cited_by").tail() # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_global_citations  mean_global_citations_per_year
year                ...                                                      
2019   33       44  ...                  1764                            8.15
2020   77      121  ...                  2879                            3.62
2021  107      228  ...                  3511                            1.97
2022  150      378  ...                  3871                            1.20
2023   10      388  ...                  3871                            0.00
<BLANKLINE>
[5 rows x 7 columns]



>>> from pprint import pprint
>>> pprint(sorted(techminer.indicators.indicators_by_year(directory=directory).columns.to_list()))
['OCC',
 'citable_years',
 'cum_OCC',
 'cum_global_citations',
 'cum_local_citations',
 'global_citations',
 'local_citations',
 'mean_global_citations',
 'mean_global_citations_per_year',
 'mean_local_citations',
 'mean_local_citations_per_year']

"""
import plotly.express as px

from ..._read_records import read_records


def indicators_by_year(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Computes annual indicators,"""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = records.assign(OCC=1)

    columns = ["OCC", "year"]

    if "local_citations" in records.columns:
        columns.append("local_citations")
    if "global_citations" in records.columns:
        columns.append("global_citations")
    records = records[columns]

    records = records.groupby("year", as_index=True).sum()
    records = records.sort_index(ascending=True, axis=0)
    records = records.assign(cum_OCC=records.OCC.cumsum())
    records.insert(1, "cum_OCC", records.pop("cum_OCC"))

    current_year = records.index.max()
    records = records.assign(citable_years=current_year - records.index + 1)

    if "global_citations" in records.columns:
        records = records.assign(
            mean_global_citations=records.global_citations / records.OCC
        )
        records = records.assign(cum_global_citations=records.global_citations.cumsum())
        records = records.assign(
            mean_global_citations_per_year=records.mean_global_citations
            / records.citable_years
        )
        records.mean_global_citations_per_year = (
            records.mean_global_citations_per_year.round(2)
        )

    if "local_citations" in records.columns:
        records = records.assign(
            mean_local_citations=records.local_citations / records.OCC
        )
        records = records.assign(cum_local_citations=records.local_citations.cumsum())
        records = records.assign(
            mean_local_citations_per_year=records.mean_local_citations
            / records.citable_years
        )
        records.mean_local_citations_per_year = (
            records.mean_local_citations_per_year.round(2)
        )

    return records


def time_plot(
    indicators,
    metric,
    title,
):
    """Makes a line plot for annual indicators."""

    column_names = {
        column: column.replace("_", " ").title()
        for column in indicators.columns
        if column not in ["OCC", "cum_OCC"]
    }
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum_OCC"
    indicators = indicators.rename(columns=column_names)

    fig = px.line(
        indicators,
        x=indicators.index,
        y=column_names[metric],
        title=title,
        markers=True,
        hover_data=["OCC", "Global Citations", "Local Citations"],
    )
    fig.update_traces(
        marker=dict(size=10, line=dict(color="darkslategray", width=2)),
        marker_color="rgb(171,171,171)",
        line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )
    return fig
