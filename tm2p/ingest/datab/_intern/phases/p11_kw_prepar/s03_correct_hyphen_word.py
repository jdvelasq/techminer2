import json
import os
from pathlib import Path

import pandas as pd  # type: ignore
from openai import APIError, OpenAI
from tqdm import tqdm  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.packag_data import (
    add_new_words_to_builtin_word_list,
    load_builtin_word_list,
)

SYSTEM_PROMPT = """
INSTRUCTION:
You will be provided with two variations of the same word: one in hyphenated form and the other in non-hyphenated form.


TASK:
1. Analyze the two forms and determine which is correct in scientific or technical English usage.
2. Respond with "yes" if:
    - The hyphenated form is the only form correct.
    - The word is not standard English.
    - Both forms (hyphenated and non-hyphenated) are correct.
    - The hyphenated form is commonly used and accepted in scientific or technical contexts, even if the non-hyphenated form is also correct.
    - Neither form is correct.
3. Respond "no" if:
    - The non-hyphenated form is the only form correct.
    - The correct form is different from both provided forms.
3. Respond "split" if:
    - Both, the hyphenated and the non-hyphenated forms are incorrect, and thecorrect form is only obtained by reemplazing the "-" by an space ()" ").  
    
OUTPUT FORMAT (STRICT — JSON ONLY):
The output MUST be a JSON object with the following structure:

{{
    "answer": "yes" or "no" or "split",
}}

Any output different of this must be considered invalid.

"""

USER_PROMPT = """

WORDS:
- Hyphenated: "{}"
- Non-hyphenated: "{}"

"""


