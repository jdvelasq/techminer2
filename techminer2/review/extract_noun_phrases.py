"""
Extract Noun Phrases
===============================================================================

Smoke test:
    >>> from techminer2.review import ExtractNounPhrases
    >>> (
    ...     ExtractNounPhrases()
    ...     .where_root_directory("examples/small/")
    ... ).run()


"""

import sys
from typing import Any

from techminer2._internals import ParamsMixin
from techminer2.io._internals.step import Step

__reviewed__ = "2026-01-28"


class ExtractNounPhrases(
    ParamsMixin,
):
    """:meta private:"""

    _HEADER_WIDTH = 70
    _STEP_PREFIX = "  → "
    _DETAIL_PREFIX = "    "

    # -------------------------------------------------------------------------
    # I/O
    # -------------------------------------------------------------------------

    def _write(self, text: str) -> None:
        sys.stderr.write(text)
        sys.stderr.flush()

    def _print_header(self) -> None:
        separator = "=" * self._HEADER_WIDTH
        self._write(f"\n{separator}\nExtracting noun phrases\n{separator}\n")

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

    # ------------------------------------------------------------------------
    # Execution
    # ------------------------------------------------------------------------

    def _execute_step(self, step: Step) -> None:
        self._print_step(step.name)
        result = step()

        if step.count_message:
            self._print_step_result(result, step.count_message)

    def _build_steps(self) -> list[Step]:

        from techminer2.io._internals.words_and_np.extract_abstract_phrases import (
            extract_abstract_phrases,
        )
        from techminer2.io._internals.words_and_np.extract_title_phrases import (
            extract_title_phrases,
        )
        from techminer2.io._internals.words_and_np.merge_keywords_phrases import (
            merge_keywords_phrases,
        )
        from techminer2.io._internals.words_and_np.merge_title_abstract_phrases import (
            merge_title_abstract_phrases,
        )
        from techminer2.io._internals.words_and_np.uppercase_abstract_phrases import (
            uppercase_abstract_phrases,
        )
        from techminer2.io._internals.words_and_np.uppercase_title_phrases import (
            uppercase_title_phrases,
        )

        common_kwargs = {"root_directory": self.params.root_directory}

        return [
            Step(
                name="Uppercasing abstract NP",
                function=uppercase_abstract_phrases,
                kwargs=common_kwargs,
                count_message="{count} records processed",
            ),
            Step(
                name="Uppercasing title NP",
                function=uppercase_title_phrases,
                kwargs=common_kwargs,
                count_message="{count} records processed",
            ),
            Step(
                name="Extracting abstract phrases",
                function=extract_abstract_phrases,
                kwargs=common_kwargs,
                count_message="{count} records processed",
            ),
            Step(
                name="Extracting title phrases",
                function=extract_title_phrases,
                kwargs=common_kwargs,
                count_message="{count}  records processed",
            ),
            Step(
                name="Merging title and abstract phrases",
                function=merge_title_abstract_phrases,
                kwargs=common_kwargs,
                count_message="{count}  records processed",
            ),
            Step(
                name="Merging keywords and NP",
                function=merge_keywords_phrases,
                kwargs=common_kwargs,
                count_message="{count} keywords and NP merged",
            ),
        ]

    def run(self) -> None:

        self._print_header()
        for step in self._build_steps():
            self._execute_step(step)
