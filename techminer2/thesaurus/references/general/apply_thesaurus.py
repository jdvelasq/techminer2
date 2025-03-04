# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Apply Thesaurus 
===============================================================================


>>> #
>>> # TEST PREPARATION:
>>> #
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> # CODE:
>>> #
>>> from techminer2.thesaurus.references import ApplyThesaurus
>>> ApplyThesaurus(root_directory="example/").run()
>>> #
>>> # TEST EXECUTION:
>>> #
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Applying user thesaurus to database
          File : example/thesaurus/references.the.txt
  Source field : raw_global_references
  Target field : global_references
  Thesaurus application completed successfully
<BLANKLINE>
<BLANKLINE>



"""

from ...._internals.mixins import ParamsMixin
from ..._internals import ThesaurusMixin
from ...user import ApplyThesaurus as ApplyUserThesaurus


#
#
class ApplyThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    def run(self):

        ApplyUserThesaurus(
            thesaurus_file="references.the.txt",
            field="raw_global_references",
            other_field="global_references",
            root_directory=self.params.root_directory,
        ).run()


# def _apply_thesaurus(root_dir):
#     # Apply the thesaurus to raw_global_references

#     file_path = pathlib.Path(root_dir) / "thesaurus/references.the.txt"
#     th = internal__load_reversed_thesaurus_as_mapping(file_path=file_path)

#     dataframe = pd.read_csv(
#         pathlib.Path(root_dir) / "databases/database.csv.zip",
#         encoding="utf-8",
#         compression="zip",
#     )

#     # creates a list of references
#     dataframe["global_references"] = dataframe["raw_global_references"].str.split("; ")

#     # replace the oriignal references by the record_id
#     dataframe["global_references"] = dataframe["global_references"].map(
#         lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
#     )
#     dataframe["global_references"] = dataframe["global_references"].map(
#         lambda x: pd.NA if x == [] else x, na_action="ignore"
#     )
#     dataframe["global_references"] = dataframe["global_references"].map(
#         lambda x: "; ".join(sorted(x)) if isinstance(x, list) else x
#     )

#     dataframe.to_csv(
#         pathlib.Path(root_dir) / "databases/database.csv.zip",
#         sep=",",
#         encoding="utf-8",
#         index=False,
#         compression="zip",
#     )
