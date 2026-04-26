# High-Impact Papers (Q1 Target)

## Intellectual Structure

- Subpackage: `intellectual/`

- Research question: What is the knowledge base and intellectual lineage of the field?

- Data requirements: WoS

- Key tables and plots:
  - co-citation clusters (authors, references, sources)
  - historiograph
  - main path analysis
  - core references by cluster

- Contribution:

  - reconstructs the knowledge base and intellectual lineage of the field

---

## Thematic Structure

- Subpackage: `thematic/`

- Research question: What are the main conceptual domains (themes) of the field?

- Data requirements: keywords or extracted concepts (all sources via NLP pipeline)

- Key tables and plots:
  - co-occurrence network
  - correlation map
  - thematic map (centrality vs density)
  - cluster descriptors (e.g., TF-IDF)

- Contribution:
  - defines the conceptual architecture of the field

- Note:

    We analyze the thematic structure of the field using two complementary approaches:

    (1) First-order analysis based on term distributions across documents (TF-IDF),
    capturing research topics.

    (2) Second-order analysis based on term co-occurrence patterns,
    capturing the conceptual structure of the field.


---

## Temporal Evolution

- Subpackage: `temporal_evolution/`

- Research question: How have the themes evolved over time?


- Data requirements: publication year + concepts (all sources)

- Key tables and plots:
  - thematic evolution (Sankey/alluvial)
  - time-sliced clustering
  - lifecycle plots
  - long-term trend curves

- Contribution:
  - explains how themes evolve across periods

---

## Frontier / Emergence

- Subpackage: `emergence/`

- Research question: Which topics show significant recent growth and define the research frontier?

- Data requirements: time + concepts (all sources)

- Key tables and plots:
  - burst detection
  - emergence rankings
  - acceleration plots
  - recent growth indicators
  - union-of-signals table (multiple emergence metrics)

- Contribution:
  - identifies topics with statistically significant temporal growth, signaling research frontiers

---

## Structural Gaps / Novelty

- Subpackage: `novelty/`

- Research question: Where are the structural gaps and opportunities in the field?

- Data requirements: network structure (concepts or citations; stronger with Scopus/WoS)

- Key tables and plots:
  - structural variation analysis (SVA)
  - white-space maps
  - missing-link maps
  - bridging-node tables

- Contribution:
  - identifies research gaps and opportunities for future work

---

# Low-Impact Papers (Q4 Target)

## Performance Mapping

- Subpackage: `performance/`

- Research question: What is the productivity and impact profile of the field?

- Data requirements: basic metadata (all sources)

- Key tables and plots:
  - annual production
  - top authors, institutions, countries
  - Bradford zones
  - citation indicators

- Contribution:
  - descriptive overview of productivity and impact

---

## Social Structure

- Subpackage: `social/`

- Research question:How is the field socially organized?

- Data requirements: author and affiliation fields (stronger in Scopus/WoS)

- Key tables and plots:
  - co-authorship networks
  - country collaboration maps
  - institutional collaboration tables

- Contribution:
  - describes collaboration patterns in the field


## Tech Mining / Applied Intelligence

- Subpackage: `techmining/`

- Research question: How can the scientific structure be translated into actionable technological and application insights?

- Data requirements: concepts + optional metadata (stronger in Scopus/WoS)

- Key tables and plots:
  - technology clusters
  - trend radars
  - application maps
  - portfolio tables

- Contribution:
  - transforms thematic and structural results into actionable technological and application-oriented insights

