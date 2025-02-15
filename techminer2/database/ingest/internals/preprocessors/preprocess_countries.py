# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import pathlib
import sys

from .....thesaurus.countries import ApplyThesaurus, ResetThesaurusToInitialState


# -------------------------------------------------------------------------
def internal__preprocess_countries(root_dir):
    """:meta private:"""

    ResetThesaurusToInitialState().update(root_dir=root_dir).build()
    ApplyThesaurus().update(root_dir=root_dir).build()


# =============================================================================
