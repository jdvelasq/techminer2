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

   See ``Import Scopus Files`` in `Data <_user_data.html>`__. 


Filter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::

      user_filters


Overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   
   .. toctree::

      main_information
      annual_scientific_production
      average_citations_per_year

   TODO:

   .. toctree::

      three_fields_plot


Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::

      most_frequent_sources
      most_global_cited_sources
      most_local_cited_sources
      sources_production_over_time
      source_local_impact
      core_sources  

   TODO:

   .. toctree::

      bradford_law     
      source_dynamics_table
      source_dynamics_plot




Authors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_frequent_authors
      most_global_cited_authors
      most_local_cited_authors
      authors_production_over_time
      author_local_impact
      authors_production_per_year


   TODO:

   .. toctree::
      :maxdepth: 1
      
      lotka_law    
      


Institutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_frequent_institutions
      most_global_cited_institutions
      most_local_cited_institutions
      institutions_production_over_time
      institution_local_impact
      institutions_production_per_year

      


Countries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_frequent_countries
      most_global_cited_countries
      most_local_cited_countries
      countries_production_over_time
      country_local_impact
      countries_production_per_year
      country_scientific_production

   TODO:

   .. toctree::
      :maxdepth: 1
      
      corresponding_authors_country
      
      
      




Documents 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_global_cited_documents
      most_local_cited_documents

   .. toctree::
      :maxdepth: 1

      documents_by_author
      documents_by_country
      documents_by_institution

   .. toctree::

      num_documents_by_type
      global_citations_by_type
      local_citations_by_type


Cited References
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_local_cited_references


   TODO:

   .. toctree::
      :maxdepth: 1

      rpys


Citing Documents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1



Words
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1

      most_frequent_words
      word_cloud
      tree_map


   TODO:

   .. toctree::
      :maxdepth: 1
      
      topic_dynamics
      word_dynamics_plot
      word_dynamics_table
      trend_topics



Clustering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. toctree::
      :maxdepth: 1



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