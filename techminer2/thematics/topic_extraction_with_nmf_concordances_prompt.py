# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Topic Extraction with NMF concordances prompt
===============================================================================

Topic extraction using non-negative matrix factorization.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

>>> tm2.topic_extraction_with_nmf_concordances_prompt(
...     field="author_keywords",
...     occ_range=(2, None),
...     n_components=10,
...     root_dir=root_dir,
... )
--INFO-- Prompts were generated in 'data/regtech/reports/topic_extraction_NMF'

"""
import os
import os.path

from .._read_records import read_records

# from .concordances_prompt_from_records import concordances_prompt_from_records
from .topic_extraction_with_nmf import topic_extraction_with_nmf


def topic_extraction_with_nmf_concordances_prompt(
    #
    # TFIDF PARAMS:
    field: str,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NMF PARAMS:
    n_components=10,
    init=None,
    solver="cd",
    beta_loss="frobenius",
    tol=0.0001,
    max_iter=200,
    alpha_W=0.0,
    alpha_H=0.0,
    l1_ratio=0.0,
    shuffle=False,
    random_state=0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    (
        n_components,
        terms_by_theme,
        documents_by_theme,
    ) = topic_extraction_with_nmf(
        #
        # TFIDF PARAMS:
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
        # NMF PARAMS:
        n_components=n_components,
        init=init,
        solver=solver,
        beta_loss=beta_loss,
        tol=tol,
        max_iter=max_iter,
        alpha_W=alpha_W,
        alpha_H=alpha_H,
        l1_ratio=l1_ratio,
        shuffle=shuffle,
        random_state=random_state,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    path = os.path.join(root_dir, "reports", "topic_extraction_NMF")
    if os.path.exists(path):
        files = os.listdir(path)
        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)
    else:
        os.makedirs(path)

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    # terms_by_theme is a dictionary with themes as keys and terms as values
    # {'TH_00': ['REGTECH 28:329', 'FINTECH 12:249', 'SEMANTIC_TECHNOLOGIES 02:041', ....
    # documents_by_theme is a dictionary with themes as keys and documents as values
    # {'TH_00': ['Anagnostopoulos I, 2..., V100, P7', ...

    for theme, terms in terms_by_theme.items():
        documents = documents_by_theme[theme]

        for term in terms:
            #
            term = term.split(" ")[:-1]
            term = " ".join(term)

            file_name = f"concordances_{theme}_{term}.txt"
            file_path = os.path.join(root_dir, "reports", "topic_extraction_NMF", file_name)
            records_by_theme = records[records.article.isin(documents)]

            prompt = concordances_prompt_from_records(
                search_for=term,
                top_n=100,
                records=records_by_theme,
            )

            if "Paragraph" not in prompt:
                continue

            with open(file_path, "w", encoding="utf-8") as file:
                print(prompt, file=file)

    print(
        f"--INFO-- Prompts were generated in '{os.path.join(root_dir, 'reports', 'topic_extraction_NMF')}'"
    )
