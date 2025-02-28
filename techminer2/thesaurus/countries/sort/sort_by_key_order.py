# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort by Key Order
===============================================================================

>>> from techminer2.thesaurus.countries import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.countries import SortByKeyOrder
>>> (
...     SortByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Sorting thesaurus alphabetically
  File : example/thesaurus/countries.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/countries.the.txt
<BLANKLINE>
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




>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.countries import SortByKeyOrder
>>> (
...     SortByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("key_length")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )      
Sorting thesaurus by key length
  File : example/thesaurus/countries.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/countries.the.txt
<BLANKLINE>
    Brunei Darussalam
      Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
    United Kingdom
      Bristol Business School, University of the West of England, Bristol, Unit...
    United States
      Baylor University, United States; Columbia Graduate School of Business, U...
    Netherlands
      Erasmus University Rotterdam, Burgemeester Oudlaan, Rotterdam, 50, Nether...
    South Korea
      College of Business Administration, Soongsil University, South Korea; Dep...
    Switzerland
      Department of Informatics, University of Zurich, Binzmuehlestrasse 14, Zu...
    Kazakhstan
      Department of Accounting and Finance, Bang College of Business, KIMEP Uni...
    Australia
      Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
<BLANKLINE>




>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.countries import SortByKeyOrder
>>> (
...     SortByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("word_length")
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     #
...     .run()
... )
Sorting thesaurus by word length
  File : example/thesaurus/countries.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/countries.the.txt
<BLANKLINE>
    Netherlands
      Erasmus University Rotterdam, Burgemeester Oudlaan, Rotterdam, 50, Nether...
    Switzerland
      Department of Informatics, University of Zurich, Binzmuehlestrasse 14, Zu...
    Brunei Darussalam
      Universiti Brunei Darussalam, School of Business and Economics, Jln Tungk...
    Kazakhstan
      Department of Accounting and Finance, Bang College of Business, KIMEP Uni...
    Australia
      Centre for Law, Markets & Regulation, UNSW Australia, Australia; Charles ...
    Indonesia
      Department of Management, Faculty of Economics and Business, Universitas ...
    Singapore
      School of Information Systems, Singapore Management University (SMU), Sin...
    Slovenia
      Faculty of Economics, University of Ljubljana, Kardeljeva pl. 17, Ljublja...
<BLANKLINE>


"""
from ...._internals.mixins import ParamsMixin
from ...user import SortByKeyOrder as UserSortByKeyOrder


class SortByKeyOrder(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            UserSortByKeyOrder()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .run()
        )
