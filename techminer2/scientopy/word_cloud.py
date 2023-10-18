# flake8: noqa
"""
Word Cloud
===============================================================================

**Basic Usage**

# >>> from techminer2.performance import word_cloud
# >>> chart = word_cloud(
# ...     #
# ...     # PERFORMANCE PARAMS:
# ...     field='descriptors',
# ...     metric="OCC",
# ...     #
# ...     # CHART PARAMS:
# ...     title="Basic Usage",
# ...     width=400, 
# ...     height=400,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=50,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_items=None,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... )
# >>> chart.fig_.save("sphinx/_static/performance/word_cloud_basic_usage.png")

# .. image:: ../../../../_static/performance/word_cloud_basic_usage.png
#     :width: 900px
#     :align: center



# **Time Filter**

# >>> from techminer2.performance import word_cloud
# >>> chart = word_cloud(
# ...     #
# ...     # PERFORMANCE PARAMS:
# ...     field='descriptors',
# ...     metric="OCC",
# ...     #
# ...     # CHART PARAMS:
# ...     title="Time Filter",
# ...     width=400, 
# ...     height=400,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=50,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_items=None,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(2018, 2021),
# ...     cited_by_filter=(None, None),
# ... )
# >>> chart.fig_.save("sphinx/_static/performance/word_cloud_time_filter.png")

# .. image:: ../../../../_static/performance/word_cloud_time_filter.png
#     :width: 900px
#     :align: center

    
# **Custom Topics Extraction**

# >>> from techminer2.performance import word_cloud
# >>> chart = word_cloud(
# ...     #
# ...     # PERFORMANCE PARAMS:
# ...     field='descriptors',
# ...     metric="OCC",
# ...     #
# ...     # CHART PARAMS:
# ...     title="Custom Topics",
# ...     width=400, 
# ...     height=400,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=None,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_items=[
# ...         "FINTECH",
# ...         "BLOCKCHAIN",
# ...         "FINANCIAL_REGULATION",
# ...         "MACHINE_LEARNING",
# ...         "BIG_DATA",
# ...         "CRYPTOCURRENCY",
# ...     ],
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(2018, 2021),
# ...     cited_by_filter=(None, None),
# ... )
# >>> chart.fig_.save("sphinx/_static/performance/word_cloud_custom_topics.png")

# .. image:: ../../../../_static/performance/word_cloud_custom_topics.png
#     :width: 900px
#     :align: center


# **Filters (previous search results)**

# >>> from techminer2.performance import word_cloud
# >>> chart = word_cloud(
# ...     #
# ...     # PERFORMANCE PARAMS:
# ...     field='descriptors',
# ...     metric="OCC",
# ...     #
# ...     # CHART PARAMS:
# ...     title="Custom Topics",
# ...     width=400, 
# ...     height=400,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=None,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_items=[
# ...         "FINTECH",
# ...         "BLOCKCHAIN",
# ...         "FINANCIAL_REGULATION",
# ...         "MACHINE_LEARNING",
# ...         "BIG_DATA",
# ...         "CRYPTOCURRENCY",
# ...     ],
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(2018, 2021),
# ...     cited_by_filter=(None, None),
# ...     countries=[
# ...         "Australia", 
# ...         "United Kingdom", 
# ...         "United States"
# ...     ],
# ... )
# >>> chart.fig_.save("sphinx/_static/performance/word_cloud_previous_results.png")

# .. image:: ../../../../_static/performance/word_cloud_previous_results.png
#     :width: 900px
#     :align: center


# **Trend Analysis.**

# >>> from techminer2.performance import word_cloud
# >>> chart = word_cloud(
# ...     #
# ...     # PERFORMANCE PARAMS:
# ...     field='descriptors',
# ...     metric="OCC",
# ...     #
# ...     # CHART PARAMS:
# ...     title="Custom Topics",
# ...     width=400, 
# ...     height=400,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=20,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_items=None,
# ...     #
# ...     # TREND ANALYSIS:
# ...     time_window=2,
# ...     is_trend_analysis=True,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(2018, 2021),
# ...     cited_by_filter=(None, None),
# ...     countries=[
# ...         "Australia", 
# ...         "United Kingdom", 
# ...         "United States"
# ...     ],
# ... )
# >>> chart.fig_.save("sphinx/_static/performance/word_cloud_trend_analysis.png")

# .. image:: ../../../../_static/performance/word_cloud_trend_analysis.png
#     :width: 900px
#     :align: center


    
# >>> from techminer2.analyze import performance_metrics
# >>> metrics = performance_metrics(
# ...     #
# ...     # ITEMS PARAMS:
# ...     field='author_keywords',
# ...     metric="OCC",
# ...     #
# ...     # CHART PARAMS:
# ...     title=None,
# ...     field_label=None,
# ...     metric_label=None,
# ...     textfont_size=10,
# ...     marker_size=7,
# ...     line_width=1.5,
# ...     yshift=4,
# ...     #
# ...     # ITEM FILTERS:
# ...     top_n=20,
# ...     occ_range=(None, None),
# ...     gc_range=(None, None),
# ...     custom_items=None,
# ...     #
# ...     # TREND ANALYSIS:
# ...     time_window=2,
# ...     is_trend_analysis=True,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... ).df_
# >>> print(metrics.to_markdown())
# | author_keywords           |   rank_occ |   OCC |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |
# |:--------------------------|-----------:|------:|----------------------:|------------------------:|----------------------------:|
# | ANNUAL_GENERAL_MEETINGS   |        111 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | BENEFIT                   |        116 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | CHALLENGE                 |        117 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | COMPANIES                 |        119 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | COSTS_OF_VOTING           |        120 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | MIFID_II                  |        134 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | ONLINE_SHAREHOLDER_VOTING |        136 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | SHAREHOLDER_MONITORING    |        141 |     1 |                   0.5 |                     0.5 |                    0.5      |
# | COMPLIANCE                |          4 |     7 |                   0   |                     1   |                    0.142857 |
# | FINANCIAL_SERVICES        |          7 |     4 |                   0   |                     0.5 |                    0.125    |
# | FINANCIAL_REGULATION      |          8 |     4 |                   0   |                     1   |                    0.25     |
# | ARTIFICIAL_INTELLIGENCE   |          9 |     4 |                   0   |                     0.5 |                    0.125    |
# | RISK_MANAGEMENT           |         10 |     3 |                   0   |                     0.5 |                    0.166667 |
# | SUPTECH                   |         13 |     3 |                   0   |                     1   |                    0.333333 |
# | SEMANTIC_TECHNOLOGIES     |         14 |     2 |                   0   |                     0   |                    0        |
# | DATA_PROTECTION           |         15 |     2 |                   0   |                     0.5 |                    0.25     |
# | SMART_CONTRACTS           |         16 |     2 |                   0   |                     0   |                    0        |
# | CHARITYTECH               |         17 |     2 |                   0   |                     0.5 |                    0.25     |
# | ENGLISH_LAW               |         18 |     2 |                   0   |                     0.5 |                    0.25     |
# | TECHNOLOGY                |         23 |     2 |                   0   |                     0.5 |                    0.25     |


"""
