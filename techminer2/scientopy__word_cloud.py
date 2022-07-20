"""
Word Cloud
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/scientopy__word_cloud.png"


>>> from techminer2 import scientopy__word_cloud
>>> scientopy__word_cloud(
...     column='author_keywords',
...     title="Author Keywords",
...     top_n=50,
...     directory=directory,
... ).savefig(file_name)

.. image:: ../images/scientopy__word_cloud.png
    :width: 900px
    :align: center

"""
from .wordcloud import wordcloud

scientopy__word_cloud = wordcloud
