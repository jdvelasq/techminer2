# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Sort Thesaurus by Key
===============================================================================

>>> # TEST:
>>> from techminer2.thesaurus._internals import internal__print_thesaurus_head
>>> from techminer2._internals import Params
>>> params = Params().update(thesaurus_file="descriptors.the.txt", root_dir="example/")


>>> # with_keys_order_by: "alphabetical", "key_length", "word_length"
>>> from techminer2.thesaurus.user import SortThesaurusByKey
>>> (
...     SortThesaurusByKey()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_ordered_by("alphabetical")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
>>> internal__print_thesaurus_head(params)
-- INFO -- Thesaurus head 'example/thesaurus/descriptors.the.txt'.
         :    'BEST_PRACTICE_ERP_PACKAGES : 'BEST_PRACTICE_ERP_PACKAGES                       
         :                         'FRAUD : 'FRAUD                                            
         :                  3D_NAVIGATION : 3D_NAVIGATION                                     
         :                    3G_CELLULAR : 3G_CELLULAR                                       
         :     3G_CELLULAR_COMMUNICATIONS : 3G_CELLULAR_COMMUNICATIONS                        
         :                 3_D_TRAJECTORY : 3_D_TRAJECTORY                                    
         :          4TH_GENERATION_MOBILE : 4TH_GENERATION_MOBILE                             
         :                             5G : 5G                                                
>>> from techminer2.thesaurus.user import SortThesaurusByKey
>>> (
...     SortThesaurusByKey()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_ordered_by("key_length")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
>>> internal__print_thesaurus_head(params)
-- INFO -- Thesaurus head 'example/thesaurus/descriptors.the.txt'.
         :                             5G : 5G                                                
         :                             AI : AI                                                
         :                             CO : CO                                                
         :                             DR : DR                                                
         :                             EU : EU                                                
         :                              G : G                                                 
         :                             IT : IT                                                
         :                             OM : OM                                                
>>> from techminer2.thesaurus.user import SortThesaurusByKey
>>> (
...     SortThesaurusByKey()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("descriptors.the.txt")
...     .having_keys_ordered_by("word_length")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )
>>> internal__print_thesaurus_head(params)
-- INFO -- Thesaurus head 'example/thesaurus/descriptors.the.txt'.
         : INFORMATION_TECHNOLOGY (IT ... : INFORMATION_TECHNOLOGY (IT) ACCEPTANCE            
         : MANAGEMENT_INFORMATION_SYS ... : MANAGEMENT_INFORMATION_SYSTEM (MIS) IMPLEMENTATION
         : NEAR_FIELD_COMMUNICATION ( ... : NEAR_FIELD_COMMUNICATION (NFC) TECHNOLOGY         
         : POWER_MANAGEMENT (TELECOMM ... : POWER_MANAGEMENT (TELECOMMUNICATION)              
         : RADIO_FREQUENCY_IDENTIFICA ... : RADIO_FREQUENCY_IDENTIFICATION (RFID) TECHNOLOGY  
         :     REINFORCEMENT (PSYCHOLOGY) : REINFORCEMENT (PSYCHOLOGY)                        
         : THEROLEOFSOCIALCAPITALINPEOPLE : THEROLEOFSOCIALCAPITALINPEOPLE                    
         : THE_FINTECHPHILANTHROPYDEV ... : THE_FINTECHPHILANTHROPYDEVELOPMENT_COMPLEX        

             
"""
from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from .._internals import (
    ThesaurusMixin,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)


class SortThesaurusByKey(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_get_thesaurus_path(self):
        return internal__generate_user_thesaurus_file_path(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_print_info_header(self, file_path, order_by):
        internal__log_message(
            msgs=[
                f"Sorting thesaurus {order_by}.",
                f"      Thesaurus file: '{file_path}'",
            ],
            prompt_flag=self.params.prompt_flag,
            initial_newline=True,
        )

    # -------------------------------------------------------------------------
    def get_thesaurus_sorted_keys(self, th_dict):
        #
        if self.params.keys_order_by == "alphabetical":
            return sorted(th_dict.keys(), reverse=False)
        #
        if self.params.keys_order_by == "key_length":
            return sorted(th_dict.keys(), key=lambda x: (len(x), x), reverse=False)
        #
        if self.params.keys_order_by == "word_length":
            return sorted(
                th_dict.keys(),
                key=lambda x: (max(len(y) for y in x.split("_")), x),
                reverse=True,
            )
        #
        return th_dict.keys()

    # -------------------------------------------------------------------------
    def save_sorted_thesaurus_on_disk(self, file_path, th_dict, sorted_keys):
        with open(file_path, "w", encoding="utf-8") as file:
            for key in sorted_keys:
                file.write(key + "\n")
                for item in sorted(set(th_dict[key])):
                    file.write("    " + item + "\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)

        order_by = {
            "alphabetical": "alphabetically",
            "key_length": "by key length",
            "word_length": "by word length",
        }[self.params.keys_order_by]

        th_dict = internal__load_thesaurus_as_mapping(file_path)
        sorted_keys = self.get_thesaurus_sorted_keys(th_dict)
        self.save_sorted_thesaurus_on_disk(file_path, th_dict, sorted_keys)
        #
        self.print_thesaurus_head()
        internal__log_message(msgs="  Done.", prompt_flag=-1)


# =============================================================================
