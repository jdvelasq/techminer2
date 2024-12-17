# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Ingest Raw Data
===============================================================================
# doctest: +SKIP 


>>> from techminer2.ingest import ingest_raw_data
>>> ingest_raw_data( 
...     #
...     # DATABASE PARAMS:
...     root_dir="example/",
... ) # doctest: +ELLIPSIS
-- 001 -- Compressing raw data files
-- 002 -- Creating working directories
-- 003 -- Creating stopwords.txt file
-- 004 -- Creating database files
...


"""
import os
import time

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ...internals.utils.utils_abstracts_and_titles_to_lower_case import (
    _utils_abstracts_and_titles_to_lower_case,
)
from ...prepare.thesaurus.countries.apply_thesaurus import (
    apply_thesaurus as apply_countries_thesaurus,
)
from ...prepare.thesaurus.descriptors.apply_thesaurus import (
    apply_thesaurus as apply_descriptors_thesaurus,
)
from ...prepare.thesaurus.organizations.apply_thesaurus import (
    apply_thesaurus as apply_organizations_thesaurus,
)
from ...prepare.transformations.replace_keywords import replace_keywords
from ._create_abbreviations_thesaurus import _create_abbreviations_thesaurus
from ._list_cleanup_countries import list_cleanup_countries
from ._list_cleanup_organizations import list_cleanup_organizations
from ._message import message
from ._replace_descriptors import _replace_descriptors
from ._report_imported_records_per_file import report_imported_records_per_file
from .internals.database.database__compress_raw_files import (
    database__compress_raw_files,
)
from .internals.database.database__create_project_structure import (
    database__create_project_structure,
)
from .internals.database.database__drop_empty_columns import (
    database__drop_empty_columns,
)
from .internals.database.database__load_raw_files import database__load_raw_files
from .internals.database.database__rename_columns import database__rename_columns
from .internals.preprocessing._create_local_citations_column_in_cited_by_database import (
    create_local_citations_column_in_cited_by_database,
)
from .internals.preprocessing._create_local_citations_column_in_documents_database import (
    create_local_citations_column_in_documents_database,
)
from .internals.preprocessing._create_local_citations_column_in_references_database import (
    create_local_citations_column_in_references_database,
)
from .internals.preprocessing.preprocessing__abbr_source_title import (
    preprocessing__abbr_source_title,
)
from .internals.preprocessing.preprocessing__abstract import preprocessing__abstract
from .internals.preprocessing.preprocessing__author_keywords import (
    preprocessing__author_keywords,
)
from .internals.preprocessing.preprocessing__author_names import (
    preprocessing__author_names,
)
from .internals.preprocessing.preprocessing__authors import preprocessing__authors
from .internals.preprocessing.preprocessing__authors_id import preprocessing__authors_id
from .internals.preprocessing.preprocessing__document_title import (
    preprocessing__document_title,
)
from .internals.preprocessing.preprocessing__document_type import (
    preprocessing__document_type,
)
from .internals.preprocessing.preprocessing__doi import preprocessing__doi
from .internals.preprocessing.preprocessing__eissn import preprocessing__eissn
from .internals.preprocessing.preprocessing__global_citations import (
    preprocessing__global_citations,
)

#
#
from .internals.preprocessing.preprocessing__global_references import (
    preprocessing__global_references,
)
from .internals.preprocessing.preprocessing__index_keywords import (
    preprocessing__index_keywords,
)
from .internals.preprocessing.preprocessing__local_references import (
    preprocessing__local_references,
)
from .internals.preprocessing.preprocessing__num_authors import (
    preprocessing__num_authors,
)
from .internals.preprocessing.preprocessing__num_global_references import (
    preprocessing__num_global_references,
)
from .internals.preprocessing.preprocessing__raw_abstract_nlp_phrases import (
    preprocessing__raw_abstract_nlp_phrases,
)
from .internals.preprocessing.preprocessing__raw_author_keywords import (
    preprocessing__raw_author_keywords,
)
from .internals.preprocessing.preprocessing__raw_descriptors import (
    preprocessing__raw_descriptors,
)
from .internals.preprocessing.preprocessing__raw_index_keywords import (
    preprocessing__raw_index_keywords,
)
from .internals.preprocessing.preprocessing__raw_keywords import (
    preprocessing__raw_keywords,
)
from .internals.preprocessing.preprocessing__raw_nlp_phrases import (
    preprocessing__raw_nlp_phrases,
)
from .internals.preprocessing.preprocessing__raw_title_nlp_phrases import (
    preprocessing__raw_title_nlp_phrases,
)
from .internals.preprocessing.preprocessing__record_id import preprocessing__record_id
from .internals.preprocessing.preprocessing__record_no import preprocessing__record_no
from .internals.preprocessing.preprocessing__source_title import (
    preprocessing__source_title,
)
from .internals.preprocessing.proprocessing__references import preprocessing__references

# -------------------------------------------------------------------------------------
# Field basic operations
# -------------------------------------------------------------------------------------


# from ._adds_countries_and_regions_to_stopwords import _adds_countries_and_regions_to_stopwords


def ingest_raw_data(
    #
    # DATABASE PARAMS:
    root_dir="./",
):
    """:meta private:"""

    # This file is very long. Process original csv Scopus files to a format that is
    # easier to work with. Due to great number of transformations, I decide to put
    # each function and the their inmediate call, in order to clarify the process.

    #
    # Preparation
    # =================================================================================
    #

    # Register tqdm pandas progress bar
    tqdm.pandas()

    # Elapsed time report
    start_time = time.time()

    #
    # PHASE 1: Preparing database files and folders
    # =================================================================================
    #
    database__compress_raw_files(root_dir)
    database__create_project_structure(root_dir)
    database__load_raw_files(root_dir)
    database__rename_columns(root_dir)
    database__drop_empty_columns(root_dir)

    #
    #
    # PHASE 2: Process each column in isolation
    # =================================================================================
    #
    #
    preprocessing__raw_author_keywords(root_dir)
    preprocessing__raw_index_keywords(root_dir)
    preprocessing__abbr_source_title(root_dir)
    preprocessing__abstract(root_dir)
    preprocessing__author_names(root_dir)
    preprocessing__authors_id(root_dir)
    preprocessing__authors(root_dir)
    preprocessing__document_title(root_dir)
    preprocessing__document_type(root_dir)
    preprocessing__doi(root_dir)
    preprocessing__eissn(root_dir)
    preprocessing__global_citations(root_dir)
    preprocessing__source_title(root_dir)
    preprocessing__num_authors(root_dir)
    preprocessing__num_global_references(root_dir)

    preprocessing__references(root_dir)
    preprocessing__record_id(root_dir)
    preprocessing__record_no(root_dir)

    #
    #
    # PHASE 2: Keywords & noun phrases & abstracts
    # =============================================================================================
    #
    #

    # In the context of topic modeling for research abstracts, it is generally
    # more common and beneficial to use "noun phrases" extracted using text
    # mining techniques rather than relying solely on provided "keywords" for
    # the given document.
    #
    # Research abstracts often contain technical and domain-specific
    # language, making it challenging to accurately capture the main topics
    # and themes using only manually assigned or provided keywords. On the
    # other hand, using text mining techniques to extract noun phrases can
    # help uncover more nuanced and contextually relevant phrases that better
    # represent the content of the abstracts.
    #
    # Text mining techniques, such as part-of-speech tagging, noun phrase
    # chunking, or natural language processing algorithms, can identify
    # meaningful noun phrases that may not be explicitly listed as keywords.
    # These extracted noun phrases can provide a more comprehensive
    # representation of the topics present in the research abstracts,
    # allowing for more accurate and informative topic modeling.
    #
    # Therefore, leveraging text mining techniques to extract noun phrases is
    # often preferred over relying solely on provided keywords when
    # conducting topic modeling on research abstracts.

    #
    # Prepare author/index keywords:
    # To upper() and replace spaces with underscores
    # Merge author/index keywords into a single column
    #
    preprocessing__index_keywords(root_dir)
    preprocessing__author_keywords(root_dir)
    preprocessing__raw_keywords(root_dir)

    #
    # Prepare title:
    # To lower() & remove brackets & remove multiple spaces & strip
    #

    #
    # Technological Emergence Indicators using Emergence Score.
    # Garner et al. 2017.
    # ------------------------------------------------------------------------
    #
    # Suitable terms for determining emergence are presented both in title and
    # the abstract. This allows to augment the list of terms given by the
    # authors/index keywords
    #

    #
    # Step 1: Create a candidate list of abstract noun phrases
    #

    #
    # In textblob, text in upper case is recognized as noun:
    # >>> TextBlob("Face-to-face".upper())
    # [('FACE-TO-FACE', 'NN')]
    replace_keywords(
        root_dir=root_dir,
    )

    preprocessing__raw_abstract_nlp_phrases(root_dir)
    preprocessing__raw_title_nlp_phrases(root_dir)

    _utils_abstracts_and_titles_to_lower_case(root_dir=root_dir)

    #
    # Step 2: Create a candidate list of title noun phrases
    #

    # _replace_noun_phrases(
    #     column_to_process="document_title",
    #     noun_phrases_column="raw_title_nlp_phrases",
    #     root_dir=root_dir,
    # )

    #
    # Step 3: Merge fields
    #
    preprocessing__raw_nlp_phrases(root_dir)
    preprocessing__raw_descriptors(root_dir)

    #
    # Highlight author and index keywords
    #
    _replace_descriptors(root_dir)
    # replace_keywords(
    #     root_dir=root_dir,
    # )

    #
    #
    # PHASE 4: References
    # =============================================================================================
    #
    #

    preprocessing__local_references(root_dir)
    preprocessing__global_references(root_dir)

    #
    create_local_citations_column_in_documents_database(root_dir)
    create_local_citations_column_in_references_database(root_dir)
    create_local_citations_column_in_cited_by_database(root_dir)

    #
    #
    # PHASE 5: Thesaurus files
    # =============================================================================================
    #
    #

    list_cleanup_countries(root_dir)
    apply_countries_thesaurus(root_dir)

    list_cleanup_organizations(root_dir)
    apply_organizations_thesaurus(root_dir)

    #
    # Generate a list of raw entries for the descriptors thesaurus.
    #
    file = os.path.join(root_dir, "databases/_main.csv.zip")
    data_frame = pd.read_csv(file, encoding="utf-8", compression="zip")
    words = (
        data_frame["raw_descriptors"]
        .dropna()
        .str.split("; ", expand=False)
        .explode()
        .str.strip()
        .drop_duplicates()
        .sort_values()
        .to_list()
    )

    #
    # Creates a thesaurus with an entry for each differnt descriptor
    #
    thesaurus_file = os.path.join(root_dir, "thesauri/descriptors.the.txt")
    with open(thesaurus_file, "w", encoding="utf-8") as f:
        for word in words:
            f.write(word + "\n")
            f.write("    " + word + "\n")

    apply_descriptors_thesaurus(root_dir)

    _create_abbreviations_thesaurus(root_dir)

    ## ------------------------------------------------------------------------------------------

    # Removed: _adds_countries_and_regions_to_stopwords(root_dir)

    report_imported_records_per_file(root_dir)

    message("Process finished!!!")

    #
    # Elapsed time report
    end_time = time.time()
    print("Execution time:", round(end_time - start_time, 1), "seconds")
