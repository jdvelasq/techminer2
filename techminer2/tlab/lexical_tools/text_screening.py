"""
Text screening --- ChatGPT
===============================================================================

This funcion searchs for them specified in the parameter ``search_for`` in the
abstracts of the records and creates a file with the report.

>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> tlab.lexical_tools.text_screening(
...     search_for='regtech',
...     directory=directory,
... )
--INFO-- The file 'data/regtech/processed/text_screening.txt' was created.


"""
from ... import vantagepoint


def text_screening(
    search_for,
    case=False,
    flags=0,
    regex=True,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Generates the file ``text_screening.txt`` with the abstracts matching \
    the search string.

    Parameters
    ----------

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

    database: str ``{"documents", "references", "cited_by"}, by default \
        "documents"``
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

    return vantagepoint.record_display(
        criterion="abstract",
        search_for=search_for,
        report_filename="text_screening.txt",
        case=case,
        flags=flags,
        regex=regex,
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
