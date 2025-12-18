# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=attribute-defined-outside-init
"""
Get Values
===============================================================================


Example:
    >>> # Redirecting stderr to avoid messages during doctests
    >>> import sys
    >>> from io import StringIO
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()

    >>> # Reset the thesaurus to initial state
    >>> from techminer2.thesaurus.user import InitializeThesaurus
    >>> InitializeThesaurus(thesaurus_file="demo.the.txt", field="raw_descriptors",
    ...     root_directory="examples/fintech/", quiet=True).run()

    >>> # Creates, configures, an run the exploder
    >>> from techminer2.thesaurus.user import GetValues
    >>> terms = (
    ...     GetValues()
    ...     .with_thesaurus_file("demo.the.txt")
    ...     .with_patterns(["FINTECH", "FINANCIAL_TECHNOLOGIES"])
    ...     .where_root_directory_is("examples/fintech/")
    ...     .run()
    ... )
    >>> terms[:5]
    ['FINANCIAL_TECHNOLOGIES', 'FINANCIAL_TECHNOLOGY', 'FINTECH', 'FINTECHS']


    # >>> # Capture and print stderr output to test the code using doctest
    # >>> output = sys.stderr.getvalue()
    # >>> sys.stderr = original_stderr
    # >>> print(output) # doctest: +SKIP


"""
import sys

from techminer2._internals import ParamsMixin
from techminer2.thesaurus._internals import ThesaurusMixin


class GetValues(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__get_values(self):
        self.data_frame = self.data_frame[
            self.data_frame["key"].isin(self.params.pattern)
        ].copy()
        values = self.data_frame["value"].to_list()
        values = [t.strip() for v in values for t in v.split("; ")]
        self.values = values

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        if self.params.quiet is False:
            sys.stderr.write("Getting thesaurus values...\n")
            sys.stderr.flush()

        self.internal__build_user_thesaurus_path()
        self.internal__load_thesaurus_as_mapping()
        self.internal__transform_mapping_to_data_frame()
        self.internal__get_values()

        if self.params.quiet is False:
            sys.stderr.write("Getting thesaurus values completed successfully\n")
            sys.stderr.flush()

        return self.values
