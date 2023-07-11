# flake8: noqa
"""
Authors Radial Diagram
===============================================================================


>>> ROOT_DIR = "data/regtech/"
>>> FIELD = "authors"
>>> ITEM = "Arner DW"
>>> file_name = "sphinx/_static/examples/social_structure/associations/radial_diagram/authors.html"

>>> import techminer2plus
>>> chart = techminer2plus.analyze.associations.radial_diagram(
...     root_dir=ROOT_DIR,
...     item=ITEM,
...     columns=FIELD,
...     col_top_n=20,
...     nx_k=None,
...     nx_iterations=20,
... )

>>> chart.item_name_
'Arner DW 3:185'

>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/social_structure/associations/radial_diagram/authors.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.series_
authors
Buckley RP 3:185     3
Barberis JN 2:161    2
Weber RH 1:024       1
Zetzsche DA 1:024    1
Name: Arner DW 3:185, dtype: int64



# pylint: disable=line-too-long
"""
