# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
import sys

from techminer2.thesaurus.organizations import ApplyThesaurus, InitializeThesaurus


def normalize_organizations(root_directory: str) -> int:

    sys.stderr.write("INFO: Creating 'organizations' column\n")
    sys.stderr.flush()

    InitializeThesaurus(root_directory=root_directory).run()
    ApplyThesaurus(root_directory=root_directory).run()

    return 0


# =============================================================================
