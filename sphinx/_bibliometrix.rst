
Bibliometrix
#########################################################################################

.. raw:: html

   <hr style="height:4px;border-width:0;color:gray;background-color:black">


In this section, the library's functionalities are presented in the structure used 
internally in Bibliometrix, in order to facilitate comparison. Likewise, functions have
been created with the same names as the Bibliometrix menus to facilitate the use of the
tool by users. It should be noted that the functions presented in this section cover only
a part of TechMiner's capabilities, and in this sense, Bibliometrix contains only a 
subset of the analytical capabilities of TechMiner.




Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

See ``Import Scopus Files`` in `Data <_user_data.html>`__. 



Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. toctree::

    user_filters  


Dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. toctree::

    main_information
    annual_scientific_production
    average_citations_per_year

* ``TODO: Three-Fields Plot``

Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. toctree::

    most_relevant_sources
    most_local_cited_sources
    bradford_law
    core_sources 
    source_local_impact
    source_dynamics



Authors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. raw:: html

    <p style="color:gray">Authors:</p>

.. toctree::
    :maxdepth: 1

    most_relevant_authors
    most_local_cited_authors
    authors_production_over_time
    lotka_law    
    author_local_impact

.. raw:: html

    <p style="color:gray">Affiliations:</p>

.. toctree::
    :maxdepth: 1

    most_relevant_institutions


.. raw:: html

    <p style="color:gray">Countries:</p>

.. toctree::
    :maxdepth: 1

    corresponding_authors_country
    country_scientific_production
    most_global_cited_countries


Documents 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">


.. raw:: html

    <p style="color:gray">Documents:</p>


.. toctree::
    :maxdepth: 1

    most_global_cited_documents
    most_local_cited_documents     

.. raw:: html

    <p style="color:gray">Cited References:</p>

.. toctree::
    :maxdepth: 1

    most_local_cited_references

.. raw:: html

    <p style="color:gray">Words:</p>

.. toctree::
    :maxdepth: 1

    most_frequent_words
    word_dynamics
    trend_topics



Clustering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. toctree::
    :maxdepth: 1

    coupling_by_column_matrix
    coupling_by_references_matrix
    coupling_network  


Conceptual Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">


.. raw:: html

    <p style="color:gray">Network Approach:</p>


.. toctree::
    :maxdepth: 1

    co_occurrence_network
    co_occurrence_indicators
    co_occurrence_degree_plot
    co_occurrence_communities



.. toctree::
    :maxdepth: 1

    thematic_map_communities
    thematic_map_degree_plot
    thematic_map_indicators
    thematic_map_network


.. toctree::
    :maxdepth: 1


.. raw:: html

    <p style="color:gray">Factorial Approach:</p>

.. toctree::
    :maxdepth: 1

    factorial_analysis_mds_communities
    factorial_analysis_mds_data
    factorial_analysis_mds_map
    factorial_analysis_mds_silhouette_scores

* ``TODO: Factorial Approach / CA``

Intellectual Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. toctree::
    :maxdepth: 1

    co_citation_network_communities
    co_citation_network_degree_plot
    co_citation_network_graph    
    co_citation_network_indicators


.. Note::
    In addition, **TechMiner** implements the following functions:

        .. toctree::
            :maxdepth: 1

            co_citation_matrix    
            main_path_network


* ``TODO: Historiograph``


Social Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <hr style="width:70%;height:2px;border-width:0;color:gray;background-color:black">

.. note:: 
    A collaboration network is a generic co-occurrence network where the analized column
    is restricted to the following columns in the dataset:

    * Authors.

    * Institutions. 

    * Countries.

    As a consequence, many implemented plots and analysis are valid for analyzing a 
    co-occurrence network, including heat maps and other plot types.

.. toctree::
    :maxdepth: 1

    collaboration_network_communities
    collaboration_network_degree_plot
    collaboration_network_graph
    collaboration_network_indicators
    

* ``TODO: Collaboration WorldMap``