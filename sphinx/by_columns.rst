By columns
-----------------------------------------------------------------------------------------

**Data cleaning**

.. toctree::
    :maxdepth: 1

    clean_institutions
    clean_keywords

**Column analysis**

.. toctree::
    :maxdepth: 1

    column_coverage
    column_dynamics
    column_frequency
    column_frequency_over_time 
    column_global_citations
    column_trends
    column_wordcloud
    column_h_index


**Specialized functions**

.. toctree::
    :maxdepth: 1

    countries_frequency
    corresponding_authors_country
    
**Thematic analysis**

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

    bradford_law
    core_sources 
    lotka_law



**Laws**

.. toctree::
    :maxdepth: 1

    bradford_law
    core_sources 
    lotka_law

