T-Lab
#########################################################################################

.. raw:: html

   <hr style="height:4px;border-width:0;color:gray;background-color:black">


Co-occurrence Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">


.. raw:: html

    <p style="color:gray">Word Associations</p>

.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_topic_associations
    co_occurrence_matrix_mds_map



.. raw:: html

    <p style="color:gray">Co-word Analysis</p>


.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_manifold
    column_cleveland_dot_chart
    

.. raw:: html

    <p style="color:gray">Comparison between word pairs</p>

.. toctree::
    :maxdepth: 1



.. raw:: html

    <p style="color:gray">Sequence and Network Analysis</p>

.. toctree::
    :maxdepth: 1



.. raw:: html

    <p style="color:gray">Concordances</p>

.. toctree::
    :maxdepth: 1


.. toctree::
    :maxdepth: 1

    abstract_concordances



Thematic Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">


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



Comparative Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">




.. raw:: html

    <p style="color:gray">Singunlar Value Decomposition:</p>


.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_svd_map
    tf_idf_matrix_svd_map


Lexical and other tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">


.. toctree::
    :maxdepth: 1

    abstract_screening
    abstract_summarization
    

