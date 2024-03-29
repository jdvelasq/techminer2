# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.202.5/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.7"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi


RUN apt-get update \
    && apt-get -yq --no-install-recommends install  pandoc  make \
    && apt-get clean \
    && apt-get autoremove -yq \
    && rm -rf /var/lib/apt/lists/* 

RUN pip3 --disable-pip-version-check --no-cache-dir install \
    twine \
    setuptools \
    wheel 

RUN pip3 --disable-pip-version-check --no-cache-dir install \
    black \
    isort \
    pylint \
    pytest

RUN pip3 --disable-pip-version-check --no-cache-dir install \
    sphinx==4.0.3 \
    sphinx-intl \
    nbsphinx \
    sphinx-rtd-theme \ 
    sphinx_copybutton \
    sphinx-toggleprompt \
    pygments

RUN pip3 --disable-pip-version-check --no-cache-dir install \
    cdlib==0.2.6 \
    fuzzywuzzy==0.18.0 \
    networkx==2.6.3 \
    nltk==3.7 \
    pandas==1.3.5 \
    plotly==5.9.0 \
    python-Levenshtein==0.12.2 \
    PyYAML==5.4.1 \
    scikit-learn==1.0.2 \
    sumy==0.10.0 \
    textblob==0.15.3 \
    wordcloud==1.5.0 \
    squarify==0.4.3

RUN python3 -c "import nltk; nltk.download('punkt'); nltk.download('brown'); nltk.download('averaged_perceptron_tagger'); nltk.download('stopwords')"



RUN apt update \
    && apt -yq --no-install-recommends install  graphviz \
    && apt clean \
    && apt autoremove -yq \
    && rm -rf /var/lib/apt/lists/* 



# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1