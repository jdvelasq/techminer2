import json
import os
import re
from typing import List

from diskcache import Cache
from openai import APIError, OpenAI

SYSTEM_PROMPT = """
You are a conservative classifier for reusable stopwords used in scientometrics, co-word analysis, and tech mining.

The input term has already been classified as a stopword for the current project. Do not determine whether it is a stopword.

Your task is only to determine whether this stopword should be stored in a reusable cross-domain stopword list.

Return exactly one of the following labels:

- "scientific": generic scientific-and-academic vocabulary, including single-word and multiword expressions that represent typical scholarly writing, reporting, and rhetorical scaffolding appearing across scientific and technological publications (especially titles, abstracts, methods, results, and conclusions), and that contribute little or no thematic information across scientific disciplines.
- "common": generic common-and-basic vocabulary that is uninformative across both scientific and non-scientific domains. It is a generic stopword that do not belongs to "scientific" or "generic" categories.
- "no": keep the stopword project-specific or domain-specific. Although it is a valid stopword for the current project, it should not be reused across unrelated domains because it may carry meaningful thematic, methodological, technical, or disciplinary information elsewhere.

Decision rules:

- Assume the term is already a valid stopword.
- Stopwords are terms that do not help to interpret and understand the thematic content of a document, cluster, or corpus.
- Evaluate only whether it is reusable across unrelated domains.
- If its stopword status depends on the project or domain, return "no".
- Otherwise, classify it as "common", "scientific", or "generic".
- When uncertain, return "no".

Examples:

- additional → common
- important → common
- abstract → scientific
- article → scientific
- manuscript → scientific
- publication → scientific
- doi → scientific
- issn → scientific
- copyright → scientific
- algorithm → no
- machine learning → no
- regression → no
- peace → no
- energy → no

OUTPUT FORMAT (STRICT — JSON ONLY):
The output MUST be a JSON object with the following structure:

{{
    "answer": "<common|scientific|no>"
}}

Any output different of this must be considered invalid. Do not include explanations, comments, 
markdown, code fences, additional keys, or any text outside the JSON object.

"""

USER_TEMPLATE = """

TERM: "{term}"


"""

CLIENT = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CACHE = Cache("/volumes/GitHub/stopwords.tm2p.cache", size_limit=4 * 1024**2)


def update_stopwords(preferred: str, variants: List[str]) -> str:

    from .add_new_words_to_builtin_word_list import add_new_words_to_builtin_word_list

    answer = _is_stopword(preferred)

    if answer == "common":
        filename = "common_and_basic.txt"
    elif answer == "scientific":
        filename = "scientific_and_academic.txt"
    else:
        filename = None

    if filename is not None:
        add_new_words_to_builtin_word_list(
            filename=filename,  # type: ignore
            new_words=[preferred],
        )

        add_new_words_to_builtin_word_list(
            filename=filename,  # type: ignore
            new_words=variants,
        )

    return answer


def _is_stopword(term: str) -> str:

    cache_key = term
    if cache_key in CACHE:
        return CACHE[cache_key]  # type: ignore

    user_prompt = USER_TEMPLATE.format(term=term)

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
    if answer not in {"no", "common", "scientific"}:
        raise ValueError(f"Invalid answer from OpenAI API: {answer}")

    CACHE[cache_key] = answer  # type: ignore
    return answer


def _extract_json_text(content: str) -> str:
    """Extract JSON payload, accepting fenced markdown responses."""
    fenced_match = re.match(r"^```(?:json)?\s*(.*?)\s*```$", content, re.DOTALL)
    if fenced_match:
        return fenced_match.group(1).strip()
    return content
