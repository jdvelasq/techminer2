# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.transformations.extract_noun_phrases import _extract_noun_phrases


def preprocessing__raw_title_nlp_phrases(root_dir):

    _extract_noun_phrases(
        source="document_title",
        dest="raw_title_nlp_phrases",
        root_dir=root_dir,
    )
