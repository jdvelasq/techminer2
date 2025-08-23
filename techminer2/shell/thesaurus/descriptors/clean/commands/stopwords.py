# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

import os
from pprint import pprint  # type: ignore

import openai
from colorama import Fore
from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2.database.search import ConcordantSentences
from techminer2.database.tools import ExtendStopwords
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import GetValues

PROMPT = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word and tech-mining studies.


CONTEXT:
Decide whether a candidate TERM should be treated as a stopword for bibliometric/tech-mining theme discovery
in the core area <<{core_area}>>. A stopword is a generic or non-discriminative term that does not help surface
dominant/emergent themes.

Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms (noun phrases / keywords).
-   Multi-word terms are indexed separately from their headwords. Therefore, contexts for an isolated TERM
    do not include occurrences that belong to its multi-word variants (e.g., contexts for "value" exclude
    "market value", "net present value", etc.).


TASK:
Return exactly one lowercase word with no punctuation:
-   "yes": exclude the TERM as a stopword
-   "no": retain the TERM as useful


CLASSIFICATION RULES:

Step 0 — Knowledge & extraction prior (apply once to the TERM):
-   Classify the TERM as one of:
    A)  Likely compound headword (common head of domain collocations).
    B)  Linguistic scaffolding operator (generic connector).
    C)  Core technical/economic variable that often stands alone with units/quantification.

 - Priors:
    *   If (A) compound headword → exclude ("yes") only if virtually all (e.g., >95%) 
        of its own contexts show repeated, explicit technical anchoring (units, equations, 
        explicit variable/measure). Generic labeling of types, cases, or examples is 
        not sufficient for retention unless it is present in nearly all contexts.
    *   If (B) scaffolding operator → default GS unless a clear majority of contexts show domain-specific meaning.
    *   If (C) core variable → default TS unless all contexts are GS.

Step 1 — Phrase-level labeling (for each context phrase independently):
-   Label the TERM as:
    *   TS (technical-specific) if, in that phrase, the TERM itself is measured/defined/parametrized
        (e.g., units, numeric comparison, equation, optimization/forecasting of this TERM, or it names
        a domain construct).
    *   GS (generic-scaffolding) if the TERM only frames language (label/connector/quantifier) and does not
        denote a domain construct in that phrase.


Step 2 — Deterministic aggregation:
-   Count TS and GS across the phrases (each phrase = one vote).
-   Decision rule:
    *   Exclude the TERM ("yes") only if GS votes are virtually unanimous and there is clear, 
        unambiguous evidence across all context phrases that the TERM is generic, vague, or 
        ambiguous. For compound headwords, this is the default unless technical anchoring is 
        clear and frequent.
    *   Otherwise, retain the TERM ("no").
- Tie-break:
    * If TS = GS → use Step 0 prior:
        * (A) or (B) → "yes"
        * (C) → "no"


CONSTRAINTS:
-   Use only the provided phrases plus general scientific knowledge of <<{core_area}>>.
-   Many stopwords are generic across domains; if a term is generic in most fields, it is 
    likely a stopword here unless strong domain-specific evidence is present.
-   Do not infer meaning from multi-word variants that are indexed as separate terms.
-   Always return the same answer for the same TERM + contexts. 
-   The decision should be robust to minor variations in context phrasing.
-   Output exactly one word: yes or no.
-   If any context phrase could reasonably be interpreted as technical or domain-specific 
    within the current core area, always retain ("no"), regardless of the majority or any other rule.
-   Only exclude ("yes") if all context phrases are clearly generic, vague, or ambiguous, 
    and none can reasonably be interpreted as technical or domain-specific in the current core area.


   
OUTPUT:
Return exactly one word with no quotes: yes or no.


TERM:
<<{pattern}>>


CONTEXT PHRASES:
{contexts}

