# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Update Abstract
===============================================================================


# >>> from techminer2.ingest import update_abstract
# >>> update_abstract(
# ...     record_id=
# ...     new_text=
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ... )




"""
# import os
#
# from ....internals.read_filtered_database import read_filtered_database
#
#
# def update_abstract(
#     article,
#     new_text,
#     #
#     # DATABASE PARAMS:
#     root_dir="./",
# ):
#     """
#     :meta private:
#     """
#
#     records = read_filtered_database(
#         root_dir=root_dir,
#         database="main",
#         year_filter=(None, None),
#         cited_by_filter=(None, None),
#     )
#
#     current_abstract = records.loc[records.article == article, "abstract"]
#     if len(current_abstract) == 0:
#         raise ValueError(f"Article '{article}' not found.")
#
#     if len(current_abstract) > 1:
#         raise ValueError(f"Key '{article}' match multiple records.")
#
#     if not (
#         current_abstract.iloc[0] == "[no abstract available]"
#         or current_abstract.isna().iloc[0]
#     ):
#         raise ValueError(f"Article '{article}' has already an abstract.")
#
#     print("Current abstract:")
#     print(current_abstract.iloc[0])
#
#     records.loc[records.article == article, "abstract"] = new_text
#
#     file_path = os.path.join(root_dir, "databases/_main.csv.zip")
#     records.to_csv(file_path, sep=",", encoding="utf-8", compression="zip")
#
#     print(f"--INFO-- The record {article} was updated.")
#
