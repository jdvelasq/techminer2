# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
"""
Create thesaurus
===============================================================================


>>> from techminer2.thesaurus.user import CreateThesaurus
>>> (
...     CreateThesaurus()
...     # 
...     # THESAURUS:
...     .with_thesaurus_file("demo.the.txt")
...     #
...     # FIELD:
...     .with_field("descriptors")
...     #
...     # DATABASE:
...     .where_directory_is("example/")
...     #
...     .build()
... )

>>> # TEST:
>>> from techminer2.thesaurus._internals import internal__print_thesaurus_head
>>> from techminer2.internals import Params
>>> params = Params().update(thesaurus_file="demo.the.txt", root_dir="example/")
>>> internal__print_thesaurus_head(params, n=10)
-- INFO -- Thesaurus head 'example/thesaurus/demo.the.txt'.
         :    'BEST_PRACTICE_ERP_PACKAGES : 'BEST_PRACTICE_ERP_PACKAGES                       
         :                         'FRAUD : 'FRAUD                                            
         :                  3D_NAVIGATION : 3D_NAVIGATION                                     
         :                    3G_CELLULAR : 3G_CELLULAR                                       
         :     3G_CELLULAR_COMMUNICATIONS : 3G_CELLULAR_COMMUNICATIONS                        
         :                 3_D_TRAJECTORY : 3_D_TRAJECTORY                                    
         :          4TH_GENERATION_MOBILE : 4TH_GENERATION_MOBILE                             
         :                             5G : 5G                                                
         : 5G_MOBILE_COMMUNICATION_SY ... : 5G_MOBILE_COMMUNICATION_SYSTEMS                   
         :                           ABAC : ABAC                                              


"""
import re

import pandas as pd  # type: ignore
from textblob import Word  # type: ignore
from tqdm import tqdm  # type: ignore

from ..._internals.log_message import internal__log_message
from ..._internals.mixins import ParamsMixin
from ...database._internals.io import internal__load_records
from ...package_data.text_processing import internal__load_text_processing_terms
from .._internals import (
    ThesaurusMixin,
    internal__generate_system_thesaurus_file_path,
    internal__generate_user_thesaurus_file_path,
    internal__load_thesaurus_as_mapping,
)

tqdm.pandas()


