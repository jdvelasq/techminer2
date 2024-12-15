# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ....prepare.fields.process_field import _process_field


def run_issb_isbn_eissn_importer(root_dir):
    """Run authors importer."""

    for field in ["isbn", "issn", "eissn"]:
        _process_field(
            source=field,
            dest=field,
            func=lambda x: x,
            root_dir=root_dir,
        )
