# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus


def _preprocess_descriptors(root_directory):

    sys.stderr.write("INFO: Creating 'descriptors' column\n")
    sys.stderr.flush()

    InitializeThesaurus(root_directory=root_directory).run()
    ApplyThesaurus(root_directory=root_directory).run()


#
