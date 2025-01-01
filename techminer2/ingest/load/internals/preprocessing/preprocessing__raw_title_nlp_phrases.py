# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....internals.transformations.transformations__extract_noun_phrases import (
    transformations__extract_noun_phrases,
)


def preprocessing__raw_title_nlp_phrases(root_dir):

    transformations__extract_noun_phrases(
        source="document_title",
        dest="raw_title_nlp_phrases",
        root_dir=root_dir,
    )
