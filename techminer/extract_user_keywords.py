"""
Extract user keywords
===============================================================================

Funcionality similar to My Keywords in VantagePoint.

"""


import os

import numpy as np
import pandas as pd

from techminer.utils.io import save_documents

from .utils import load_all_documents, load_filtered_documents, logging


def extract_user_keywords(
    directory=None,
    keywords_file="user_keywords.txt",
    input_column="author_keywords",
    output_column="extracted_user_keywords",
    flags=0,
):

    documents = load_all_documents(directory)

    # ---< loads keywords from file >----------------------------------------
    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"

    filename = os.path.join(directory, keywords_file)

    logging.info(f"Loading user keywords from {filename}")

    with open(filename, "rt", encoding="utf-8") as file:
        keywords_list = file.read().splitlines()
    keywords_regex = ")|(".join(keywords_list)
    keywords_regex = "(" + keywords_regex + ")"

    # ---< extract keywords from documents >-----------------------------------
    documents.index = documents.document_id
    result = documents[input_column].str.extractall(keywords_regex, flags)
    result = result.reset_index()
    result = pd.melt(
        result,
        id_vars=["document_id", "match"],
        var_name="keyword_index",
        value_name="captured_keyword",
    )

    result = result.dropna()
    result = result[["document_id", "captured_keyword"]]
    result = result.groupby("document_id").agg(list)
    result["captured_keyword"] = result["captured_keyword"].apply(
        lambda x: "; ".join(x)
    )

    # ---< save results >-----------------------------------------------------
    result_dict = dict(zip(result.index, result.captured_keyword))

    documents[output_column] = documents["document_id"].map(
        lambda x: np.NaN if x not in result_dict else result_dict[x]
    )

    save_documents(documents=documents, directory=directory)
    logging.info(f"User keywords extracted and saved in {directory}")
