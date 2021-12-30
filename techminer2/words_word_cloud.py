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


"""

import os

from .topic_view_word_cloud import topic_view_word_cloud

words_word_cloud = topic_view_word_cloud
