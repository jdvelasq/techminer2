# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Order
===============================================================================


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.countries import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
Sorting thesaurus alphabetically
  Loading example/thesaurus/countries.the.txt thesaurus file as mapping
  Sorting keys alphabetically
  Writing thesaurus to disk.
Printing thesaurus header
  Loading example/thesaurus/countries.the.txt thesaurus file
  Header:
    Argentina
      Sorin Capital Management, Argentina
    Australia
      Accounting Discipline, Business School, The University of Sydney, Buil...
    Austria
      Agro-Industries Branch, UNIDO, Austria; Department of Business Adminis...
    Belgium
      Brussels, Belgium; CERMi (Centre for European Research in Microfinance...
    Brazil
      Brazilian School of Public and Business Administration, Getulio Vargas...
    Brunei Darussalam
      Centre for Lifelong Learning, Universiti Brunei Darussalam, Gadong, Br...
    Bulgaria
      International University College, 3 Bulgaria Str, 9300 Dobrich, Bulgar...
    Cambodia
      Future Forum, Phnom Penh, Cambodia; National ICT Development Authority...


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.countries import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("key_length")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )      
Sorting thesaurus by key length
  Loading example/thesaurus/countries.the.txt thesaurus file as mapping
  Sorting keys by key length
  Writing thesaurus to disk.
Printing thesaurus header
  Loading example/thesaurus/countries.the.txt thesaurus file
  Header:
    Iran
      Department of Business Management, Qazvin Branch, Islamic Azad Univers...
    Oman
      Dept. of Computer Science, German University of Technology in Oman (GU...
    Chile
      Central Bank of Chile, Santiago, Chile; Facultad de Ingeniería, Univer...
    China
      Anhui University of Technology, Maanshan, China; Antai College of Econ...
    Egypt
      Department of Accounting and Auditing, Faculty of Commerce, Ain Shams ...
    Ghana
      Department of Liberal Studies, Bolgatanga Polytechnic, Bolgatanga, Gha...
    India
      Amrita Vishwa Vidyapeetham, Coimbatore, India; Center for Research in ...
    Italy
      Banca d'Italia, DG-Economics, Statistics and Research, Rome, Italy; Ba...


      
>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.countries import SortThesaurusByKeyOrder
>>> (
...     SortThesaurusByKeyOrder()
...     # 
...     # THESAURUS:
...     .having_keys_ordered_by("word_length")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
Sorting thesaurus by word length
  Loading example/thesaurus/countries.the.txt thesaurus file as mapping
  Sorting keys by word length
  Writing thesaurus to disk.
Printing thesaurus header
  Loading example/thesaurus/countries.the.txt thesaurus file
  Header:
    United Arab Emirates
      Alhosn University, Abu Dhabi, United Arab Emirates; Department of Entr...
    Brunei Darussalam
      Centre for Lifelong Learning, Universiti Brunei Darussalam, Gadong, Br...
    North Macedonia
      South East European University, Former Yugoslav Republic of Macedonia,...
    United Kingdom
      451 Group, London, United Kingdom; All Souls College, Oxford, United K...
    United States
      102 South Hall, Berkeley, CA 94720-4600, United States; 403 Communicat...
    Liechtenstein
      Institute of Information Systems, University of Liechtenstein, Fürst-F...
    South Africa
      Academy for Information Technology, University of Johannesburg, Johann...
    Saudi Arabia
      College of Computing and Informatics, Saudi Electronic University, Riy...

          

"""
from ..._internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_key_order import (
    SortThesaurusByKeyOrder as SortUserThesaurusByKeyOrder,
)


class SortThesaurusByKeyOrder(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByKeyOrder()
            .update(**self.params.__dict__)
            .with_thesaurus_file("countries.the.txt")
            .build()
        )
