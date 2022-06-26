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

* **Data**


   See ``Import Scopus Files`` in `Data <_user_data.html>`__. 


* **Filter**


   .. toctree::

      user_filters


* **Overview**

   .. toctree::

      main_information
      annual_scientific_production
      average_citations_per_year
      three_fields_plot


Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::

      most_relevant_sources
      most_local_cited_sources
      bradford_law
      core_sources 
      source_local_impact
      source_dynamics_table
      source_dynamics_plot




Authors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      num_documents_by_author
      most_local_cited_authors
      authors_production_over_time
      authors_production_per_year
      lotka_law    
      author_local_impact


Institutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_relevant_institutions
      most_global_cited_institutions
      institutions_production_over_time
      institutions_production_per_year
      institution_local_impact


Countries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      corresponding_authors_country
      country_scientific_production
      countries_production_over_time
      countries_production_per_year
      most_global_cited_countries
      country_local_impact




Documents 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_global_cited_documents
      most_local_cited_documents     
      documents_per_author
      documents_per_country
      documents_per_institution

Cited References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_local_cited_references
      rpys

Words
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


   .. toctree::
      :maxdepth: 1

      most_frequent_words
      word_cloud
      tree_map
      topic_dynamics
      word_dynamics_plot
      word_dynamics_table
      trend_topics



Clustering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      coupling_matrix
      coupling_network_communities
      coupling_network_degree_plot
      coupling_network_graph


Conceptual Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. raw:: html

      <p style="color:gray">Network Approach:</p>


   .. toctree::
      :maxdepth: 1

      co_occurrence_network_communities
      co_occurrence_network_degree_plot
      co_occurrence_network_graph
      co_occurrence_network_indicators
      co_occurrence_network_summarization



   .. toctree::
      :maxdepth: 1

      thematic_map_communities
      thematic_map_degree_plot
      thematic_map_indicators
      thematic_map_network
      thematic_map_strategic_diagram
      thematic_map_summarization

   .. toctree::
      :maxdepth: 1

      thematic_evolution_plot

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