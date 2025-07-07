# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Clean abstract and title texts."""

import pathlib

import contractions  # type: ignore
import pandas as pd  # type: ignore
from nltk.tokenize import word_tokenize


def internal__clean_text(
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
        dataframe[dest] = clean_text(dataframe[source])

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )


def clean_text(text):
    """:meta private:"""

    # remove [...]
    text = text.map(
        lambda w: pd.NA if w[0] == "[" and w[-1] == "]" else w, na_action="ignore"
    )

    text = text.str.lower()

    # remove contractions
    text = text.map(contractions.fix, na_action="ignore")

    # process puntuation
    text = text.str.replace("’", "'", regex=False)
    text = text.str.replace(";", ".", regex=False)
    text = text.str.replace("`", "'", regex=False)

    # remove all html tags
    text = text.str.replace("<.*?>", "", regex=True)

    # process punctuation
    text = text.str.replace(r"&", r" and ", regex=False)  # and
    text = text.str.replace(r"e-mail", r"email", regex=False)  # email
    text = text.str.replace("—", "-", regex=False)
    text = text.str.replace("-", " ", regex=False)

    # tokenize text
    text = text.map(
        lambda w: " ".join(word_tokenize(w)) if isinstance(w, str) else w,
        na_action="ignore",
    )

    # urls and emails
    text = text.str.replace("http : //", "http://", regex=False)
    text = text.str.replace("https : //", "http://", regex=False)
    text = text.str.replace("mail : ", "mail:", regex=False)
    text = text.str.replace(" @ ", "@", regex=False)

    text = text.str.replace(
        r"\s([a-zA-Z])\.\s",
        r" \1 . ",
        regex=True,
    )

    text = text.str.replace(
        r"\s([a-zA-Z])\.([a-zA-Z])\s",
        r" \1 . \2 ",
        regex=True,
    )
    text = text.str.replace(
        r"\s([a-zA-Z])\.([a-zA-Z])\.([a-zA-Z])\s",
        r" \1 . \2 . \3 ",
        regex=True,
    )
    text = text.str.replace(
        r"\s([a-zA-Z])\.([a-zA-Z])\.([a-zA-Z])\.([a-zA-Z])\s",
        r" \1 . \2 . \3 . \4 ",
        regex=True,
    )

    text = text.str.replace(
        r"\s([a-zA-Z][a-zA-Z])\.\s",
        r" \1 . ",
        regex=True,
    )

    text = text.str.replace(
        r"\s([a-zA-Z]+)\.\s\)",
        r" \1 . )",
        regex=True,
    )

    text = text.str.replace(
        r"\s\.\.\s",
        r" . . ",
        regex=True,
    )

    text = text.str.replace(
        r"\s=(\d+)",
        r" = \1",
        regex=True,
    )

    # url_pattern = r"(http[s]?://[^\s]+"

    # Replace URLs with their lower-case version
    # text = text.str.replace(
    #     url_pattern,
    #     lambda m: m.group(0).lower(),
    #     regex=True,
    # )

    # Replace email directions with their lower-case version
    # text = text.str.replace(" email : ", " *email*:", regex=True)
    # text = text.str.replace(" e_mail : ", " +email+:", regex=True)
    # text = text.str.replace(" e-mail : ", " #email#:", regex=True)

    # email_pattern = r"[a-zA-Z0-9._%+-]+@[_a-zA-Z0-9.-]+\.[_a-zA-Z]{2,}"
    # text = text.str.replace(
    #     email_pattern,
    #     lambda m: m.group(0).lower(),
    #     regex=True,
    # )

    text = text.str.replace(" (\d{4})\. ", r" \1 . ", regex=True)  # 2020.
    text = text.str.replace(" et al. ", r" et al . ", regex=False)  # et al.
    text = text.str.replace(" ltd. ", r" ltd . ", regex=False)
    text = text.str.replace(" inc. ", r" inc . ", regex=False)
    text = text.str.replace("_'S_", r"_", regex=False)
    text = text.str.replace(" 's ", r" ", regex=False)
    text = text.str.replace(" '' ", r" ' ' ", regex=False)
    text = text.str.replace(" `` ", " ' ' ", regex=False)
    text = text.str.replace(" .. ", " . . ", regex=False)
    text = text.str.replace(" \.\.$", " . .", regex=True)

    text = text.str.replace(
        " trial registration : ", " trial_registration:", regex=True
    )

    # remove all non-ascii characters
    text = text.str.normalize("NFKD")
    text = text.str.encode("ascii", errors="ignore")
    text = text.str.decode("utf-8")

    # rempve multiple spaces
    text = text.str.replace(r"\s+", r" ", regex=True)
    text = text.str.strip()

    return text


# https : huggingface \. co
# https : github \. com
# https : doi \. org
# https : creativecommons \. org
# http : publichealth \. jmir\.org
# http : doi \. org
# http : creativecommons \. org


