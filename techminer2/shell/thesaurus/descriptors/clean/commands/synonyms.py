# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import os
import textwrap

import openai
from colorama import Fore
from openai import OpenAI

from techminer2.database.search import ConcordantSentences
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import GetValues, MergeKeys

# -----------------------------------------------------------------------------

PROMPT_WITH_CONTEXTS = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.


CONTEXT:
This task is part of a process to refine the thesaurus for co-word and 
tech-mining analysis in the core area <<{core_area}>>. 
The goal is to determine whether two terms are conceptual synonyms—meaning they 
refer to the same concept or idea in the provided context phrases and core area.

Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms 
    (noun phrases / keywords).
-   Both terms have co-word occurrences greater than zero, indicating they are 
    present together in at least one document.
-   Multi-word terms are indexed separately from their headwords. Therefore, 
    phrases for an isolated term do not include occurrences that belong to its 
    multi-word variants (e.g., phrases for "value" exclude "market value", 
    "net present value", etc.).


TASK:
Return exactly one lowercase word with no punctuation:
-   "yes": when the LEAD-TERM and CANDIDATE-TERM are conceptual synonyms.
-   "no": when the LEAD-TERM and CANDIDATE-TERM are not conceptual synonyms.


DECISION RULES:
Step 0 - Isolated analysis: 
-   Analyze the LEAD-TERM and determine its meaning and usage using the provided phrases 
    plus general scientific knowledge of <<{core_area}>>.
-   Analyze the CANDIDATE-TERM and determine its meaning and usage using the provided phrases
    plus general scientific knowledge of <<{core_area}>>.

Step 1 - Comparative analysis.
-   Compare the meanings and usages of the LEAD-TERM and CANDIDATE-TERM based on the provided context phrases.
-   Decide "yes" if both terms are very similar and likely refer to the same concept in practice, even if there 
    are minor differences in wording, singular/plural form, or inclusion of generic words, as long as the 
    context and domain indicate they are used interchangeably.
-   Decide "no" only if there is clear and consistent evidence that the terms refer to different concepts or 
    ideas in <<{core_area}>>.
-   Do not guess or speculate, but allow for practical synonymy when the context and domain usage support it.



CONSTRAINTS:
-   Use only the provided context phrases plus general scientific knowledge of <<{core_area}>>.
-   If, in the context of <<{core_area}>>, it is clear from the provided context phrases and domain 
    knowledge that both terms consistently refer to the same concept, you must consider them conceptual 
    synonyms, even if not every phrase explicitly qualifies the term.
-   Minor differences in wording, singular/plural, or inclusion of generic words should not prevent synonymy 
    if the terms are used interchangeably in the domain.
-   For the same terms and context phrases, always return the same answer.
-   The decision should be robust to minor variations in context phrasing.


OUTPUT:
Return exactly one word with no quotes: "yes" or "no".


TERMS:
LEAD-TERM: <<{lead_term}>>
CANDIDATE-TERM: <<{candidate_term}>>


CONTEXT PHRASES FOR THE LEAD-TERM:
{contexts_lead}


CONTEXT PHRASES FOR THE CANDIDATE-TERM:
{contexts_candidate}

"""

# -----------------------------------------------------------------------------

PROMPT_WITHOUT_CONTEXTS = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.

CONTEXT:
This task is part of a process to refine the thesaurus for co-word and 
tech-mining analysis in the core area <<{core_area}>>. The goal is to determine 
whether two terms are conceptual synonyms—meaning they refer to the same concept 
or idea in the core area <<{core_area}>>.

Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms (noun phrases / keywords).
-   Both terms have co-word occurrences greater than zero, indicating they are 
    present together in at least one document.
-   Multi-word terms are indexed separately from their headwords.

TASK:
Return exactly one lowercase word with no punctuation:
-   "yes": when the LEAD-TERM and CANDIDATE-TERM are conceptual synonyms.
-   "no": when the LEAD-TERM and CANDIDATE-TERM are not conceptual synonyms.

DECISION RULES:
- Analyze the LEAD-TERM and CANDIDATE-TERM using your scientific and domain knowledge of <<{core_area}>>.
- Decide "yes" if both terms are very similar and likely refer to the same concept in practice, even if there are minor differences in wording, singular/plural form, or inclusion of generic words, as long as the context and domain indicate they are used interchangeably.
- Decide "no" only if there is clear and consistent evidence that the terms refer to different concepts or ideas in <<{core_area}>>.
- Do not guess or speculate, but allow for practical synonymy when domain usage supports it.
- For the same terms, always return the same answer.

OUTPUT:
Return exactly one word with no quotes: yes or no.

TERMS:
LEAD-TERM: <<{lead_term}>>
CANDIDATE-TERM: <<{candidate_term}>>
"""

