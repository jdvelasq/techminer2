# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import pathlib

import pkg_resources  # type: ignore


def internal__generate_system_thesaurus_file_path(thesaurus_file):
    internal_file_path = pathlib.Path("package_data/thesaurus/") / thesaurus_file
    internal_file_path = str(internal_file_path)
    file_path = pkg_resources.resource_filename("techminer2", internal_file_path)
    return file_path
