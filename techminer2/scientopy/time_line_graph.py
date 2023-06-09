# flake8: noqa
"""
Time Line Graph
===============================================================================

ScientoPy Time Line Plot.


>>> root_dir = "data/regtech/"
>>> from techminer2 import scientopy

>>> file_name = "sphinx/_static/scientopy__time_line-1.html"
>>> r = scientopy.time_line_graph(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-1.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
             author_keywords  Year  OCC
0             REGTECH 28:329  2017    2
1  FINANCIAL_SERVICES 04:168  2017    1
2             REGTECH 28:329  2018    3
3             FINTECH 12:249  2018    2
4          REGULATION 05:164  2018    2

>>> print(r.prompt_)
<BLANKLINE>



**Time Filter.**

>>> file_name = "sphinx/_static/scientopy__time_line-3.html"
>>> r = scientopy.time_line_graph(
...     field="author_keywords",
...     top_n=5,
...     root_dir=root_dir,
...     year_filter=(2018, 2021),
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-3.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
     author_keywords  Year  OCC
0     REGTECH 18:297  2018    3
1     FINTECH 10:235  2018    2
2  REGULATION 04:163  2018    2
3     REGTECH 18:297  2019    4
4     FINTECH 10:235  2019    4



**Custom Topics Extraction.**

>>> file_name = "sphinx/_static/scientopy__time_line-4.html"
>>> r = scientopy.time_line_graph(
...     field="author_keywords",
...     custom_items=[
...         "FINTECH",
...         "BLOCKCHAIN",
...         "FINANCIAL_REGULATION",
...         "MACHINE_LEARNING",
...         "BIG_DATA",
...         "CRYPTOCURRENCY",
...     ],
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-4.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> file_name = "sphinx/_static/scientopy__time_line-5.html"
>>> r = scientopy.time_line_graph(
...     field="author_keywords",
...     top_n=5,
...     is_trend_analysis=True,
...     year_filter=(2018, 2021),
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../_static/scientopy__time_line-5.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> print(r.prompt_)
<BLANKLINE>


# pylint: disable=line-too-long
"""
## ScientoPy // Time Line
import textwrap
from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px

from ..classes import TermsByYear
from ..counters import add_counters_to_axis
from ..item_utils import generate_custom_items
from ..sort_utils import sort_indicators_by_metric
from ..techminer.indicators.growth_indicators_by_field import (
    growth_indicators_by_field,
)
from ..techminer.indicators.indicators_by_field_per_year import (
    indicators_by_field_per_year,
)
from ..techminer.indicators.items_occ_by_year import items_occ_by_year
from ..vantagepoint.analyze import terms_by_year
from ..vantagepoint.report.gantt_chart import gantt_chart
from .common import PROMPT, get_default_indicators, get_trend_indicators

TEXTLEN = 40


@dataclass(init=False)
class _Results:
    plot_ = None
    table_ = None
    prompt_ = None


def time_line_graph(
    field,
    # Specific params:
    time_window=2,
    is_trend_analysis=False,
    title="Time Line",
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """ScientoPy Bar Trend."""

    if is_trend_analysis:
        return trend_analysis_time_line_graph(
            field=field,
            # Specific params:
            time_window=time_window,
            title=title,
            # Item filters:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            # Database params:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

    return default_time_line_graph(
        field=field,
        # Specific params:
        time_window=time_window,
        title=title,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )


def default_time_line_graph(
    field,
    # Specific params:
    time_window,
    title,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """ScientoPy Defatul Time Line Graph."""

    indicators = get_default_indicators(
        field=field,
        # Specific params:
        time_window=time_window,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    items_by_year = items_occ_by_year(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    items_by_year = items_by_year.loc[indicators.index.to_list(), :]

    items_by_year = add_counters_to_axis(
        items_by_year,
        axis=0,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj = TermsByYear()
    obj.metric_ = "OCC"
    obj.criterion_ = "years"
    obj.other_criterion_ = field
    obj.cumulative_ = False
    obj.table_ = items_by_year
    obj.prompt_ = ""

    return gantt_chart(obj, title)


def trend_analysis_time_line_graph(
    field,
    # Specific params:
    time_window,
    title,
    # Item filters:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    # Database params:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """ScientoPy Defatul Time Line Graph."""

    indicators = get_trend_indicators(
        field=field,
        # Specific params:
        time_window=time_window,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    items_by_year = items_occ_by_year(
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    items_by_year = items_by_year.loc[indicators.index.to_list(), :]

    items_by_year = add_counters_to_axis(
        items_by_year,
        axis=0,
        field=field,
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    obj = TermsByYear()
    obj.metric_ = "OCC"
    obj.criterion_ = "years"
    obj.other_criterion_ = field
    obj.cumulative_ = False
    obj.table_ = items_by_year
    obj.prompt_ = ""

    return gantt_chart(obj, title)