# -----------------------------------------------------------------------------

EXPLAIN = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.


CONTEXT:
This task is part of a process to refine the thesaurus for co-word and 
tech-mining analysis in the core area <<{core_area}>>. The provided terms are 
NOT conceptual synonyms—meaning they refer to different concepts or ideas in 
the provided context phrases and core area.

Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms 
    (noun phrases / keywords).
-   Both terms have co-word occurrences greater than zero, indicating they are 
    present together in at least one document.    
-   Multi-word terms are indexed separately from their headwords. 
    Therefore, phrases for an isolated term do not include occurrences that 
    belong to its multi-word variants (e.g., phrases for "value" exclude
    "market value", "net present value", etc.).


TASK:
Write a paragraph explaining why the provided terms are not conceptual synonyms 
in the context of <<{core_area}>>.


REQUERIMENTS:
-   Provide a clear and concise explanation based on the provided context phrases.
-   Use specific examples from the context phrases to support your explanation.
-   Avoid vague statements and ensure your reasoning is grounded in the provided context.


LENGTH:
100 to 150 words.

TERMS:
LEAD-TERM: <<{lead_term}>>
CANDIDATE-TERM: <<{candidate_term}>>


CONTEXT PHRASES FOR THE LEAD-TERM:
{contexts_lead}


CONTEXT PHRASES FOR THE CANDIDATE-TERM:
{contexts_candidate}


