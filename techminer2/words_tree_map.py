"""
Words / Tree Map
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/words_tree_map.png"
>>> words_tree_map('author_keywords', 15, directory=directory).savefig(file_name)

.. image:: images/words_tree_map.png
    :width: 700px
    :align: center


>>> words_tree_map('author_keywords', 15, directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
block-chain                        17               149               22
bank                               13               193               23

"""

from .column_tree_map import column_tree_map

words_tree_map = column_tree_map
