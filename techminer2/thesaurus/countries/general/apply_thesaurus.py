# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Apply Thesaurus
===============================================================================

Example:
    >>> import sys
    >>> from io import StringIO
    >>> from techminer2.thesaurus.countries import ApplyThesaurus, InitializeThesaurus

    >>> # Redirect stderr to capture output
    >>> original_stderr = sys.stderr
    >>> sys.stderr = StringIO()


    >>> # Create and apply the thesaurus
    >>> InitializeThesaurus(root_directory="example/", quiet=True).run()
    >>> ApplyThesaurus(use_colorama=False).where_root_directory_is("examples/fintech/").run()

    >>> # Capture and print stderr output
    >>> output = sys.stderr.getvalue()
    >>> sys.stderr = original_stderr
    >>> print(output)
    Applying user thesaurus to database...
              File : example/data/thesaurus/countries.the.txt
      Source field : affiliations
      Target field : countries
      Application process completed successfully
    <BLANKLINE>
    Applying system thesaurus to database...
              File : ...2/package_data/thesaurus/geography/country_to_region.the.txt
      Source field : countries
      Target field : regions
      Application process completed successfully
    <BLANKLINE>
    Applying system thesaurus to database...
              File : ...ackage_data/thesaurus/geography/country_to_subregion.the.txt
      Source field : countries
      Target field : subregions
      Application process completed successfully
    <BLANKLINE>
    <BLANKLINE>

    >>> # Query the database to verify the results
    >>> from techminer2.tools import Query
    >>> result = Query(
    ...     query_expression="SELECT countries FROM database LIMIT 10;",
    ...     root_directory="example/",
    ...     database="main",
    ...     record_years_range=(None, None),
    ...     record_citations_range=(None, None),
    ... ).run()
    >>> print(result)
                       countries
    0                South Korea
    1                South Korea
    2                      China
    3                     Latvia
    4             United Kingdom
    5       United States; China
    6                Switzerland
    7  Australia; Denmark; China
    8                Switzerland
    9                    Germany

    >>> result = Query(
    ...     query_expression="SELECT regions FROM database LIMIT 10;",
    ...     root_directory="example/",
    ...     database="main",
    ...     record_years_range=(None, None),
    ...     record_citations_range=(None, None),
    ... ).run()
    >>> print(result)
                     regions
    0                   Asia
    1                   Asia
    2                   Asia
    3                 Europe
    4                 Europe
    5         Americas; Asia
    6                 Europe
    7  Oceania; Europe; Asia
    8                 Europe
    9                 Europe

    >>> result = Query(
    ...     query_expression="SELECT subregions FROM database LIMIT 10;",
    ...     root_directory="example/",
    ...     database="main",
    ...     record_years_range=(None, None),
    ...     record_citations_range=(None, None),
    ... ).run()
    >>> print(result)
                                              subregions
    0                                       Eastern Asia
    1                                       Eastern Asia
    2                                       Eastern Asia
    3                                    Northern Europe
    4                                    Northern Europe
    5                     Northern America; Eastern Asia
    6                                     Western Europe
    7  Australia and New Zealand; Northern Europe; Ea...
    8                                     Western Europe
    9                                     Western Europe


"""
from ...._internals.mixins import ParamsMixin
from ....database.ingest._internals.operators.transform_field import (
    internal__transform_field,
)
from ...system import ApplyThesaurus as ApplySystemThesaurus
from ...user import ApplyThesaurus as ApplyUserThesaurus


class ApplyThesaurus(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        # Affiliations to countries mmapping
        ApplyUserThesaurus().update(**self.params.__dict__).update(
            thesaurus_file="countries.the.txt",
            field="affiliations",
            other_field="countries",
            root_directory=self.params.root_directory,
            quiet=self.params.quiet,
        ).run()

        # Country of first author
        internal__transform_field(
            #
            # FIELD:
            field="countries",
            other_field="country_1st_author",
            function=lambda x: x.str.split("; ").str[0],
            root_dir=self.params.root_directory,
        )

        # Country to region mapping
        ApplySystemThesaurus().update(**self.params.__dict__).update(
            thesaurus_file="geography/country_to_region.the.txt",
            field="countries",
            other_field="regions",
            root_directory=self.params.root_directory,
            quiet=self.params.quiet,
        ).run()

        # Country to subregion mapping
        ApplySystemThesaurus().update(**self.params.__dict__).update(
            thesaurus_file="geography/country_to_subregion.the.txt",
            field="countries",
            other_field="subregions",
            root_directory=self.params.root_directory,
            quiet=self.params.quiet,
        ).run()
