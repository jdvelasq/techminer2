# flake8: noqa
# pylint: disable=missing-docstring
# pylint: disable=line-too-long
"""
Records
==============================================================================



* **USER COMPUTATIONAL INTERFACE:**

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

>>> tm2p.Records(root_dir=root_dir)
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={})

    
>>> tm2p.Records(root_dir=root_dir, filters={
...     "countries": ['Australia', 'United Kingdom', 'United States']
... })
Records(root_dir='data/regtech/', database='main', year_filter=(None, None),
    cited_by_filter=(None, None), filters={'countries': ['Australia', 'United
    Kingdom', 'United States']})


"""

import textwrap
from dataclasses import dataclass
from dataclasses import field as datafield

from .concordances import Concordances
from .coverage import coverage

# from .counters_lib import add_counters_to_frame_axis
from .list_items import ListItems
from .main_information import MainInformation
from .summary_view import summary_view

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
    def concordances(
        self,
        search_for,
        top_n=50,
        report_file="concordances_report.txt",
        prompt_file="concordances_prompt.txt",
    ):
        """Returns a Concordances object."""
        return Concordances(
            #
            # Parameters:
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
            filters=self.filters,
        )

    def main_information(self):
        """Returns a MainInformation object."""
        return MainInformation(
            #
            # DATABASE PARAMS:
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def summary_view(self):
        """Returns a summary sheet of the database."""
        return summary_view(
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
    def list_items(
        self,
        field,
        metric="OCC",
        top_n=None,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
    ):
        """Field"""
        return ListItems(
            #
            # FUNCTION PARAMS:
            field=field,
            metric=metric,
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items if custom_items is not None else [],
            #
            # DATABASE PARAMS:
            #
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )
