# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================


Example:

    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus

    >>> # Restore the column values to initial values
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()

    >>> from techminer2.manuscript.discussion import ClusterDefinition
    >>> (
    ...     ClusterDefinition()
    ...     #
    ...     # FIELD:
    ...     .with_field("descriptors")
    ...     .having_terms_in_top(30)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # TEXT:
    ...     .with_core_area("fintech")
    ...     .with_word_length((200, 400, 300))
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )

       Cluster  ...                                              Terms
    0        0  ...  FINTECH 38:6131; THE_FINANCIAL_INDUSTRY 09:200...
    1        1  ...  TECHNOLOGIES 15:1633; FINANCIAL_TECHNOLOGIES 1...
    <BLANKLINE>
    [2 rows x 4 columns]

"""
import os

from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2._internals.load_template import internal_load_template
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_occurrence.user import (
    DocumentsByClusterMapping,
    TermsByClusterSummary,
)


class ClusterDefinition(
    ParamsMixin,
):
    """:meta private:"""

    # -------------------------------------------------------------------------
    def internal__load_cluster_definition_template(self):
        self.definition_template = internal_load_template(
            "internals.genai.cluster_definition.txt"
        )

    # -------------------------------------------------------------------------
    def internal__generate_terms_by_cluster_mapping(self):
        data_frame = (
            TermsByClusterSummary()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )

        data_frame["Terms"] = data_frame["Terms"].str.split("; ")
        data_frame["Terms"] = data_frame["Terms"].apply(
            lambda x: [y.split()[0] for y in x]
        )
        data_frame["Terms"] = data_frame["Terms"].apply(
            lambda x: [y.strip() for y in x]
        )
        data_frame["Terms"] = data_frame["Terms"].str.join("; ")
        self.terms_by_cluster_mapping = {
            key: value for key, value in zip(data_frame["Cluster"], data_frame["Terms"])
        }

    # -------------------------------------------------------------------------
    def internal__generate_documents_by_cluster_mapping(self):
        self.documents_by_cluster_mapping = (
            DocumentsByClusterMapping()
            .update(**self.params.__dict__)
            .with_field("descriptors")
            .run()
        )

    # -------------------------------------------------------------------------
    def internal__generate_raw_summaries_by_cluster_mapping(self):

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        summaries_by_cluster = {}

        for cluster in tqdm(
            range(self.terms_by_cluster_mapping.__len__()),
            total=self.terms_by_cluster_mapping.__len__(),
            desc="  Clusters ",
        ):

            cluster_keywords = self.terms_by_cluster_mapping[cluster]
            cluster_keywords = cluster_keywords.lower().replace("_", " ")

            documents = self.documents_by_cluster_mapping.get(cluster, [])
            documents = documents[:100]
            documents = [documents[i : i + 10] for i in range(0, len(documents), 10)]

            answers = []

            for docs in tqdm(
                documents, total=len(documents), desc="    Chunks ", leave=False
            ):

                docs = "\n\n" + "\n---\n\n".join(docs) + "\n\n"

                prompt = self.definition_template.format(
                    core_area=self.params.core_area,
                    word_length=self.params.word_length[0],
                    abstracts=docs,
                    cluster_keywords=cluster_keywords,
                )

                try:
                    response = client.responses.create(
                        model="gpt-4.1",
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
        # delete the content of the directory if it exists
        if os.path.exists(path):
            for file in os.listdir(path):
                file_path = os.path.join(path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)

        os.makedirs(path, exist_ok=True)

        self.cluster_full_definitions = {}

        for i_cluster in tqdm(
            range(self.raw_summaries_by_cluster.__len__()),
            total=self.raw_summaries_by_cluster.__len__(),
            desc="  Final summaries ",
        ):

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
                text = [definition[section] for definition in definitions]
                text = "\n\n--\n\n".join(text)
                template = internal_load_template(
                    f"internals.genai.cluster_{section}_summary.txt"
                )
                prompt = template.format(
                    core_area=self.params.core_area,
                    word_length=self.params.word_length[1],
                    paragraphs_to_combine=text,
                )

                client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

                try:
                    response = client.responses.create(
                        model="gpt-4.1",
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

        template = internal_load_template("internals.genai.cluster_short_summary.txt")

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        for i_cluster in tqdm(
            range(self.cluster_full_definitions.__len__()),
            total=self.cluster_full_definitions.__len__(),
            desc="  Short summaries ",
        ):

            paragraphs_to_combine = "\n\n".join(
                self.cluster_full_definitions[i_cluster]
            )

            prompt = template.format(
                core_area=self.params.core_area,
                word_length=self.params.word_length[2],
                paragraphs_to_combine=paragraphs_to_combine,
            )

            try:
                response = client.responses.create(
                    model="gpt-4.1",
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
