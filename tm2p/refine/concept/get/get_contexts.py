"""
Get Contexts
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.get import GetContexts
    >>> contexts = (
    ...     GetContexts()
    ...     .having_text_matching("fintech")
    ...     .having_n_contexts(10)
    ...     .where_root_directory("tests/scopus/")
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(contexts[:5])
    ['- this research delves into the transformative potential of integrating '
     'financial technology ( fintech ) and blockchain in green finance . .',
     '- purpose : the purpose of this study is to discuss the united arab emirates '
     "' ( uae ) favorable attitude toward the financial sector digital "
     'transformation and the development of fintech due to the rise of financial '
     'technology . .',
     '- fintech blends innovation and technology to provide financial inclusion to '
     'stakeholders through various new products and services such metaverse and '
     'artificial intelligence . .',
     '- originality / value : this study is critical because the uae banking '
     'sector serves diverse nationalities , and its success is contingent on '
     'fintech and its competitive edge . .',
     '- in recent years , the progress in fintech has emerged a significant source '
     'to decline the energy which turns to enhance the environmental quality . .']

"""

from tm2p._intern import ParamsMixin
from tm2p.explore.concordance import SentenceConcordance


class GetContexts(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from .get_variants import GetVariants

        terms = (
            GetVariants(quiet=self.params.quiet).update(**self.params.__dict__).run()
        )

        complete_contexts = []

        for term in terms:

            contexts = (
                SentenceConcordance()
                .update(**self.params.__dict__)
                .having_text_matching(term)
                .run()
            )

            contexts = [c for c in contexts if len(c) > 80]
            contexts = [f"- {c} ." for c in contexts]
            contexts = [c.lower().replace("_", " ") for c in contexts]

            complete_contexts.extend(contexts)

        patterns = [
            pattern.lower().replace("_", " ") for pattern in self.params.pattern
        ]
        complete_contexts = [
            c for c in complete_contexts if any(pattern in c for pattern in patterns)
        ]

        return complete_contexts[: self.params.n_contexts]
