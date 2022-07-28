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
        "cdlib==0.2.6",
        "networkx==2.6.3",
        "pandas==1.3.5",
        "plotly==5.8.2",
        "python-Levenshtein==0.12.2",
        "sumy==0.10.0",
    ],
    packages=[
        "techminer2",
        "techminer2._indicators",
        "techminer2._plots",
        "techminer2._px",
        "techminer2.files",
        "techminer2.templates",
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
