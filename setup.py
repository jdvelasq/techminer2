from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyCommand(build_py):
    def run(self):
        #
        # import nltk

        #
        # nltk.download("stopwords")
        # nltk.download("punkt")
        # nltk.download("brown")
        # nltk.download("averaged_perceptron_tagger")
        # nltk.download("punkt")
        #
        build_py.run(self)


setup(
    cmdclass={"build_py": BuildPyCommand},
    name="techminer2",
    version="0.1.0",
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
        # "graphviz==0.10.1",
        # "ipykernel==4.10.1",
        # "ipywidgets==7.6.5",
        # "matplotlib==3.5.2",
        # "networkx==2.8.4",
        # "nltk==3.2.5",
        # "numpy==1.19.5",
        # "pandas==1.1.5",
        # "PyYAML==5.4.1",
        # "scikit-learn==1.0.2",
        # "seaborn==0.11.2",
        # "textblob==0.15.3",
        # "wordcloud==1.5.0",
        # not in colab:
        # "sumy",
        # "itables==1.0.0",
        # "fuzzywuzzy==0.18.0",
        # "dash==2.5.1",
        "cdlib==0.2.6",
        "squarify==0.4.3",
        "python-Levenshtein==0.12.2",
        "wordcloud==1.8.1",
    ],
    packages=[
        "techminer2",
        "techminer2.files",
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
