# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Heatmap
===============================================================================


>>> from techminer2.analyze.co_occurrence_matrix import CoOccurrenceHeatmap
>>> (
...     CoOccurrenceHeatmap()
...     .set_column_params(
...         field="author_keywords",
...         top_n=10,
...         occ_range=(2, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_rows_params(
...         field="authors",
...         top_n=None,
...         occ_range=(2, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_format_params(
...         retain_counters=True,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... ) # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler ...


"""
from ...internals.params.columns_and_rows_params import ColumnsAndRowsParamsMixin
from ...internals.params.database_params import DatabaseParams, DatabaseParamsMixin
from ...internals.params.item_params import ItemParams
from .co_occurrence_matrix import CoOccurrenceMatrix
from .internals.output_params import OutputParams, OutputParamsMixin


class CoOccurrenceHeatmap(
    ColumnsAndRowsParamsMixin,
    DatabaseParamsMixin,
    OutputParamsMixin,
):
    """:meta private:"""

    def __init__(self):

        self.column_params = ItemParams()
        self.database_params = DatabaseParams()
        self.row_params = ItemParams()
        self.format_params = OutputParams()

    def build(self):

        def make_heat_map(styler):
            styler.background_gradient(
                axis=None,
                vmin=1,
                vmax=5,
                cmap="Oranges",
            )
            return styler

        matrix = (
            CoOccurrenceMatrix()
            .set_columns_params(**self.column_params.__dict__)
            .set_rows_params(**self.row_params.__dict__)
            .set_format_params(**self.format_params.__dict__)
            .set_database_params(**self.database_params.__dict__)
            .build()
        )

        return matrix.style.pipe(make_heat_map)
