# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
import sys


def internal__preprocess_global_references(root_directory):
    """:meta private:"""

    from techminer2.thesaurus.references import ApplyThesaurus, InitializeThesaurus

    sys.stderr.write("INFO: Processing 'references' column\n")
    sys.stderr.flush()

    InitializeThesaurus(root_directory=root_directory).run()
    ApplyThesaurus(root_directory=root_directory).run()


#
