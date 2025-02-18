# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Reset Thesaurus to Initial State
===============================================================================


## >>> from techminer2.thesaurus.user import ResetThesaurusToInitialState
## >>> (
## ...     ResetThesaurusToInitialState()
## ...     # 
## ...     # THESAURUS:
## ...     .with_thesaurus_file("descriptors.the.txt")
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     #
## ...     .build()
## ... )
--INFO-- The thesaurus file 'example/thesaurus/descriptors.the.txt' has been reseted.

"""
import sys

from ...internals.log_message import internal__log_message
from ...internals.mixins import ParamsMixin
from .._internals import (
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)


class ResetThesaurusToInitialState(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def build_new_th_dict(self, th_dict):
        new_th_dict = {}
        for _, values in th_dict.items():
            for value in values:
                new_th_dict[value] = [value]
        return new_th_dict

    # -------------------------------------------------------------------------
    def save_thesaurus(self, file_path, th_dict):
        sorted_keys = sorted(th_dict.keys())
        with open(file_path, "w", encoding="utf-8") as file:
            for key in sorted_keys:
                file.write(key + "\n")
                for item in sorted(set(th_dict[key])):
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        #
        # LOG:
        internal__log_message(
            msgs=[
                "Reseting thesaurus to initial state.",
                "  Thesaurus file: '{file_path}'.",
            ],
            prompt_flag=self.params.prompt_flag,
        )
        #
        th_dict = internal__load_thesaurus_as_mapping(file_path)
        new_th_dict = self.build_new_th_dict(th_dict)
        self.save_thesaurus(file_path, new_th_dict)
        #
        # LOG:
        internal__log_message(
            msgs="  Done.",
            prompt_flag=-1,
        )


# =============================================================================
