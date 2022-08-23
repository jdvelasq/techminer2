"""
Indicators by Year
===============================================================================


>>> directory = "data/regtech/"


>>> from techminer2 import tm2__indicators_by_year
>>> indicators_by_year(directory) # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2016    2        2  ...                  7.0                           0.50
2017    5        7  ...                 27.0                           0.67
2018   16       23  ...                 63.0                           0.45
2019   14       37  ...                 76.0                           0.23
2020   25       62  ...                 93.0                           0.23
2021   22       84  ...                 96.0                           0.07
2022   10       94  ...                 96.0                           0.00
<BLANKLINE>
[7 rows x 11 columns]


>>> tm2__indicators_by_year(directory, database="references").tail() # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_local_citations  mean_local_citations_per_year
year                ...                                                    
2018  189      885  ...                994.0                           0.26
2019  139     1024  ...               1141.0                           0.26
2020  146     1170  ...               1292.0                           0.34
2021   40     1210  ...               1331.0                           0.49
2022    3     1213  ...               1334.0                           1.00
<BLANKLINE>
[5 rows x 11 columns]


>>> tm2__indicators_by_year(directory, database="cited_by").tail() # doctest: +NORMALIZE_WHITESPACE
      OCC  cum_OCC  ...  cum_global_citations  mean_global_citations_per_year
year                ...                                                      
2018   11       14  ...                   385                            6.56
2019   52       66  ...                  1677                            6.21
2020  105      171  ...                  2516                            2.66
2021  184      355  ...                  3113                            1.62
2022  119      474  ...                  3198                            0.71
<BLANKLINE>
[5 rows x 7 columns]



>>> from pprint import pprint
>>> pprint(sorted(tm2__indicators_by_year(directory=directory).columns.to_list()))
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

from ._read_records import read_records


def tm2__indicators_by_year(
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
