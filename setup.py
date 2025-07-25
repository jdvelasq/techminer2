"""Setup module for TechMiner2+"""

from setuptools import find_packages, setup

setup(
    # cmdclass={"build_py": BuildPyCommand},
    name="techminer2",
    version="2024.7.22",
    author="Juan D. Velasquez",
    author_email="jdvelasq@unal.edu.co",
    license="MIT",
    url="http://github.com/jdvelasq/techminer2",
    description="Tech Mining Analysis of Bibliography",
    long_description="Tech Mining Analysis of Bibliography",
    keywords="bibliography",
    platforms="any",
    provides=["techminer2"],
    install_requires=[
        "cdlib",
        "contractions",
        "duckdb",
        "fuzzywuzzy",
        "graphviz",
        "igraph",
        "kaleido",
        "langdetect",
        "leidenalg",
        "networkx",
        "nltk",
        "pandas",
        "plotly",
        "pyspellchecker",
        "python-Levenshtein",
        "PyYAML",
        "scikit-learn",
        "spacy",
        "sumy",
        "tabulate",
        "textblob",
        "urllib3==1.26.6",
        "wordcloud",
        "colorama",
        "pyzotero",
    ],
    packages=find_packages(),
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