def clean_text_ORIGINAL(text):
    """:meta private:"""

    # remove [...]
    text = text.map(
        lambda w: pd.NA if w[0] == "[" and w[-1] == "]" else w, na_action="ignore"
    )

    text = text.str.lower()

    # remove contractions
    text = text.map(contractions.fix, na_action="ignore")

    # remove all html tags
    text = text.str.replace("<.*?>", "", regex=True)

    # process puntuation
    text = text.str.replace("’", "'", regex=False)
    text = text.str.replace(";", ".", regex=False)
    text = text.str.replace(",.", ", .", regex=False)
    text = text.str.replace(r"(", r" ( ", regex=False)  # (
    text = text.str.replace(r")", r" ) ", regex=False)  # )

    text = text.str.replace(r"[", r" [ ", regex=False)  # (
    text = text.str.replace(r"]", r" ] ", regex=False)  # )

    text = text.str.replace(r"$", r" $ ", regex=False)  # $
    text = text.str.replace(r"/", r" / ", regex=False)  # /
    text = text.str.replace(r"?", r" ? ", regex=False)  # ?
    text = text.str.replace(r"¿", r" ¿ ", regex=False)  # ?
    text = text.str.replace(r"!", r" ! ", regex=False)  # !
    text = text.str.replace(r"¡", r" ¡ ", regex=False)  # ¡
    text = text.str.replace(r"=", r" = ", regex=False)  # =
    text = text.str.replace(r'"', r' " ', regex=False)  # "
    text = text.str.replace(r":", r" : ", regex=False)  # :
    text = text.str.replace(r"%", r" % ", regex=False)  # %

    text = text.str.replace(r"<", r" < ", regex=False)  # <
    text = text.str.replace(r">", r" > ", regex=False)  # >
    text = text.str.replace(r"<=", r" <= ", regex=False)  # <=
    text = text.str.replace(r">=", r" >= ", regex=False)  # >=
    text = text.str.replace(r"==", r" == ", regex=False)  # ==
    text = text.str.replace(r"!=", r" == ", regex=False)  # !=

    text = text.str.replace(r"&", r" and ", regex=False)  # and

    text = text.str.replace(r"(\w+)(,\s)", r"\1 \2", regex=True)  # ,
    text = text.str.replace(r"(\w+)(,)(\w+)\s", r"\1 , \3", regex=True)  # ,
    text = text.str.replace(r"\s,(\w+)\s", r" , \1", regex=True)  # ,
    text = text.str.replace(r"(\')(,\s)", r"\1 \2", regex=True)  # ,
    text = text.str.replace(r"(\w+)(\.\s)", r"\1 \2", regex=True)  # .
    text = text.str.replace(r"(\w+)(\.\.\s)", r"\1 . . ", regex=True)  # ..
    text = text.str.replace(r"(\w+)(\.\.)$", r"\1 . .", regex=True)  # ..
    text = text.str.replace(r"(\w+)(,\.)$", r"\1 , .", regex=True)  # ..

    text = text.str.replace(r"(\w+)('\s)", r"\1 \2", regex=True)  # '
    text = text.str.replace(r"(\w+)(',)", r"\1 ' ,", regex=True)  # '
    text = text.str.replace(r"(\w+)(,')", r"\1 , '", regex=True)  # '
    text = text.str.replace(r"(\w+)(\.')", r"\1 . '", regex=True)  # '
    text = text.str.replace(r"(\w+)('\.)", r"\1 ' .", regex=True)  # '
    text = text.str.replace(r"''(\w+)", r"' ' \1", regex=True)  # '
    text = text.str.replace(r"'(\w+)", r"' \1", regex=True)  # '

    text = text.str.replace(r"(\w+)(\.)(\w+)", r"\1 . \3", regex=True)  # b.v
    text = text.str.replace(r"(\w+)(,)(\w+)", r"\1 , \3", regex=True)  # b.v
    text = text.str.replace(r" \.(\w+)", r" . \1", regex=True)  # b.v
    text = text.str.replace(r"(\w+)(\.)(,\s)", r"\1 . \3", regex=True)  # e. g.,
    text = text.str.replace(r"(\w+)(,)(\w+)", r"\1 , \3", regex=True)  # b.v

    text = text.str.replace(r"(\w+)\.$", r"\1 .", regex=True)  # .
    text = text.str.replace(r"(\w+)'s(\b)", r"\1\2", regex=True)
    text = text.str.replace(r"(\w+)'(\s)", r"\1\2", regex=True)  # 's  # s
    text = text.str.replace(r"' .'", r"' , '", regex=False)
    text = text.str.replace("—", "-", regex=False)
    text = text.str.replace("-", " ", regex=False)

    # digits
    text = text.str.replace(r"(\d+) (\.) (\d+)", r"\1.\3", regex=True)  # 1 . 2
    text = text.str.replace(r"(\d+) (,) (\d+)", r"\1.\3", regex=True)  # 1 , 2

    # remove all non-ascii characters
    text = text.str.normalize("NFKD")
    text = text.str.encode("ascii", errors="ignore")
    text = text.str.decode("utf-8")

    # rempve multiple spaces
    text = text.str.replace(r"\s+", r" ", regex=True)
    text = text.str.strip()

    return text
