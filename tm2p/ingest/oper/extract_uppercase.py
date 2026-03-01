"""
ExtractUppercase
===============================================================================

Smoke test:
    >>> from tm2p import CorpusField
    >>> from tm2p.ingest.operationsimport TokenizeOperator
    >>> (
    ...     TokenizeOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("raw_abstract")
    ...     .with_other_field("cleaned_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     #
    ...     .run()
    ... )


    >>> # Creates, configure, and run the operator
    >>> from tm2p.ingest.operationsimport HighlightOperator
    >>> (
    ...     HighlightOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("cleaned_raw_abstract")
    ...     .with_other_field("highlighted_raw_abstract")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     #
    ...     .run()
    ... )


    >>> # Collect terms in upper case from the field
    >>> from tm2p.ingest.operationsimport CollectOperator
    >>> (
    ...     CollectOperator()
    ...     #
    ...     # FIELDS:
    ...     .with_field("highlighted_raw_abstract")
    ...     .with_other_field("extracted_nouns_and_phrases")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     #
    ...     .run()
    ... )



    >>> # Query the database to test the cleaner
    >>> from tm2p.io import Query
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT extracted_nouns_and_phrases FROM database LIMIT 10;")
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .run()
    ... )
    >>> import textwrap
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
    >>> from tm2p.ingest.operationsimport DeleteOperator
    >>> field_deleter = (
    ...     DeleteOperator()
    ...     .where_root_directory("tests/fintech/")
    ... )
    >>> field_deleter.with_field("cleaned_raw_abstract").run()
    >>> field_deleter.with_field("highlighted_raw_abstract").run()
    >>> field_deleter.with_field("extracted_nouns_and_phrases").run()

"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.data_sourc._intern.oper import extract_uppercase
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class ExtractUppercase(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        if self.params.index_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.index_field}` is protected")

        extract_uppercase(
            source=self.params.source_field,
            target=self.params.index_field,
            #
            # DATABASE PARAMS:
            root_directory=self.params.root_directory,
        )


#
