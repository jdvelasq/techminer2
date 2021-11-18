from setuptools import setup
from setuptools.command.build_py import build_py


class BuildPyCommand(build_py):
    def run(self):
        import nltk

        nltk.download("stopwords")
        nltk.download("wordnet")
        nltk.download("averaged_perceptron_tagger")
        nltk.download("punkt")

        build_py.run(self)


setup(
    cmdclass={"build_py": BuildPyCommand},
    name="techminer",
    version="0.1.0",
    author="Juan D. Velasquez",
    author_email="jdvelasq@unal.edu.co",
    license="MIT",
    url="http://github.com/jdvelasq/techminer",
    description="Tech Mining of Bibliograpy",
    long_description="Tech Mining of Bibliograpy",
    keywords="bibliograpy",
    platforms="any",
    provides=["techminer"],
    install_requires=[
        "cdlib==0.2.5",
        "graphviz==0.10.1",
        "ipykernel==4.10.1",
        "ipywidgets==7.6.5",
        "matplotlib==3.1.0",
        "networkx==2.5.1",
        "nltk==3.2.5",
        "numpy==1.19.5",
        "pandas==1.1.5",
        "python-Levenshtein",
        "pyvis",
        "scikit-learn==0.22.2.post1",
        "seaborn==0.11.2",
        "squarify==0.4.3",
        "textblob",
        "wordcloud==1.5.0",
    ],
    packages=[
        "techminer",
        "techminer.correspondence_analysis",
        "techminer.dashboard",
        "techminer.files",
        "techminer.networkx",
        "techminer.plots",
        "techminer.text",
        "techminer.utils",
    ],
    package_dir={"techminer": "techminer"},
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
