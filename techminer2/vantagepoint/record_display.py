"""
Record Display
===============================================================================

Extracts documents from the databaase containing the text string specified by
the parameter ``search_for`` in the column specified by the parameter
``criterion``. This functions allows the use of regular expressions for
searching. The report is saved to the file ``processed/record_display.txt``.

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.record_display(
...     criterion='author_keywords',
...     search_for='regtech',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/processed/record_display.txt' was created.

"""


from ..utils import records


# pylint: disable=too-many-arguments
def record_display(
    criterion,
    search_for,
    case=False,
    flags=0,
    regex=True,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    report_filename="record_display.txt",
    **filters,
):
    """Record display the documents matching the specied sarch criteria.

    Args:
        criterion (str): Criterion to be used to generate the terms.
        search_for (str): Text string to be searched.
        case (bool, optional): If True, the search is case sensitive. Defaults
            to False.
        flags (int, optional): Flags to be used in the search. Defaults to 0.
        regex (bool, optional): If True, the search is performed using regular
            expressions. Defaults to True.
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database to be used. Defaults to "documents".
        start_year (int, optional): Start year. Defaults to None.
        end_year (int, optional): End year. Defaults to None.
        report_filename (str, optional): Name of the report file. Defaults to
            "record_display.txt".
        filters (dict, optional): Filters to be applied to the database.
            Defaults to {}.

    Returns:
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

    records = records.read_records(
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = filter_records(
        criterion, search_for, case, flags, regex, records
    )

    records.create_records_report(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename=report_filename,
    )
