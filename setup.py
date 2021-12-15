from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyCommand(build_py):
    def run(self):
        #
        import nltk

        #
        # nltk.download("stopwords")
        # nltk.download("wordnet")
        # nltk.download("averaged_perceptron_tagger")
        nltk.download("punkt")
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
    description="Tech Mining of Bibliograpy",
    long_description="Tech Mining of Bibliograpy",
    keywords="bibliograpy",
    platforms="any",
    provides=["techminer2"],
    install_requires=[
        "graphviz==0.10.1",
        "ipykernel==4.10.1",
        "matplotlib==3.2.2",
        "networkx==2.6.3",
        "nltk==3.2.5",
        "numpy==1.19.5",
        "pandas==1.1.5",
        "scikit-learn==1.0.1",
        "seaborn==0.11.2",
        "textblob==0.15.3",
        "python-Levenshtein==0.12.2",
        "PyYAML==5.4.1",
        "wordcloud==1.5.0",
        # not in colab:
        "cdlib==0.2.5",
        "squarify==0.4.3",
        "python-Levenshtein==0.12.2",
    ],
    packages=[
        "techminer2",
        "techminer2.correspondence_analysis",
        "techminer2.dashboard",
        "techminer2.files",
        "techminer2.networkx",
        "techminer2.plots",
        "techminer2.text",
        "techminer2.utils",
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
