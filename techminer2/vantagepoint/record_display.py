"""
Record display --- ChatGPT
===============================================================================

Extracts documents from the databaase containing the text string specified by
the parameter ``search_for`` in the column specified by the parameter
``criterion``. This functions allows the use of regular expressions for
searching. The report is saved to the file ``processed/record_display.txt``.

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.record_display(
...     criterion='author_keywords',
...     search_for='regtech',
...     directory=directory,
... )
--INFO-- The file 'data/regtech/processed/record_display.txt' was created.

"""

from .._read_records import read_records
from ..build_records_report import build_records_report


def record_display(
    criterion,
    search_for,
    case=False,
    flags=0,
    regex=True,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    report_filename="record_display.txt",
    **filters,
):
    """Record display the documents matching the specied sarch criteria.

    Parameters
    ----------
    criterion: str
        The column name to be searched.

    search_for: str
        The string to be searched.

    case: bool
        If True, the search is case sensitive.

    flags: int
        Flags to be passed to the ``re`` module.

    regex: bool
        If True, the search string is a regular expression.

    directory: str
        The root directory of the project.

    database: str ``{"documents", "references", "cited_by"}, by default "documents"``
        The database name.

    start_year: int or None, optional
        The start year to be considered.

    end_year: int or None, optional

    filters: dict
        The filters to be applied to the database.

    Returns
    -------
    None






    """

    def filter_records(criterion, search_for, case, flags, regex, records):
        """Filter records by the specified criteria."""

        records = records.copy()
        contains = records[criterion].str.contains(
            search_for, case=case, flags=flags, regex=regex
        )
        contains = contains.dropna()
        contains = contains[contains]
        records = records.loc[contains.index, :]

        return records

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = filter_records(
        criterion, search_for, case, flags, regex, records
    )

    build_records_report(
        directory=directory,
        target_dir="",
        records=records,
        report_filename=report_filename,
    )
