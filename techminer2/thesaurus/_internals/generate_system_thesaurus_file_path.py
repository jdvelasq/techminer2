# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
import pathlib
from importlib.resources import files


def internal__generate_system_thesaurus_file_path(thesaurus_file):

    file_path = files("techminer2.package_data.thesaurus").joinpath(thesaurus_file)
    file_path = str(file_path)
    return file_path
