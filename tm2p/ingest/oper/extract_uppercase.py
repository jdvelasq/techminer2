"""
ExtractUppercase
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import ExtractUppercase
    >>> (
    ...     ExtractUppercase()
    ...     #
    ...     # FIELDS:
    ...     .with_source_field(Field.ABSTR_UPPER)
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
    high dimensional optimization; computational intelligence; resource constraints;
    evolutionary algorithms; mimic; heritable characteristics; biological populations; favor;
    generations; stochastic variations; introduce suboptimal candidates; population diversity;
    balance exploration and exploitation; suboptimal solutions; premature convergence;
    computational demands; resource constrained environments; monkeypox optimization; mo;
    novel evolutionary algorithm; infection and replication lifecycle; monkeypox virus; mo
    mimics; virus; rapid spread; virus to cell infection; virus; vulnerable cells; global
    exploration; search space; cell to cell transmission; fast local propagation; modeling;
    refinement; high potential solutions; accelerated replication; mo; effective virion
    copies; compact and memory efficient population; biologically grounded design; accelerates
    convergence; aligns mo; tinyml principles; low power; resource constrained iot
    environments; mo; recent algorithms; functions; engineering design problems; mo; lower
    energy consumption; execution time; state of the art competitors; robust accuracy;
    theoretical analysis reveals mo; time complexity; scalability; statistical validation;
    friedman and fisher tests; supports mo; performance gains

"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper import extract_uppercase
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class ExtractUppercase(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.target_field}` is protected")

        extract_uppercase(
            source=self.params.source_field,
            target=self.params.target_field,
            root_directory=self.params.root_directory,
        )
