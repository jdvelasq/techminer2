# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import numpy as np
import pandas as pd
from sklearn.decomposition import NMF, LatentDirichletAllocation

from ...helpers.format_report_for_records import format_report_for_records
from ...helpers.make_report_dir import make_report_dir
from ...core.read_filtered_database import read_filtered_database
from ...metrics import tfidf


class TopicModeler:
    def __init__(self):
        #
        self.tf_matrix = None
        self.estimator = None
        self.records = None
        self.root_dir = None
        self.method = None
        self.n_components = None
        self.components = None
        self.documents_by_theme = None
        self.root_dir = None

    def build_tf_matrix(
        self,
        #
        # TF PARAMS:
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
        # DATABASE PARAMS:
        root_dir="./",
        database="main",
        year_filter=(None, None),
        cited_by_filter=(None, None),
        **filters,
    ):
        self.root_dir = root_dir

        self.records = read_filtered_database(
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        self.tf_matrix = tfidf(
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
            # TF-IDF parameters:
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
        )

    def nmf(
        self,
        #
        # NMF PARAMS:
        n_components,
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
    ):
        self.method = "nmf"
        self.n_components = n_components
        self.estimator = NMF(
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
        )

    def lda(
        self,
        #
        # LDA PARAMS:
        n_components=10,
        learning_decay=0.7,
        learning_offset=50.0,
        max_iter=10,
        batch_size=128,
        evaluate_every=-1,
        perp_tol=0.1,
        mean_change_tol=0.001,
        max_doc_update_iter=100,
        random_state=0,
    ):
        self.method = "lda"
        self.n_components = n_components
        self.estimator = LatentDirichletAllocation(
            n_components=n_components,
            learning_decay=learning_decay,
            learning_offset=learning_offset,
            max_iter=max_iter,
            batch_size=batch_size,
            evaluate_every=evaluate_every,
            perp_tol=perp_tol,
            mean_change_tol=mean_change_tol,
            max_doc_update_iter=max_doc_update_iter,
            random_state=random_state,
        )

    def fit(self):
        self.estimator.fit(self.tf_matrix)

    def compute_components(self):
        n_zeros = int(np.log10(self.n_components - 1)) + 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        self.components = pd.DataFrame(
            self.estimator.components_,
            index=[fmt.format(i) for i in range(self.n_components)],
            columns=self.tf_matrix.columns,
        )

    def compute_documents_by_theme(self):
        #
        #
        # n_zeros = int(np.log10(self.n_components - 1)) + 1
        # fmt = "TH_{:0" + str(n_zeros) + "d}"

        doc_topic_matrix = pd.DataFrame(
            self.estimator.transform(self.tf_matrix),
            index=self.tf_matrix.index,
            columns=[i for i in range(self.n_components)],
        )

        # extracts the column with the maximum value for each row
        assigned_topics_to_documents = doc_topic_matrix.idxmax(axis=1)

        self.documents_by_theme = {}
        for article, theme in zip(
            assigned_topics_to_documents.index, assigned_topics_to_documents
        ):
            if theme not in self.documents_by_theme:
                self.documents_by_theme[theme] = []
            self.documents_by_theme[theme].append(article)

        # return self.documents_by_theme

    def terms_by_theme_summary(self, n_top_terms):
        #
        #
        n_zeros = int(np.log10(self.n_components - 1)) + 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        #
        # Formats the theme label
        theme_term_matrix = self.estimator.components_

        terms_by_topic = {}
        for i, topic in enumerate(theme_term_matrix):
            top_terms_idx = topic.argsort()[: -n_top_terms - 1 : -1]
            top_terms = self.tf_matrix.columns[top_terms_idx]
            terms_by_topic[fmt.format(i)] = top_terms

        labels = sorted(terms_by_topic.keys())
        n_terms = [len(terms_by_topic[label]) for label in labels]
        terms = ["; ".join(terms_by_topic[label]) for label in labels]
        percentage = [round(n_term / sum(n_terms) * 100, 1) for n_term in n_terms]

        data_frame = pd.DataFrame(
            {
                "Theme": labels,
                "Num Terms": n_terms,
                "Percentage": percentage,
                "Terms": terms,
            }
        )

        return data_frame

    def report(self):
        #
        # Creates the report directory
        target_dir = f"topic_modeling/{self.method}"
        make_report_dir(self.root_dir, target_dir)

        #
        #
        for theme in range(self.n_components):
            #
            docs = self.documents_by_theme[theme]

            records = self.records.loc[self.records.article.map(lambda x: x in docs), :]
            records = records.sort_values(
                ["global_citations", "local_citations", "year"], ascending=False
            )

            file_name = f"theme_{theme:03d}_abstracts_report.txt"
            format_report_for_records(
                root_dir=self.root_dir,
                target_dir=target_dir,
                records=records,
                report_filename=file_name,
            )

    def themes(self, n_top_terms):
        #
        #
        n_zeros = int(np.log10(self.n_components - 1)) + 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        #
        # Formats the theme label
        theme_term_matrix = self.estimator.components_

        terms_by_topic = {}
        for i, topic in enumerate(theme_term_matrix):
            top_terms_idx = topic.argsort()[: -n_top_terms - 1 : -1]
            top_terms = self.tf_matrix.columns[top_terms_idx]
            terms_by_topic[fmt.format(i)] = top_terms

        communities = pd.DataFrame.from_dict(terms_by_topic, orient="index").T
        communities = communities.fillna("")
        communities = communities.sort_index(axis=1)
        return communities
