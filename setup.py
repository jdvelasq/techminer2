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
    version="2023.07.21",
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
        # "nltk",
        # "cdlib",
        # "fuzzywuzzy",
        # "networkx",
        # "pandas",
        # "plotly",
        # "python-Levenshtein",
        # "PyYAML",
        # "scikit-learn",
        # "pyspellchecker",
        # "sumy",
        # "textblob",
        # "wordcloud",
        # # "kelaido",
        # "igraph",
        # "leidenalg",
    ],
    packages=[
        "techminer2",
        "techminer2._files",
        #
        # ======================================================================
        "techminer2.co_occurrence_analysis",
        "techminer2.co_occurrence_analysis.associations",
        "techminer2.co_occurrence_analysis.associations.graphs",
        # "techminer2.co_occurrence_analysis.associations.tables",
        "techminer2.co_occurrence_analysis.graphs",
        "techminer2.co_occurrence_analysis.word_pairs",
        #
        # ======================================================================
        # "techminer2.co_word_analysis",
        #
        # ======================================================================
        "techminer2.correlation_analysis",
        #
        # ======================================================================
        "techminer2.emergence_analysis",
        #
        # ======================================================================
        "techminer2.factor_analysis",
        "techminer2.factor_analysis.co_occurrences",
        "techminer2.factor_analysis.co_occurrences.kernel_pca",
        "techminer2.factor_analysis.co_occurrences.pca",
        "techminer2.factor_analysis.co_occurrences.svd",
        "techminer2.factor_analysis.tfidf",
        "techminer2.factor_analysis.tfidf.kernel_pca",
        "techminer2.factor_analysis.tfidf.pca",
        "techminer2.factor_analysis.tfidf.svd",
        #
        # ======================================================================
        "techminer2.ingest",
        #
        # ======================================================================
        "techminer2.network_analysis",
        #
        "techminer2.network_analysis.bibliographic_coupling",
        #
        "techminer2.network_analysis.bibliographic_coupling.authors",
        "techminer2.network_analysis.bibliographic_coupling.countries",
        "techminer2.network_analysis.bibliographic_coupling.documents",
        "techminer2.network_analysis.bibliographic_coupling.organizations",
        "techminer2.network_analysis.bibliographic_coupling.sources",
        #
        "techminer2.network_analysis.citation",
        #
        "techminer2.network_analysis.citation.authors",
        "techminer2.network_analysis.citation.countries",
        "techminer2.network_analysis.citation.documents",
        "techminer2.network_analysis.citation.organizations",
        "techminer2.network_analysis.citation.publications",
        "techminer2.network_analysis.citation.references",
        "techminer2.network_analysis.citation.sources",
        #
        "techminer2.network_analysis.co_authorship",
        #
        "techminer2.network_analysis.co_authorship.authors",
        "techminer2.network_analysis.co_authorship.countries",
        "techminer2.network_analysis.co_authorship.organizations",
        #
        "techminer2.network_analysis.co_citation",
        #
        "techminer2.network_analysis.co_citation.cited_authors",
        "techminer2.network_analysis.co_citation.cited_references",
        "techminer2.network_analysis.co_citation.cited_sources",
        #
        "techminer2.network_analysis.co_occurrence",
        "techminer2.network_analysis.co_occurrence.abstract_nlp_phrases",
        "techminer2.network_analysis.co_occurrence.author_keywords",
        "techminer2.network_analysis.co_occurrence.descriptors",
        "techminer2.network_analysis.co_occurrence.index_keywords",
        "techminer2.network_analysis.co_occurrence.keywords",
        "techminer2.network_analysis.co_occurrence.nlp_phrases",
        "techminer2.network_analysis.co_occurrence.title_nlp_phrases",
        #
        "techminer2.network_analysis.thematic_map",
        "techminer2.network_analysis.thematic_map.abstract_nlp_phrases",
        "techminer2.network_analysis.thematic_map.author_keywords",
        "techminer2.network_analysis.thematic_map.descriptors",
        "techminer2.network_analysis.thematic_map.index_keywords",
        "techminer2.network_analysis.thematic_map.keywords",
        "techminer2.network_analysis.thematic_map.nlp_phrases",
        "techminer2.network_analysis.thematic_map.title_nlp_phrases",
        #
        # ======================================================================
        "techminer2.performance_analysis",
        #
        "techminer2.performance_analysis.fields",
        "techminer2.performance_analysis.fields.authors",
        "techminer2.performance_analysis.fields.countries",
        "techminer2.performance_analysis.fields.organizations",
        "techminer2.performance_analysis.fields.sources",
        #
        "techminer2.performance_analysis.graphs",
        #
        "techminer2.performance_analysis.words",
        "techminer2.performance_analysis.words.abstract_nlp_phrases",
        "techminer2.performance_analysis.words.author_keywords",
        "techminer2.performance_analysis.words.descriptors",
        "techminer2.performance_analysis.words.index_keywords",
        "techminer2.performance_analysis.words.keywords",
        "techminer2.performance_analysis.words.nlp_phrases",
        "techminer2.performance_analysis.words.title_nlp_phrases",
        #
        # ======================================================================
        "techminer2.refine",
        #
        # ======================================================================
        "techminer2.search",
        #
        # ======================================================================
        "techminer2.techminer",
        #
        "techminer2.techminer.metrics",
        "techminer2.techminer.reports",
        "techminer2.techminer.tools",
        #
        # ======================================================================
        "techminer2.thematic_analysis",
        #
        # ======================================================================
        "techminer2.time_analysis",
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
