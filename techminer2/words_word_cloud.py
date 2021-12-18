"""
Words / Word Cloud
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/words_word_cloud.png"
>>> words_word_cloud('author_keywords', 50, directory=directory).savefig(file_name)

.. image:: images/words_word_cloud.png
    :width: 700px
    :align: center


>>> words_word_cloud('author_keywords', 50, directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
block-chain                        17               149               22
bank                               13               193               23

"""

import os

from .column_word_cloud import column_word_cloud

words_word_cloud = column_word_cloud
