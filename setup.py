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
    version="2023.9.18",
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
        "techminer2.analyze",
        #
        # ======================================================================
        "techminer2.analyze.associations",
        #
        # ======================================================================
        "techminer2.analyze.bibliographic_coupling",
        "techminer2.analyze.bibliographic_coupling.authors",
        "techminer2.analyze.bibliographic_coupling.countries",
        "techminer2.analyze.bibliographic_coupling.documents",
        "techminer2.analyze.bibliographic_coupling.organizations",
        "techminer2.analyze.bibliographic_coupling.sources",
        #
        # ======================================================================
        "techminer2.analyze.citation",
        #
        "techminer2.analyze.citation.network",
        "techminer2.analyze.citation.network.authors",
        "techminer2.analyze.citation.network.countries",
        "techminer2.analyze.citation.network.documents",
        "techminer2.analyze.citation.network.organizations",
        "techminer2.analyze.citation.network.sources",
        #
        "techminer2.analyze.citation.publications",
        #
        # ======================================================================
        "techminer2.analyze.co_authorship",
        #
        "techminer2.analyze.co_authorship.network",
        #
        "techminer2.analyze.co_authorship.network.authors",
        "techminer2.analyze.co_authorship.network.countries",
        "techminer2.analyze.co_authorship.network.organizations",
        #
        # ======================================================================
        "techminer2.analyze.co_citation",
        #
        "techminer2.analyze.co_citation.cited_authors",
        "techminer2.analyze.co_citation.cited_references",
        "techminer2.analyze.co_citation.cited_sources",
        #
        # ======================================================================
        "techminer2.analyze.co_occurrence",
        #
        "techminer2.analyze.co_occurrence.network",
        #
        # ======================================================================
        "techminer2.analyze.contributors",
        #
        "techminer2.analyze.contributors.authors",
        "techminer2.analyze.contributors.countries",
        "techminer2.analyze.contributors.organizations",
        "techminer2.analyze.contributors.sources",
        #
        # ======================================================================
        "techminer2.analyze.words",
        #
        "techminer2.analyze.words.abstract_nlp_phrases",
        "techminer2.analyze.words.author_keywords",
        "techminer2.analyze.words.descriptors",
        "techminer2.analyze.words.index_keywords",
        "techminer2.analyze.words.keywords",
        "techminer2.analyze.words.nlp_phrases",
        "techminer2.analyze.words.title_nlp_phrases",
        #
        # ======================================================================
        "techminer2.analyze.correlation",
        #
        # ======================================================================
        "techminer2.analyze.emergence",
        #
        # ======================================================================
        "techminer2.analyze.overview",
        #
        # ======================================================================
        "techminer2.analyze.pca",
        #
        "techminer2.analyze.pca.cooc_matrix",
        "techminer2.analyze.pca.cooc_matrix.hierarchical",
        "techminer2.analyze.pca.cooc_matrix.kmeans",
        #
        "techminer2.analyze.pca.tfidf_matrix",
        "techminer2.analyze.pca.tfidf_matrix.hierarchical",
        "techminer2.analyze.pca.tfidf_matrix.kmeans",
        #
        # ======================================================================
        "techminer2.analyze.research_agenda",
        #
        # ======================================================================
        "techminer2.analyze.svd",
        #
        "techminer2.analyze.svd.cooc_matrix",
        "techminer2.analyze.svd.cooc_matrix.hierarchical",
        "techminer2.analyze.svd.cooc_matrix.kmeans",
        #
        "techminer2.analyze.svd.tfidf_matrix",
        "techminer2.analyze.svd.tfidf_matrix.hierarchical",
        "techminer2.analyze.svd.tfidf_matrix.kmeans",
        #
        # ======================================================================
        "techminer2.analyze.topic_modeling",
        #
        "techminer2.analyze.topic_modeling.berttopic",
        "techminer2.analyze.topic_modeling.lda",
        "techminer2.analyze.topic_modeling.nmf",
        #
        # ======================================================================
        "techminer2.indicators",
        #
        # ======================================================================
        "techminer2.ingest",
        #
        # ======================================================================
        "techminer2.refine",
        #
        # ======================================================================
        "techminer2.report",
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
