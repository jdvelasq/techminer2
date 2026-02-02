![logo](https://raw.githubusercontent.com/jdvelasq/techminer2/main/assets/logo.jpg)

A Python Library for Tech-Mining, Bibliometrics and Science Mapping.


Noun phrases
------------------------------------------------------------------------------

Unlike commonly used bibliometric and scientometric tools, which extract noun phrases using a single linguistic pipeline and resolve overlapping or fragmented terms through post hoc cleaning, TechMiner2+ implements a deterministic, multi-source extraction strategy designed to preserve conceptual integrity at extraction time. Noun phrases are independently derived from multiple NLP engines, combined with author and index keywords and curated vocabularies, and ordered by phrase length to enforce longest-term precedence. By re-injecting these terms into tokenized abstracts through a masking strategy, tm2+ prevents the fragmentation of multiword concepts, ensuring stable and semantically coherent units for downstream analysis.

Country and organization extraction from affiliations
------------------------------------------------------------------------------

VantagePoint extracts organizations using import filters that parse affiliation strings during data import, followed by iterative manual cleanup using fuzzy matching algorithms and user-managed thesauri—requiring users to repeatedly review suggested equivalents (e.g., "J. Smith" vs "James Smith") and confirm merges through interactive dialogs. In contrast, techminer2+ uses a fully automated rule-based algorithm with 99.75% accuracy, validated on 40,000 Scopus affiliations. The functional extractor applies hierarchical detection strategies without user intervention: it identifies department prefixes, disambiguates ambiguous units (Institute/Center/School), and recognizes corporate/government entities through multi-language keyword matching. This zero-configuration approach eliminates iterative review sessions while maintaining high precision across 120+ countries and 15+ languages.





