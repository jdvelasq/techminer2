# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""Search for acronyms in a thesaurus."""
import sys


def internal__preprocess_acronyms(root_dir):

    from techminer2.thesaurus.acronyms import InitializeThesaurus

    sys.stderr.write("INFO: Preprocessing acronyms\n")
    sys.stderr.flush()

    InitializeThesaurus(root_directory=root_dir).run()


#
