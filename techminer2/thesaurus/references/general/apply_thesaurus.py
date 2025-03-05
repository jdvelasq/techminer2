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
>>> # TEST PREPARATION
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
>>> # TEST EXECUTION
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
import pathlib

import pandas as pd

from ...._internals.mixins import ParamsMixin
from ....database._internals.io import internal__load_records, internal__write_records
from ..._internals import ThesaurusMixin, internal__load_reversed_thesaurus_as_mapping


#
#
class ApplyThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    def run(self):

        root_directory = self.params.root_directory

        file_path = pathlib.Path(root_directory) / "thesaurus/references.the.txt"
        th = internal__load_reversed_thesaurus_as_mapping(file_path=file_path)

        records = internal__load_records(self.params)

        # creates a list of references
        records["global_references"] = records["raw_global_references"].str.split("; ")

        # replace the oriignal references by the record_id
        records["global_references"] = records["global_references"].map(
            lambda x: [th[t] for t in x if t in th.keys()], na_action="ignore"
        )
        records["global_references"] = records["global_references"].map(
            lambda x: pd.NA if x == [] else x, na_action="ignore"
        )
        records["global_references"] = records["global_references"].map(
            lambda x: "; ".join(sorted(x)) if isinstance(x, list) else x
        )

        internal__write_records(params=self.params, records=records)
