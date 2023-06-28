# flake8: noqa
"""
Field
===============================================================================





"""

from .chatbot_prompts import format_chatbot_prompt_for_df
from .filtering_lib import generate_custom_items
from .metrics_lib import indicators_by_field
from .sorting_lib import sort_indicators_by_metric


# pylint: disable=too-many-instance-attributes
class Field:
    """Class to manage the field of a database."""

    root_dir: str
    database: str
    year_filter: str
    cited_by_filter: str
    filters: dict

    def __init__(
        # pylint: disable=too-many-arguments
        self,
    ):
        """Constructor"""

        self.dbfield = None
        self.metric = None
        self.top_n = None
        self.occ_range = None
        self.gc_range = None
        self.custom_items = None
        self.indicators = None
        self.chatbot_prompt = None

    # pylint: disable=too-many-arguments
    def field(
        self,
        field,
        metric="OCC",
        top_n=None,
        occ_range=None,
        gc_range=None,
        custom_items=None,
    ):
        """Returns the field of the database."""

        self.dbfield = field
        self.metric = metric
        self.top_n = top_n
        self.occ_range = occ_range
        self.gc_range = gc_range
        self.custom_items = custom_items
        self.indicators = None
        self.chatbot_prompt = None

        self.compute_indicators_by_field()
        self.sort_indicators_by_metric()
        self.compute_custom_items()
        self.filter_indicators()
        self.check_metric()

        return self

    def compute_indicators_by_field(self):
        """Compute indicators by field

        :meta private:
        """

        self.indicators = indicators_by_field(
            field=self.dbfield,
            root_dir=self.root_dir,
            database=self.database,
            year_filter=self.year_filter,
            cited_by_filter=self.cited_by_filter,
            **self.filters,
        )

    def sort_indicators_by_metric(self):
        """Sort indicators by metric.

        :meta private:
        """
        self.indicators = sort_indicators_by_metric(
            indicators=self.indicators,
            metric=self.metric,
        )

    def compute_custom_items(self):
        """Compute custom items.

        :meta private:
        """

        if self.custom_items is not None:
            return

        if self.metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(self.indicators, "OCC"),
                top_n=self.top_n,
                occ_range=self.occ_range,
                gc_range=self.gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    self.indicators, "global_citations"
                ),
                top_n=self.top_n,
                occ_range=self.occ_range,
                gc_range=self.gc_range,
            )

            self.custom_items = custom_items_occ[:]
            self.custom_items += [
                item
                for item in custom_items_gc
                if item not in custom_items_occ
            ]

        else:
            self.custom_items = generate_custom_items(
                indicators=self.indicators,
                top_n=self.top_n,
                occ_range=self.occ_range,
                gc_range=self.gc_range,
            )

    def filter_indicators(self):
        """Filter indicators.

        :meta private:
        """
        self.indicators = self.indicators[
            self.indicators.index.isin(self.custom_items)
        ]

    def check_metric(self):
        """Check metric.

        :meta private:
        """
        self.metric = "OCC" if self.metric == "OCCGC" else self.metric

    @property
    def df_(self):
        """Indicators dataframe."""
        return self.indicators

    @property
    def chatbot_prompt_(self):
        """Chat GPT prompt."""
        main_text = (
            "Your task is to generate an analysis about the bibliometric indicators of the "
            f"'{self.dbfield}' field in a scientific bibliography database. Summarize the table below, "
            f"sorted by the '{self.metric}' metric, and delimited by triple backticks, identify "
            "any notable patterns, trends, or outliers in the data, and discuss their "
            "implications for the research field. Be sure to provide a concise summary "
            "of your findings in no more than 150 words."
        )
        return format_chatbot_prompt_for_df(
            main_text, self.indicators.to_markdown()
        )
