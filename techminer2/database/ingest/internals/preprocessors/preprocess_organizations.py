# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches


from .....internals.log_message import internal__log_message
from .....thesaurus.organizations import ApplyThesaurus, ResetThesaurusToInitialState


def internal__preprocess_organizations(root_dir):

    internal__log_message(
        msgs="Processing 'organizations' column.",
        prompt_flag=True,
    )

    ResetThesaurusToInitialState().update(root_dir=root_dir).with_prompt_flag(
        -1
    ).build()
    ApplyThesaurus().update(root_dir=root_dir).with_prompt_flag(-1).build()


# =============================================================================
