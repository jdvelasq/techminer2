# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import sys


def internal__preprocess_organizations(root_directory):

    from .....thesaurus.organizations import ApplyThesaurus, CreateThesaurus

    sys.stderr.write("INFO  Creating 'organizations' column\n")
    sys.stderr.flush()

    CreateThesaurus(root_directory=root_directory).run()
    ApplyThesaurus(root_directory=root_directory).run()


# =============================================================================
