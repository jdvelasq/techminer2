# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Clean abstract and title texts."""
import pathlib
import re

import contractions  # type: ignore
import pandas as pd  # type: ignore
from nltk.tokenize import word_tokenize


def internal__tokenize(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    database_file = pathlib.Path(root_dir) / "data/processed/database.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source in dataframe.columns and not dataframe[source].dropna().empty:
        dataframe[dest] = tokenize(dataframe[source])

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def tokenize(text):
    """:meta private:"""

    # remove [...]
    text = text.map(
        lambda w: pd.NA if w[0] == "[" and w[-1] == "]" else w, na_action="ignore"
    )

    # find all URLs in the pandas series
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    urls = text.str.findall(url_pattern).explode().dropna().unique()

    # Replace URLs with the by "__url{i}__" where i is the index
    # of the URL in the list of unique URLs.
    for i, url in enumerate(urls):
        placeholder = f" . . . url{i} . . . "
        text = text.str.replace(url, placeholder, regex=False)

    text = text.str.lower()

    # Remove all HTML tags
    text = text.str.replace("<.*?>", "", regex=True)

    # Standardize "e-mail" to "email" for consistency.
    text = text.str.replace(r"e-mail", r"email", regex=False)

    # Expand contractions (e.g., "don't" -> "do not")
    text = text.map(contractions.fix, na_action="ignore")

    # Standardize punctuation:
    # Replace curly apostrophes (’) and backticks (`) with straight apostrophes (') for consistency.
    # Replace semicolons (;) with periods (.) to simplify sentence structure.
    # Replace em dashes (—) with hyphens (-) for uniformity.
    text = text.str.replace("’", "'", regex=False)
    text = text.str.replace(";", ".", regex=False)
    text = text.str.replace("`", "'", regex=False)
    text = text.str.replace("—", "-", regex=False)
    text = text.str.replace("-", " ", regex=False)
    text = text.str.replace("&", " and ", regex=False)  # and

    # Tokenize text into individual words:
    # Split each string into tokens (words) using NLTK's word_tokenize.
    # If the value is not a string, it is left unchanged.
    text = text.map(
        lambda w: " ".join(word_tokenize(w)) if isinstance(w, str) else w,
        na_action="ignore",
    )

    # Correction: Standardize URLs and email formatting to preserve entities.
    # Replace "http : //" and "https : //" with "http://" for consistency.
    # Replace "mail : " with "mail:" to standardize email formatting.
    # Replace " @ " with "@" to ensure proper email address formatting.
    text = text.str.replace("http : //", "http://", regex=False)
    text = text.str.replace("https : //", "http://", regex=False)
    text = text.str.replace("mail : ", "mail:", regex=False)
    text = text.str.replace(" @ ", "@", regex=False)

    # Correction: Add spaces around slashes between words for clarity.
    # (e.g., "setting/participants/intervention" becomes "setting / participants / intervention").
    text = text.str.replace(r"([a-zA-Z])/([a-zA-Z])", r"\1 / \2", regex=True)

    # Correction: Standardize punctuation for edge cases not handled by word_tokenize.
    # Add a space before an opening parenthesis if it follows a period.
    text = text.str.replace(" .(", " . (", regex=False)

    # Correction: Ensure proper spacing around single letters followed by a period
    # (e.g., " A. " becomes " A . ").
    text = text.str.replace(r"\s([a-zA-Z])\.\s", r" \1 . ", regex=True)

    text = text.str.replace(":. ", ": . ", regex=False)

    # Correction: Add a space after an apostrophe if followed by alphanumeric
    # characters or a period. (e.g., " 's " becomes " ' s ").
    text = text.str.replace(r" '([a-zA-Z0-9\.]+)\s", r" ' \1 ", regex=True)

    # Correction: Add a space after an apostrophe if followed by numeric characters.
    # (e.g., " '123" becomes " ' 123").
    text = text.str.replace(r" '(\d+)", r" ' \1", regex=True)

    # Correction: Add spaces around single-letter abbreviations separated by periods.
    # (e.g., " A.B " becomes " A . B ").
    text = text.str.replace(
        r"\s([a-zA-Z])\.([a-zA-Z])\s",
        r" \1 . \2 ",
        regex=True,
    )

    # Correction: Add spaces around tokens separated by periods.
    # (e.g., "xxx.yyy " becomes " xxx . yyy ").
    text = text.str.replace(
        r"\s([a-zA-Z]+)\.([a-zA-Z]+)\s",
        r" \1 . \2 ",
        regex=True,
    )

    # Correction: Add spaces around a text separated by a two points.
    # (e.g., "xxx:yyy " becomes "xxx : yyy ").
    text = text.str.replace(
        r"([a-zA-Z]+):([a-zA-Z]+)",
        r"\1 : \2",
        regex=True,
    )

    # Correction: add spaces around three-letter abbreviations separated by periods.
    # (e.g., " A.B.C " becomes " A . B . C ").
    text = text.str.replace(
        r"\s([a-zA-Z])\.([a-zA-Z])\.([a-zA-Z])\s",
        r" \1 . \2 . \3 ",
        regex=True,
    )

    # Correction: Add spaces around four-letter abbreviations separated by periods.
    # (e.g., " A.B.C.D " becomes " A . B . C . D ").
    text = text.str.replace(
        r"\s([a-zA-Z])\.([a-zA-Z])\.([a-zA-Z])\.([a-zA-Z])\s",
        r" \1 . \2 . \3 . \4 ",
        regex=True,
    )

    # Correction: Add spaces around two-letter abbreviations followed by a period.
    # (e.g., " AB. " becomes " AB . ").
    text = text.str.replace(r"\s([a-zA-Z][a-zA-Z])\.\s", r" \1 . ", regex=True)

    # Correction: Add a space before a closing parenthesis if preceded by a word and a period.
    # (e.g., " AB.) " becomes " AB . ) ").
    text = text.str.replace(r"\s([a-zA-Z]+)\.\s\)", r" \1 . )", regex=True)

    # Correction: Replace ellipses (" .. ") with spaced periods (" . . ") for consistency.
    text = text.str.replace(r"\s\.\.\s", r" . . ", regex=True)

    # Correction: Add a space before an equals sign if followed by numeric characters.
    # (e.g., " =123" becomes " = 123").
    text = text.str.replace(r"\s=(\d+)", r" = \1", regex=True)

    # Correction: Add a space around a four-digit year followed by a period.
    # (e.g., " 2020. " becomes " 2020 . ").
    text = text.str.replace(" (\d{4})\. ", r" \1 . ", regex=True)

    # Correction: Add spacing around "et al." for consistency.
    # (e.g., "et al." becomes "et al .").
    text = text.str.replace(" et al. ", " et al . ", regex=False)

    # Correction: Add spacing around "ltd." for consistency.
    # (e.g., "ltd." becomes "ltd .").
    text = text.str.replace(" ltd. ", " ltd . ", regex=False)

    # Correction: Add spacing around "inc." for consistency.
    # (e.g., "inc." becomes "inc .").
    text = text.str.replace(" inc. ", " inc . ", regex=False)

    # Correction: Remove possessive "'s" when surrounded by underscores
    # for consistency. (e.g., "_'s_" becomes "_").
    text = text.str.replace("_'s_", "_", regex=False)
    text = text.str.replace(" 's ", " ", regex=False)

    # Correction: Replace double quotes (" '' " and " `` ") with single
    # quotes (" ' ' ") for consistency.
    text = text.str.replace(" '' ", " ' ' ", regex=False)
    text = text.str.replace(" `` ", " ' ' ", regex=False)

    # Correction: Replace ellipses (" .. ") with spaced periods (" . . ")
    # for uniformity.
    text = text.str.replace(" .. ", " . . ", regex=False)

    # Correction: Replace trailing ellipses (" ..") at the end of a sentence
    # with spaced periods (" . .").
    text = text.str.replace(" \.\.$", " . .", regex=True)

    # Correction: Add spacing between the point and the letter in " .LETTER"
    text = text.str.replace(r" \.([a-z])", r" . \1", regex=True)

    # Correction: Replace "trial registration :" with "trial_registration:"
    # to standardize the format.
    text = text.str.replace(
        " trial registration : ", " trial_registration :", regex=True
    )

    # Correction: energy units
    text = text.str.replace(" g / kwh ", " g/kwh ", regex=False)
    text = text.str.replace("/mw h ", "/mwh ", regex=False)
    text = text.str.replace("/kw h ", "/kwh ", regex=False)
    text = text.str.replace("/kw hr ", "/kwh ", regex=False)
    text = text.str.replace("us cents/kwh ", "uscents/kwh ", regex=False)

    # Remove all non-ASCII characters:
    # Normalize text to NFKD form, encode to ASCII (ignoring errors), and decode back to UTF-8.
    text = text.str.normalize("NFKD")
    text = text.str.encode("ascii", errors="ignore")
    text = text.str.decode("utf-8")

    # Remove multiple spaces and trim leading/trailing whitespace.
    text = text.str.replace(r"\s+", r" ", regex=True)
    text = text.str.strip()

    # URLs
    urls = [url.replace("_", "-") for url in urls]

    for i, url in enumerate(urls):

        #
        if url.endswith(")."):
            url = url[:-2] + " ) ."
            urls[i] = url
            continue

        if url.endswith("),"):
            url = url[:-2] + " ) ,"
            urls[i] = url
            continue

        if url.endswith(","):
            url = url[:-1] + " ,"
            urls[i] = url
            continue

        if url.endswith("."):
            url = url[:-1] + " ."
            urls[i] = url
            continue

        if url.endswith(")"):
            url = url[:-1] + " )"
            urls[i] = url
            continue

    # Restore URLs
    for i, url in enumerate(urls):
        placeholder = f". . . url{i} . . ."
        text = text.str.replace(placeholder, url, regex=False)

    text = text.str.replace(" :http", " : http", regex=False)

    return text
