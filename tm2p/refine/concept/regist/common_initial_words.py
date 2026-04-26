"""
CommonInitialWords
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.regist import CommonInitialWords
    >>> (
    ...     CommonInitialWords()
    ...     .having_word("abandon")
    ...     .run()
    ... )  # doctest: +SKIP

"""

import sys
from importlib.resources import files

from tm2p._intern import ParamsMixin


class CommonInitialWords(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        data_path = files("tm2p.package_data.text_processing.data").joinpath(
            "common_initial_words.txt"
        )

        with open(str(data_path), "r", encoding="utf-8") as file:
            existing_words = set(line.strip() for line in file)

        words = self.params.word
        if isinstance(words, str):
            words = [words]

        existing_words.update(words)

        with open(str(data_path), "a", encoding="utf-8") as file:
            for word in sorted(existing_words):
                file.write(f"\n{word}")

        sys.stderr.write("New initial words registered successfully.\n")
        sys.stderr.flush()
