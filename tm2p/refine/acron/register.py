"""
Register Phrases
===============================================================================

Smoke tests:
   >>> from tm2p.refine.thesaurus_old.acronyms import Register
   >>> (
   ...     Register(root_directory="examples/fintech/", )
   ..      .run()
   ... ) # doctest: +SKIP

"""

from pathlib import Path

from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data.word_lists import (
    load_builtin_word_list,
    save_builtin_word_list,
)


class Register(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        acronym_path = (
            Path(self.params.root_directory)
            / "refine"
            / "thesaurus"
            / "acronyms.the.txt"
        )

        if acronym_path.is_file() is False:
            raise FileNotFoundError(f"File not found: {acronym_path}\n")

        new_noun_phrases = []
        with open(acronym_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.startswith(" "):
                    continue
                noun_phrase = line.strip()
                if len(noun_phrase.split(" ")) > 1:
                    new_noun_phrases.append(noun_phrase)

        existent_noun_phrases = load_builtin_word_list("noun_phrases.txt")
        updated_noun_phrases = sorted(existent_noun_phrases.union(new_noun_phrases))
        save_builtin_word_list("noun_phrases.txt", updated_noun_phrases)


if __name__ == "__main__":

    Register().where_root_directory("./").run()
