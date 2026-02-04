![logo](https://raw.githubusercontent.com/jdvelasq/techminer2/main/assets/logo.jpg)

A Python Library for Tech-Mining, Bibliometrics and Science Mapping.


Noun phrases
------------------------------------------------------------------------------

Unlike commonly used bibliometric and scientometric tools, which extract noun phrases using a single linguistic pipeline and resolve overlapping or fragmented terms through post hoc cleaning, TechMiner2+ implements a deterministic, multi-source extraction strategy designed to preserve conceptual integrity at extraction time. Noun phrases are independently derived from multiple NLP engines, combined with author and index keywords and curated vocabularies, and ordered by phrase length to enforce longest-term precedence. By re-injecting these terms into tokenized abstracts through a masking strategy, tm2+ prevents the fragmentation of multiword concepts, ensuring stable and semantically coherent units for downstream analysis.

Country and organization extraction from affiliations
------------------------------------------------------------------------------

VantagePoint extracts organizations using import filters that parse affiliation strings during data import, followed by iterative manual cleanup using fuzzy matching algorithms and user-managed thesauri—requiring users to repeatedly review suggested equivalents (e.g., "J. Smith" vs "James Smith") and confirm merges through interactive dialogs. In contrast, techminer2+ uses a fully automated rule-based algorithm with 99.75% accuracy, validated on 40,000 Scopus affiliations. The functional extractor applies hierarchical detection strategies without user intervention: it identifies department prefixes, disambiguates ambiguous units (Institute/Center/School), and recognizes corporate/government entities through multi-language keyword matching. This zero-configuration approach eliminates iterative review sessions while maintaining high precision across 120+ countries and 15+ languages.

References
------------------------------------------------------------------------------

Web of Science (WoS) provides cited references in a standardized, preprocessed format that can be directly used for citation-based analyses, whereas Scopus delivers references as unstructured text strings. To address this limitation, TechMiner2+ scans and parses Scopus document references to generate a normalized Rec-ID field that mirrors the structure of WoS reference identifiers. This Rec-ID is then used to reformat Scopus references, effectively emulating WoS-style downloaded data and enabling consistent citation, co-citation, and coupling analyses across data sources. This field is used to compute local citation counts and build citation networks from Scopus data.


General metrics and indicators
------------------------------------------------------------------------------

Bibliometrix provides a well-established, publication-ready snapshot of a bibliographic dataset, focusing on core productivity and collaboration indicators. tm2+ retains this foundation but improves semantic precision, separates overlapping concepts, extends collaboration and affiliation analytics, and—critically—integrates NLP and lexical diagnostics that prepare the dataset for advanced modeling. As a result, tm2+ shifts descriptive statistics from a reporting artifact into an active quality-control and readiness layer for end-to-end bibliometric and text-based analysis.


Review of recgonized noun phrases
------------------------------------------------------------------------------

tm2+ allows the user to inspect and validate noun phrase extraction directly on the original abstracts**, highlighting extracted noun phrases in uppercase to distinguish them from surrounding text. It also supports focused review of abstract suffixes, where copyright and publisher boilerplate are often appended and mistakenly identified as noun phrases. In addition, tm2+ exposes colon-delimited headings in structured abstracts, which can otherwise be confused with meaningful concepts. By making these artifacts explicit, tm2+ enables manual correction and re-execution of noun phrase extraction, turning NLP preprocessing into an iterative, transparent, and quality-controlled process.


Thesaurus
------------------------------------------------------------------------------

In VantagePoint, thesaurus management is implemented as an interactive, exploratory process in which fuzzy-cutoff algorithms are used to identify candidate key matches and the user manually decides which keys to merge, with no automatic consolidation. In tm2+, the same conceptual approach is preserved but implemented in a console-based, scriptable workflow: matchers generate explicit candidate pairs, merge decisions are applied explicitly and logged, and recomputation is triggered deliberately rather than implicitly. Unlike VantagePoint, tm2+ exposes the matching and merging steps as repeatable operations that can be integrated into analytical pipelines, while still respecting the core VantagePoint principle that similarity detection suggests merges but never performs them automatically. The main matchers implemented in tm2+ are:

- ExactMatch (words-based):     
    Detects exact string equality (after minimal normalization such as trimming).
    Used as a baseline and for sanity checks.
    Case-senstive or insensitive based on configuration.

- FuzzyCutoffMatch (words-based): 
    Detects near-duplicate strings using surface-form fuzzy similarity with a cutoff threshold.
    Produces candidate pairs only, never merges.
    Scope: Keywords, noun phrases, organizations, sources (very conservative), authors (high cutoff).
    Case-insensitive.

- StemMatch (words-based):
    Finds words sharing the same root (Singular/Plural identification). It uses NLP lemmatization / stemming.
    Compare words in the same order.
    Case-insensitive.

- SignatureMatch (words-based):
    Detects equivalence by comparing normalized string signatures (fingerprints).
    Typical signature steps:
        lowercase
        remove punctuation
        tokenize
        optional stemming
        sort tokens
    Case-insensitive.

- HyphenationMatch (words-based): 
    Detects variants caused by hyphenation and spacing differences.
    Reduces fuzzy noise and catches high-confidence variants early.
    Case-insensitive.

- CaseVariationMatch (words-based): 
    Present strings that differ only in capitalization
    Case-sensitive.

- PunctuationVariationMatch (words-based): 
    Present strings that differ only in punctuation.
    Case-insensitive.

- AbbreviationMatch (words-based): 
    Detects acronym ↔ long-form relationships using first-letter logic and token alignment.
    Explicitly used by ClusterSuite (Acronym Identifier) and essential for keyword cleanup.
    Case-senstive or insensitive based on configuration.

- WordOrderMatch (words-based): 
    Detects strings composed of the same tokens in different orders.
    Case-insensitive.

- PluralSingularMatch (words-based):
    Present strings that differ only by pluralization.
    Case-insensitive.

- NumericVariationMatch (string-based): 
    Present strings with numeric variations (e.g., "test1" vs "test2")






