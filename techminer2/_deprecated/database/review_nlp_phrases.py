# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# import pandas as pd  # type: ignore
# from ...operations.operations__process_field import internal__process_field
# from ..preprocessing.internal__preprocess_raw_descriptors import internal__preprocess_raw_descriptors
# from ..preprocessing.internal__preprocess_raw_nlp_phrases import internal__preprocess_raw_nlp_phrases
# def _collect_uppercase_tokens(column):
#     column = column.str.split()
#     column = column.map(
#         lambda y: [word for word in y if word.isupper()], na_action="ignore"
#     )
#     column = column.map(lambda y: pd.NA if len(y) == 0 else y, na_action="ignore")
#     column = column.str.join("; ")
#     return column
# def preprocessing__review_nlp_phrases(root_dir):
#     """:meta private:"""
#     internal__process_field(
#         source="document_title",
#         dest="raw_title_nlp_phrases",
#         func=_collect_uppercase_tokens,
#         root_dir=root_dir,
#     )
#     internal__process_field(
#         source="abstract",
#         dest="raw_abstract_nlp_phrases",
#         func=_collect_uppercase_tokens,
#         root_dir=root_dir,
#     )
#     internal__preprocess_raw_nlp_phrases(root_dir)
#     internal__preprocess_raw_descriptors(root_dir)
