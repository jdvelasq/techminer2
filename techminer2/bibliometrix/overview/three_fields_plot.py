# flake8: noqa
"""
Three Fields Plot
===============================================================================

In TechMiner2, this diagram can be used for two or more fields in the 
database, and not it is limited to three fields.


Example
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix_three_fields_plot.html"

>>> from techminer2 import bibliometrix
>>> bibliometrix.overview.three_fields_plot(
...     root_dir=root_dir,
...     fields=["authors", "countries", "author_keywords"],
...     top_n=10,
...     max_n=20,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix_three_fields_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>

# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import sankey_plot

three_fields_plot = sankey_plot
