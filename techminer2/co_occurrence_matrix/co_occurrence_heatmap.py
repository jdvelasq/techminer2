# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Heatmap
===============================================================================


>>> from techminer2.co_occurrence_matrix import co_occurrence_heatmap
>>> co_occurrence_heatmap(
...     #
...     # FUNCTION PARAMS:
...     columns='author_keywords',
...     rows='authors',
...     retain_counters=True,
...     #
...     # COLUMN PARAMS:
...     col_top_n=None,
...     col_occ_range=(2, None),
...     col_gc_range=(None, None),
...     col_custom_terms=None,
...     #
...     # ROW PARAMS:
...     row_top_n=None,
...     row_occ_range=(2, None),
...     row_gc_range=(None, None),
...     row_custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ) # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler ...


"""
from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_heatmap(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
    retain_counters=True,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_terms=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    def make_heat_map(styler):
        styler.background_gradient(
            axis=None,
            vmin=1,
            vmax=5,
            cmap="Oranges",
        )
        return styler

    matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        retain_counters=retain_counters,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_terms=col_custom_terms,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_terms=row_custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return matrix.style.pipe(make_heat_map)
