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
    version="2024.7.22",
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
        "techminer2._core.metrics",
        "techminer2._core.nx",
        "techminer2._core.stopwords",
        "techminer2._core",
        "techminer2._files",
        "techminer2.citation_network._core",
        "techminer2.citation_network",
        "techminer2.co_citation_network",
        "techminer2.co_occurrence_matrix",
        "techminer2.co_occurrence_network",
        "techminer2.correlation_matrix",
        "techminer2.coupling_network._core.docs",
        "techminer2.coupling_network._core.others",
        "techminer2.coupling_network._core",
        "techminer2.coupling_network",
        "techminer2.document_clustering",
        "techminer2.documents",
        "techminer2.emergence",
        "techminer2.factor_analysis._core",
        "techminer2.factor_analysis.co_occurrence",
        "techminer2.factor_analysis.tfidf",
        "techminer2.factor_analysis",
        "techminer2.fields.further_processing",
        "techminer2.fields",
        "techminer2.helpers",
        "techminer2.ingest.field_importers",
        "techminer2.ingest",
        "techminer2.main_path_analysis._core",
        "techminer2.main_path_analysis",
        "techminer2.metrics",
        "techminer2.raw",
        "techminer2.report",
        "techminer2.rpys",
        "techminer2.search",
        "techminer2.thesauri_data",
        "techminer2.thesaurus._core",
        "techminer2.thesaurus.abbreviations",
        "techminer2.thesaurus.countries",
        "techminer2.thesaurus.descriptors",
        "techminer2.thesaurus.organizations",
        "techminer2.thesaurus.references",
        "techminer2.thesaurus",
        "techminer2.tools.associations",
        "techminer2.tools",
        "techminer2.topic_modeling",
        "techminer2.word_lists",
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
