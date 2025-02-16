# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

from .....internals.log_message import internal__log_message
from .....thesaurus.countries import ApplyThesaurus, ResetThesaurusToInitialState


# -------------------------------------------------------------------------
def internal__preprocess_countries(root_dir):
    """:meta private:"""

    internal__log_message(
        msgs="Processing 'countries' column.",
        counter_flag=True,
    )

    th = ResetThesaurusToInitialState()
    th.update(root_dir=root_dir)
    th.with_counter_flag(-1)
    th.build()

    th = ApplyThesaurus()
    th.update(root_dir=root_dir)
    th.with_counter_flag(-1)
    th.build()


# =============================================================================
