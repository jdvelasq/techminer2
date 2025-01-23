# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ....load import load__user_stopwords


def internal__remove_stopwords_from_axis(
    dataframe,
    root_dir,
    axis,
):
    stopwords = load__user_stopwords(root_dir=root_dir)
    dataframe = dataframe.drop(stopwords, axis=axis, errors="ignore")
    # dataframe = dataframe.drop(field, axis=1)
    return dataframe
