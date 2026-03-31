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
You will be provided with two variations of the same term:
1) A hyphenated form
2) A non-hyphenated form


TASK:
Determine which form is correct in scientific or technical English usage.

Respond according to the following rules:

- "yes" →
    The hyphenated form is correct OR acceptable in technical/scientific usage.
    This includes:
        - Only the hyphenated form is correct
        - Both forms are correct but hyphenated is acceptable
        - The term is non-standard but hyphenated form is used in practice

- "no" →
    The hyphenated form is incorrect, and the correct form is:
        - The non-hyphenated form
        - Another hyphenated form (hyphen position is wrong)
        - A completely different valid form

- "split" →
    The correct form consists of two separate words (space-separated),
    and both provided forms are incorrect.

OUTPUT FORMAT (STRICT — JSON ONLY):

{{
    "answer": "yes" | "no" | "split"
}}

"""

USER_PROMPT = """

WORDS:
- Hyphenated: "{}"
- Non-hyphenated: "{}"

"""


def s03_correct_hyphen_word(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    words_valid, words_to_split, words_wrong = _classify_hyphenated_words(
        root_directory, df
    )

    df = _add_padding(df)
    df = _hyphen_to_compact(df)
    df = _compact_to_space(df, words_to_split)
    df = _compact_to_hyphen(df, words_valid)
    df = _space_to_hyphen(df, words_valid)
    df = _space_to_compact(df, words_wrong)
    df = _remove_padding(df)

    save_main_csv_zip(df, root_directory)

    result = 0
    if Field.AUTHKW_TOK.value in df.columns:
        result = max(result, int(df[Field.AUTHKW_TOK.value].notna().sum()))
    if Field.IDXKW_TOK.value in df.columns:
        result = max(result, int(df[Field.IDXKW_TOK.value].notna().sum()))
    return result


def _space_to_compact(df: pd.DataFrame, wrong_words: set) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            for word in wrong_words:
                df[col] = df[col].str.replace(
                    f" {word.replace('-', ' ')} ",
                    f" {word.replace('-', '')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f"/{word.replace('-', ' ')} ",
                    f"/{word.replace('-', '')} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f" {word.replace('-', ' ')}/",
                    f" {word.replace('-', '')}/",
                    regex=False,
                )
    return df


def _hyphen_to_compact(df: pd.DataFrame) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            df[col] = df[col].str.replace("-", "", regex=False)

    return df


def _remove_padding(df: pd.DataFrame) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            df[col] = df[col].str.replace(" ; ", "; ", regex=False)
            df[col] = df[col].str.strip()

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


def _space_to_hyphen(df: pd.DataFrame, words_to_split: set) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            for word in words_to_split:
                df[col] = df[col].str.replace(
                    f" {word.replace('-', ' ')} ",
                    f" {word} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f"/{word.replace('-', ' ')} ",
                    f"/{word} ",
                    regex=False,
                )
                df[col] = df[col].str.replace(
                    f" {word.replace('-', ' ')}/",
                    f" {word}/",
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


def _classify_hyphenated_words(root_directory, df) -> tuple[set, set, set]:

    words = _extract_hyphenated_words(df)
    if not words:
        return set(), set(), set()

    known_correct_words = load_builtin_word_list("hyphen_correct_words.txt")
    known_wrong_words = load_builtin_word_list("hyphen_wrong_words.txt")
    known_individual_words = load_builtin_word_list("hyphen_individual_words.txt")

    known_words = (
        set(known_correct_words) | set(known_individual_words) | set(known_wrong_words)
    )
    unknown_words = words - set(known_words)

    new_correct_words, new_wrong_words, new_individual_words = _classify_unknown_words(
        unknown_words
    )

    _report_new_words(
        new_correct_words=new_correct_words,
        new_wrong_words=new_wrong_words,
        new_individual_words=new_individual_words,
        root_directory=root_directory,
    )

    return (
        set(known_correct_words) | new_correct_words,
        set(known_individual_words) | new_individual_words,
        set(known_wrong_words) | new_wrong_words,
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
                model="gpt-5.2",
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
    new_correct_words: set,
    new_wrong_words: set,
    new_individual_words: set,
    root_directory: str,
) -> None:

    my_keywords_path = Path(root_directory) / "refine" / "word_lists"

    if new_correct_words:

        report_file = my_keywords_path / "hyphen_correct_words.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            for word in sorted(new_correct_words):
                f.write(f"{word}\n")

        add_new_words_to_builtin_word_list(
            "hyphen_correct_words.txt", list(new_correct_words)
        )

    if new_wrong_words:

        report_file = my_keywords_path / "invalid_hyphenated_words.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            for word in sorted(new_wrong_words):
                f.write(f"{word}\n")

        add_new_words_to_builtin_word_list(
            "hyphen_wrong_words.txt", list(new_wrong_words)
        )

    if new_individual_words:

        report_file = my_keywords_path / "hypen_individual_words.txt"

        with open(report_file, "w", encoding="utf-8") as f:
            for word in sorted(new_individual_words):
                f.write(f"{word}\n")

        add_new_words_to_builtin_word_list(
            "hypen_individual_words.txt", list(new_individual_words)
        )
