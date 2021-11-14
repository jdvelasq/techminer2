"""
Extract user keywords
===============================================================================
"""


import pandas as pd

from .utils import Keywords, load_filtered_documents, logging


def _extract_user_keywords_from_records(
    records,
    keywords_list,
    input_column,
    output_column,
    full_match,
    ignore_case,
    use_re,
):

    records[output_column] = pd.NA

    if isinstance(keywords_list, str):
        with open(keywords_list, "rt", encoding="utf-8") as file:
            keywords_list = file.read().splitlines()
    elif isinstance(keywords_list, list):
        if not all([isinstance(x, str) for x in keywords_list]):
            raise ValueError("keywords_list must be a list of strings")
    else:
        raise ValueError("keywords_list must be a list of strings or a filename")

    keywords = Keywords(ignore_case=ignore_case, full_match=full_match, use_re=use_re)
    keywords.add_keywords(keywords_list)
    keywords.compile()

    records[output_column] = records[input_column].map(
        keywords.extract_from_text, na_action="ignore"
    )

    records[output_column] = records[output_column].map(
        lambda x: pd.NA if x is None else x, na_action="ignore"
    )

    return records


def _extract_user_keywords_from_directory(
    directory,
    keywords_list,
    input_column,
    output_column,
    full_match,
    ignore_case,
    use_re,
):

    return _extract_user_keywords_from_records(
        records=load_records(directory),
        keywords_list=keywords_list,
        input_column=input_column,
        output_column=output_column,
        full_match=full_match,
        ignore_case=ignore_case,
        use_re=use_re,
    )


def extract_keywords(
    directory_or_records,
    keywords_list,
    input_column,
    output_column,
    full_match,
    ignore_case,
    use_re,
):
    if isinstance(directory_or_records, str):
        return _extract_user_keywords_from_directory(
            directory=directory_or_records,
            keywords_list=keywords_list,
            input_column=input_column,
            output_column=output_column,
            full_match=full_match,
            ignore_case=ignore_case,
            use_re=use_re,
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _extract_user_keywords_from_records(
            records=directory_or_records,
            keywords_list=keywords_list,
            input_column=input_column,
            output_column=output_column,
            full_match=full_match,
            ignore_case=ignore_case,
            use_re=use_re,
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
