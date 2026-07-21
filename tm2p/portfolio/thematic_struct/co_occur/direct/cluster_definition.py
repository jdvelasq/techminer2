"""
ClusterDefinition
===============================================================================

Smoke tests:

    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.direct import ClusterDefinition
    >>> (
    ...     ClusterDefinition()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     #
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(2)    
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.JACCARD)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # TEXT:
    ...     .with_core_area("fintech")
    ...     .using_word_length(400)
    ...     .using_gpt_model("gpt-4.1")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )



"""

import os

from openai import OpenAI  # type: ignore
from tqdm import tqdm  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data.templates.load_builtin_template import (
    load_builtin_template,
)
from tm2p.enum import Field
from tm2p.enum.order_by import RecordOrderBy
from tm2p.ingest.rec.rec_view import RecordViewer

CLUSTER = "CLUSTER"
PERCENTAGE = "PERCENTAGE"
UNITS = "UNITS"
REC_ID = "REC_ID"


class ClusterDefinition(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_cluster_definition_template(self):
        self.definition_template = load_builtin_template(
            "internals.genai.cluster_definition.txt"
        )

    # -------------------------------------------------------------------------
    def internal__generate_terms_by_cluster_mapping(self):

        from .cluster_composition import ClusterComposition

        df = ClusterComposition().update(**self.params.__dict__).using_counters(False).run()  # type: ignore

        df[UNITS] = df[UNITS].str.split("; ")
        df[UNITS] = df[UNITS].apply(lambda x: [y.split()[0] for y in x])
        df[UNITS] = df[UNITS].apply(lambda x: [y.strip() for y in x])
        df[UNITS] = df[UNITS].str.join("; ")

        self.cluster_coverages = df[PERCENTAGE].to_list()

        self.terms_by_cluster_mapping = {
            key: value for key, value in zip(df[CLUSTER], df[UNITS])
        }

    # -------------------------------------------------------------------------
    def internal__generate_documents_by_cluster_mapping(self):

        from tm2p.ingest.rec import RecordViewer

        from .cluster_to_documents_soft import ClusterToDocumentsSoft

        cluster_to_documents = (
            ClusterToDocumentsSoft()  # type: ignore
            .update(**self.params.__dict__)
            .run()
        )

        self.documents_by_cluster_mapping = {}

        for cluster, documents in cluster_to_documents.items():

            docs = (
                RecordViewer()
                #
                .with_source_field(Field.ABSTR_RAW)
                .update(**self.params.__dict__)
                .where_records_match({Field.REC_ID: documents})
                .where_records_ordered_by(RecordOrderBy.YEAR_NEWEST)
                .run()
            )

            self.documents_by_cluster_mapping[cluster] = docs

    # -------------------------------------------------------------------------
    def internal__generate_raw_summaries_by_cluster_mapping(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        summaries_by_cluster = {}

        for cluster in tqdm(
            range(self.terms_by_cluster_mapping.__len__()),
            total=self.terms_by_cluster_mapping.__len__(),
            desc="         Clusters ",
            ncols=80,
        ):

            cluster_keywords = self.terms_by_cluster_mapping[cluster]
            cluster_keywords = cluster_keywords.lower().replace("_", " ")

            documents = self.documents_by_cluster_mapping.get(cluster, [])
            documents = documents[:100]
            documents = [documents[i : i + 10] for i in range(0, len(documents), 10)]

            answers = []

            for docs in tqdm(
                documents,
                total=len(documents),
                desc="           Chunks ",
                leave=False,
                ncols=80,
            ):

                docs = "\n\n" + "\n---\n\n".join(docs) + "\n\n"

                prompt = self.definition_template.format(
                    core_area=self.params.core_area,
                    word_length=self.params.word_length,  # type: ignore
                    abstracts=docs,
                    cluster_keywords=cluster_keywords,
                    cluster_name=self.params.cluster_names[cluster],  # type: ignore
                    cluster_coverage=self.cluster_coverages[cluster],  # type: ignore
                )

                try:
                    response = client.responses.create(
                        model=self.params.gpt_model,
                        input=prompt,
                    )
                    answer = response.output_text
                    answer = eval(answer)
                    answers.append(answer)

                except Exception as e:
                    print(f"Error processing: {e}")

                answers.append(answer)

            summaries_by_cluster[cluster] = answers

        self.raw_summaries_by_cluster = summaries_by_cluster

    # -------------------------------------------------------------------------
    def internal__generate_full_summaries_by_cluster(self):

        path = os.path.join(
            self.params.root_directory, "outputs", "section_5_discussion"
        )

        if os.path.exists(path):
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path) and file.endswith("summary.txt"):
                    os.remove(file_path)

        os.makedirs(path, exist_ok=True)

        self.cluster_full_definitions = {}

        for i_cluster in tqdm(
            range(self.raw_summaries_by_cluster.__len__()),
            total=self.raw_summaries_by_cluster.__len__(),
            desc="  Final summaries ",
            ncols=80,
        ):

            cluster_keywords = self.terms_by_cluster_mapping[i_cluster]
            cluster_keywords = cluster_keywords.lower().replace("_", " ")

            complete_text = []
            self.cluster_full_definitions[i_cluster] = []

            definitions = self.raw_summaries_by_cluster[i_cluster]

            for section in [
                "definition",
                "trends",
                "challenges",
                "opportunities",
                "value",
            ]:
                text = [
                    definition[section]
                    for definition in definitions
                    if section in definition
                ]
                text = "\n\n--\n\n".join(text)
                template = load_builtin_template(
                    f"internals.genai.cluster_{section}_summary.txt"
                )
                prompt = template.format(
                    core_area=self.params.core_area,
                    word_length=self.params.word_length,  # type: ignore
                    paragraphs_to_combine=text,
                    cluster_keywords=cluster_keywords,
                )

                client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

                try:
                    response = client.responses.create(
                        model=self.params.gpt_model,
                        input=prompt,
                    )
                    answer = response.output_text

                    self.cluster_full_definitions[i_cluster].append(answer)

                    complete_text.append(section.upper() + ":\n\n")
                    complete_text.append(answer)
                    complete_text.append("\n\n")

                except Exception as e:
                    print(f"Error processing: {e}")

            with open(
                os.path.join(
                    self.params.root_directory,
                    "outputs",
                    "section_5_discussion",
                    f"cluster_{i_cluster}_full_summary.txt",
                ),
                "w",
            ) as file:
                file.writelines(complete_text)

    # -------------------------------------------------------------------------
    def internal__generate_short_summaries_by_cluster(self):

        template = load_builtin_template("internals.genai.cluster_short_summary.txt")

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        for i_cluster in tqdm(
            range(self.cluster_full_definitions.__len__()),
            total=self.cluster_full_definitions.__len__(),
            desc="  Short summaries ",
            ncols=80,
        ):

            cluster_keywords = self.terms_by_cluster_mapping[i_cluster]
            cluster_keywords = cluster_keywords.lower().replace("_", " ")

            paragraphs_to_combine = "\n\n".join(
                self.cluster_full_definitions[i_cluster]
            )

            prompt = template.format(
                core_area=self.params.core_area,
                word_length=self.params.word_length,  # type: ignore
                paragraphs_to_combine=paragraphs_to_combine,
                cluster_keywords=cluster_keywords,
            )

            try:
                response = client.responses.create(
                    model=self.params.gpt_model,
                    input=prompt,
                )
                answer = response.output_text

                with open(
                    os.path.join(
                        self.params.root_directory,
                        "outputs",
                        "section_5_discussion",
                        f"cluster_{i_cluster}_short_summary.txt",
                    ),
                    "w",
                ) as file:
                    file.writelines(answer)

            except Exception as e:
                print(f"Error processing: {e}")

    # -------------------------------------------------------------------------
    def run(self):
        """:meta private:"""

        self.internal__load_cluster_definition_template()
        self.internal__generate_terms_by_cluster_mapping()
        self.internal__generate_documents_by_cluster_mapping()
        self.internal__generate_raw_summaries_by_cluster_mapping()
        self.internal__generate_full_summaries_by_cluster()
        self.internal__generate_short_summaries_by_cluster()