"""


# -----------------------------------------------------------------------------
def internal__user_input(core_area, n_contexts):

    # -------------------------------------------------------------------------
    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None, None, None
        core_area = answer.upper()

    # -------------------------------------------------------------------------
    if n_contexts is None:
        n_contexts = colorized_input(
            ". Enter the number of contexts [default: 30] > "
        ).strip()
        if n_contexts == "":
            n_contexts = 30
        else:
            n_contexts = int(n_contexts)

    # -------------------------------------------------------------------------
    lead_term = colorized_input(". Enter the lead term > ").strip()
    if lead_term == "":
        return None, None, None, None

    # -------------------------------------------------------------------------
    candidate_term = colorized_input(". Enter the candidate term > ").strip()
    if candidate_term == "":
        return None, None, None, None

    return core_area, lead_term, candidate_term, n_contexts


# -----------------------------------------------------------------------------
def internal__filter_contexts(
    n_contexts,
    contexts_lead_term,
    contexts_candidate_term,
):
    if contexts_lead_term:
        contexts_lead_term = contexts_lead_term[:n_contexts]
    if contexts_candidate_term:
        contexts_candidate_term = contexts_candidate_term[:n_contexts]

    return contexts_lead_term, contexts_candidate_term


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
        contexts = [c for c in contexts if pattern in c]

        complete_contexts.extend(contexts)

        if len(complete_contexts) >= n_contexts:
            break

    pattern = pattern.lower().replace("_", " ")
    complete_contexts = [c for c in complete_contexts if pattern in c]

    if len(complete_contexts) < 5:
        return None

    return complete_contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query_with_contexts(
    core_area,
    lead_term,
    candidate_term,
    contexts_lead,
    contexts_candidate,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if isinstance(contexts_lead, list):
        contexts_lead = "\n".join(contexts_lead)
    if isinstance(contexts_candidate, list):
        contexts_candidate = "\n".join(contexts_candidate)

    query = PROMPT_WITH_CONTEXTS.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
        contexts_lead=contexts_lead,
        contexts_candidate=contexts_candidate,
        core_area=core_area,
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
def internal__execute_query_without_contexts(
    core_area,
    lead_term,
    candidate_term,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = PROMPT_WITHOUT_CONTEXTS.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
        core_area=core_area,
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
        print(f"Error processing the query: {e}")
        return None


# -----------------------------------------------------------------------------
def internal__print_answer(answer):

    text = (
        Fore.LIGHTBLACK_EX
        + "The terms "
        + Fore.RESET
        + "{result}"
        + Fore.LIGHTBLACK_EX
        + " synonymous."
        + Fore.RESET
    )

    if answer.lower() == "yes":
        text = text.format(result="ARE")
    elif answer.lower() == "no":
        text = text.format(result="ARE NOT")
    elif answer.lower() == "na-lead":
        text = "No context available for the lead term."
    elif answer.lower() == "na-candidate":
        text = "No context available for the candidate term."
    else:
        text = f"Obtained answer: {answer}"

    print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def internal__merge_keys(lead_term, candidate_term):

    answer = colorized_input(". Merge lead and candidate terms (y/[n])? > ").strip()
    if answer.lower() in ["n", "no", "not", ""]:
        print()
        return

    (
        MergeKeys(use_colorama=False)
        .with_patterns([lead_term, candidate_term])
        .where_root_directory_is("./")
        .run()
    )

    print()


# -----------------------------------------------------------------------------
def internal__explain(
    core_area,
    lead_term,
    candidate_term,
    contexts_lead,
    contexts_candidate,
):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    if contexts_lead:
        contexts_lead = "\n".join(contexts_lead)
    else:
        contexts_lead = "N/A"

    if contexts_candidate:
        contexts_candidate = "\n".join(contexts_candidate)
    else:
        contexts_candidate = "N/A"

    query = EXPLAIN.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
        contexts_lead=contexts_lead,
        contexts_candidate=contexts_candidate,
        core_area=core_area,
    )

    try:

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        answer = response.output_text
        answer = answer.strip()
        return answer

    except openai.OpenAIError as e:
        print()
        print(f"Error processing the query: {e}")
        print()
        return None


# -----------------------------------------------------------------------------
def internal__print(msg):
    print(Fore.LIGHTBLACK_EX + msg + Fore.RESET)


# -----------------------------------------------------------------------------
def execute_synonyms_command():

    print()
    core_area = None
    n_contexts = None

    while True:

        core_area, lead_term, candidate_term, n_contexts = internal__user_input(
            core_area, n_contexts
        )

        print()
        internal__print("Evaluating synonyms...")

        if lead_term is None or candidate_term is None:
            print()
            return

        internal__print("  Building contexts for the lead term...")
        contexts_lead = internal__get_contexts(lead_term, n_contexts)
        if not contexts_lead:
            internal__print(
                "  No sufficient contextual information found for the lead term."
            )

        if contexts_lead:
            internal__print("  Building contexts for the candidate term...")
            contexts_candidate = internal__get_contexts(candidate_term, n_contexts)
            if not contexts_candidate:
                internal__print(
                    "  No sufficient contextual information found for the candidate term."
                )
        else:
            contexts_candidate = None

        internal__print("  Executing the query...")
        if not contexts_lead and not contexts_candidate:
            answer = internal__execute_query_without_contexts(
                core_area, lead_term, candidate_term
            )
        else:
            contexts_lead, contexts_candidate = internal__filter_contexts(
                n_contexts, contexts_lead, contexts_candidate
            )
            if not contexts_lead:
                contexts_lead = "N/A"
            if not contexts_candidate:
                contexts_candidate = "N/A"
            answer = internal__execute_query_with_contexts(
                core_area, lead_term, candidate_term, contexts_lead, contexts_candidate
            )

        internal__print("  Evaluation process completed successfully.")

        internal__print_answer(answer)

        if answer == "yes":
            internal__merge_keys(lead_term, candidate_term)
        else:
            explanation = internal__explain(
                core_area,
                lead_term,
                candidate_term,
                contexts_lead,
                contexts_candidate,
            )
            explanation = textwrap.fill(explanation, width=80)
            if explanation:
                print(explanation)
                print()


#
