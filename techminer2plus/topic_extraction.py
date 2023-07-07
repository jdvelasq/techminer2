"""Topic extraction with LDA/NMF"""


import textwrap
from dataclasses import dataclass

import numpy as np
import pandas as pd

from .tfidf import tfidf


# pylint: disable=too-many-instance-attributes
@dataclass
class Themes:
    """Emergent themes extraction"""

    #
    # RESULTS
    n_themes_: int
    terms_by_theme_: dict
    documents_by_theme_: dict

    def __repr__(self):
        text = "Themes("
        text += f"n-themes={self.n_themes_}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")

        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def topic_extraction(
    #
    # TFIDF PARAMS:
    field,
    is_binary=False,
    cooc_within=1,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # ESTIMATOR PARAMS:
    n_components=1,
    estimator_class=None,
    estimator_parms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Emergent themes extraction with LDA"""

    def build_tfidf_matrix():
        return tfidf(
            #
            # TF PARAMS:
            field=field,
            is_binary=is_binary,
            cooc_within=cooc_within,
            #
            # ITEM FILTERS:
            top_n=top_n,
            occ_range=occ_range,
            gc_range=gc_range,
            custom_items=custom_items,
            #
            # TFIDF PARAMS:
            norm=None,
            use_idf=False,
            smooth_idf=False,
            sublinear_tf=False,
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        ).df_

    def build_estimator():
        return estimator_class(n_components, **estimator_parms)

    def get_components():
        """Get the components as a dataframe"""
        n_zeros = int(np.log10(n_components - 1)) + 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        return pd.DataFrame(
            estimator.components_,
            index=[fmt.format(i) for i in range(n_components)],
            columns=tfidf_matrix.columns,
        )

    def assign_terms_to_themes():
        """Assign terms to themes"""

        items_by_theme_matrix = components.copy().transpose()
        assigned_themes_to_terms = items_by_theme_matrix.idxmax(axis=1)

        items_by_theme = {}
        for article, theme in assigned_themes_to_terms.items():
            if theme not in items_by_theme:
                items_by_theme[theme] = []
            items_by_theme[theme].append(article)

        return items_by_theme

    def count_themes_with_assigned_terms():
        """Count the number of terms by theme"""

        n_themes = 0
        for _, value in terms_by_theme.items():
            if len(value) > 0:
                n_themes += 1
        return n_themes

    def assign_documents_to_themes():
        """Assign documents to themes"""

        n_zeros = int(np.log10(n_components - 1)) + 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        doc_theme_matrix = pd.DataFrame(
            estimator.transform(tfidf_matrix),
            index=tfidf_matrix.index,
            columns=[fmt.format(i) for i in range(n_components)],
        )

        # extracts the column with the maximum value for each row
        assigned_themes_to_documents = doc_theme_matrix.idxmax(axis=1)

        documents_by_theme = {}
        for article, theme in assigned_themes_to_documents.items():
            if theme not in documents_by_theme:
                documents_by_theme[theme] = []
            documents_by_theme[theme].append(article)

        return documents_by_theme

    def reorder_themes(terms_by_theme, documents_by_theme):
        """Reorder themes based on the number of assigned items"""

        n_zeros = int(np.log10(n_components)) + 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        # Sort themes by number of assigned items
        themes_by_n_items = sorted(
            terms_by_theme.items(), key=lambda x: len(x[1]), reverse=True
        )

        # Reorder themes
        new_terms_by_theme = {}
        new_documents_by_theme = {}
        for i, (theme, terms) in enumerate(themes_by_n_items):
            new_terms_by_theme[fmt.format(i)] = terms
            new_documents_by_theme[fmt.format(i)] = documents_by_theme[theme]

        return new_terms_by_theme, new_documents_by_theme

    #
    # MAIN CODE:
    #

    tfidf_matrix = build_tfidf_matrix()

    # Check if the themes with terms is equal to the number f specified
    # components. If not, we need to re-run the estimator
    max_runs = n_components + 1
    n_themes_with_terms = n_components

    for _ in range(max_runs):
        n_components = n_themes_with_terms

        estimator = build_estimator()
        estimator.fit(tfidf_matrix)
        components = get_components()
        terms_by_theme = assign_terms_to_themes()

        n_themes_with_terms = count_themes_with_assigned_terms()
        if n_themes_with_terms == n_components:
            break

    documents_by_theme = assign_documents_to_themes()

    terms_by_theme, documents_by_theme = reorder_themes(
        terms_by_theme, documents_by_theme
    )

    return Themes(
        n_themes_=n_components,
        terms_by_theme_=terms_by_theme,
        documents_by_theme_=documents_by_theme,
    )
