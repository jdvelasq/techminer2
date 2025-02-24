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

## >>> from techminer2.thesaurus.references import ApplyThesaurus
## >>> (
## ...     ApplyThesaurus()
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The example/global_references.txt thesaurus file was applied to global_references in 'main' database

"""

from ..._internals.mixins import ParamsMixin
from ..user.apply_thesaurus import ApplyThesaurus as ApplyUserThesaurus


#
#
class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):

        # Affiliations to countries mmapping
        (
            ApplyUserThesaurus()
            .with_thesaurus_file("references.the.txt")
            .with_field("raw_global_references")
            .with_other_field("global_references")
            .where_directory_is(self.params.root_dir)
            .build()
        )


# def _apply_thesaurus(root_dir):
#     # Apply the thesaurus to raw_global_references

#     file_path = pathlib.Path(root_dir) / "thesaurus/global_references.the.txt"
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
