"""
TransformColumn
===============================================================================

Smoke test:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.oper import TransformColumn
    >>> (
    ...     TransformColumn()
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .with_target_field(Field.USR0)
    ...     .with_transformation_function(lambda x: x.str.upper())
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .run()
    ... )

    >>> from tm2p.ingest.oper import Query
    >>> (
    ...     Query()
    ...     .with_query_expression("SELECT USR0 FROM database LIMIT 10;")
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )  # doctest: +SKIP
                                                    USR0
    0  AUDIO CLASSIFICATION; INTERPRETABILITY; STATE ...
    1  EVOLUTIONARY COMPUTATION; HIGH-DIMENSIONAL BEN...
    2  CONVOLUTIONAL NEURAL NETWORK (CNN); HARDWARE (...
    3         ANDROID; HDC; HEALTH MONITORING; WEARABLES
    4  ADAPTIVE MODELING; GEOTECHNICAL ENGINEERING; I...
    5  CNNS; ENERGY-EFFICIENT TRAINING; MODEL COMPRES...
    6  HYPERDIMENSIONAL COMPUTING; INTERNET-OF-THINGS...
    7                ALU; MICROPROCESSOR; RISC-V; TINYML
    8  EDGE SYSTEMS; FREEMARK; POST-TRAINING; TINY MA...
    9  DENDRITIC PROCESSING; ENERGY EFFICIENCY; GRADE...


"""

from tm2p._intern import ParamsMixin
from tm2p.ingest.datasrc._intern.oper.transform_col import transform_column
from tm2p.ingest.extr._helpers._protected_fields import PROTECTED_FIELDS


class TransformColumn(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> None:

        if self.params.source_field == self.params.target_field:
            raise ValueError(
                f"Source and target fields must differ (got `{self.params.source_field}`)"
            )

        if self.params.target_field in PROTECTED_FIELDS:
            raise ValueError(f"Field `{self.params.source_field}` is protected")

        if self.params.transformation_function is None:
            raise ValueError("Transformation function must be provided")

        transform_column(
            #
            # FIELD:
            source=self.params.source_field,
            target=self.params.target_field,
            function=self.params.transformation_function,
            root_directory=self.params.root_directory,
        )
