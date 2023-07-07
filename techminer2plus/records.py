# flake8: noqa
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
"""
Records
==============================================================================

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> tm2p.records(root_dir=root_dir)
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={})

    
>>> tm2p.records(root_dir=root_dir, filters={
...     "countries": ['Australia', 'United Kingdom', 'United States']
... })
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={'countries': ['Australia', 'United
    Kingdom', 'United States']})


"""

import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield

from .auto_correlation_matrix import auto_correlation_matrix
from .average_citations_per_year import average_citations_per_year
from .bradford_law import bradford_law
from .cluster_records import cluster_records
from .co_occurrence_matrix import co_occurrence_matrix
from .concordances import concordances
from .coverage import coverage
from .cross_correlation_matrix import cross_correlation_matrix

# from .filter.records_per_year_chart import annual_scientific_production
from .filter.list_items.list_items import list_items
from .main_information import main_information
from .sankey_chart import sankey_chart
from .statistics import statistics
from .summary_sheet import summary_sheet
from .terms_by_year import terms_by_year

# =============================================================================
#
#
#  USER COMPUTATIONAL INTERFACE:
#
#
# =============================================================================


@dataclass
class Records:
    """Records"""

    #
    # PARAMETERS:
    #
    root_dir: str = "./"
    database: str = "main"
    year_filter: tuple = (None, None)
    cited_by_filter: tuple = (None, None)
    filters: dict = datafield(default_factory=dict)

    #
    # RESULTS:
    #
    # records_: pd.DataFrame = pd.DataFrame()

    # def __init__(self, root_dir, database, **filters):
    #     self.filters = filters

    def __post_init__(self):
        if self.filters is None:
            self.filters = {}

        #  if records_ is an empty dataframe print a message

        # if len(self.records_) == 0:
        #     self.records_ = read_records(
        #         root_dir=self.root_dir,
        #         database=self.database,
        #         year_filter=self.year_filter,
        #         cited_by_filter=self.cited_by_filter,
        #         **self.filters,
        #     )

    def __repr__(self):
        text = (
            "Records("
            f"root_dir='{self.root_dir}'"
            f", database='{self.database}'"
            f", year_filter={self.year_filter}"
            f", cited_by_filter={self.cited_by_filter}"
            f", filters={self.filters}"
            ")"
        )

        return textwrap.fill(text, width=80, subsequent_indent="    ")

    #
    #
    # USER INTERFACE:
    #
    #

    def annual_scientific_production(
        self, title="Annual Scientific Production"
    ):
        """Returns a coverage of the database."""
        return annual_scientific_production(
            #
            # FUNCTION PARAMS:
            title=title,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def average_citations_per_year(self, title="Average Citations per Year"):
        """Returns a average citations per year of the database."""
        return average_citations_per_year(
            #
            # FUNCTION PARAMS:
            title=title,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    # pylint: disable=too-many-arguments
    def auto_correlation_matrix(
        self,
        #
        # FUNCTION PARAMS:
        rows_and_columns,
        method="pearson",
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        return auto_correlation_matrix(
            #
            # FUNCTION PARAMS:
            rows_and_columns=rows_and_columns,
            method=method,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def bradford_law(self):
        """Bradford Law."""
        return bradford_law(
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def cluster_records(
        self,
        field,
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        """Cluster records."""
        return cluster_records(
            #
            # FUNCTION PARAMS:
            field=field,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    # pylint: disable=too-many-arguments
    def co_occurrence_matrix(
        self,
        columns,
        rows=None,
        #
        # COLUMN FILTERS:
        col_top_n=None,
        col_occ_range=(None, None),
        col_gc_range=(None, None),
        col_custom_items=None,
        #
        # ROW FILTERS:
        row_top_n=None,
        row_occ_range=(None, None),
        row_gc_range=(None, None),
        row_custom_items=None,
    ):
        """Co-occurrence matrix."""

        return co_occurrence_matrix(
            columns=columns,
            rows=rows,
            #
            # COLUMN PARAMS:
            col_top_n=col_top_n,
            col_occ_range=col_occ_range,
            col_gc_range=col_gc_range,
            col_custom_items=col_custom_items,
            #
            # ROW PARAMS:
            row_top_n=row_top_n,
            row_occ_range=row_occ_range,
            row_gc_range=row_gc_range,
            row_custom_items=row_custom_items,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def concordances(
        self,
        search_for,
        top_n=50,
        report_file="concordances_report.txt",
        prompt_file="concordances_prompt.txt",
    ):
        """Returns a Concordances object."""
        return concordances(
            #
            # FUNCTION PARAMS:
            search_for=search_for,
            top_n=top_n,
            report_file=report_file,
            prompt_file=prompt_file,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def coverage(self, field):
        """Returns a coverage of the database."""
        return coverage(
            #
            # FUNCTION PARAMS:
            field=field,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    # pylint: disable=too-many-arguments
    def cross_correlation_matrix(
        self,
        #
        # FUNCTION PARAMS:
        rows_and_columns,
        cross_with,
        method="pearson",
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        return cross_correlation_matrix(
            #
            # FUNCTION PARAMS:
            rows_and_columns=rows_and_columns,
            cross_with=cross_with,
            method=method,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def main_information(self):
        """Returns a MainInformation object."""
        return main_information(
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    # pylint: disable=too-many-arguments
    def list_items(
        self,
        field,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        """Field"""
        return list_items(
            #
            # FUNCTION PARAMS:
            field=field,
            metric=metric,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items if custom_items is not None else None,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def sankey_plot(
        self,
        #
        # PARAMS:
        fields,
        max_n=50,
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=None,
        gc_range=None,
        custom_items=None,
        #
        # PARAMS:
        font_size=8,
        title=None,
        color=None,
    ):
        """Sankey plot."""
        return sankey_chart(
            #
            # PARAMS:
            fields=fields,
            max_n=max_n,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # PARAMS:
            font_size=font_size,
            title=title,
            color=color,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def statistics(self):
        """Returns a statistics sheet of the database."""
        return statistics(
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def summary_sheet(self):
        """Returns a summary sheet of the database."""
        return summary_sheet(
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def terms_by_year(
        self,
        #
        # PARAMS:
        field,
        cumulative=False,
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        return terms_by_year(
            #
            # PARAMS:
            field=field,
            cumulative=cumulative,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )


def records(
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    return Records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
