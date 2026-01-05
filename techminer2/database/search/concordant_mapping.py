# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Concordant Mapping
=========================================================================================


Example:
    >>> from pprint import pprint
    >>> from techminer2.database.search import ConcordantMapping

    >>> # Create, configure, and run the mapper
    >>> # order_records_by:
    >>> #   date_newest, date_oldest, global_cited_by_highest, global_cited_by_lowest
    >>> #   local_cited_by_highest, local_cited_by_lowest, first_author_a_to_z
    >>> #   first_author_z_to_a, source_title_a_to_z, source_title_z_to_a
    >>> #

    >>> mapper = (
    ...     ConcordantMapping()
    ...     #
    ...     .with_abstract_having_pattern("FINTECH")
    ...     #
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("date_newest")
    ... )
    >>> mapping = mapper.run()
    >>> pprint(mapping[0])
    {'AB': 'we investigate the economic and technological determinants inducing '
           'entrepreneurs to establish ventures with the purpose of reinventing '
           'financial technology ( fintech ) . we find that countries witness more '
           'fintech startup formations when the economy is well developed and '
           'venture capital is readily available . finally , the more difficult it '
           'is for companies to access loans , the higher is the number of fintech '
           'startups in a country . overall , the evidence suggests that fintech '
           'startup formation need not be left to chance , but active policies can '
           'influence the emergence of this new sector',
     'AR': 'Haddad C., 2019, SMALL BUS ECON, V53, P81',
     'AU': 'Haddad C.; Hornuf L.',
     'DE': 'ENTREPRENEURSHIP; FINANCIAL_INSTITUTIONS; FINTECH; STARTUPS',
     'ID': nan,
     'PY': 2019,
     'SO': 'Small Business Economics',
     'TC': 258,
     'TI': 'The emergence of the global fintech market: economic and technological '
           'determinants',
     'UT': 26}



"""
import re

from textblob import TextBlob  # type: ignore

from techminer2._internals.mixins import (
    ParamsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
)
from techminer2.database._internals.io.load_filtered_records_from_database import (
    internal__load_filtered_records_from_database,
)


class ConcordantMapping(
    ParamsMixin,
    RecordMappingMixin,
    RecordViewerMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def _step_1_load_the_database(self):
        return internal__load_filtered_records_from_database(params=self.params)

    # -------------------------------------------------------------------------
    def _step_2_filter_by_concordance(self, records):

        self.search_for = self.params.pattern.lower().replace("_", " ")

        found = (
            records["abstract"]
            .astype(str)
            .str.contains(r"\b" + self.search_for + r"\b", regex=True)
        )
        records = records[found]
        return records

    # -------------------------------------------------------------------------
    def _step_3_process_abstracts(self, records):

        #
        # extract phrases.
        records["abstract"] = records["abstract"].map(lambda x: TextBlob(x).sentences)
        records["abstract"] = records["abstract"].map(lambda x: [str(y) for y in x])
        records["abstract"] = records["abstract"].map(
            lambda x: [y[:-2] if y[-2:] == " ." else y for y in x]
        )
        #
        regex = r"\b" + self.search_for + r"\b"
        #
        records["abstract"] = records["abstract"].map(
            lambda x: [y for y in x if re.search(regex, y)]
        )
        records["abstract"] = records["abstract"].map(" . ".join)

        return records

    # -------------------------------------------------------------------------
    def run(self):

        records = self._step_1_load_the_database()
        records["abstract"] = records["tokenized_abstract"]
        records = self._step_2_filter_by_concordance(records)
        records = self._step_3_process_abstracts(records)
        mapping = self.build_record_mapping(records)

        return mapping
