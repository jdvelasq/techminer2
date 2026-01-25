# pylint: disable=import-outside-toplevel
"""
Importer
===============================================================================
# doctest: +SKIP

Smoke test:
    >>> from techminer2.scopus import Importer
    >>> (
    ...     Importer()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )


"""

import sys
import time

from techminer2._internals.mixins import ParamsMixin

from ._internals import Step
from ._internals.bibliographical_information.build_steps import (
    build_bibliographical_information_steps,
)
from ._internals.funding_details.build_steps import build_funding_details_steps
from ._internals.other_information.build_steps import build_other_information_steps
from ._internals.scaffolding.build_steps import build_scaffolding_steps
from ._internals.scopus_result import ScopusResult
from ._internals.title_abstract_keywords.build_steps import (
    build_title_abstract_keywords_steps,
)


class Scopus(
    ParamsMixin,
):
    """:meta private:"""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._phase: int = 0

    # ------------------------------------------------------------------------
    # Message printing methods
    # ------------------------------------------------------------------------

    def _print_header(self) -> None:
        sys.stderr.write("\n" + "=" * 70 + "\n")
        sys.stderr.write("Importing Scopus Data\n")
        sys.stderr.write("=" * 70 + "\n")
        sys.stderr.flush()

    def _print_phase(self, description: str) -> None:
        sys.stderr.write(f"\n[{self._phase}] {description}\n")
        sys.stderr.flush()

    def _print_step(self, message: str):
        sys.stderr.write(f"  → {message}...\n")
        sys.stderr.flush()

    def _print_detail(self, message: str, leading_newline: bool = False) -> None:
        prefix = "\n" if leading_newline else ""
        sys.stderr.write(f"{prefix}    {message}\n")
        sys.stderr.flush()

    # ------------------------------------------------------------------------
    # Pipeline definition
    # ------------------------------------------------------------------------

    def _build_pipeline(self) -> dict[str, list[Step]]:

        return {
            # ----------------------------------------------------------------
            "Building project scaffold": build_scaffolding_steps(
                self.params,
            ),
            "Preparing title, abstract, and keywords": build_title_abstract_keywords_steps(
                self.params,
            ),
            "Processing bibliographical information": build_bibliographical_information_steps(
                self.params,
            ),
            "Processing funding details": build_funding_details_steps(
                self.params,
            ),
            "Processing other information": build_other_information_steps(
                self.params,
            ),
            # ----------------------------------------------------------------
            "Creating record identifiers": [],
        }

    # ------------------------------------------------------------------------
    # Pipeline execution
    # ------------------------------------------------------------------------

    def _execute_step(self, step: Step) -> None:

        self._print_step(step.name)

        result = step.function(self.params.root_directory, **step.kwargs)

        if not step.count_message:
            return

        if isinstance(result, dict):
            for key, value in result.items():
                self._print_detail(f"{key}: {value}")
        elif isinstance(result, (list, int)):
            count = len(result) if isinstance(result, list) else result
            if count > 0:
                self._print_detail(step.count_message.format(count=count))

    def run(self) -> ScopusResult:

        start_time = time.time()

        self._print_header()

        for phase_name, steps in self._build_pipeline().items():
            self._phase += 1
            self._print_phase(phase_name)
            for step in steps:
                self._execute_step(step)

        end_time = time.time()
        elapsed_time = end_time - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        status = f"Execution time : {int(hours):02}:{int(minutes):02}:{seconds:04.1f}"

        return ScopusResult(
            colored_output=self.params.colored_output,
            file_path=str(self.params.root_directory),
            msg="Data imported successfully.",
            success=True,
            status=status,
        )
