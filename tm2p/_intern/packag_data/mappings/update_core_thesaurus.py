import json
import os
import re
from importlib.resources import files

from diskcache import Cache
from openai import APIError, OpenAI

from .update_builtin_mapping import update_builtin_mapping

SYSTEM_PROMPT = """
ROLE:

You are an expert in scientometrics, terminology normalization, co-word analysis, and tech mining.

CONTEXT:

This task supports a reusable generic thesaurus applied across projects, corpora, disciplines, and periods.

Given two terms, determine whether they denote the same underlying concept and can be normalized together without losing meaningful information.

Evaluate only the terms provided. Do not assume a specific corpus, cluster, discipline, application, period, or local context.

The relationship is symmetric: swapping LEAD-TERM and CANDIDATE-TERM must not change the answer.

DECISION RULE:

Return "yes" only when both terms clearly denote the same concept and their difference is exclusively:

singular/plural or grammatical variation;
spelling, hyphenation, spacing, punctuation, or harmless word-order variation;
a clear typographical error;
an unambiguous acronym, abbreviation, or expanded form;
an established shortened, informal, or alternative technical name;
an optional generic word whose addition or removal does not change the referent, scope, or entity type.
missing hyphens in a compound word or phrase;
iis a clear error like duplication of words, wrong hypenation, or plural/singular mismatch.

The terms need not be interchangeable in every sentence, but replacing them with one descriptor must preserve the conceptual information required for co-word analysis and tech mining.

Return "no" when:

one term is broader, narrower, or a subtype of the other;
a qualifier changes the scope, object, population, location, method, purpose, attribute, or level of analysis;
one term denotes a method and the other its result, measure, output, implementation, application, or data source;
one term denotes a project, program, organization, database, dataset, index, framework, platform, system, model, code, or tool associated with the other;
the terms are merely related, associated, co-occurring, or members of the same conceptual family;
equivalence depends on a particular corpus, discipline, application, period, or local usage;
an acronym or shortened form has multiple plausible meanings;
either term is unfamiliar or its established usage cannot be confidently determined;
there is reasonable doubt that the terms denote exactly the same concept.

Lexical similarity, substring inclusion, or a shared lexical core is not sufficient evidence. Organizational or resource-designating words such as "project", "program", "database", "dataset", "framework", "system", and "tool" are not automatically removable.

Use maximum academic rigour. When uncertain, return "no".

CALIBRATION EXAMPLES:

"neural network" | "neural networks" → yes
"external stimulus" | "external stimuli" → yes
"agent-based modelling" | "agent-based modeling" → yes
"agent based modeling" | "agent-based modeling" → yes
"e-government" | "electronic governance" → yes
"neural networks" | "neural nets" → yes
"peace agreement" | "peace accord" → yes
"social network analysis" | "SNA" → yes
"convolutional neural network" | "convolutional neural network network" → yes

"neural networks" | "deep neural networks" → no
"intermarriage" | "ethnic intermarriage" → no
"data architecture" | "big data architecture" → no
"social network analysis" | "social network analysis measures" → no
"georeferencing of ethnic groups" | "georeferencing of ethnic groups dataset" → no
"global systems analysis and simulation" | "global systems analysis and simulation project" → no
"system dynamics" | "SD" → no

INPUT:

LEAD-TERM: {lead_term}
CANDIDATE-TERM: {candidate_term}

OUTPUT FORMAT (STRICT — JSON ONLY):
The output MUST be a JSON object with the following structure:

{{
    "answer": "yes"
}}

Any output different of this must be considered invalid. Do not include explanations, comments, 
markdown, code fences, additional keys, or any text outside the JSON object.

"""

USER_TEMPLATE = """

LEAD-TERM: "{lead_term}"

CANDIDATE-TERM: "{candidate_term}"

"""

CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


CACHE = Cache("/volumes/GitHub/synonyms.tm2p.cache", size_limit=4 * 1024**2)


def update_core_thesaurus(
    preferred: str,
    variant: str,
) -> bool:

    answer = _are_synonyms(preferred, variant)

    if answer is True:
        print("✓ Synonym.\n")

        update_builtin_mapping(
            filename="core_thesaurus.the.json",
            mapping={preferred: [variant]},
        )
    else:
        print("✗ Not a synonym.\n")
    return answer


def _are_synonyms(lead_term: str, candidate_term: str) -> bool:

    first, second = sorted([lead_term, candidate_term])
    cache_key = f"{first}\t{second}"
    if cache_key in CACHE:
        return CACHE[cache_key]  # type: ignore

    user_prompt = USER_TEMPLATE.format(
        lead_term=lead_term,
        candidate_term=candidate_term,
    )

    try:

        response = CLIENT.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
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

    except APIError as e:
        raise RuntimeError(f"OpenAI API error: {e}")

    content = response.choices[0].message.content.strip()  # type: ignore
    json_text = _extract_json_text(content)

    try:
        result = json.loads(json_text)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON output from OpenAI API: {content}")

    answer = result.get("answer")
    if answer not in {"yes", "no"}:
        raise ValueError(f"Invalid answer from OpenAI API: {answer}")

    CACHE[cache_key] = answer == "yes"  # type: ignore
    return answer == "yes"


def _extract_json_text(content: str) -> str:
    """Extract JSON payload, accepting fenced markdown responses."""
    fenced_match = re.match(r"^```(?:json)?\s*(.*?)\s*```$", content, re.DOTALL)
    if fenced_match:
        return fenced_match.group(1).strip()
    return content
