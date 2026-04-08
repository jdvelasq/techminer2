import sys
import time
from abc import ABC, abstractmethod
from datetime import timedelta
from pathlib import Path
from typing import Any

from tm2p._intern import ParamsMixin
from tm2p.enum import Field
from tm2p.ingest.records import RecordViewer

from .._intern import Step
from .phases.p01_scaffold.p01_project_structure import p01_project_structure


class BaseIngest(
    ABC,
    ParamsMixin,
):

    _HEADER_WIDTH = 80
    _STEP_PREFIX = "  → "
    _DETAIL_PREFIX = "    "

    # -------------------------------------------------------------------------
    # Phase descriptions
    # -------------------------------------------------------------------------

    _02_COMPRESS = "Compressing raw data"
    _03_PARS = "Parsing data"
    _04_FILTER = "Filtering data"
    _05_PREPARE = "Preparing data"
    _06_AUTH = "Preparing author thesaurus"
    _07_AFFIL = "Extracting affiliation information"
    _08_ORG = "Extracting organization information"
    _09_CTRY = "Extracting country information"
    _10_SRC = "Preparing source information"
    _11_KW_PREPAR = "Preparing keywords"
    _12_NLP_PREPAR = "Preparing NLP"
    _13_CONCEPT = "Extracting concepts"
    _14_REC = "Preparing records"
    _15_CIT_REF = "Preparing cited references"
    _16_REVIEW = "Reviewing"

    # -------------------------------------------------------------------------
    # I/O
    # -------------------------------------------------------------------------

    def _write(self, text: str) -> None:
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_header(self) -> None:
        separator = "=" * self._HEADER_WIDTH
        self._write(f"\n{separator}\nImporting Data\n{separator}\n")

    def _print_phase(self, index: int, description: str) -> None:
        self._write(f"\n[{index}] {description}\n")

    def _print_step(self, message: str) -> None:
        self._write(f"{self._STEP_PREFIX}{message}...\n")

    def _print_detail(self, message: str) -> None:
        self._write(f"{self._DETAIL_PREFIX}{message}\n")

    def _print_step_result(self, result: Any, count_message: str) -> None:
        if isinstance(result, dict):
            for key, value in result.items():
                self._print_detail(f"{key}: {value}")
        elif isinstance(result, list):
            count = len(result)
            if count > 0:
                self._print_detail(count_message.format(count=count))
        elif isinstance(result, int):
            if result > 0:
                self._print_detail(count_message.format(count=result))

    def _format_elapsed_time(self, elapsed: timedelta) -> str:
        total_seconds = int(elapsed.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def ingestion_pipeline(self) -> tuple[tuple[str, list[Step]], ...]:

        from .phases.p02_compress import p02_compress
        from .phases.p03_pars import p03_pars
        from .phases.p04_filter import p04_filter
        from .phases.p05_prepare import p05_prepare
        from .phases.p06_auth import p06_auth
        from .phases.p07_affil import p07_affil
        from .phases.p08_org import p08_org
        from .phases.p09_ctry import p09_ctry
        from .phases.p10_src import p10_src
        from .phases.p11_kw_prepar import p11_kw_prepar
        from .phases.p12_nlp_prepar import p12_nlp_prepar
        from .phases.p13_concept import p13_concept
        from .phases.p14_rec import p14_rec
        from .phases.p15_cit_ref import p15_cit_ref
        from .phases.p16_review import p16_review

        return (
            (self._02_COMPRESS, p02_compress(self.params)),
            (self._03_PARS, p03_pars(self.params)),
            (self._04_FILTER, p04_filter(self.params)),
            (self._05_PREPARE, p05_prepare(self.params)),
            (self._06_AUTH, p06_auth(self.params)),
            (self._07_AFFIL, p07_affil(self.params)),
            (self._08_ORG, p08_org(self.params)),
            (self._09_CTRY, p09_ctry(self.params)),
            (self._10_SRC, p10_src(self.params)),
            (self._11_KW_PREPAR, p11_kw_prepar(self.params)),
            (self._12_NLP_PREPAR, p12_nlp_prepar(self.params)),
            (self._13_CONCEPT, p13_concept(self.params)),
            (self._14_REC, p14_rec(self.params)),
            (self._15_CIT_REF, p15_cit_ref(self.params)),
            (self._16_REVIEW, p16_review(self.params)),
        )

    # ------------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------------

    def _execute_step(self, step: Step) -> None:
        self._print_step(step.name)
        result = step()

        if step.count_message:
            self._print_step_result(result, step.count_message)

    def _set_marker(self) -> None:
        marker = self.get_marker()
        filename = f"_{marker.upper()}"
        filepath = Path(self.params.root_directory) / "ingest" / "process" / filename
        filepath.touch()

    def _generate_documents_report(self) -> None:

        docs = (
            RecordViewer()
            .update(**self.params.__dict__)
            .with_source_field(Field.ABSTR_RAW)
            .run()
        )

        filepath = Path(self.params.root_directory) / "report" / "documents.txt"
        with filepath.open("w", encoding="utf-8") as f:
            for doc in docs:
                f.write(f"{doc}\n---\n\n")

    def run(self) -> None:

        start_time = time.monotonic()
        self._print_header()

        self._set_marker()

        p01_project_structure(str(self.params.root_directory))

        for phase_index, (phase_name, steps) in enumerate(
            self.ingestion_pipeline(), start=1
        ):
            self._print_phase(phase_index, phase_name)
            for step in steps:
                self._execute_step(step)

        end_time = time.monotonic()
        elapsed = timedelta(seconds=end_time - start_time)
        status = f"Execution time : {self._format_elapsed_time(elapsed)}"

        self._generate_documents_report()

        self._write("\n" + "-" * self._HEADER_WIDTH + "\n")
        self._write(f"{status}\n")
        self._write("-" * self._HEADER_WIDTH + "\n")

    @abstractmethod
    def get_marker(self) -> str:
        pass
