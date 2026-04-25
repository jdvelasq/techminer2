"""
TokenizeColumn
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import TokenizeColumn
    >>> (
    ...     TokenizeColumn()
    ...     #
    ...     # FIELDS:
    ...     .with_source_field(Field.ABSTR_RAW)
    ...     .with_target_field(Field.USR0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     #
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> df = (
    ...     Query()
    ...     .with_query_expression("SELECT USR0 FROM database LIMIT 10;")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> import textwrap
    >>> print(textwrap.fill(df.values[1][0], width=90))  # doctest: +SKIP
    high_dimensional optimization remains a key challenge in computational intelligence ,
    especially under resource constraints . evolutionary algorithms , which mimic the change
    in heritable characteristics of biological populations , have been proposed to address
    this . these algorithms apply selection pressure to favor better solutions over
    generations , and stochastic variations may occasionally introduce suboptimal candidates
    to preserve population diversity . however , they often struggle to balance exploration
    and exploitation , leading to suboptimal solutions , premature convergence , and
    significant computational demands , making them unsuitable for resource_constrained
    environments . this paper introduces monkeypox optimization ( mo ) , a novel evolutionary
    algorithm inspired by the infection and replication lifecycle of the monkeypox virus . mo
    mimics the virus ' s rapid spread by employing virus_to_cell infection , where the virus
    persistently seeks out vulnerable cells to penetrate_representing global exploration of
    the search space . once inside , cell_to_cell transmission enables fast local propagation
    , modeling the refinement of high_potential solutions through accelerated replication . to
    conserve resources , mo continuously deletes the least effective virion copies ,
    maintaining a compact and memory_efficient population . this biologically grounded design
    not only accelerates convergence but also aligns mo with tinyml principles , making it
    ideally suited for low_power , resource_constrained iot environments . mo is benchmarked
    against 21 recent algorithms across 90 functions from cec_2017 , cec_2019 , and cec_2020 ,
    and validated on three engineering design problems . results show mo achieves up to 13 %
    lower energy consumption and 34 % shorter execution time compared to state_of_the_art
    competitors , while maintaining robust accuracy . a theoretical analysis reveals mo ' s
    time complexity is o ( mn+rtn ) , confirming its scalability . statistical validation via
    friedman and fisher tests further supports mo ' s performance gains . 2025 the authors


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.token_col import tokenize_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class TokenizeColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(
                f"Cannot overwrite protected field `{self.params.target_field}`"
            )

        tokenize_column(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )


#
