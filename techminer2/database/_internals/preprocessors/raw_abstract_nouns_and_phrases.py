# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys


def internal__preprocess_raw_abstract_nouns_and_phrases(root_dir):

    from techminer2.database._internals.operators.collect import internal__collect

    sys.stderr.write("INFO: Collecting raw noun and phrases from abstract\n")
    sys.stderr.flush()

    internal__collect(
        source="abstract",
        dest="raw_abstract_nouns_and_phrases",
        root_dir=root_dir,
    )


#
