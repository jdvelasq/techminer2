"""
Extract Colon Phrases
===============================================================================

Smoke test:
    >>> from techminer2.review import ExtractColonPhrases
    >>> text = (
    ...     ExtractColonPhrases()
    ...     .having_text_matching(None)
    ...     .where_root_directory("examples/small/")
    ... ).run()
    >>> assert isinstance(text, list)
    >>> assert all(isinstance(t, str) for t in text)
    >>> for t in text[:20]: print(t)


"""

from techminer2._internals import ParamsMixin
from techminer2.text.concordances import ConcordanceUppercase

__reviewed__ = "2026-01-28"


class ExtractColonPhrases(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> list[str]:

        return (
            ConcordanceUppercase()
            .update(**self.params.__dict__)
            .having_text_matching(" : ")
            .run()
        )
