# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.merge_database_fields import fields__merge


def preprocessing__raw_nlp_phrases(root_dir):

    fields__merge(
        sources=["raw_title_nlp_phrases", "raw_abstract_nlp_phrases"],
        dest="raw_nlp_phrases",
        root_dir=root_dir,
    )
