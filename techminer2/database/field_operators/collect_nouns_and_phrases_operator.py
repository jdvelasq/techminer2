# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Collect Nouns and Phrases
===============================================================================


Example:
    >>> import textwrap
    >>> from techminer2.database.field_operators import (
    ...     TokenizeOperator,
    ...     CollectNounAndPhrasesOperator,
    ...     DeleteFieldOperator,
    ...     HighlightNounAndPhrasesOperator,
    ... )
    >>> from techminer2.tools import Query

    >>> # Creates, configure, and run the cleaner to prepare the field
    >>> (
    ...     TokenizeOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_abstract")
    ...     .with_other_field("cleaned_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )


    >>> # Creates, configure, and run the highlighter
    >>> (
    ...     HighlightNounAndPhrasesOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("cleaned_raw_abstract")
    ...     .with_other_field("highlighted_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )


    >>> # Collect terms in upper case from the field
    >>> (
    ...     CollectNounAndPhrasesOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("highlighted_raw_abstract")
    ...     .with_other_field("extracted_nouns_and_phrases")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     #
    ...     .run()
    ... )



    >>> # Query the database to test the cleaner
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT extracted_nouns_and_phrases FROM database LIMIT 10;")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .run()
    ... )
    >>> print(textwrap.fill(df.values[1][0], width=80))
    THE_RAPID_DEVELOPMENT; INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY;
    THE_ENTIRE_INDUSTRY_LANDSCAPE; A_NEW_ERA; CONVERGENCE_SERVICES;
    THE_DEVELOPING_COUNTRIES; THE_FINANCIAL_SECTOR; CHINA; AN_UNPRECEDENTED_LEVEL;
    CONVERGENCE; FINANCE; TECHNOLOGY; THE_LENS; ACTOR_NETWORK_THEORY; ANT;
    A_MULTI_LEVEL_ANALYSIS; THE_HISTORICAL_DEVELOPMENT; CHINA;
    FINANCIAL_TECHNOLOGY_INDUSTRY; THE_PROCESS; BUILDING; A_VARIETY; NETWORKS;
    HETEROGENEOUS_ACTORS; THE_NEWLY_EMERGING_CONVERGENCE_INDUSTRY; A_STEPPING_STONE;
    THE_INTERACTION; FINTECH; SOCIAL_AND_POLITICAL_CONTEXT;
    DISCUSSES_POLICY_IMPLICATIONS; CHINA_FINTECH_INDUSTRY; THE_CHANGING_ROLE;
    THE_STATE; THE_GROWTH; NATIONAL_INDUSTRY; CHINA


    >>> # Highlighted abstract:
    >>> #   THE_RAPID_DEVELOPMENT of INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY is
    >>> #   transforming THE_ENTIRE_INDUSTRY_LANDSCAPE , heralding A_NEW_ERA of
    >>> #   CONVERGENCE_SERVICES . as one of THE_DEVELOPING_COUNTRIES in
    >>> #   THE_FINANCIAL_SECTOR , CHINA is experiencing AN_UNPRECEDENTED_LEVEL of
    >>> #   CONVERGENCE between FINANCE and TECHNOLOGY . THIS_STUDY applies THE_LENS of
    >>> #   ACTOR_NETWORK_THEORY ( ant ) to conduct A_MULTI_LEVEL_ANALYSIS of
    >>> #   THE_HISTORICAL_DEVELOPMENT of CHINA FINANCIAL_TECHNOLOGY ( FINTECH ) INDUSTRY .
    >>> #   it attempts to elucidate THE_PROCESS of BUILDING and disrupting A_VARIETY of
    >>> #   NETWORKS comprising HETEROGENEOUS_ACTORS involved in
    >>> #   THE_NEWLY_EMERGING_CONVERGENCE_INDUSTRY . THIS_RESEARCH represents
    >>> #   A_STEPPING_STONE in exploring THE_INTERACTION between FINTECH and its yet
    >>> #   unfolding SOCIAL_AND_POLITICAL_CONTEXT . it also DISCUSSES_POLICY_IMPLICATIONS
    >>> #   for CHINA_FINTECH_INDUSTRY , focusing_on THE_CHANGING_ROLE of THE_STATE in
    >>> #   fostering THE_GROWTH of NATIONAL_INDUSTRY within and outside_of CHINA . 2015
    >>> #   ELSEVIER_LTD .

    >>> # Deletes the fields
    >>> field_deleter = (
    ...     DeleteFieldOperator()
    ...     .where_root_directory_is("examples/fintech/")
    ... )


    >>> field_deleter.with_field("cleaned_raw_abstract").run()
    >>> field_deleter.with_field("highlighted_raw_abstract").run()
    >>> field_deleter.with_field("extracted_nouns_and_phrases").run()

"""
from ..._internals.mixins import ParamsMixin
from .._internals.protected_fields import PROTECTED_FIELDS
from ..ingest._internals.operators.collect_nouns_and_phrases import (
    internal__collect_nouns_and_phrases,
)


class CollectNounAndPhrasesOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__collect_nouns_and_phrases(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_dir=self.params.root_directory,
        )
