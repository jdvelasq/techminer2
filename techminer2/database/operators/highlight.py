# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Highlight Nouns and Noun Phrases
===============================================================================


Example:
    >>> import textwrap
    >>> from techminer2.database.operators import (
    ...     TokenizeOperator,
    ...     DeleteOperator,
    ...     HighlightOperator,
    ... )
    >>> from techminer2.database.tools import Query

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
    ...     .run()
    ... )


    >>> # Creates, configure, and run the highlighter
    >>> highlighter = (
    ...     HighlightOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("cleaned_raw_abstract")
    ...     .with_other_field("highlighted_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> highlighter.run()

    >>> # Query the database to test the cleaner
    >>> query = (
    ...     Query()
    ...     .with_query_expression("SELECT highlighted_raw_abstract FROM database LIMIT 10;")
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ... )
    >>> df = query.run()
    >>> print(textwrap.fill(df.values[1][0], width=80))
    THE_RAPID_DEVELOPMENT of INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY is
    transforming THE_ENTIRE_INDUSTRY_LANDSCAPE , heralding A_NEW_ERA of
    CONVERGENCE_SERVICES . as one of THE_DEVELOPING_COUNTRIES in
    THE_FINANCIAL_SECTOR , CHINA is experiencing AN_UNPRECEDENTED_LEVEL of
    CONVERGENCE between FINANCE and TECHNOLOGY . this study applies THE_LENS of
    ACTOR_NETWORK_THEORY ( ANT ) to conduct A_MULTI_LEVEL_ANALYSIS of
    THE_HISTORICAL_DEVELOPMENT of CHINA ' s FINANCIAL_TECHNOLOGY_INDUSTRY . it
    attempts to elucidate THE_PROCESS of BUILDING and disrupting A_VARIETY of
    NETWORKS comprising HETEROGENEOUS_ACTORS involved in
    THE_NEWLY_EMERGING_CONVERGENCE_INDUSTRY . this research represents
    A_STEPPING_STONE in exploring THE_INTERACTION between FINTECH and its yet
    unfolding SOCIAL_AND_POLITICAL_CONTEXT . it also DISCUSSES_POLICY_IMPLICATIONS
    for CHINA_FINTECH_INDUSTRY , focusing_on THE_CHANGING_ROLE of THE_STATE in
    fostering THE_GROWTH of NATIONAL_INDUSTRY within_and_outside_of CHINA . 2015
    elsevier ltd .





    >>> # Deletes the fields
    >>> field_deleter = (
    ...     DeleteOperator()
    ...     .where_root_directory_is("examples/fintech/")
    ... )
    >>> field_deleter.with_field("cleaned_raw_abstract").run()
    >>> field_deleter.with_field("highlighted_raw_abstract").run()



"""
from ..._internals.mixins import ParamsMixin
from .._internals.operators.highlight import internal__highlight
from .._internals.protected_fields import PROTECTED_FIELDS


class HighlightOperator(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.other_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.other_field}` is protected")

        internal__highlight(
            source=self.params.field,
            dest=self.params.other_field,
            #
            # DATABASE PARAMS:
            root_directory=self.params.root_directory,
        )


#
