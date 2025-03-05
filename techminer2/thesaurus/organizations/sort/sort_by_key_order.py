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


>>> # TEST PREPARATION
>>> import sys
>>> from io import StringIO
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()
>>> #
>>> from techminer2.thesaurus.organizations import CreateThesaurus
>>> CreateThesaurus(root_directory="example/", quiet=True).run()


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.organizations import SortByKeyOrder
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


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus alphabetically
  File : example/thesaurus/organizations.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/organizations.the.txt
<BLANKLINE>
    Anhui Univ of Finan and Econ (CHN)
      School of Finance, Anhui University of Finance and Economics, Bengbu, 233...
    Baekseok Univ (KOR)
      Division of Tourism, Baekseok University, South Korea
    Baewha Women’s Univ (KOR)
      Department of Information Security, Baewha Women’s University, Seoul, Sou...
    Baylor Univ (USA)
      Baylor University, United States; Hankamer School of Business, Baylor Uni...
    Beihang Univ (CHN)
      School of Economics and Management, Beihang University, China
    Brussels, Belgium (BEL)
      Brussels, Belgium
    CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
      CESifo, Poschingerstr. 5, Munich, 81679, Germany
    Cent for Law, Markets & Regulation, UNSW Australia, Australia (AUS)
      Centre for Law, Markets & Regulation, UNSW Australia, Australia
<BLANKLINE>
<BLANKLINE>



>>> # TEST PREPARATION
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()

>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.organizations import SortByKeyOrder
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


>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus by key length
  File : example/thesaurus/organizations.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/organizations.the.txt
<BLANKLINE>
    The Res center of information technology & economic and social development of...
      The Research center of information technology & economic and social devel...
    Cent for Law, Markets & Regulation, UNSW Australia, Australia (AUS)
      Centre for Law, Markets & Regulation, UNSW Australia, Australia
    Stanford GSB and the Hoover Institution, United States (USA)
      Stanford GSB and the Hoover Institution, United States
    Johns Hopkins SAIS, Washington, DC, United States (USA)
      Johns Hopkins SAIS, Washington, DC, United States
    CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
      CESifo, Poschingerstr. 5, Munich, 81679, Germany
    Univ of the Free State and Univ of Ghana Bus Sch (GHA)
      University of the Free State and University of Ghana Business School, Uni...
    Hochschule für Wirtschaft Fribourg, Switzerland (CHE)
      Hochschule für Wirtschaft Fribourg, Switzerland
    Max Planck Inst for Innovation and Competition (DEU)
      Max Planck Institute for Innovation and Competition, Marstallplatz 1, Mun...
<BLANKLINE>
<BLANKLINE>


>>> # TEST PREPARATION
>>> old_stderr = sys.stderr
>>> sys.stderr = StringIO()

>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.organizations import SortByKeyOrder
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

>>> # TEST EXECUTION
>>> output = sys.stderr.getvalue()
>>> sys.stderr = old_stderr
>>> print(output)
Sorting thesaurus by word length
  File : example/thesaurus/organizations.the.txt
  Thesaurus sorting completed successfully
<BLANKLINE>
Printing thesaurus header
  File : example/thesaurus/organizations.the.txt
<BLANKLINE>
    Transport and Telecomunication Inst (LVA)
      Transport and Telecomunication Institute, Latvia
    Fraunhofer-Inst for Soft and Syst Eng ISST (DEU)
      Fraunhofer-Institute for Software and Systems Engineering ISST, Dortmund,...
    CESifo, Poschingerstr. 5, Munich, 81679, Germany (DEU)
      CESifo, Poschingerstr. 5, Munich, 81679, Germany
    Univ Koblenz-Landau (DEU)
      Institute for Software Technology IST, Universität Koblenz-Landau, Koblen...
    Fed Reserv Bank of Philadelphia (USA)
      Federal Reserve Bank of Philadelphia, Philadelphia, PA, United States; Fe...
    Pennsylvania State Univ (USA)
      Department of Supply Chain and Information Systems, Smeal College of Busi...
    Stanford GSB and the Hoover Institution, United States (USA)
      Stanford GSB and the Hoover Institution, United States
    Sungkyunkwan Univ (KOR)
      Software College, Sungkyunkwan University, Suwon, South Korea; Sungkyunkw...
<BLANKLINE>
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
            .with_thesaurus_file("organizations.the.txt")
            .run()
        )
