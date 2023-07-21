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
        "techminer2.bibliometrix",
        "techminer2.bibliometrix.abstract_nlp_phrases",
        "techminer2.bibliometrix.author_keywords",
        "techminer2.bibliometrix.authors",
        "techminer2.bibliometrix.cited_references",
        "techminer2.bibliometrix.conceptual_structure",
        "techminer2.bibliometrix.countries",
        "techminer2.bibliometrix.coupling",
        "techminer2.bibliometrix.data",
        "techminer2.bibliometrix.descriptors",
        "techminer2.bibliometrix.documents",
        "techminer2.bibliometrix.index_keywords",
        "techminer2.bibliometrix.intellectual_structure",
        "techminer2.bibliometrix.keywords",
        "techminer2.bibliometrix.nlp_phrases",
        "techminer2.bibliometrix.organizations",
        "techminer2.bibliometrix.overview",
        "techminer2.bibliometrix.social_structure",
        "techminer2.bibliometrix.sources",
        "techminer2.bibliometrix.nlp_phrases",
        #
        "techminer2.vosviewer",
        "techminer2.vosviewer.bibliographing_coupling_by_refs",
        "techminer2.vosviewer.bibliographing_coupling_by_refs.authors",
        "techminer2.vosviewer.bibliographing_coupling_by_refs.countries",
        "techminer2.vosviewer.bibliographing_coupling_by_refs.documents",
        "techminer2.vosviewer.bibliographing_coupling_by_refs.organizations",
        "techminer2.vosviewer.bibliographing_coupling_by_refs.sources",
        #
        "techminer2.vosviewer.citation.authors",
        "techminer2.vosviewer.citation.countries",
        "techminer2.vosviewer.citation.documents",
        "techminer2.vosviewer.citation.organizations",
        "techminer2.vosviewer.citation.sources",
        #
        "techminer2.vosviewer.co_authorship.authors",
        "techminer2.vosviewer.co_authorship.countries",
        "techminer2.vosviewer.co_authorship.organizations",
        #
        "techminer2.vosviewer.co_citation.cited_authors",
        "techminer2.vosviewer.co_citation.cited_references",
        "techminer2.vosviewer.co_citation.cited_sources",
        #
        "techminer2.vosviewer.co_occurrence.abstract_nlp_phrases",
        "techminer2.vosviewer.co_occurrence.title_nlp_phrases",
        "techminer2.vosviewer.co_occurrence.nlp_phrases",
        "techminer2.vosviewer.co_occurrence.author_keywords",
        "techminer2.vosviewer.co_occurrence.index_keywords",
        "techminer2.vosviewer.co_occurrence.keywords",
        "techminer2.vosviewer.co_occurrence.descriptors",
        #
        "techminer2.vosviewer.thematic_map.abstract_nlp_phrases",
        "techminer2.vosviewer.thematic_map.title_nlp_phrases",
        "techminer2.vosviewer.thematic_map.nlp_phrases",
        "techminer2.vosviewer.thematic_map.author_keywords",
        "techminer2.vosviewer.thematic_map.index_keywords",
        "techminer2.vosviewer.thematic_map.keywords",
        "techminer2.vosviewer.thematic_map.descriptors",
        #
        "techminer2.vantagepoint.calculate",
        "techminer2.vantagepoint.classify",
        "techminer2.vantagepoint.discover.factor_matrix.co_occ_matrix",
        "techminer2.vantagepoint.discover.factor_matrix.tfidf",
        "techminer2.vantagepoint.discover.factor_matrix",
        "techminer2.vantagepoint.discover.map",
        "techminer2.vantagepoint.discover.matrix",
        "techminer2.vantagepoint.discover",
        "techminer2.vantagepoint.explore.concept_grid.co_occ_matrix",
        "techminer2.vantagepoint.explore.concept_grid.tfidf",
        "techminer2.vantagepoint.explore.concept_grid",
        "techminer2.vantagepoint.explore",
        "techminer2.vantagepoint.ingest",
        "techminer2.vantagepoint.refine",
        "techminer2.vantagepoint.search",
        "techminer2.vantagepoint",
        #
        "techminer2.scientopy",
        #
        "techminer2.techminer",
        "techminer2.techminer.metrics",
        "techminer2.techminer.reports",
        "techminer2.techminer.tools",
        #
        #
        "techminer2.visualize",
        "techminer2.analyze",
        "techminer2.analyze.terms",
        #
        #
        "techminer2.tlab",
        "techminer2.tlab.co_occurrence_analysis",
        "techminer2.tlab.co_occurrence_analysis.co_word_analysis",
        "techminer2.tlab.co_occurrence_analysis.concordances",
        "techminer2.tlab.co_occurrence_analysis.sequences_and_network_analysis",
        "techminer2.tlab.co_occurrence_analysis.word_associations",
        "techminer2.tlab.co_occurrence_analysis.word_pairs",
        "techminer2.tlab.comparative_analysis",
        "techminer2.tlab.thematic_analysis",
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
