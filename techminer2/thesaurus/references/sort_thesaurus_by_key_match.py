# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key Match
===============================================================================

Finds a string in the terms of a thesaurus.


>>> from techminer2.thesaurus.references import SortThesaurusByKeyMatch
>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like("BANK")
...     .having_keys_starting_with(None)
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/global_references.the.txt
           Keys like: BANK
  Keys starting with: None
    Keys ending with: None
  31 matching keys found
Printing thesaurus header
  Loading example/thesaurus/global_references.the.txt thesaurus file
  Header:
    Angelini P., 1998, J BANK FINANC, V22, P1
      Angelini P., An analysis of competitive externalities in gross settlem...
    Bartoli F., 2013, J BANK FINANC, V37, P5476
      Bartoli F., Ferri G., Murro P., Rotondi Z., SME Financing and the Choi...
    Beck T., 2016, J BANK FINANC, V72, P28
      Beck T., Chen T., Lin C., Song F., Financial innovation: The bright an...
    Beijnen C., 2009, J BANK FINANC, V33, P203
      Beijnen C., Bolt W., Size Matters: Economies of Scale in European Paym...
    Berentsen A., 2018, FED RESERVE BANK ST LOUIS REV,...
      Berentsen A., Schaer F., A short introduction to the world of cryptocu...
    Berger A.N., 2003, J MONEY CREDIT BANK, V35, P141
      Berger A.N., The economic effects of technological progress: Evidence ...
    Berger A.N., 2006, J BANK FINANC, V30, P2945
      Berger A.N., Udell G.F., A More Complete Conceptual Framework for SME ...
    Berger A.N., 2011, J BANK FINANC, V35, P724
      Berger A.N., Black L.K., Bank Size, Lending Technologies, and Small Bu...

>>> (
...     SortThesaurusByKeyMatch()
...     # 
...     # THESAURUS:
...     .having_keys_like(None)
...     .having_keys_starting_with("Black")
...     .having_keys_ending_with(None)
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... ) 
Sorting thesaurus file by key match.
      Thesaurus file: example/thesaurus/global_references.the.txt
           Keys like: None
  Keys starting with: Black
    Keys ending with: None
  4 matching keys found
Printing thesaurus header
  Loading example/thesaurus/global_references.the.txt thesaurus file
  Header:
    Black B.S., 2001, UCLA LAW REV, V48, P781
      Black B.S., The legal and institutional preconditions for strong secur...
    Black E., 2016, BULL AM METEOROL SOC, V97, PES203
      Black E., Greatrex H., Young M., Maidment R., Incorporating satellite ...
    Black E., 2016, REMOTE SENS, V8
      Black E., Tarnavsky E., Maidment R., Greatrex H., Mookerjee A., Quaife...
    Black F., 1973, J POLIT ECON, V81, P637
      Black F., Scholes M., The pricing of options and corporate liabilities...
    Aastveit K.A., 2014, J BUS ECON STAT, V32, P48
      Aastveita K.A., Gerdrupa K.R., Jore A.S., Thorsrudb L.A., Nowcasting G...
    Abawajy J., 2016, FUTURE GENER COMPUT SYST, V55, P...
      Abawajy J., Wang G., Yang L., Javadi B., Trust, security and privacy i...
    Abbad M.M., 2013, BEHAV INF TECHNOL, V32, P681
      Abbad M.M., E-Banking in Jordan, Behav. Inf. Technol, 32, pp. 681-694,...
    Abraham C., 2011, J STRATEGIC INFORM SYST, V20, P1...
      Abraham C., Junglas I., From cacophony to harmony: a case study about ...


"""
from ..._internals.mixins import ParamsMixin
from ..user.sort_thesaurus_by_key_match import (
    SortThesaurusByKeyMatch as SortUserThesaurusByKeyMatch,
)


class SortThesaurusByKeyMatch(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            SortUserThesaurusByKeyMatch()
            .update(**self.params.__dict__)
            .with_thesaurus_file("global_references.the.txt")
            .build()
        )
