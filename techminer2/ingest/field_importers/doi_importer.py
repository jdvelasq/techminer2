# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...fields.process_field import _process_field


def run_doi_importer(root_dir):
    """Run authors importer."""

    #                                    10.7667/PSPC180358
    #                   10.7688/j.issn.1000-1646.2014.02.06
    #   https://doi.org/10.7688/j.issn.1000-1646.2014.02.06
    # http://dx.doi.org/10.7688/j.issn.1000-1646.2014.02.06

    _process_field(
        source="doi",
        dest="doi",
        func=lambda x: x.str.replace("https://doi.org/", "")
        .str.replace("http://dx.doi.org/", "")
        .str.upper(),
        root_dir=root_dir,
    )
