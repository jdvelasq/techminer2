"""
Text Screening --- ChatGPT
===============================================================================

This funcion searchs for them specified in the parameter ``search_for`` in the
abstracts of the records and creates a file with the report.

>>> root_dir = "data/regtech/"

>>> from techminer2 import tlab
>>> tlab.lexical_tools.text_screening(
...     search_for='regtech',
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/processed/text_screening.txt' was created.


"""
import inspect

from ...vantagepoint import record_display


# pylint: disable=too-many-arguments
# pylint: disable=W0613
def text_screening(
    search_for,
    case=False,
    flags=0,
    regex=True,
    root_dir="./",
    database="documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Generates the file ``text_screening.txt`` with the abstracts matching \
    the search string.

    Args:
        search_for (str): string to be searched in the abstracts.
        case (bool): if True, the search is case sensitive.
        flags (int): flags for the regular expression search.
        regex (bool): if True, the search string is a regular expression.
        root_dir (str): root directory.
        database (str): database name.
        start_year (int): start year.
        end_year (int): end year.
        **filters: filters.

    Returns:
        None

    """

    param_names = [
        key
        for key in inspect.signature(text_screening).parameters.keys()
        if key not in ["self", "filters"]
    ]

    local_vars = locals()
    params = {key: local_vars[key] for key in param_names}

    record_display(
        **{
            **{
                "field": "abstract",
                "report_filename": "text_screening.txt",
            },
            **params,
            **filters,
        }
    )

    # return record_display(
    #     field="abstract",
    #     search_for=search_for,
    #     report_filename="text_screening.txt",
    #     case=case,
    #     flags=flags,
    #     regex=regex,
    #     root_dir=root_dir,
    #     database=database,
    #     start_year=start_year,
    #     end_year=end_year,
    #     **filters,
    # )
