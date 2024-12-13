# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import glob
import os.path
import re

import pandas as pd  # type: ignore
from textblob import TextBlob  # type: ignore
from tqdm import tqdm  # type: ignore

from ..fields.protected_fields import PROTECTED_FIELDS


def extract_nouns_and_noun_phrases(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """
    :meta private:
    """

    if dest in PROTECTED_FIELDS:
        raise ValueError(f"Field `{dest}` is protected")

    _extract_nouns_and_noun_phrases(
        source=source,
        dest=dest,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
    )


def _extract_nouns_and_noun_phrases(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_dir,
):
    # Register tqdm pandas progress bar
    tqdm.pandas()

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        #
        if source not in data.columns:
            continue
        data[dest] = data[source].progress_apply(extract_noun_phrases)
        #
        #
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


#
#
def extract_noun_phrases(text):
    #
    # extract noun phrases
    if not isinstance(text, str):
        return pd.NA

    noun_phrases = [str(phrase) for phrase in TextBlob(text.lower()).noun_phrases]
    #
    #
    noun_phrases = [phrase for phrase in noun_phrases if not phrase.startswith("//")]
    noun_phrases = [phrase.replace("'", "") for phrase in noun_phrases]
    noun_phrases = [
        phrase for phrase in noun_phrases if not re.search(r"[^\w\s]", phrase)
    ]
    noun_phrases = [phrase for phrase in noun_phrases if phrase not in ""]
    #
    #
    noun_phrases = sorted(noun_phrases, key=lambda x: len(x.split(" ")), reverse=True)

    #
    # transform noun phrases to upper cases and replace space with underscore
    if len(noun_phrases) > 0:
        regex = "|".join([re.escape(phrase) for phrase in noun_phrases])
        regex = re.compile(r"\b(" + regex + r")\b")
        text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

    tags = TextBlob(text).tags
    noun_phrases = sorted(set(tag[0].upper() for tag in tags if tag[1][:2] == "NN"))
    #
    #
    noun_phrases = [phrase for phrase in noun_phrases if not phrase.startswith("//")]
    noun_phrases = [phrase.replace("'", "") for phrase in noun_phrases]
    noun_phrases = [
        phrase for phrase in noun_phrases if not re.search(r"[^\w\s]", phrase)
    ]
    noun_phrases = [phrase for phrase in noun_phrases if phrase not in ""]
    #
    #
    noun_phrases = "; ".join(noun_phrases)

    return noun_phrases
