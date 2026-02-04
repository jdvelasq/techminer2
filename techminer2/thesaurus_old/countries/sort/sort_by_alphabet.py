# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Alphabet
===============================================================================


Example:
    >>> from techminer2.thesaurus_old.countries import InitializeThesaurus
    >>> (
    ...     InitializeThesaurus()
    ...     .where_root_directory("examples/small/")
    ... ).run()


    >>> from techminer2.thesaurus_old.countries import SortByAlphabet
    >>> (
    ...     SortByAlphabet()
    ...     .where_root_directory("examples/small/")
    ...     .run()
    ... )

    >>> from techminer2.thesaurus_old.countries import PrintHeader
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
      Cheung Kong Graduate School of Business, and Institute of Internet Financ...
    Denmark
      Copenhagen Business School, Department of IT Management, Howitzvej 60, Fr...
    France
      SKEMA Business School, Lille, France; University of Lille Nord de France,...
    Germany
      CESifo, Poschingerstr. 5, Munich, 81679, Germany; Chair of e-Finance, Goe...
    Ghana
      University of the Free State and University of Ghana Business School, Uni...
    <BLANKLINE>


"""
from techminer2._internals import ParamsMixin
from techminer2.thesaurus_old.user import SortByAlphabet as UserSortByAlphabet


class SortByAlphabet(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByAlphabet()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )
