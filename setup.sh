#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install --quiet --upgrade pip
pip3 install --quiet -e .

pip3 install --quiet \
    docutils \
    furo \
    ipykernel \
    nbsphinx \
    pytest \
    pygments \
    sphinx \
    sphinx_copybutton \
    sphinx_rtd_theme \
    sphinx-autodoc-typehints \
    sphinx-intl \
    sphinx-toggleprompt

python3 -m spacy download en_core_web_sm
python3 -m nltk.downloader averaged_perceptron_tagger
python3 -m nltk.downloader punkt