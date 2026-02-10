"""

Smoke test:
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> # Countries:
    >>> from techminer2.refine.thesaurus_old.countries import InitializeThesaurus, ApplyThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Organizations:
    >>> from techminer2.refine.thesaurus_old.organizations import InitializeThesaurus, ApplyThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Descriptors:
    >>> from techminer2.refine.thesaurus_old.descriptors import InitializeThesaurus, ApplyThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2._internals import Params
    >>> from techminer2.database._internals.io import load_filtered_main_data
    >>> df = (
    ...     load_filtered_main_data(
    ...         Params(
    ...             database="main",
    ...             record_years_range=(None, None),
    ...             record_citations_range=(None, None),
    ...             records_order_by=None,
    ...             records_match=None,
    ...             root_directory="examples/fintech/",
    ...         )
    ...     ).head()
    ... )
    >>> assert isinstance(df, pd.DataFrame)
    >>> assert len(df) > 0
    >>> assert "year" in df.columns
    >>> df # doctest: +SKIP
                        source_title_abbr  ...  year
    0             Int. J. Appl. Eng. Res.  ...  2016
    1                   Telecommun Policy  ...  2016
    3                      China Econ. J.  ...  2016
    4  Contemp. Stud. Econ. Financ. Anal.  ...  2016
    5                    New Polit. Econ.  ...  2017
    <BLANKLINE>
    [5 rows x 80 columns]



"""

import pandas as pd  # type: ignore

from techminer2 import CorpusField, RecordsOrderBy
from techminer2._internals import Params
from techminer2._internals.data_access.load_main_data import load_main_data


def _filter_dataframe_by_year(params: Params, dataframe: pd.DataFrame) -> pd.DataFrame:

    years_range = params.record_years_range

    if years_range is None:
        return dataframe

    if not isinstance(years_range, tuple):
        raise TypeError(
            "The record_years_range parameter must be a tuple of two values."
        )

    if len(years_range) != 2:
        raise ValueError(
            "The record_years_range parameter must be a tuple of two values."
        )

    start_year, end_year = years_range

    if start_year is not None:
        dataframe = dataframe[dataframe.year >= start_year]

    if end_year is not None:
        dataframe = dataframe[dataframe.year <= end_year]

    return dataframe


def _filter_dataframe_by_citations(
    params: Params, dataframe: pd.DataFrame
) -> pd.DataFrame:

    citations_range = params.record_citations_range

    if citations_range is None:
        return dataframe

    if not isinstance(citations_range, tuple):
        raise TypeError(
            "The record_citations_range parameter must be a tuple of two values."
        )

    if len(citations_range) != 2:
        raise ValueError(
            "The record_citations_range parameter must be a tuple of two values."
        )

    cited_by_min, cited_by_max = citations_range

    if cited_by_min is not None:
        dataframe = dataframe[dataframe.global_citations >= cited_by_min]

    if cited_by_max is not None:
        dataframe = dataframe[dataframe.global_citations <= cited_by_max]

    return dataframe


def _filter_dataframe_by_match(params: Params, dataframe: pd.DataFrame) -> pd.DataFrame:

    filters = params.records_match

    if filters is None:
        return dataframe

    for filter_name, filter_value in filters.items():

        if filter_name == CorpusField.REC_ID.value:

            dataframe = dataframe[dataframe["record_id"].isin(filter_value)]

        else:

            # Split the filter value into a list of strings
            database = dataframe[["record_id", filter_name]].copy()
            database.loc[:, filter_name] = database[filter_name].str.split(";")

            # Explode the list of strings into multiple rows
            database = database.explode(filter_name)

            # Remove leading and trailing whitespace from the strings
            database[filter_name] = database[filter_name].str.strip()

            # Keep only records that match the filter value
            database = database[database[filter_name].isin(filter_value)]

            dataframe = dataframe[dataframe["record_id"].isin(database["record_id"])]

    return dataframe


def _sort_dataframe_by(params: Params, dataframe: pd.DataFrame) -> pd.DataFrame:

    sort_by = params.records_order_by

    if sort_by is None:
        return dataframe

    if sort_by == RecordsOrderBy.PUBYEAR_NEWEST:
        dataframe = dataframe.sort_values(
            [
                CorpusField.PUBYEAR.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[False, False, False],
        )
    elif sort_by == RecordsOrderBy.PUBYEAR_OLDEST:
        dataframe = dataframe.sort_values(
            [
                CorpusField.PUBYEAR.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[True, False, False],
        )
    elif sort_by == RecordsOrderBy.CIT_COUNT_GLOBAL_BY_HIGHEST:
        dataframe = dataframe.sort_values(
            [
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.PUBYEAR.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[False, False, False],
        )
    elif sort_by == RecordsOrderBy.CIT_COUNT_GLOBAL_BY_LOWEST:
        dataframe = dataframe.sort_values(
            [
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.PUBYEAR.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[True, False, False],
        )

    elif sort_by == RecordsOrderBy.CIT_COUNT_LOCAL_BY_HIGHEST:
        dataframe = dataframe.sort_values(
            [
                CorpusField.CIT_COUNT_LOCAL.value,
                CorpusField.PUBYEAR.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
            ],
            ascending=[False, False, False],
        )

    elif sort_by == RecordsOrderBy.CIT_COUNT_LOCAL_BY_LOWEST:
        dataframe = dataframe.sort_values(
            [
                CorpusField.CIT_COUNT_LOCAL.value,
                CorpusField.PUBYEAR.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
            ],
            ascending=[True, False, False],
        )

    elif sort_by == RecordsOrderBy.FIRST_AUTH_A_TO_Z:
        dataframe = dataframe.sort_values(
            [
                CorpusField.AUTH_NORM.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[True, False, False],
        )

    elif sort_by == RecordsOrderBy.FIRST_AUTH_Z_TO_A:
        dataframe = dataframe.sort_values(
            [
                CorpusField.AUTH_NORM.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[False, False, False],
        )
    elif sort_by == RecordsOrderBy.SRC_TITLE_A_TO_Z:
        dataframe = dataframe.sort_values(
            [
                CorpusField.SRC_TITLE_NORM.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[True, False, False],
        )

    elif sort_by == RecordsOrderBy.SRE_TITLE_Z_TO_A:
        dataframe = dataframe.sort_values(
            [
                CorpusField.SRC_TITLE_NORM.value,
                CorpusField.CIT_COUNT_GLOBAL.value,
                CorpusField.CIT_COUNT_LOCAL.value,
            ],
            ascending=[False, False, False],
        )
    else:
        raise ValueError(f"Unsupported sort option: {sort_by}")

    columns = sorted(dataframe.columns)
    dataframe = dataframe[columns]

    return dataframe


def load_filtered_main_data(params: Params) -> pd.DataFrame:

    dataframe = load_main_data(root_directory=params.root_directory, usecols=None)
    dataframe = _filter_dataframe_by_year(params, dataframe)
    dataframe = _filter_dataframe_by_citations(params, dataframe)
    dataframe = _filter_dataframe_by_match(params, dataframe)
    dataframe = _sort_dataframe_by(params, dataframe)

    return dataframe
