T-Lab
#########################################################################################

.. raw:: html

   <hr style="height:4px;border-width:0;color:gray;background-color:black">


Co-occurrence Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">


Word Associations
.......................................

.. raw:: html

    <hr style="width:50%;height:1px;border-width:0;color:gray;background-color:black">

.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_topic_associations
    co_occurrence_matrix_mds_map


Co-Word Analysis
.......................................

.. raw:: html

    <hr style="width:50%;height:1px;border-width:0;color:gray;background-color:black">

.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_cluster_mds_map
    co_occurrence_matrix_cluster_tsne_map
    co_occurrence_matrix_manifold
    column_cleveland_dot_chart
    

Comparison between word pairs
.......................................

.. raw:: html

    <hr style="width:50%;height:1px;border-width:0;color:gray;background-color:black">

.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_topics_comparison_chart
    co_occurrence_matrix_topics_comparison_network


Sequence and Network Analysis
.......................................

.. raw:: html

    <hr style="width:50%;height:1px;border-width:0;color:gray;background-color:black">

.. toctree::
    :maxdepth: 1

    co_occurrence_matrix_ego_graph
    co_occurrence_matrix_ego_network


Concordances
.......................................

.. raw:: html

    <hr style="width:50%;height:1px;border-width:0;color:gray;background-color:black">

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


Singunlar Value Decomposition
.......................................

.. raw:: html

    <hr style="width:50%;height:1px;border-width:0;color:gray;background-color:black">

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
    

