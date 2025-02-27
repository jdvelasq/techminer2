# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import sys

from ....._internals.log_message import internal__log_message
from .....thesaurus.organizations import ApplyThesaurus, CreateThesaurus


def internal__preprocess_organizations(root_dir):

    sys.stdout.write("\nINFO  Processing 'organizations' column.")
    sys.stdout.flush()

    CreateThesaurus().update(root_dir=root_dir).build()
    ApplyThesaurus().update(root_dir=root_dir).build()


# =============================================================================
