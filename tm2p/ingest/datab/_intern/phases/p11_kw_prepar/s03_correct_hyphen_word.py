import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip


def s03_correct_hyphen_word(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    keywords = _extract_keywords(df)
    hyphenated_words = _extract_hyphenated_words(df)
    df = _add_padding(df)

    for word_with_hyphen in tqdm(
        hyphenated_words,
        total=len(hyphenated_words),
        bar_format="  {percentage:3.2f}% {bar} | {n_fmt}/{total_fmt} [{rate_fmt}] |",
        ascii=" :",
        ncols=73,
    ):

        word_with_space = word_with_hyphen.replace("-", " ")
        word_without_hyphen = word_with_hyphen.replace("-", "")

        m = _compute_frequency(word_with_hyphen, keywords)
        n = _compute_frequency(word_with_space, keywords)
        k = _compute_frequency(word_without_hyphen, keywords)

        if m >= max(n, k):
            df = _replace(df, pattern=word_with_space, replacement=word_with_hyphen)
            df = _replace(df, pattern=word_without_hyphen, replacement=word_with_hyphen)
            continue

        if n > k:
            df = _replace(df, pattern=word_with_hyphen, replacement=word_with_space)
            df = _replace(df, pattern=word_without_hyphen, replacement=word_with_space)
            continue

        df = _replace(df, pattern=word_with_hyphen, replacement=word_without_hyphen)
        df = _replace(df, pattern=word_with_space, replacement=word_without_hyphen)

    df = _remove_padding(df)

    save_main_csv_zip(df, root_directory)

    result = 0
    if Field.AUTHKW_TOK.value in df.columns:
        result = max(result, int(df[Field.AUTHKW_TOK.value].notna().sum()))
    if Field.IDXKW_TOK.value in df.columns:
        result = max(result, int(df[Field.IDXKW_TOK.value].notna().sum()))
    return result


def _replace(df: pd.DataFrame, pattern: str, replacement: str) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            df[col] = df[col].str.replace(
                f" {pattern} ",
                f" {replacement} ",
                regex=False,
            )
            df[col] = df[col].str.replace(
                f"/{pattern} ",
                f"/{replacement} ",
                regex=False,
            )
            df[col] = df[col].str.replace(
                f" {pattern}/",
                f" {replacement}/",
                regex=False,
            )
            df[col] = df[col].str.replace(
                f"/{pattern}/",
                f"/{replacement}/",
                regex=False,
            )

    return df


def _compute_frequency(word: str, keywords: pd.Series) -> int:
    word = f" {word} "
    frequency = keywords.str.contains(word, case=False, regex=False).sum()
    return frequency


def _extract_keywords(df: pd.DataFrame) -> pd.Series:

    authkw = (
        df[Field.AUTHKW_TOK.value]
        if Field.AUTHKW_TOK.value in df.columns
        else pd.Series(dtype=str)
    )

    idxkw = (
        df[Field.IDXKW_TOK.value]
        if Field.IDXKW_TOK.value in df.columns
        else pd.Series(dtype=str)
    )

    kw = pd.concat([authkw, idxkw], ignore_index=True)
    kw = kw.dropna()
    kw = kw.str.split("; ").explode()
    kw = kw.str.strip()
    kw = kw.apply(lambda x: f" {x} ")

    return kw


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


def _remove_padding(df: pd.DataFrame) -> pd.DataFrame:

    for col in [
        Field.AUTHKW_TOK.value,
        Field.IDXKW_TOK.value,
    ]:
        if col in df.columns:
            df[col] = df[col].str.replace(" ; ", "; ", regex=False)
            df[col] = df[col].str.strip()

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
