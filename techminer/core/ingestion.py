"""
Data Importers
===============================================================================

"""

import re
import unicodedata
from os.path import dirname, isfile, join

import pandas as pd
from techminer.core.thesaurus import load_file_as_dict

#
# ETL:
#    Extracts data from raw data sources
#    Transforms data into a common format
#    Loads data into a common format
#


# def _strip_accents(text):
#     try:
#         text = decode(text, "utf-8")
#     except NameError:  # unicode is a default on python 3
#         pass

#     if isinstance(text, str):
#         text = (
#             unicodedata.normalize("NFD", text).encode("ascii", "ignore").decode("utf-8")
#         )
#         return str(text)

#     return text
