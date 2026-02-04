# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

"""
Combine Keys
===============================================================================

Example:
    >>> # Preparation
    >>> from techminer2.thesaurus_old.descriptors import InitializeThesaurus
    >>> from techminer2.thesaurus_old.descriptors import ApplyThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> # Use
    >>> from techminer2.thesaurus_old.descriptors import CombineKeys
    >>> df = (
    ...     CombineKeys()
    ...     #
    ...     # FIELD:
    ...     .with_field_pattern('FINTECH')
    ...     .having_terms_in_top(30)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(2, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head()  # doctest: +SKIP
           rows                 columns  probability combine?
    3   FINTECH            TECHNOLOGIES        0.316       no
    6   FINTECH  FINANCIAL_TECHNOLOGIES        0.289       no
    8   FINTECH  THE_FINANCIAL_INDUSTRY        0.237       no
    13  FINTECH              REGULATORS        0.211       no
    23  FINTECH                   BANKS        0.184       no



"""

from techminer2._internals import ParamsMixin
from techminer2.thesaurus_old.user import CombineKeys as UserCombineKeys


class CombineKeys(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            UserCombineKeys()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )
