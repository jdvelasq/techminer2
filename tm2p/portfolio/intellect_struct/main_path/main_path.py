"""
MainPath
===============================================================================

Smoke tests:
    >>> from tm2p.enum import RecordOrderBy  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.main_path import MainPath  # type: ignore
    >>> df = (
    ...     MainPath()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .having_top_n_units(None)
    ...     .having_minimum_cited_unit_occurrences(0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
    ...     #
    ...     .run()
    ... )
    >>> assert len(df) > 0
    >>> print(df[0])
    UT 60
    AR Chen YL, 2025, BUILD, V15, DOI 10.3390/buildings15060949
    TI What Kind of Policy Intensity Can Promote the Development of Intelligent
       Construction in Construction Enterprises?  Study Based on Evolutionary Games
       and System Dynamics Analysis
    AU Chen YL; Shi YZ; Lin SZ; Ding MC
    TC 1
    SO BUILD
    PY 2025
    AB Previous studies have focused on the fact that government policies are the
       key factors in promoting the development of intelligent construction in
       construction enterprises.  However, how to select different forms of policy
       support and quantify the intensity of policy support, as well as the impact
       on the behavioral strategies of construction enterprises and the government,
       still needs in-depth exploration.  This paper constructs an evolutionary
       game model between construction companies and the government, using the
       system dynamics simulation software Vensim to analyze the model under three
       different government policy support scenarios.  The study explores how
       varying levels of policy support and key factors influence the strategic
       choices of the game participants, providing valuable insights for promoting
       the development of intelligent construction.  The key findings are as
       follows: (1) The willingness to adopt intelligent construction is heavily
       dependent on policy incentives.  The incentive effect of the three single
       policies is much lower than that of the combined policies, and only high-
       intensity special fund support (more than 8 CNY/m2) significantly promotes
       widespread adoption.  Among combinations of policies, tax incentives coupled
       with special funds prove most effective.  (2) The government's decision to
       actively promote intelligent construction hinges on a cost-benefit analysis.
       Under medium to high levels of special fund support, medium to low levels of
       service support are more beneficial for reaching a stable state of
       intelligent construction implementation.  (3) Reducing the incremental costs
       of intelligent construction transformation is the primary key factor in
       promoting construction.  The findings contribute to a deeper understanding
       of how both the government and construction companies can adjust their
       strategies in response to policy changes, ultimately leading to more
       effective policy implementation and strategic decision-making.
    DE evolutionary game theory; intelligent construction; policy incentive;
       simulation modeling; system dynamics
    ID industry 40; government; technologies
    <BLANKLINE>





"""

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.rec import RecordViewer
from tm2p.portfolio.intellect_struct.main_path._intern.comp_main_path import (
    compute_main_path,
)


class MainPath(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        #
        # Creates a table with citing and cited articles
        articles_in_main_path, _ = compute_main_path(params=self.params)

        #
        # remove counters
        articles_in_main_path = [
            " ".join(article.split(" ")[:-1]) for article in articles_in_main_path
        ]

        #
        # build the filter
        records_match = {Field.REC_ID: articles_in_main_path}

        documents = (
            RecordViewer()
            .update(**self.params.__dict__)
            .with_source_field(Field.ABSTR_RAW)
            .where_records_match(records_match)
            .run()
        )

        return documents
