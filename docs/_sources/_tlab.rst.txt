T-Lab
-----------------------------------------------------------------------------------------

.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">


Co-occurrence Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Word Associations
***************************************

.. toctree::
    :maxdepth: 1

    co_occurrence_item_associations
    co_occurrence_associations
    co_occurrence_mds_map


Co-Word Analysis
***************************************

.. toctree::
    :maxdepth: 1

    co_occurrence_manifold
    co_occurrence_matrix


Comparison between word pairs
***************************************

.. toctree::
    :maxdepth: 1




Concordances
***************************************

.. toctree::
    :maxdepth: 1

    abstract_concordances


.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">

Thematic Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This analysis is used to obtain and explore a representation of the documents
throught thematic clusters.

The implemented methodology is based on the Thematic Analysis of Elementary
Contexts implemented in T-LAB.

**Algorithm**

    1. Obtain the TF-IDF normalized matrix with rows scaled to unit length 
       using the Euclidean norm. Rows represent documents and columns represent
       keywords.

    2. Clustering the rows (cosine similarity).

    3. Build a table of keywords by clusters.

    4. Analyze the keywords by clusters.

    5. Visualization with n-1 clusters  

.. toctree::
    :maxdepth: 1


.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">

Comparative Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    co_occurrence_svd_map


.. raw:: html

   <hr style="height:2px;border-width:0;color:gray;background-color:gray">

Lexical and other tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
    :maxdepth: 1

    abstract_screening
    abstract_summarization
    

