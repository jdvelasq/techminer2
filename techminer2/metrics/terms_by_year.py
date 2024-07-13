# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Year
===============================================================================

>>> from techminer2.metrics import terms_by_year
>>> terms_by_year(
...     field="author_keywords",
...     cumulative=False,
...     title=None,
...     #
...     # FILTER PARAMS:
...     metric='OCC',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).df_
year                             2015  2016  2017  2018  2019
author_keywords                                              
FINTECH 31:5168                     0     5     8    12     6
INNOVATION 07:0911                  0     3     3     1     0
FINANCIAL_SERVICES 04:0667          0     1     0     3     0
FINANCIAL_INCLUSION 03:0590         0     1     2     0     0
FINANCIAL_TECHNOLOGY 03:0461        0     0     1     1     1
CROWDFUNDING 03:0335                0     0     1     1     1
MARKETPLACE_LENDING 03:0317         0     0     0     2     1
BUSINESS_MODELS 02:0759             0     0     0     2     0
CYBER_SECURITY 02:0342              0     0     0     2     0
CASE_STUDY 02:0340                  0     0     1     0     1
ARTIFICIAL_INTELLIGENCE 02:0327     0     0     0     0     2
TECHNOLOGY 02:0310                  0     1     1     0     0
FINANCE 02:0309                     0     0     1     0     1
BLOCKCHAIN 02:0305                  0     0     0     1     1
BANKING 02:0291                     0     1     1     0     0
ROBOTS 02:0289                      0     0     0     0     2
REGTECH 02:0266                     0     0     0     1     1
LENDINGCLUB 02:0253                 0     0     0     1     1
PEER_TO_PEER_LENDING 02:0253        0     0     0     1     1
SHADOW_BANKING 02:0253              0     0     0     1     1



>>> from techminer2.metrics import terms_by_year
>>> terms_by_year(
...     field="author_keywords",
...     cumulative=False,
...     title=None,
...     #
...     # FILTER PARAMS:
...     metric='OCC',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).fig_.write_html("sphinx/_static/metrics/terms_by_year.html")

.. raw:: html

    <iframe src="../_static/metrics/terms_by_year.html" 
    height="800px" width="100%" frameBorder="0"></iframe>

    
>>> from techminer2.metrics import terms_by_year
>>> print(
...     terms_by_year(
...         field="author_keywords",
...         cumulative=False,
...         title=None,
...         #
...         # FILTER PARAMS:
...         metric='OCC',
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_items=None,
...         #
...         # DATABASE PARAMS:
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).prompt_
... ) # doctest: +ELLIPSIS
Your task is ...



>>> from techminer2.metrics import terms_by_year
>>> print(
...     terms_by_year(
...         field="author_keywords",
...         cumulative=False,
...         title=None,
...         #
...         # FILTER PARAMS:
...         metric='OCC',
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_items=None,
...         #
...         # DATABASE PARAMS:
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...         ).metrics_.head(20).to_markdown()
... )
|    | author_keywords      |   year |   OCC |   cum_OCC |   global_citations |   local_citations |   age |   global_citations_per_year |   local_citations_per_year |
|---:|:---------------------|-------:|------:|----------:|-------------------:|------------------:|------:|----------------------------:|---------------------------:|
|  0 | FINTECH              |   2016 |     5 |         5 |                498 |                 5 |     4 |                     124.5   |                      1.25  |
|  1 | FINTECH              |   2017 |     8 |        13 |               1572 |                11 |     3 |                     524     |                      3.667 |
|  2 | FINTECH              |   2018 |    12 |        25 |               2338 |                 9 |     2 |                    1169     |                      4.5   |
|  3 | FINTECH              |   2019 |     6 |        31 |                760 |                 1 |     1 |                     760     |                      1     |
|  4 | INNOVATION           |   2016 |     3 |         3 |                407 |                 3 |     4 |                     101.75  |                      0.75  |
|  5 | INNOVATION           |   2017 |     3 |         6 |                402 |                 2 |     3 |                     134     |                      0.667 |
|  6 | INNOVATION           |   2018 |     1 |         7 |                102 |                 0 |     2 |                      51     |                      0     |
|  7 | FINANCIAL_SERVICES   |   2016 |     1 |         1 |                226 |                 0 |     4 |                      56.5   |                      0     |
|  8 | FINANCIAL_SERVICES   |   2018 |     3 |         4 |                441 |                 1 |     2 |                     220.5   |                      0.5   |
|  9 | FINANCIAL_INCLUSION  |   2016 |     1 |         1 |                 96 |                 1 |     4 |                      24     |                      0.25  |
| 10 | FINANCIAL_INCLUSION  |   2017 |     2 |         3 |                494 |                 4 |     3 |                     164.667 |                      1.333 |
| 11 | FINANCIAL_TECHNOLOGY |   2017 |     1 |         1 |                253 |                 1 |     3 |                      84.333 |                      0.333 |
| 12 | FINANCIAL_TECHNOLOGY |   2018 |     1 |         2 |                137 |                 0 |     2 |                      68.5   |                      0     |
| 13 | FINANCIAL_TECHNOLOGY |   2019 |     1 |         3 |                 71 |                 0 |     1 |                      71     |                      0     |
| 14 | CROWDFUNDING         |   2017 |     1 |         1 |                100 |                 1 |     3 |                      33.333 |                      0.333 |
| 15 | CROWDFUNDING         |   2018 |     1 |         2 |                145 |                 0 |     2 |                      72.5   |                      0     |
| 16 | CROWDFUNDING         |   2019 |     1 |         3 |                 90 |                 0 |     1 |                      90     |                      0     |
| 17 | MARKETPLACE_LENDING  |   2018 |     2 |         2 |                220 |                 2 |     2 |                     110     |                      1     |
| 18 | MARKETPLACE_LENDING  |   2019 |     1 |         3 |                 97 |                 0 |     1 |                      97     |                      0     |
| 19 | BUSINESS_MODELS      |   2018 |     2 |         2 |                759 |                 3 |     2 |                     379.5   |                      1.5   |




