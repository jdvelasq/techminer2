# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering, KMeans

from ..._read_records import read_records
from ...analyze import tfidf
from ...format_report_for_records import format_report_for_records
from ...make_report_dir import make_report_dir


class DocumentClassifier:
    def __init__(
        self,
    ):
        #
        self.tf_matrix = None
        self.n_themes = None
        self.estimator = None
        self.records = None
        self.method = None
        self.root_dir = None
        self.labels = None

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

        self.records = read_records(
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

    def kmeans(
        self,
        #
        # KMEANS PARAMS:
        n_themes=8,
        init="k-means++",
        n_init=10,
        max_iter=300,
        tol=0.0001,
        algorithm="auto",
        random_state=0,
    ):
        self.method = "kmeans"
        self.n_themes = n_themes
        self.estimator = KMeans(
            n_clusters=n_themes,
            init=init,
            n_init=n_init,
            max_iter=max_iter,
            tol=tol,
            algorithm=algorithm,
            random_state=random_state,
        )

    def hierarchical(
        self,
        #
        # HIERARCHICAL PARAMS:
        n_themes=None,
        metric=None,
        memory=None,
        connectivity=None,
        compute_full_tree="auto",
        linkage="ward",
        distance_threshold=None,
    ):
        self.method = "hierarchical"
        self.n_themes = n_themes
        self.estimator = AgglomerativeClustering(
            n_clusters=n_themes,
            metric=metric,
            memory=memory,
            connectivity=connectivity,
            compute_full_tree=compute_full_tree,
            linkage=linkage,
            distance_threshold=distance_threshold,
        )

    def fit(self):
        self.estimator.fit(self.tf_matrix)

    def report(self):
        #
        # Assigns the cluster to the record
        self.records["theme"] = self.estimator.labels_

        #
        # Creates the report directory
        target_dir = f"document_clustering/{self.method}"
        make_report_dir(self.root_dir, target_dir)

        #
        #
        for theme in range(self.n_themes):
            records = self.records.loc[self.records.theme == theme, :]
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

    def contingecy_table(self):
        #
        # Formats the theme label
        if self.n_themes > 1:
            n_zeros = int(np.log10(self.n_themes - 1)) + 1
        else:
            n_zeros = 1
        fmt = "TH_{:0" + str(n_zeros) + "d}"

        #
        # Assigns the cluster to the record
        tf_matrix = self.tf_matrix.copy()
        tf_matrix["theme"] = [fmt.format(label) for label in self.estimator.labels_]
        data_frame = tf_matrix.groupby("theme").sum()
        data_frame = data_frame.T
        return data_frame

    def themes_summary(self):
        #
        # Formats the theme label
        table = self.contingecy_table()
        themes = table.idxmax(axis=1)

        result = {}
        for word, theme in zip(themes.index, themes):
            if theme not in result:
                result[theme] = []
            result[theme].append(word)

        labels = sorted(result.keys())
        n_terms = [len(result[label]) for label in labels]
        terms = ["; ".join(result[label]) for label in labels]
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

    def themes(self):
        #
        #
        table = self.contingecy_table()
        themes = table.idxmax(axis=1)

        result = {}
        for word, theme in zip(themes.index, themes):
            if theme not in result:
                result[theme] = []
            result[theme].append(word)

        communities = pd.DataFrame.from_dict(result, orient="index").T
        communities = communities.fillna("")
        communities = communities.sort_index(axis=1)
        return communities
