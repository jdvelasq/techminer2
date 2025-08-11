# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# import glob
# import os.path
# import re
# import pandas as pd  # type: ignore
# from nltk.stem import WordNetLemmatizer  # type: ignore
# from textblob import TextBlob  # type: ignore
# from tqdm import tqdm  # type: ignore
# from ....internals.stopwords.load_package_stopwords import load_package_stopwords
# from ...operations.operations__protected_fields import PROTECTED_FIELDS
# #
# # A lemmatizer is defined to use in each cell of the dataframe
# lemmatizer = WordNetLemmatizer()
# def to_lemma(tag):
#     if tag[0] == tag[0].upper():
#         return tag
#     if tag[1][:2] == "NN":
#         return (lemmatizer.lemmatize(tag[0], pos="n"), tag[1])
#     if tag[1][:2] == "VB":
#         return (lemmatizer.lemmatize(tag[0], pos="v"), tag[1])
#     if tag[1][:2] == "RB":
#         return (lemmatizer.lemmatize(tag[0], pos="r"), tag[1])
#     if tag[1][:2] == "JJ":
#         return (lemmatizer.lemmatize(tag[0], pos="a"), tag[1])
#     return None
# #
# #
# def extract_meaningful_words(
#     source,
#     dest,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
# ):
#     """:meta private:"""
#     if dest in PROTECTED_FIELDS:
#         raise ValueError(f"Field `{dest}` is protected")
#     transformations__extract_meaningful_words(
#         source=source,
#         dest=dest,
#         #
#         # DATABASE PARAMS:
#         root_dir=root_dir,
#     )
