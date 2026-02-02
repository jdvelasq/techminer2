![logo](https://raw.githubusercontent.com/jdvelasq/techminer2/main/assets/logo.jpg)

A Python Library for Tech-Mining, Bibliometrics and Science Mapping.


Noun phrases
------------------------------------------------------------------------------

Unlike commonly used bibliometric and scientometric tools, which extract noun phrases using a single linguistic pipeline and resolve overlapping or fragmented terms through post hoc cleaning, TechMiner2+ implements a deterministic, multi-source extraction strategy designed to preserve conceptual integrity at extraction time. Noun phrases are independently derived from multiple NLP engines, combined with author and index keywords and curated vocabularies, and ordered by phrase length to enforce longest-term precedence. By re-injecting these terms into tokenized abstracts through a masking strategy, tm2+ prevents the fragmentation of multiword concepts, ensuring stable and semantically coherent units for downstream analysis.



