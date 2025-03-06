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
import sys

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

    #
    # NOTIFICATIONS:
    # -------------------------------------------------------------------------
    def internal__notify_process_start(self):

        if not self.params.quiet:

            file_path = str(self.thesaurus_path)
            field = self.params.field
            other_field = self.params.other_field

            if len(file_path) > 64:
                file_path = "..." + file_path[-60:]

            sys.stderr.write("Applying user thesaurus to database\n")
            sys.stderr.write(f"          File : {file_path}\n")
            sys.stderr.write(f"  Source field : {field}\n")
            sys.stderr.write(f"  Target field : {other_field}\n")
            sys.stderr.flush()

    # -------------------------------------------------------------------------
    def internal__notify_process_end(self):

        if not self.params.quiet:

            sys.stderr.write(f"  Thesaurus application completed successfully\n\n")
            sys.stderr.flush()

    #
    # ALGORITHM:
    # -------------------------------------------------------------------------
    def internal__load_records(self):
        self.records = internal__load_records(params=self.params)

    # -------------------------------------------------------------------------
    def internal__apply_thesaurus(self):

        field = self.params.field
        other_field = self.params.other_field

        # creates a list of references
        self.records[other_field] = self.records[field].str.split("; ")

        # replace the oriignal references by the record_id
        self.records[other_field] = self.records[other_field].map(
            lambda x: [self.mapping[t] for t in x if t in self.mapping.keys()],
            na_action="ignore",
        )
        self.records[other_field] = self.records[other_field].map(
            lambda x: pd.NA if x == [] else x, na_action="ignore"
        )
        self.records[other_field] = self.records[other_field].map(
            lambda x: "; ".join(sorted(x)) if isinstance(x, list) else x
        )

    # -------------------------------------------------------------------------
    def internal__write_records_to_file(self):
        internal__write_records(params=self.params, records=self.records)

    # -------------------------------------------------------------------------
    def run(self):

        self.params.thesaurus_file = "references.the.txt"
        self.params.field = "raw_global_references"
        self.params.other_field = "global_references"

        self.internal__build_user_thesaurus_path()
        self.internal__notify_process_start()
        self.internal__load_reversed_thesaurus_as_mapping()
        self.internal__load_records()
        self.internal__apply_thesaurus()
        self.internal__write_records_to_file()
        self.internal__notify_process_end()