def s03_correct_hyphen_word(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    words_valid, words_invalid, words_to_split = _classify_hyphenated_words(
        root_directory, df
    )

    df = _add_padding(df)
    df = _split_to_space(df, words_to_split)
    df = _compact_to_space(df, words_to_split)
    df = _invalid_to_compact(df, words_invalid)
    df = _compact_to_space(df, words_to_split)
    df = _compact_to_hyphen(df, words_valid)
    df = _remove_padding(df)

    save_main_csv_zip(df, root_directory)

    result = 0
    if Field.AUTHKW_TOK.value in df.columns:
        result = max(result, int(df[Field.AUTHKW_TOK.value].notna().sum()))
    if Field.IDXKW_TOK.value in df.columns:
        result = max(result, int(df[Field.IDXKW_TOK.value].notna().sum()))
    return result


def _remove_padding(df: pd.DataFrame) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            df[col] = df[col].str.strip()
            df[col] = df[col].str.replace(" ; ", "; ", regex=False)

    return df


def _split_to_space(df: pd.DataFrame, words_to_split: set) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            for word in words_to_split:
                df[col] = df[col].str.replace(
                    f" {word} ",
                    f" {word.replace('-', ' ')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f"/{word} ",
                    f"/{word.replace('-', ' ')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f" {word}/",
                    f" {word.replace('-', ' ')}/",
                    regex=False,
                )

    return df


def _compact_to_space(df: pd.DataFrame, words_to_split: set) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            for word in words_to_split:
                df[col] = df[col].str.replace(
                    f" {word.replace('-', '')} ",
                    f" {word.replace('-', ' ')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f"/{word.replace('-', '')} ",
                    f"/{word.replace('-', ' ')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f" {word.replace('-', '')}/",
                    f" {word.replace('-', ' ')}/",
                    regex=False,
                )
    return df


def _compact_to_hyphen(df: pd.DataFrame, words_to_split: set) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            for word in words_to_split:
                df[col] = df[col].str.replace(
                    f" {word.replace('-', '')} ",
                    f" {word} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f"/{word.replace('-', '')} ",
                    f"/{word} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f" {word.replace('-', '')}/",
                    f" {word}/",
                    regex=False,
                )
    return df


def _invalid_to_compact(df: pd.DataFrame, words_invalid: set) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            for word in words_invalid:
                df[col] = df[col].str.replace(
                    f" {word} ",
                    f" {word.replace('-', '')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f"/{word} ",
                    f"/{word.replace('-', '')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f" {word}/",
                    f" {word.replace('-', '')}/",
                    regex=False,
                )

    return df


def _add_padding(df: pd.DataFrame) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            df[col] = df[col].map(lambda x: f" {x} " if pd.notna(x) else x)
            df[col] = df[col].str.replace("; ", " ; ", regex=False)

    return df


def _classify_hyphenated_words(root_directory, df):

    words = _extract_hyphenated_words(df)
    if not words:
        return set(), set(), set()

    known_words_valid = load_builtin_word_list("valid_hyphenated_words.txt")
    known_words_invalid = load_builtin_word_list("invalid_hyphenated_words.txt")
    known_words_to_split = load_builtin_word_list(
        "invalid_hyphenated_words_splitted.txt"
    )

    known_words_valid = set(known_words_valid)
    known_words_invalid = set(known_words_invalid)
    known_words_to_split = set(known_words_to_split)

    known_words = (
        set(known_words_valid) | set(known_words_invalid) | set(known_words_to_split)
    )

    unknown_words = words - set(known_words)

    new_words_valid, new_words_invalid, new_words_split = _classify_unknown_words(
        unknown_words
    )

    _report_new_words(
        new_valid_words=new_words_valid,
        new_invalid_words=new_words_invalid,
        new_split_words=new_words_split,
        root_directory=root_directory,
    )

    return (
        known_words_valid | new_words_valid,
        known_words_invalid | new_words_invalid,
        known_words_to_split | new_words_split,
    )


def _extract_hyphenated_words(dataframe: pd.DataFrame) -> set:

    hypenated_words: set[str] = set()
    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col not in dataframe.columns:
            continue

        series = dataframe[col].dropna()
        series = series.str.lower()
        keywords = series.str.split("; ").explode()
        keywords = keywords.str.strip()
        words = keywords.str.split(" ").explode()
        words = words.str.strip()
        words = words[~words.str.startswith("-")]
        words = words[~words.str.endswith("-")]
        words = words[words.str.contains("-")]
        words = words[~words.str.contains("--")]
        words = words[words.map(lambda x: x != "-")]
        words_set = set(words.tolist())
        hypenated_words.update(words_set)

    return hypenated_words


def _classify_unknown_words(unknown_words: set) -> tuple[set, set, set]:

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    valid_words: set[str] = set()
    invalid_words: set[str] = set()
    split_words: set[str] = set()

    if not unknown_words:
        return valid_words, invalid_words, split_words

    for word in tqdm(
        unknown_words,
        total=len(unknown_words),
        bar_format="  {percentage:3.2f}% {bar} | {n_fmt}/{total_fmt} [{rate_fmt}] |",
        ascii=" :",
        ncols=73,
    ):

        if "-" not in word:
            raise ValueError(f"Word '{word}' does not contain a hyphen.")

        parts = word.split("-")
        if parts[0] == parts[1]:
            invalid_words.add(word)
            continue

        query = USER_PROMPT.format(word.lower(), word.lower().replace("-", ""))

        try:

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",  # type: ignore
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
            if answer is None:
                print(f"Error: Empty response for word '{word}'")
                continue
            answer = json.loads(answer)
            answer = answer["answer"]
            answer = answer.lower()

            if answer == "no":
                invalid_words.add(word)
            elif answer == "yes":
                valid_words.add(word)
            elif answer == "split":
                split_words.add(word)
            else:
                print(f"Error: Invalid answer '{answer}' for word '{word}'")

        except (APIError, json.JSONDecodeError, KeyError) as e:
            print(f"Error processing {e}")

    return valid_words, invalid_words, split_words


def _report_new_words(
    new_valid_words: set,
    new_invalid_words: set,
    new_split_words: set,
    root_directory: str,
) -> None:

    my_keywords_path = Path(root_directory) / "refine" / "word_lists"

    if new_valid_words:

        report_file = my_keywords_path / "valid_hyphenated_words.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            for word in sorted(new_valid_words):
                f.write(f"{word}\n")

        add_new_words_to_builtin_word_list(
            "valid_hyphenated_words.txt", list(new_valid_words)
        )

    if new_invalid_words:

        report_file = my_keywords_path / "invalid_hyphenated_words.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            for word in sorted(new_invalid_words):
                f.write(f"{word}\n")

        add_new_words_to_builtin_word_list(
            "invalid_hyphenated_words.txt", list(new_invalid_words)
        )

    if new_split_words:

        report_file = my_keywords_path / "invalid_hyphenated_words_splitted.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            for word in sorted(new_split_words):
                f.write(f"{word}\n")

        add_new_words_to_builtin_word_list(
            "invalid_hyphenated_words_splitted.txt", list(new_split_words)
        )
