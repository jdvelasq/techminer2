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

from ..io._internals.pipeline import (
    Step,
    build_funding_details_steps,
    build_other_information_steps,
    build_scaffolding_steps,
    build_title_abstract_keywords_steps,
)


class Importer(
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
            "Building project scaffold": build_scaffolding_steps(self.params),
            "Preparing title, abstract, and keywords": build_title_abstract_keywords_steps(
                self.params
            ),
            # ----------------------------------------------------------------
            "Preparing descriptors": [
                Step(
                    name="Repairing strange cases in abstracts",
                    function=repair_strange_cases,
                    kwargs={
                        "root_directory": self.params.root_directory,
                        "source": "abstract",
                        "target": "abstract",
                    },
                    count_message="{count} abstracts with repaired strange cases",
                ),
                # _preprocess_raw_abstract_nouns_and_phrases(root_directory)
                # internal__check_empty_terms(
                #     "raw_abstract_nouns_and_phrases", root_directory=root_directory
                # )
                #
                # _preprocess_raw_document_title_nouns_and_phrases(root_directory)
                # internal__check_empty_terms(
                #     "raw_document_title_nouns_and_phrases", root_directory=root_directory
                # )
                # _preprocess_raw_noun_and_phrases(root_directory)
                # internal__check_empty_terms(
                #     "raw_noun_and_phrases", root_directory=root_directory
                # )
            ],
            # ----------------------------------------------------------------
            "Creating record identifiers": [],
            # ----------------------------------------------------------------
            # ----------------------------------------------------------------
            "Processing funding details": build_funding_details_steps(self.params),
            "Processing other information": build_other_information_steps(self.params),
            # ----------------------------------------------------------------
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

    def run(self) -> None:

        self._print_header()

        for phase_name, steps in self._build_pipeline().items():
            self._phase += 1
            self._print_phase(phase_name)
            for step in steps:
                self._execute_step(step)

            #
            # Elapsed time report
            # end_time = time.time()
            # elapsed_time = end_time - start_time
            # hours, rem = divmod(elapsed_time, 3600)
            # minutes, seconds = divmod(rem, 60)

            # internal__report_imported_records(root_directory)

            # sys.stderr.write(
            #     f"INFO: Execution time : {int(hours):02}:{int(minutes):02}:{seconds:04.1f}\n\n"
            # )

            # sys.stderr.flush()

    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    def run_(self) -> None:
        pass

        # root_directory = self.params.root_directory
        #
        # Preparation
        # ---------------------------------------------------------------------------------
        #

        # Register tqdm pandas progress bar
        # tqdm.pandas()

        # Elapsed time report
        # sys.stderr.write("\n")
        # sys.stderr.flush()
        # start_time = time.time()

        #

        #
        # internal__check_hyphenated_form(root_directory)

        #
        #
        # PHASE 2: Keywords & noun phrases & abstracts
        # ---------------------------------------------------------------------------------
        #
        # _preprocess_abstract(root_directory)
        # _preprocess_document_title(root_directory)

        #

        #
        #
        # PHASE 3: Process each column in isolation
        # ---------------------------------------------------------------------------------
        #
        #

        #
        #

        #

        #
        #
        # PHASE 4: References
        # ---------------------------------------------------------------------------------
        #
        #

        #
        #
        # PHASE 5: Thesaurus files
        # ---------------------------------------------------------------------------------
        #
        #

        ## ------------------------------------------------------------------------------------------


#
