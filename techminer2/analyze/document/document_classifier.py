# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

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
