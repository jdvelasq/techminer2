# flake8: noqa
# pylint: disable=line-too-long
"""
.. _bar_chart:

Bar Chart
===============================================================================

Displays a horizontal bar graph of the selected items in a ItemLlist object. 
Items in your list are the Y-axis, and the number of records are the X-axis.

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bar_chart_0.html"
>>> (
...     tm2p.Records(root_dir=root_dir) 
...     .list_items("author_keywords", top_n=10) 
...     .bar_chart(title="Most Frequent Author Keywords")
...     .write_html(file_name)
... )

.. raw:: html

    <iframe src="../../_static/bar_chart_0.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
