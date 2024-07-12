"""Setup module for TechMiner2+"""

# import nltk
from setuptools import setup

# from setuptools.command.build_py import build_py

# class BuildPyCommand(build_py):
#     def run(self):
#         #
#         import nltk

#         nltk.download("punkt")
#         nltk.download("brown")
#         # nltk.download("stopwords")
#         # nltk.download("averaged_perceptron_tagger")
#         #
#         build_py.run(self)


# def _post_install():
#     nltk.download("punkt")
#     nltk.download("brown")
#     nltk.download("stopwords")
#     nltk.download("averaged_perceptron_tagger")


setup(
    # cmdclass={"build_py": BuildPyCommand},
    name="techminer2",
    version="2023.12.04",
    author="Juan D. Velasquez",
    author_email="jdvelasq@unal.edu.co",
    license="MIT",
    url="http://github.com/jdvelasq/techminer2",
    description="Tech Mining Analysis of Bibliograpy",
    long_description="Tech Mining Analysis of Bibliograpy",
    keywords="bibliograpy",
    platforms="any",
    provides=["techminer2"],
    install_requires=[
        "cdlib",
        "duckdb",
        "fuzzywuzzy",
        "igraph",
        "leidenalg",
        "networkx",
        "nltk",
        "pandas",
        "plotly",
        "pyspellchecker",
        "python-Levenshtein",
        "PyYAML",
        "scikit-learn",
        "sumy",
        "tabulate",
        "textblob",
        "wordcloud",
    ],
    packages=[
        #
        "techminer2.core",
        "techminer2.core.thesaurus",
        #
        "techminer2.helpers",
        #
        "techminer2._common",
        #
        "techminer2._files",
        #
        "techminer2.fields.further_processing",
        "techminer2.fields.tests",
        "techminer2.fields",
        #
        "techminer2.ingest.field_importers",
        "techminer2.ingest",
        #
        "techminer2.metrics.globals",
        "techminer2.metrics",
        #
        "techminer2.raw",
        #
        "techminer2.refine.thesaurus.countries",
        "techminer2.refine.thesaurus.organizations",
        "techminer2.refine.thesaurus.references",
        "techminer2.refine.thesaurus.descriptors",
        "techminer2.refine.thesaurus",
        "techminer2.refine",
        #
        "techminer2.report",
        #
        "techminer2.science_mapping.bibliographic_coupling.authors",
        "techminer2.science_mapping.bibliographic_coupling.countries",
        "techminer2.science_mapping.bibliographic_coupling.documents",
        "techminer2.science_mapping.bibliographic_coupling.organizations",
        "techminer2.science_mapping.bibliographic_coupling.sources",
        "techminer2.science_mapping.bibliographic_coupling",
        #
        "techminer2.science_mapping.citation.publications",
        "techminer2.science_mapping.citation.network.authors",
        "techminer2.science_mapping.citation.network.countries",
        "techminer2.science_mapping.citation.network.documents",
        "techminer2.science_mapping.citation.network.organizations",
        "techminer2.science_mapping.citation.network.sources",
        "techminer2.science_mapping.citation.network",
        "techminer2.science_mapping.citation",
        #
        "techminer2.science_mapping.co_authorship.network.authors",
        "techminer2.science_mapping.co_authorship.network.countries",
        "techminer2.science_mapping.co_authorship.network.organizations",
        "techminer2.science_mapping.co_authorship.network",
        "techminer2.science_mapping.co_authorship",
        #
        "techminer2.science_mapping.co_citation.cited_authors",
        "techminer2.science_mapping.co_citation.cited_references",
        "techminer2.science_mapping.co_citation.cited_sources",
        "techminer2.science_mapping.co_citation",
        #
        "techminer2.science_mapping.co_occurrence",
        #
        "techminer2.science_mapping.topic_modeling.berttopic",
        "techminer2.science_mapping.topic_modeling.lda",
        "techminer2.science_mapping.topic_modeling.nmf",
        "techminer2.science_mapping.topic_modeling",
        #
        "techminer2.science_mapping",
        #
        "techminer2.search",
        #
        "techminer2.tech_mining.co_occurrence",
        "techminer2.tech_mining.correlation",
        "techminer2.tech_mining.document",
        "techminer2.tech_mining.emergence",
        #
        "techminer2.tech_mining.pca.cooc_matrix.brute_force",
        "techminer2.tech_mining.pca.cooc_matrix.hierarchical",
        "techminer2.tech_mining.pca.cooc_matrix.kmeans",
        "techminer2.tech_mining.pca.cooc_matrix.pcd",
        "techminer2.tech_mining.pca.cooc_matrix",
        #
        "techminer2.tech_mining.pca.tfidf_matrix.brute_force",
        "techminer2.tech_mining.pca.tfidf_matrix.hierarchical",
        "techminer2.tech_mining.pca.tfidf_matrix.kmeans",
        "techminer2.tech_mining.pca.tfidf_matrix.pcd",
        "techminer2.tech_mining.pca.tfidf_matrix",
        #
        "techminer2.tech_mining.pca",
        #
        "techminer2.tech_mining.research_agenda.network",
        "techminer2.tech_mining.research_agenda",
        #
        "techminer2.tech_mining.svd.cooc_matrix.brute_force",
        "techminer2.tech_mining.svd.cooc_matrix.hierarchical",
        "techminer2.tech_mining.svd.cooc_matrix.kmeans",
        "techminer2.tech_mining.svd.cooc_matrix",
        #
        "techminer2.tech_mining.svd.tfidf_matrix.brute_force",
        "techminer2.tech_mining.svd.tfidf_matrix.hierarchical",
        "techminer2.tech_mining.svd.tfidf_matrix.kmeans",
        "techminer2.tech_mining.svd.tfidf_matrix",
        #
        "techminer2.tech_mining.svd",
        #
        "techminer2.tech_mining",
        #
        "techminer2.thesauri_data",
        #
        "techminer2.tools.associations",
        "techminer2.tools",
        #
        "techminer2.word_lists",
        #
        "techminer2",
    ],
    package_dir={"techminer2": "techminer2"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)

# _post_install()
