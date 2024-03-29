# """
# Create Thesaurus
# ===============================================================================

# >>> from techminer2 import *
# >>> root_dir = "data/regtech/"

# >>> from techminer2 import vantagepoint
# >>> vantagepoint.refine.create_thesaurus(
# ...     criterion="author_keywords",
# ...     output_file="test_keywords.txt",
# ...     root_dir=root_dir,
# ... )
# --INFO-- Creating a thesaurus file from `author_keywords` column in all \
# databases
# --INFO-- The thesaurus file `test_keywords.txt` was created


# """
# import glob
# import os
# import os.path
# import sys

# import pandas as pd

# # from ..._thesaurus import Thesaurus, load_file_as_dict, text_clustering


# def create_thesaurus(
#     criterion,
#     output_file=None,
#     root_dir="./",
# ):
#     """Create a thesaurus from a column of a dataframe."""

#     if output_file is None:
#         output_file = criterion + ".txt"

#     output_file_path = os.path.join(root_dir, "processed", output_file)

#     words_list = []
#     files = list(glob.glob(os.path.join(root_dir, "processed/_*.csv")))
#     for file in files:
#         data = pd.read_csv(file, encoding="utf-8")
#         if criterion in data.columns:
#             words_list += data[criterion].tolist()
#     if len(words_list) == 0:
#         sys.stdout.write(
#             f"--ERROR-- Column '{criterion}' do not exists in any database or "
#             "it is empty\n"
#         )
#         return

#     sys.stdout.write(
#         f"--INFO-- Creating a thesaurus file from `{criterion}` column in all "
#         "databases\n"
#     )

#     words_list = pd.Series(words_list)
#     words_list = words_list.dropna()

#     words_list = words_list.str.split(";")
#     words_list = words_list.explode()

#     if os.path.isfile(output_file_path):
#         #
#         # Loads existent thesaurus
#         #
#         dict_ = load_file_as_dict(output_file_path)
#         clustered_words = [word for key in dict_.keys() for word in dict_[key]]
#         words_list = [
#             word for word in words_list if word not in clustered_words
#         ]

#         if len(words_list) > 0:
#             th_ = text_clustering(pd.Series(words_list))

#             th_ = Thesaurus(
#                 x={**th_._thesaurus, **dict_},
#                 ignore_case=True,
#                 full_match=False,
#                 use_re=False,
#             )
#             th_.to_textfile(output_file_path)
#     else:
#         #
#         # Creates a new thesaurus
#         #
#         text_clustering(pd.Series(words_list)).to_textfile(output_file_path)

#     sys.stdout.write(
#         f"--INFO-- The thesaurus file `{output_file}` was created\n"
#     )
