# flake8: noqa
"""
Record Display
===============================================================================

Extracts documents from the databaase containing the text string specified by
the parameter ``search_for`` in the column specified by the parameter
``field``. This functions allows the use of regular expressions for
searching. The report is saved to the file ``processed/record_display.txt``.

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.record_display(
...     field='author_keywords',
...     search_for='regtech',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/processed/record_display.txt' was created.


>>> vantagepoint.record_display(
...     field='abstract',
...     search_for='five-year',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/processed/record_display.txt' was created.



>>> vantagepoint.record_display(
...     field='abstract',
...     search_for='anti',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/processed/record_display.txt' was created.


# pylint: disable=line-too-long
"""


from ..record_utils import create_records_report, read_records


# pylint: disable=too-many-arguments
def record_display(
    field,
    search_for,
    case=False,
    flags=0,
    regex=True,
    report_filename="record_display.txt",
    # Database options:
    root_dir="./",
    database="main",
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Record display the documents matching the specied sarch criteria.

    Args:
        field (str): column to be used to generate the terms.
        search_for (str): Text string to be searched.
        case (bool, optional): If True, the search is case sensitive. Defaults to False.
        flags (int, optional): Flags to be used in the search. Defaults to 0.
        regex (bool, optional): If True, the search is performed using regular expressions. Defaults to True.
        report_filename (str, optional): Name of the report file. Defaults to "record_display.txt".
        root_dir (str, optional): Root directory. Defaults to "./".
        database (str, optional): Database to be used. Defaults to "documents".
        year_filter (tuple, optional): Year database filter. Defaults to None.
        cited_by_filter (tuple, optional): Cited by database filter. Defaults to None.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.


    Returns:
        None

    # pylint: disable=line-too-long
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
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = filter_records(field, search_for, case, flags, regex, records)

    create_records_report(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename=report_filename,
    )
