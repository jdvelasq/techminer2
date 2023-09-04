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
    version="2023.8.30",
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
        "nltk",
        "cdlib",
        "fuzzywuzzy",
        "networkx",
        "pandas",
        "plotly",
        "python-Levenshtein",
        "PyYAML",
        "scikit-learn",
        "pyspellchecker",
        "sumy",
        "textblob",
        "wordcloud",
        # "kelaido",
        "igraph",
        "leidenalg",
        "tabulate",
    ],
    packages=[
        "techminer2",
        "techminer2._files",
        "techminer2.word_lists",
        #
        # ======================================================================
        "techminer2.bibliographic_coupling",
        "techminer2.bibliographic_coupling.authors",
        "techminer2.bibliographic_coupling.countries",
        "techminer2.bibliographic_coupling.documents",
        "techminer2.bibliographic_coupling.sources",
        #
        # ======================================================================
        "techminer2.citation",
        #
        "techminer2.citation.documents",
        #
        "techminer2.citation.network",
        "techminer2.citation.network.authors",
        "techminer2.citation.network.countries",
        "techminer2.citation.network.documents",
        "techminer2.citation.network.organizations",
        "techminer2.citation.network.sources",
        #
        # ======================================================================
        "techminer2.co_authorship",
        #
        "techminer2.co_authorship.associations",
        "techminer2.co_authorship.associations.authors",
        "techminer2.co_authorship.associations.countries",
        "techminer2.co_authorship.associations.organizations",
        #
        "techminer2.co_authorship.factor",
        #
        "techminer2.co_authorship.factor.pca",
        #
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix",
        #
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.authors",
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.authors.hierarchical",
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.authors.kmeans",
        #
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.countries",
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.countries.hierarchical",
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.countries.kmeans",
        #
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.organizations",
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.organizations.hierarchical",
        "techminer2.co_authorship.factor.pca.co_occurrence_matrix.organizations.kmeans",
        #
        "techminer2.co_authorship.factor.pca.tfidf",
        #
        "techminer2.co_authorship.factor.pca.tfidf.authors",
        "techminer2.co_authorship.factor.pca.tfidf.authors.hierarchical",
        "techminer2.co_authorship.factor.pca.tfidf.authors.kmeans",
        #
        "techminer2.co_authorship.factor.pca.tfidf.countries",
        "techminer2.co_authorship.factor.pca.tfidf.countries.hierarchical",
        "techminer2.co_authorship.factor.pca.tfidf.countries.kmeans",
        #
        "techminer2.co_authorship.factor.pca.tfidf.organizations",
        "techminer2.co_authorship.factor.pca.tfidf.organizations.hierarchical",
        "techminer2.co_authorship.factor.pca.tfidf.organizations.kmeans",
        #
        "techminer2.co_authorship.factor.svd",
        #
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix",
        #
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.authors",
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.authors.hierarchical",
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.authors.kmeans",
        #
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.countries",
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.countries.hierarchical",
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.countries.kmeans",
        #
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.organizations",
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.organizations.hierarchical",
        "techminer2.co_authorship.factor.svd.co_occurrence_matrix.organizations.kmeans",
        #
        "techminer2.co_authorship.factor.svd.tfidf",
        #
        "techminer2.co_authorship.factor.svd.tfidf.authors",
        "techminer2.co_authorship.factor.svd.tfidf.authors.hierarchical",
        "techminer2.co_authorship.factor.svd.tfidf.authors.kmeans",
        #
        "techminer2.co_authorship.factor.svd.tfidf.countries",
        "techminer2.co_authorship.factor.svd.tfidf.countries.hierarchical",
        "techminer2.co_authorship.factor.svd.tfidf.countries.kmeans",
        #
        "techminer2.co_authorship.factor.svd.tfidf.organizations",
        "techminer2.co_authorship.factor.svd.tfidf.organizations.hierarchical",
        "techminer2.co_authorship.factor.svd.tfidf.organizations.kmeans",
        #
        "techminer2.co_authorship.network",
        #
        "techminer2.co_authorship.network.authors",
        "techminer2.co_authorship.network.countries",
        "techminer2.co_authorship.network.organizations",
        #
        # ======================================================================
        "techminer2.co_citation",
        #
        "techminer2.co_citation.cited_authors",
        "techminer2.co_citation.cited_references",
        "techminer2.co_citation.cited_sources",
        #
        # ======================================================================
        "techminer2.co_occurrence",
        #
        "techminer2.co_occurrence.associations",
        #
        "techminer2.co_occurrence.associations.abstract_nlp_phrases",
        "techminer2.co_occurrence.associations.author_keywords",
        "techminer2.co_occurrence.associations.descriptors",
        "techminer2.co_occurrence.associations.index_keywords",
        "techminer2.co_occurrence.associations.keywords",
        "techminer2.co_occurrence.associations.nlp_phrases",
        "techminer2.co_occurrence.associations.title_nlp_phrases",
        #
        "techminer2.co_occurrence.factor",
        #
        "techminer2.co_occurrence.factor.pca",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.abstract_nlp_phrases",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.abstract_nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.abstract_nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.author_keywords",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.author_keywords.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.author_keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.descriptors",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.descriptors.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.descriptors.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.index_keywords",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.index_keywords.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.index_keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.keywords",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.keywords.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.nlp_phrases",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.title_nlp_phrases",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.title_nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.pca.co_occurrence_matrix.title_nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.abstract_nlp_phrases",
        "techminer2.co_occurrence.factor.pca.tfidf.abstract_nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.abstract_nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.author_keywords",
        "techminer2.co_occurrence.factor.pca.tfidf.author_keywords.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.author_keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.descriptors",
        "techminer2.co_occurrence.factor.pca.tfidf.descriptors.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.descriptors.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.index_keywords",
        "techminer2.co_occurrence.factor.pca.tfidf.index_keywords.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.index_keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.keywords",
        "techminer2.co_occurrence.factor.pca.tfidf.keywords.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.nlp_phrases",
        "techminer2.co_occurrence.factor.pca.tfidf.nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.pca.tfidf.title_nlp_phrases",
        "techminer2.co_occurrence.factor.pca.tfidf.title_nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.pca.tfidf.title_nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.svd",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.abstract_nlp_phrases",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.abstract_nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.abstract_nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.author_keywords",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.author_keywords.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.author_keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.descriptors",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.descriptors.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.descriptors.kmeans",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.index_keywords",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.index_keywords.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.index_keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.keywords",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.keywords.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.keywords.kmeans",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.nlp_phrases",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.title_nlp_phrases",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.title_nlp_phrases.hierarchical",
        "techminer2.co_occurrence.factor.svd.co_occurrence_matrix.title_nlp_phrases.kmeans",
        #
        "techminer2.co_occurrence.network",
        #
        "techminer2.co_occurrence.network.co_occurrence",
        "techminer2.co_occurrence.network.co_occurrence.abstract_nlp_phrases",
        "techminer2.co_occurrence.network.co_occurrence.author_keywords",
        "techminer2.co_occurrence.network.co_occurrence.descriptors",
        "techminer2.co_occurrence.network.co_occurrence.index_keywords",
        "techminer2.co_occurrence.network.co_occurrence.keywords",
        "techminer2.co_occurrence.network.co_occurrence.nlp_phrases",
        "techminer2.co_occurrence.network.co_occurrence.title_nlp_phrases",
        #
        "techminer2.co_occurrence.network.thematic_map.abstract_nlp_phrases",
        "techminer2.co_occurrence.network.thematic_map.author_keywords",
        "techminer2.co_occurrence.network.thematic_map.descriptors",
        "techminer2.co_occurrence.network.thematic_map.index_keywords",
        "techminer2.co_occurrence.network.thematic_map.keywords",
        "techminer2.co_occurrence.network.thematic_map.nlp_phrases",
        "techminer2.co_occurrence.network.thematic_map.title_nlp_phrases",
        #
        # ======================================================================
        "techminer2.indicators",
        #
        # ======================================================================
        "techminer2.ingest",
        #
        # ======================================================================
        "techminer2.performance",
        #
        "techminer2.performance.contributors",
        #
        "techminer2.performance.contributors.authors",
        "techminer2.performance.contributors.countries",
        "techminer2.performance.contributors.organizations",
        "techminer2.performance.contributors.sources",
        #
        "techminer2.performance.overview",
        #
        "techminer2.performance.plots",
        #
        "techminer2.performance.words",
        #
        "techminer2.performance.words.abstract_nlp_phrases",
        "techminer2.performance.words.author_keywords",
        "techminer2.performance.words.descriptors",
        "techminer2.performance.words.index_keywords",
        "techminer2.performance.words.keywords",
        "techminer2.performance.words.nlp_phrases",
        "techminer2.performance.words.title_nlp_phrases",
        #
        # ======================================================================
        "techminer2.refine",
        #
        # ======================================================================
        "techminer2.search",
        #
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