class CreateThesaurus(
    ParamsMixin,
    ThesaurusMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def step_01_load_records(self):
        return internal__load_records(params=self.params)

    # -------------------------------------------------------------------------
    def step_02_create_data_frame(self, records):
        #
        keys = records[self.params.field].dropna()
        keys = keys.str.split("; ")
        keys = keys.explode()
        keys = keys.str.strip()
        #
        fingerprints = keys.str.lower()
        fingerprints = fingerprints.str.replace("-", " ")
        fingerprints = fingerprints.str.replace("_", " ")
        #
        counts = keys.value_counts()
        mapping = dict(zip(counts.index.tolist(), counts.values.tolist()))
        #
        data_frame = pd.DataFrame(
            {
                "key": keys,
                "value": keys,
                "fingerprint": fingerprints,
                "occ": [mapping[k] for k in keys],
            }
        )
        #
        return data_frame

    # -------------------------------------------------------------------------
    def step_03_transform_british_to_american_spelling(self, data_frame):
        file_path = internal__generate_system_thesaurus_file_path(
            "language/british2american.the.txt"
        )
        mapping = internal__load_thesaurus_as_mapping(file_path)
        mapping = {k: v[0] for k, v in mapping.items()}
        #
        tqdm.pandas(desc="         :      Transforming spelling")
        #
        data_frame["fingerprint"] = data_frame["fingerprint"].progress_apply(
            lambda x: " ".join(mapping.get(w, w) for w in x.split(" "))
        )
        #
        tqdm.pandas(desc=None)
        #
        return data_frame

    # -------------------------------------------------------------------------
    def step_04_singularize_terms(self, data_frame):
        tqdm.pandas(desc="         :        Singularizing terms")
        data_frame["fingerprint"] = data_frame["fingerprint"].progress_apply(
            lambda x: " ".join(Word(w).singularize() for w in x.split())
        )
        tqdm.pandas(desc=None)
        return data_frame

    # -------------------------------------------------------------------------
    def step_05_remove_technical_stopwords(self, data_frame):
        tqdm.pandas(desc="         :         Removing stopwords")
        stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
        data_frame["fingerprint"] = data_frame["fingerprint"].progress_apply(
            lambda x: " ".join([word for word in x.split() if word not in stopwords])
        )
        tqdm.pandas(desc=None)
        return data_frame

    # -------------------------------------------------------------------------
    def step_06_transform_hypened_words(self, data_frame):
        #
        def f(x):
            for pattern, replacement in patterns:
                x = pattern.sub(replacement, x)
            return x

        #
        hypened_words = internal__load_text_processing_terms("hypened_words.txt")
        hypened_words = [word.lower() for word in hypened_words]
        patterns = [
            (re.compile(r"\b" + word.replace("_", "") + r"\b"), word.replace("_", " "))
            for word in hypened_words
        ]
        #
        tqdm.pandas(desc="         :   Processing hypened words")
        data_frame["fingerprint"] = data_frame["fingerprint"].progress_apply(f)
        tqdm.pandas(desc=None)
        #
        return data_frame

    # -------------------------------------------------------------------------
    def step_07_sort_fingerprint_words(self, data_frame):
        data_frame["fingerprint"] = data_frame["fingerprint"].apply(
            lambda x: " ".join(sorted(x.split(" ")))
        )
        return data_frame

    # -------------------------------------------------------------------------
    def step_08_generate_fingerprint2value_mapping(self, data_frame):
        data_frame = data_frame.sort_values(
            by=["fingerprint", "occ", "value"], ascending=[True, False, True]
        )
        data_frame = data_frame.drop_duplicates(subset=["fingerprint"])
        mapping = data_frame.set_index("fingerprint")["value"].to_dict()
        return mapping

    # -------------------------------------------------------------------------
    def step_09_apply_mapping(self, data_frame, mapping):
        tqdm.pandas(desc="         :            Generating keys")
        data_frame["key"] = data_frame["fingerprint"].progress_apply(
            lambda x: mapping.get(x, x)
        )
        tqdm.pandas(desc=None)
        data_frame = data_frame[["key", "value"]]
        return data_frame

    # -------------------------------------------------------------------------
    def step_10_save_thesaurus(self, file_path, data_frame):
        data_frame = data_frame.groupby("key").agg({"value": list})
        with open(file_path, "w", encoding="utf-8") as file:
            for _, row in data_frame.iterrows():
                file.write(row.name + "\n")
                for value in row["value"]:
                    file.write(f"  {value}\n")

    # -------------------------------------------------------------------------
    def build(self):
        """:meta private:"""

        file_path = internal__generate_user_thesaurus_file_path(params=self.params)
        #
        # LOG:
        internal__log_message(
            msgs=[
                "Creating thesaurus.",
                f"            Thesaurus file: '{file_path}'",
                f"              Source field: '{self.params.field}'",
            ],
            prompt_flag=self.params.prompt_flag,
            initial_newline=True,
        )
        #
        #
        records = self.step_01_load_records()
        data_frame = self.step_02_create_data_frame(records)
        data_frame = self.step_03_transform_british_to_american_spelling(data_frame)
        data_frame = self.step_04_singularize_terms(data_frame)
        data_frame = self.step_05_remove_technical_stopwords(data_frame)
        data_frame = self.step_06_transform_hypened_words(data_frame)
        data_frame = self.step_07_sort_fingerprint_words(data_frame)
        mapping = self.step_08_generate_fingerprint2value_mapping(data_frame)
        data_frame = self.step_09_apply_mapping(data_frame, mapping)
        self.step_10_save_thesaurus(file_path, data_frame)
        #
        # LOG:
        self.print_thesaurus_head(n=5)
        internal__log_message(msgs="  Done.", prompt_flag=-1)
