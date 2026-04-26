"""
Get Contexts
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.get import GetContexts
    >>> contexts = (
    ...     GetContexts()
    ...     .having_text_matching("fintech")
    ...     .having_n_contexts(10)
    ...     #
    ...     .where_root_directory("tests/regtech-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> from pprint import pprint
    >>> pprint(contexts[:5])  # doctest: +SKIP
    ['- this study investigates the efficacy of technological solutions by '
     'examining how financial regulatory technology ( fintech ) , within the '
     'broader context of corporate digital transformation , inhibits internal '
     'corruption . .',
     '- heterogeneity analysis reveals that larger firms , with greater resources '
     'and more complex structures , derive more significant anti corruption '
     'benefits from fintech . .',
     '- fintech based crowdfunding platforms provide innovative green financial '
     'products and regulatory technologies support in compliance with regulations '
     '. .',
     '- over the last 10 years , financial development has been technologically '
     'advanced , and trends in this area are linked to the fintech phenomenon . .',
     '- the purpose of this paper is to develop theoretical provisions regarding '
     'trends and patterns of penetration of fintech into the financial system and '
     'the methodological basis for assessing the development potential of fintech '
     'at the country level in the context of financial development and economic '
     'growth . .']

"""

from tm2p._intern import ParamsMixin
from tm2p.explor.concord import SentenceConcordance


class GetContexts(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from .get_variants import GetVariants

        terms = GetVariants().update(**self.params.__dict__).run()

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
