# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
import json
import os
import os.path
import sys

import pandas as pd
from openai import OpenAI
from tqdm import tqdm

from techminer2._internals import Params
from techminer2._internals.package_data.text_processing import (
    internal__load_text_processing_terms,
)
from techminer2._internals.user_data import internal__load_all_records_from_database

SYSTEM_PROMPT = """
INSTRUCTION:
You will be provided with two variations of the same word: one in hyphenated form and the other in non-hyphenated form.


TASK:
1. Analyze the two forms and determine which is correct in scientific or technical English usage.
2. Respond with "yes" if:
    - The hyphenated form is the only form correct.
    - The word is not standard English.
    - Both forms (hyphenated and non-hyphenated) are correct.
    - Neither form is correct.
3. Respond "no" if:
    - The non-hyphenated form is the only form correct.
    - The correct form is different from both provided forms.

    
OUTPUT FORMAT (STRICT — JSON ONLY):
The output MUST be a JSON object with the following structure:

{{
    "answer": "yes" or "no",
}}

Any output different of this must be considered invalid.

"""

USER_PROMPT = """
    
WORDS:
- Hyphenated: "{}"
- Non-hyphenated: "{}"

"""


def collect_project_hyphenated_words(root_dir):

    dataframe = internal__load_all_records_from_database(
        Params(root_directory=root_dir)
    )

    words = []
    for column in [
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        if column in dataframe.columns:
            words.append(dataframe[column].dropna().copy())

    # Obtain a keyword per row
    words = pd.concat(words)
    words = words.str.upper()
    words = words.str.split("; ")
    words = words.explode()

    # Minimal preprocessing:

    # remove all html tags
    words = words.str.replace("<.*?>", "", regex=True)

    # - Space, left parenthesis, letter
    words = words.str.replace(" \(([A-Z0-9])", r" ( \1", regex=True)
    words = words.str.replace(" \[([A-Z0-9])", r" [ \1", regex=True)
    words = words.str.replace(" {([A-Z0-9])", r" { \1", regex=True)

    # - Letter, right parenthesis at end of line
    words = words.str.replace("([A-Z0-9])\)$", r"\1 )", regex=True)
    words = words.str.replace("([A-Z0-9])\]$", r"\1 ]", regex=True)
    words = words.str.replace("([A-Z0-9])}$", r"\1 }", regex=True)

    # - Parenthesis at the beginning of line, letter
    words = words.str.replace("^\(([A-Z0-9])", r"( \1", regex=True)
    words = words.str.replace("^\[([A-Z0-9])", r"[ \1", regex=True)
    words = words.str.replace("^{([A-Z0-9])", r"{ \1", regex=True)

    # - Letter, left parenthesis, letter
    words = words.str.replace("([A-Z0-9])\(([A-Z0-9])", r"\1 ( \2", regex=True)
    words = words.str.replace("([A-Z0-9])\[([A-Z0-9])", r"\1 [ \2", regex=True)
    words = words.str.replace("([A-Z0-9]){([A-Z0-9])", r"\1 { \2", regex=True)

    # Word splitting
    words = words.str.split(" ")
    words = words.explode()
    words = words.str.strip()

    words = words[words.str.contains("-")]
    words = words.str.replace("-", "_", regex=False)
    words = words[words.apply(lambda x: x != "_")]
    words = words[~words.str.startswith("_")]
    words = words[~words.str.endswith("_")]
    words = words[~words.str.endswith(")")]
    words = words[~words.str.endswith("}")]
    words = words[words.apply(lambda x: len(x) > 6)]
    words = words[words.str.match("^[A-Za-z0-9_]+$")]

    words = words.to_list()
    words = list(set(words))

    return words


def collect_system_hyphenated_words():
    words = internal__load_text_processing_terms("hyphenated_is_correct.txt")
    words += internal__load_text_processing_terms("hyphenated_is_incorrect.txt")
    return words


def internal__check_hyphenated_form(root_dir):

    sys.stderr.write("INFO: Checking hyphenated words\n")
    sys.stderr.flush()

    project_words = collect_project_hyphenated_words(root_dir)
    system_words = collect_system_hyphenated_words()
    undetected_words = set(project_words) - set(system_words)

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    hyphenated_is_incorrect = []
    hyphenated_is_correct = []

    for term in tqdm(
        undetected_words,
        total=len(undetected_words),
        desc=f"  Progress",
        ncols=80,
    ):

        if "_" not in term:
            continue

        words = term.split("_")
        if words[0] == words[1]:
            hyphenated_is_correct.append(term)
            continue

        query = USER_PROMPT.format(
            term.lower().replace("_", "-"), term.lower().replace("_", "")
        )

        try:

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    },
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
                temperature=0,
                response_format={"type": "json_object"},
            )

            answer = response.choices[0].message.content
            answer = answer.strip()
            answer = json.loads(answer)
            answer = answer["answer"]
            answer = answer.lower()

            if answer == "no":
                hyphenated_is_incorrect.append(term)
            else:
                hyphenated_is_correct.append(term)

        except Exception as e:
            print(f"Error processing {e}")

    file_path = os.path.join(root_dir, "data/my_keywords/hyphenated_is_incorrect.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        for word in sorted(hyphenated_is_incorrect):
            f.write(f"{word}\n")

    file_path = os.path.join(root_dir, "data/my_keywords/hyphenated_is_correct.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        for word in sorted(hyphenated_is_correct):
            f.write(f"{word}\n")
