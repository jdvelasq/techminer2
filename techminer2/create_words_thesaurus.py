"""
Create keywords thesaurus
===============================================================================



"""

import glob
import os
import sys

import pandas as pd

from .thesaurus import Thesaurus, read_textfile, text_clustering


def create_words_thesaurus(directory="./"):
    """Createa a keywords thesaurus from raw author/index keywords and title/abstact words."""

    sys.stdout.write(
        "--INFO-- Creating `words.txt` from author/index keywords, and abstract/title words\n"
    )

    words_list = []
    files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8")
        if "raw_author_keywords" in data.columns:
            words_list += data.raw_author_keywords.tolist()
        if "raw_index_keywords" in data.columns:
            words_list += data.raw_index_keywords.tolist()
        if "raw_title_words" in data.columns:
            words_list += data.raw_title_words.tolist()
        if "raw_abstract_words" in data.columns:
            words_list += data.raw_abstract_words.tolist()

    words_list = pd.Series(words_list)
    words_list = words_list.dropna()
    words_list = words_list.str.lower()
    words_list = words_list.str.split(";")
    words_list = words_list.explode()
    words_list = words_list.str.strip()
    words_list = words_list[words_list.str.len() > 1]

    words_list = words_list.str.replace('"', "")
    words_list = words_list.str.replace(chr(8212), "")
    words_list = words_list.str.replace(chr(8220), "")
    words_list = words_list.str.replace(chr(8221), "")

    words_list = words_list.where(
        (words_list.str[0] == "-") & words_list.str.len() > 1,
        words_list.str.replace("-", ""),
    )

    # ----< new algorithm >----------------------------------------------------
    # {palabra: clave_del_grupo}
    new_th = text_clustering(pd.Series(words_list)).to_dict()

    thesaurus_file = os.path.join(directory, "processed", "words.txt")
    if os.path.isfile(thesaurus_file):
        old_th = read_textfile(thesaurus_file).to_dict()
        new_th = {**new_th, **old_th}

    keys = list(set(new_th.values()))

    th = {key: [] for key in keys}

    for key, value in new_th.items():
        th[value].append(key)

    Thesaurus(
        x=th,
        ignore_case=True,
        full_match=False,
        use_re=False,
    ).to_textfile(thesaurus_file)