"""


# -----------------------------------------------------------------------------
def internal__user_input(core_area):

    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None, None
    else:
        answer = colorized_input(f". Enter the core area [{core_area}] > ").strip()

    if answer != "":
        core_area = answer.upper()

    pattern = colorized_input(". Enter the pattern > ").strip()
    if pattern == "":
        return None, None, None

    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 30] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 30
    else:
        n_contexts = int(n_contexts)

    return core_area, pattern, n_contexts


# -----------------------------------------------------------------------------
def internal__get_contexts(pattern, n_contexts):

    terms = GetValues().with_patterns([pattern]).where_root_directory_is("./").run()
    terms = [term for term in terms if pattern in term]

    complete_contexts = []

    for term in terms:

        contexts = (
            ConcordantSentences()
            #
            .with_abstract_having_pattern(term)
            .where_root_directory_is("./")
            .where_database_is("main")
            .where_record_years_range_is(None, None)
            .where_record_citations_range_is(None, None)
            #
            .run()
        )

        contexts = [c for c in contexts if len(c) > 80]
        contexts = [f"- {c} ." for c in contexts]
        contexts = [c.lower().replace("_", " ") for c in contexts]

        complete_contexts.extend(contexts)

    pattern = pattern.lower().replace("_", " ")
    complete_contexts = [c for c in complete_contexts if pattern in c]

    if len(complete_contexts) < 5:
        return None

    return complete_contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query(core_area, pattern, contexts):

    if contexts is None:
        return "yes"

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = PROMPT.format(
        pattern=pattern,
        core_area=core_area,
        contexts="\n".join(contexts),
    )

    answer = []

    try:

        for _ in range(3):
            response = client.responses.create(
                model="gpt-4o",
                input=query,
                temperature=0,
            )

            response = response.output_text
            response = response.strip().lower()
            answer.append(response)

        yes_count = answer.count("yes")

        if yes_count < 3:
            return "no"
        return "yes"

    except openai.OpenAIError as e:
        print()
        print(f"Error processing the query: {e}")
        print()
        return None


# -----------------------------------------------------------------------------
def internal__print_answer(answer):

    text = (
        Fore.LIGHTBLACK_EX
        + "The term "
        + Fore.RESET
        + "{result}"
        + Fore.LIGHTBLACK_EX
        + " is a STOPWORD."
        + Fore.RESET
    )

    if answer.lower() == "yes":
        text = text.format(result="IS")
    else:
        text = text.format(result="IS NOT")

    print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def internal__extend_stopwords(pattern):

    answer = colorized_input(". Extend stopwords with pattern (y/[n])? > ").strip()
    if answer.lower() not in ["n", "no", "not", ""]:
        print()
        return

    pattern = pattern.upper().replace(" ", "_")
    ExtendStopwords().with_patterns([pattern]).where_root_directory_is("./").run()
    print()


# -----------------------------------------------------------------------------
def execute_stopwords_command():

    print()
    core_area = None

    # internal__run_diagnostics()
    # return

    while True:

        core_area, pattern, n_contexts = internal__user_input(core_area)

        if pattern is None:
            print()
            return

        ## pattern = pattern.lower().replace("_", " ")

        contexts = internal__get_contexts(pattern, n_contexts)
        if not contexts:
            answer = "yes"
        else:
            answer = internal__execute_query(core_area, pattern, contexts)

        internal__print_answer(answer)

        if answer == "yes":
            internal__extend_stopwords(pattern)


# -----------------------------------------------------------------------------
def internal__run_diagnostics():

    patterns = [
        "WIND_POWER",
        "MODEL",
        "STUDY_CASE",
        "POWER",
        "SCENARIO",
        "BENEFIT",
        "APPROACH",
        "AMOUNTS",
        "EFFICIENCY",
        "GOALS",
        "BASIS",
        "CONDITION",
        "POWER_PLANTS",
        "MODELING",
        "LOSS",
        "FORMS",
        "SITUATION",
        "RESULTS",
        "WIND_TURBINE",
        "YEAR",
        "TURBINE",
        "METHOD",
        "VALUE",
        "TYPE",
        "PERFORMANCE",
        "INSTALLATION",
        "ENERGY_PRODUCTION",
        "PERFORMANCE_ASSESSMENT",
        "RATED_POWER",
        "ENERGY_GENERATION",
        "WIND_FARMS",
        "ELECTRIC_UTILITIES",
        "ACCOUNT",
        "OPERATIONS",
        "NUMBERS",
        "COMPARISONS",
        "SIZES",
        "OBJECTIVES",
        "CONSIDERATIONS",
        "CONFIGURATION",
        "FARMS",
        "TRADE_OFF",
        "BALANCE",
    ]

    summary = {}

    for pattern in tqdm(patterns, total=len(patterns), ncols=80):

        contexts = internal__get_contexts(pattern, 30)

        results = []

        for _ in range(5):

            answer = internal__execute_query(
                "economics of wind energy", pattern, contexts
            )
            results.append(answer)

        summary[pattern] = results

    print()
    print("Summary: ")
    print()
    pprint(summary)
    print()
