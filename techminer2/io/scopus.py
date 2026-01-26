# CODE_REVIEW: 2026-01-26
"""
Scopus
===============================================================================

Smoke test - successful import:
    >>> from techminer2.scopus import Scopus
    >>> result = (
    ...     Scopus()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )
    >>> result.success
    True

Smoke test - result attributes:
    >>> result.file_path
    'examples/small/'
    >>> result.status.startswith('Execution time :')
    True

Smoke test - fluent interface:
    >>> scopus = Scopus()
    >>> scopus_configured = scopus.where_root_directory("examples/small/")
    >>> scopus_configured is scopus
    True

"""

import sys
import time
from datetime import timedelta
from typing import Any

from techminer2._internals.mixins import ParamsMixin

from ._internals import Step
from ._internals.bibliographical_information.build_steps import (
    build_bibliographical_information_steps,
)
from ._internals.citation_information.build_steps import (
    build_citation_information_steps,
)
from ._internals.descriptors.build_steps import build_descriptors_steps
from ._internals.funding_details.build_steps import build_funding_details_steps
from ._internals.other_information.build_steps import build_other_information_steps
from ._internals.scaffolding.build_steps import build_scaffolding_steps
from ._internals.scopus_result import ScopusResult
from ._internals.title_abstract_keywords.build_steps import (
    build_title_abstract_keywords_steps,
)


class Scopus(ParamsMixin):
    """:meta private:"""

    _HEADER_WIDTH = 70
    _STEP_PREFIX = "  → "
    _DETAIL_PREFIX = "    "

    _PHASE_SCAFFOLDING = "Building project scaffold"
    _PHASE_CITATION = "Processing citation information"
    _PHASE_BIBLIOGRAPHICAL = "Processing bibliographical information"
    _PHASE_TEXT_CONTENT = "Processing title, abstract, and keywords"
    _PHASE_DESCRIPTORS = "Processing descriptors"
    _PHASE_FUNDING = "Processing funding details"
    _PHASE_OTHER = "Processing other information"

    # -------------------------------------------------------------------------
    # I/O
    # -------------------------------------------------------------------------

    def _write(self, text: str) -> None:
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_header(self) -> None:
        separator = "=" * self._HEADER_WIDTH
        self._write(f"\n{separator}\nImporting Scopus Data\n{separator}\n")

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

    # ------------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------------

    def _pipeline(self) -> tuple[tuple[str, list[Step]], ...]:
        return (
            (
                self._PHASE_SCAFFOLDING,
                build_scaffolding_steps(self.params),
            ),
            (self._PHASE_CITATION, build_citation_information_steps(self.params)),
            (
                self._PHASE_BIBLIOGRAPHICAL,
                build_bibliographical_information_steps(self.params),
            ),
            (
                self._PHASE_TEXT_CONTENT,
                build_title_abstract_keywords_steps(self.params),
            ),
            (
                self._PHASE_DESCRIPTORS,
                build_descriptors_steps(self.params),
            ),
            (
                self._PHASE_FUNDING,
                build_funding_details_steps(self.params),
            ),
            (
                self._PHASE_OTHER,
                build_other_information_steps(self.params),
            ),
        )

    def _execute_step(self, step: Step) -> None:
        self._print_step(step.name)
        result = step()

        if step.count_message:
            self._print_step_result(result, step.count_message)

    def run(self) -> ScopusResult:

        start_time = time.monotonic()
        self._print_header()

        for phase_index, (phase_name, steps) in enumerate(self._pipeline(), start=1):
            self._print_phase(phase_index, phase_name)
            for step in steps:
                self._execute_step(step)

        end_time = time.monotonic()
        elapsed = timedelta(seconds=end_time - start_time)
        status = f"Execution time : {self._format_elapsed_time(elapsed)}"

        return ScopusResult(
            colored_output=self.params.colored_output,
            file_path=str(self.params.root_directory),
            msg="Data imported successfully.",
            success=True,
            status=status,
        )
