# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import sys


# -------------------------------------------------------------------------
def internal__preprocess_countries(root_dir):
    """:meta private:"""

    from .....thesaurus.countries import ApplyThesaurus, CreateThesaurus

    sys.stdout.write("\nINFO  Processing 'countries' column.")
    sys.stdout.flush()

    th = CreateThesaurus()
    th.update(root_dir=root_dir)
    th.build()

    th = ApplyThesaurus()
    th.update(root_dir=root_dir)
    th.build()


# =============================================================================
