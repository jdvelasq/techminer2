"""
Define
===============================================================================

Smoke tests:
    >>> from tm2p.refine.concept.ai import Define
    >>> definitions = (
    ...     Define()
    ...     #
    ...     # FIELD:
    ...     .with_core_area("FINTECH (financial technologies)")
    ...     .having_text_matching(('fintech', 'financial technologies'))
    ...     .having_n_contexts(10)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )  # doctest: +SKIP
    >>> from textwrap import fill
    >>> for definiition in definitions:
    ...     print(fill(definiition, width=70))
    ...     print("...")  # doctest: +SKIP
    FINTECH, short for financial technology, refers to the innovative
    integration of technology into financial services, aiming to enhance
    financial inclusion and efficiency. it encompasses a wide range of
    applications, including blockchain, artificial intelligence, and the
    metaverse, to offer new products and services. FINTECH plays a crucial
    role in digital transformation within the financial sector, as seen in
    regions like the uae, where it provides a competitive edge.
    additionally, FINTECH contributes positively to environmental
    sustainability by promoting green finance and improving the green
    environmental index through financial breadth, depth, and
    digitalization. its transformative potential is evident in its ability
    to mediate green credit and investment.
    ...
    FINANCIAL TECHNOLOGIES, commonly referred to as fintech, represent the
    integration of innovation and technology within the financial sector
    to enhance and transform financial services. fintech encompasses a
    wide range of applications, including blockchain, artificial
    intelligence, and the metaverse, aimed at providing financial
    inclusion and new products to stakeholders. it plays a crucial role in
    digital transformation, as seen in regions like the united arab
    emirates, where fintech drives competitive advantage in the banking
    sector. additionally, fintech contributes to environmental
    sustainability by promoting green finance and positively influencing
    the green environmental index through financial breadth, depth, and
    digitalization.


"""

import json
import os

import openai
from openai import OpenAI

from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data.templates.load_builtin_template import (
    load_builtin_template,
)


class Define(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        from tm2p.refine.concept.get import GetContexts

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        contexts = GetContexts().update(**self.params.__dict__).run()
        core_area = self.params.core_area

        terms = self.params.pattern

        system_prompt = load_builtin_template(
            "shell.thesaurus.descriptors.clean.define.system.txt"
        )

        user_template = load_builtin_template(
            "shell.thesaurus.descriptors.clean.define.user.txt"
        )

        definitions = []

        for term in terms:

            user_prompt = user_template.format(
                term=term,
                contexts=contexts,
                core_area=core_area,
            )

            try:

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                            "cache_control": {"type": "ephemeral"},
                        },  # type: ignore
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                    temperature=0,
                    response_format={"type": "json_object"},
                )

            except openai.OpenAIError as e:
                print(f"Error processing the query: {e}")
                raise ValueError("API error") from e

            answer = response.choices[0].message.content
            answer = answer.strip()  # type: ignore
            answer = json.loads(answer)
            answer = answer["text"]
            answer = answer.lower().strip()
            answer = answer.replace(
                term.lower().replace("_", " "),
                term.upper().replace("_", " "),
            )

            definitions.append(answer)

        return definitions