>>> from techminer2.metrics import terms_by_year
>>> print(
...     terms_by_year(
...         field="author_keywords",
...         cumulative=False,
...         title=None,
...         #
...         # FILTER PARAMS:
...         metric='OCC',
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_items=None,
...         #
...         # DATABASE PARAMS:
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).documents_.head(20).to_markdown()
... )
|    | author_keywords         | document_title                                                                              |   year | source_title                                 |   global_citations |   local_citations | doi                             |
|---:|:------------------------|:--------------------------------------------------------------------------------------------|-------:|:---------------------------------------------|-------------------:|------------------:|:--------------------------------|
|  0 | BUSINESS_MODELS         | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES                   |   2018 | Business Horizons                            |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003    |
|  1 | FINTECH                 | FINTECH: ECOSYSTEM, BUSINESS_MODELS, INVESTMENT_DECISIONS, and CHALLENGES                   |   2018 | Business Horizons                            |                557 |                 2 | 10.1016/J.BUSHOR.2017.09.003    |
|  2 | FINTECH                 | DIGITAL_FINANCE and FINTECH: CURRENT_RESEARCH and FUTURE_RESEARCH_DIRECTIONS                |   2017 | Journal of Business Economics                |                489 |                 4 | 10.1007/S11573-017-0852-X       |
|  3 | FINTECH                 | FINTECH, REGULATORY_ARBITRAGE, and the RISE of SHADOW_BANKS                                 |   2018 | Journal of Financial Economics               |                390 |                 0 | 10.1016/J.JFINECO.2018.03.011   |
|  4 | FINANCIAL_INCLUSION     | the DIGITAL_REVOLUTION in FINANCIAL_INCLUSION: INTERNATIONAL_DEVELOPMENT in the FINTECH_ERA |   2017 | New Political Economy                        |                314 |                 2 | 10.1080/13563467.2017.1259298   |
|  5 | FINTECH                 | the DIGITAL_REVOLUTION in FINANCIAL_INCLUSION: INTERNATIONAL_DEVELOPMENT in the FINTECH_ERA |   2017 | New Political Economy                        |                314 |                 2 | 10.1080/13563467.2017.1259298   |
|  6 | FINTECH                 | the EMERGENCE of the GLOBAL_FINTECH_MARKET: economic and TECHNOLOGICAL_DETERMINANTS         |   2019 | Small Business Economics                     |                258 |                 1 | 10.1007/S11187-018-9991-X       |
|  7 | FINANCIAL_TECHNOLOGY    | FINTECH                                                                                     |   2017 | Business and Information Systems Engineering |                253 |                 1 | 10.1007/S12599-017-0464-6       |
|  8 | FINTECH                 | FINTECH                                                                                     |   2017 | Business and Information Systems Engineering |                253 |                 1 | 10.1007/S12599-017-0464-6       |
|  9 | INNOVATION              | FINTECH                                                                                     |   2017 | Business and Information Systems Engineering |                253 |                 1 | 10.1007/S12599-017-0464-6       |
| 10 | CYBER_SECURITY          | a SURVEY on FINTECH                                                                         |   2018 | Journal of Network and Computer Applications |                238 |                 1 | 10.1016/J.JNCA.2017.10.011      |
| 11 | FINTECH                 | a SURVEY on FINTECH                                                                         |   2018 | Journal of Network and Computer Applications |                238 |                 1 | 10.1016/J.JNCA.2017.10.011      |
| 12 | BANKING                 | taming the BEAST: a SCIENTIFIC_DEFINITION of FINTECH                                        |   2016 | Journal of Innovation Management             |                226 |                 0 | 10.24840/2183-0606_004.004_0004 |
| 13 | FINANCIAL_SERVICES      | taming the BEAST: a SCIENTIFIC_DEFINITION of FINTECH                                        |   2016 | Journal of Innovation Management             |                226 |                 0 | 10.24840/2183-0606_004.004_0004 |
| 14 | INNOVATION              | taming the BEAST: a SCIENTIFIC_DEFINITION of FINTECH                                        |   2016 | Journal of Innovation Management             |                226 |                 0 | 10.24840/2183-0606_004.004_0004 |
| 15 | TECHNOLOGY              | taming the BEAST: a SCIENTIFIC_DEFINITION of FINTECH                                        |   2016 | Journal of Innovation Management             |                226 |                 0 | 10.24840/2183-0606_004.004_0004 |
| 16 | ARTIFICIAL_INTELLIGENCE | ARTIFICIAL_INTELLIGENCE in FINTECH: UNDERSTANDING ROBO_ADVISORS ADOPTION among CUSTOMERS    |   2019 | Industrial Management and Data Systems       |                225 |                 0 | 10.1108/IMDS-08-2018-0368       |
| 17 | FINANCE                 | ARTIFICIAL_INTELLIGENCE in FINTECH: UNDERSTANDING ROBO_ADVISORS ADOPTION among CUSTOMERS    |   2019 | Industrial Management and Data Systems       |                225 |                 0 | 10.1108/IMDS-08-2018-0368       |
| 18 | ROBOTS                  | ARTIFICIAL_INTELLIGENCE in FINTECH: UNDERSTANDING ROBO_ADVISORS ADOPTION among CUSTOMERS    |   2019 | Industrial Management and Data Systems       |                225 |                 0 | 10.1108/IMDS-08-2018-0368       |
| 19 | BUSINESS_MODELS         | FINTECH and REGTECH: IMPACT on REGULATORS and BANKS                                         |   2018 | Journal of Economics and Business            |                202 |                 1 | 10.1016/J.JECONBUS.2018.07.003  |



