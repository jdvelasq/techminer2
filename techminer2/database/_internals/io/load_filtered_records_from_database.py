# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""


>>> #
>>> # TEST PREPARATION
>>> #
>>> # Countries:
>>> from techminer2.thesaurus.countries import CreateThesaurus, ApplyThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()
>>> ApplyThesaurus(root_directory="example/", quiet=True).run()

>>> # Organizations:
>>> from techminer2.thesaurus.organizations import CreateThesaurus, ApplyThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()
>>> ApplyThesaurus(root_directory="example/", quiet=True).run()

>>> # Descriptors:
>>> from techminer2.thesaurus.descriptors import CreateThesaurus, ApplyThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()
>>> ApplyThesaurus(root_directory="example/", quiet=True).run()

>>> #
>>> # CODE TESTED
>>> #
>>> from techminer2._internals.params_mixin import Params
>>> from techminer2.database._internals.io import internal__load_filtered_database
>>> (
...     internal__load_filtered_database(
...         Params(
...             database="main",
...             record_years_range=(None, None),
...             record_citations_range=(None, None),
...             records_order_by=None,
...             records_match=None,
...             root_directory="example/",
...         )
...     ).head()
... ) # doctest: +ELLIPSIS
                       abbr_source_title  ...  year
934              Int. J. Appl. Eng. Res.  ...  2016
935                    Telecommun Policy  ...  2016
1031                      China Econ. J.  ...  2016
1059  Contemp. Stud. Econ. Financ. Anal.  ...  2016
1075                    New Polit. Econ.  ...  2017
<BLANKLINE>
[5 rows x 75 columns]



"""
import pandas as pd  # type: ignore

from .get_database_file_path import internal__get_database_file_path


def internal__load_filtered_records_from_database(params):

    # -------------------------------------------------------------------------
    def step_01_get_records_from_file(params):

        file_path = internal__get_database_file_path(params)

        data_frame = pd.read_csv(
            file_path,
            encoding="utf-8",
            compression="zip",
        )

        criteria = {
            "main": "db_main",
            "references": "db_references",
            "cited_by": "db_cited_by",
        }[params.database]

        data_frame = data_frame[data_frame[criteria]]

        return data_frame

    # -------------------------------------------------------------------------
    def step_02_filter_records_by_year(params, data_frame):

        years_range = params.record_years_range

        if years_range is None:
            return data_frame

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
            data_frame = data_frame[data_frame.year >= start_year]

        if end_year is not None:
            data_frame = data_frame[data_frame.year <= end_year]

        return data_frame

    # -------------------------------------------------------------------------
    def step_03_filter_records_by_citations(params, data_frame):

        citations_range = params.record_citations_range

        if citations_range is None:
            return data_frame

        if not isinstance(citations_range, tuple):
            raise TypeError(
                "The record_years_range parameter must be a tuple of two values."
            )

        if len(citations_range) != 2:
            raise ValueError(
                "The record_years_range parameter must be a tuple of two values."
            )

        cited_by_min, cited_by_max = citations_range

        if cited_by_min is not None:
            data_frame = data_frame[data_frame.global_citations >= cited_by_min]

        if cited_by_max is not None:
            data_frame = data_frame[data_frame.global_citations <= cited_by_max]

        return data_frame

    # -------------------------------------------------------------------------
    def step_04_apply_filters_to_records(params, data_frame):

        filters = params.records_match

        if filters is None:
            return data_frame

        for filter_name, filter_value in filters.items():

            if filter_name == "record_id":

                data_frame = data_frame[data_frame["record_id"].isin(filter_value)]

            else:

                # Split the filter value into a list of strings
                database = data_frame[["record_id", filter_name]].copy()
                database.loc[:, filter_name] = database[filter_name].str.split(";")

                # Explode the list of strings into multiple rows
                database = database.explode(filter_name)

                # Remove leading and trailing whitespace from the strings
                database[filter_name] = database[filter_name].str.strip()

                # Keep only records that match the filter value
                database = database[database[filter_name].isin(filter_value)]

                data_frame = data_frame[
                    data_frame["record_id"].isin(database["record_id"])
                ]

        return data_frame

    # -------------------------------------------------------------------------
    def step_05_apply_sort_by(params, data_frame):
        #
        # sort_by: - date_newest
        #          - date_oldest
        #          - global_cited_by_highest
        #          - global_cited_by_lowest
        #          - local_cited_by_highest
        #          - local_cited_by_lowest
        #          - first_author_a_to_z
        #          - first_author_z_to_a
        #          - source_title_a_to_z
        #          - source_title_z_to_a
        #

        sort_by = params.records_order_by

        if sort_by is None:
            return data_frame

        if sort_by == "date_newest":
            data_frame = data_frame.sort_values(
                ["year", "global_citations", "local_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "date_oldest":
            data_frame = data_frame.sort_values(
                ["year", "global_citations", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "global_cited_by_highest":
            data_frame = data_frame.sort_values(
                ["global_citations", "year", "local_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "global_cited_by_lowest":
            data_frame = data_frame.sort_values(
                ["global_citations", "year", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "local_cited_by_highest":
            data_frame = data_frame.sort_values(
                ["local_citations", "year", "global_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "local_cited_by_lowest":
            data_frame = data_frame.sort_values(
                ["local_citations", "year", "global_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "first_author_a_to_z":
            data_frame = data_frame.sort_values(
                ["authors", "global_citations", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "first_author_z_to_a":
            data_frame = data_frame.sort_values(
                ["authors", "global_citations", "local_citations"],
                ascending=[False, False, False],
            )

        if sort_by == "source_title_a_to_z":
            data_frame = data_frame.sort_values(
                ["source_title", "global_citations", "local_citations"],
                ascending=[True, False, False],
            )

        if sort_by == "source_title_z_to_a":
            data_frame = data_frame.sort_values(
                ["source_title", "global_citations", "local_citations"],
                ascending=[False, False, False],
            )

        columns = sorted(data_frame.columns)
        data_frame = data_frame[columns]

        return data_frame

    # -------------------------------------------------------------------------

    data_frame = step_01_get_records_from_file(params)
    data_frame = step_02_filter_records_by_year(params, data_frame)
    data_frame = step_03_filter_records_by_citations(params, data_frame)
    data_frame = step_04_apply_filters_to_records(params, data_frame)
    data_frame = step_05_apply_sort_by(params, data_frame)

    return data_frame
