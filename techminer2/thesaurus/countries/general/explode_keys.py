# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Explode Keys
===============================================================================

Example:
    >>> from techminer2.thesaurus.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("examples/small/")
    ... ).run()


    >>> from techminer2.thesaurus.countries import ExplodeKeys
    >>> ExplodeKeys().where_root_directory("examples/fintech/").run()

    >>> from techminer2.thesaurus.countries import PrintHeader
    >>> (
    ...     PrintHeader()
    ...     .using_colored_output(False)
    ...     .where_root_directory("examples/small/")
    ... ).run()
    Australia
      Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
    Belgium
      Brussels, Belgium
    Brunei Darussalam
      Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
    China
      The Research center of information technology & economic and social devel...
    Denmark
      Copenhagen Business School, Department of IT Management, Howitzvej 60, Fr...
    France
      SKEMA Business School, Lille, France; University of Lille Nord de France,...
    Germany
      Leipzig University, Leipzig, Germany; University of Trier, Trier, Germany...
    Ghana
      University of the Free State and University of Ghana Business School, Uni...
    <BLANKLINE>



"""
from techminer2._internals import ParamsMixin
from techminer2.thesaurus.user import ExplodeKeys as UserExplodeKeys


class ExplodeKeys(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def run(self):
        (
            UserExplodeKeys()
            .update(**self.params.__dict__)
            .update(
                thesaurus_file="countries.the.txt",
                root_directory=self.params.root_directory,
            )
            .run()
        )


# =============================================================================