"""
from dataclasses import dataclass

import plotly.express as px  # type: ignore

from ..helpers.append_occurrences_and_citations_to_axis import (
    append_occurrences_and_citations_to_axis,
)
from ..helpers.format_prompt_for_dataframes import format_prompt_for_dataframes
from ..core.metrics.calculate_global_performance_metrics import (
    calculate_global_performance_metrics,
)
from ..core.metrics.extract_top_n_items_by_metric import extract_top_n_items_by_metric
from ..science_mapping.documents_per_item import documents_per_item
from .globals.global_metrics_by_field_per_year import global_metrics_by_field_per_year
from .globals.items_occurrences_by_year import items_occurrences_by_year

COLOR = "#465c6b"
TEXTLEN = 40


def terms_by_year(
    field,
    cumulative,
    title,
    #
    # FILTER PARAMS:
    metric="OCC",
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    # --------------------------------------------------------------------------------------------
    def compute_terms_by_year(custom_items):
        #
        data_frame = items_occurrences_by_year(
            field=field,
            cumulative=cumulative,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        if custom_items is None:
            indicators = calculate_global_performance_metrics(
                field=field,
                #
                # DATABASE PARAMS
                root_dir=root_dir,
                database=database,
                year_filter=year_filter,
                cited_by_filter=cited_by_filter,
                **filters,
            )

            custom_items = extract_top_n_items_by_metric(
                indicators,
                metric=metric,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        data_frame = data_frame[data_frame.index.isin(custom_items)]
        data_frame = data_frame.loc[custom_items, :]
        data_frame = append_occurrences_and_citations_to_axis(
            data_frame,
            axis=0,
            field=field,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        return data_frame

    # --------------------------------------------------------------------------------------------
    def build_prompt(data_frame):
        #
        main_text = (
            "Your task is to generate an analysis about the "
            f"{'cumulative' if cumulative else ''} occurrences by year "
            f"of the '{field}' in a scientific bibliography database. "
            "Summarize the table below, delimited by triple backticks, "
            "identify any notable patterns, trends, or outliers in the data, "
            "and disc  uss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
        )

        return format_prompt_for_dataframes(main_text, data_frame.to_markdown())

    # --------------------------------------------------------------------------------------------
    def create_gantt_diagram(data_frame):
        #
        data_frame = data_frame.copy()
        data_frame["RANKING"] = range(1, len(data_frame) + 1)
        data_frame = data_frame.melt(
            value_name="OCC",
            var_name="column",
            ignore_index=False,
            id_vars=["RANKING"],
        )

        data_frame = data_frame[data_frame.OCC > 0]
        data_frame = data_frame.sort_values(by=["RANKING"], ascending=True)
        data_frame = data_frame.drop(columns=["RANKING"])

        data_frame = data_frame.rename(columns={"column": "Year"})
        data_frame = data_frame.reset_index()

        fig = px.scatter(
            data_frame,
            x="Year",
            y=field,
            size="OCC",
            hover_data=data_frame.columns.to_list(),
            title=title,
            color=field,
        )
        fig.update_layout(
            paper_bgcolor="white",
            plot_bgcolor="white",
            showlegend=False,
            xaxis_title=None,
            yaxis_title=field.replace("_", " ").upper(),
        )
        fig.update_traces(
            marker={
                "line": {"color": "white", "width": 0.5},
                "opacity": 1.0,
            },
            marker_color=COLOR,
            mode="lines+markers",
            line={"width": 2, "color": COLOR},
        )
        fig.update_xaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
            tickangle=270,
            dtick=1.0,
        )
        fig.update_yaxes(
            linecolor="white",
            linewidth=1,
            gridcolor="gray",
            griddash="dot",
        )

        return fig

    # --------------------------------------------------------------------------------------------
    def compute_metrics(data_frame):
        #
        items = data_frame.index.tolist()
        items = [" ".join(item.split(" ")[:-1]) for item in items]

        data_frame = global_metrics_by_field_per_year(
            field=field,
            as_index=False,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        data_frame = data_frame[data_frame[field].isin(items)]

        data_frame["TOTAL_OCC"] = data_frame.groupby(field)["OCC"].transform("sum")
        data_frame["TOTAL_GC"] = data_frame.groupby(field)["global_citations"].transform("sum")
        data_frame["TOTAL_LC"] = data_frame.groupby(field)["local_citations"].transform("sum")
        data_frame = data_frame.sort_values(
            ["TOTAL_OCC", "TOTAL_GC", "TOTAL_LC", field, "year"],
            ascending=[False, False, False, True, True],
        )
        data_frame = data_frame.drop(columns=["TOTAL_OCC", "TOTAL_GC", "TOTAL_LC"])
        data_frame = data_frame.reset_index(drop=True)

        return data_frame

    # --------------------------------------------------------------------------------------------
    def extract_documents(data_frame):
        #
        items = data_frame.index.tolist()
        items = [" ".join(item.split(" ")[:-1]) for item in items]

        documents = documents_per_item(
            field=field,
            #
            # DATABASE PARAMS
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        documents = documents[documents[field].isin(items)]
        documents = documents.sort_values(
            ["global_citations", "local_citations", "year", "document_title"],
            ascending=[False, False, True, True],
        )
        documents = documents.reset_index(drop=True)

        return documents

    # --------------------------------------------------------------------------------------------
    data_frame = compute_terms_by_year(custom_items)

    @dataclass
    class Results:
        df_ = data_frame
        prompt_ = build_prompt(data_frame)
        fig_ = create_gantt_diagram(data_frame)
        metrics_ = compute_metrics(data_frame)
        documents_ = extract_documents(data_frame)

    return Results()
