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


def internal__system_user_thesaurus_file_path(file_name):
    internal_path_to_file = pathlib.Path("package_data/thesaurus/") / file_name
    file_path = pkg_resources.resource_filename("techminer2", internal_path_to_file)
    return file_path
