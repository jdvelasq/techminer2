# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

import os
from pprint import pprint  # type: ignore

import openai
from colorama import Fore
from openai import OpenAI
from tqdm import tqdm  # type: ignore

from techminer2.database.search import ConcordantSentences
from techminer2.database.tools import ExtendStopwords
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus.descriptors import GetValues

# -----------------------------------------------------------------------------

PROMPT_PHASE_1_WITH_CONTEXT_PHRASES = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.


TASK:
Determine whether the candidate TERM is a technical or domain-specific concept,
term, or entity in the current core area <<{core_area}>>, or in any closely 
related technical, scientific, business, analytics, or technology domain.


RELATED INTEREST AREAS:
-   Business analytics (risk analytics, people analytics, health analytics, 
    consumer analytics, retail analytics, fraud analytics, operational 
    research, customer analytics, marketing analytics, supply chain analytics, 
    human resources analytics, workforce analytics, data governance, data 
    privacy)
-   Machine learning and generative AI (deep learning, neural networks, 
    reinforcement learning, supervised/unsupervised learning, generative 
    models)
-   Technology-driven business domains (prop-tech, govtech, adtech, martech, 
    regtech, insurtech, legaltech, fintech, edutech, wealth tech, retailtech, 
    regulatory technology)
-   Teaching and learning analytics (blended learning, educational data mining, 
    adaptive learning, edutech)
-   Business intelligence and big data (big data analytics, chain analytics, 
    blockchain, cloud computing, data warehousing, data lakes)
-   Digital twins (virtual modeling, simulation, cyber-physical systems, IoT 
    integration)
-   Energy economics and sustainable energy (energy modeling, energy markets, 
    renewable energy, forecasting, AI in energy, smart grids)
-   Industry 4.0, Fourth Industrial Revolution, Fifth Industrial Revolution 
    (smart manufacturing, cyber-physical systems, IoT, automation, robotics, 
    human-centric innovation, edge computing, quantum computing)
-   Cybersecurity (information security, network security, data protection, 
    threat intelligence)
-   Biotechnology and bioinformatics (genomics, proteomics, biomedical 
    analytics, health informatics)
-   Smart cities and urban analytics (urban mobility, transportation 
    analytics, infrastructure analytics, sustainability, IoT for cities)
-   Mobility and transportation analytics (traffic modeling, logistics, 
    autonomous vehicles, public transport optimization)

    
DEFINITION:
A technical or domain-specific concept, term, or entity is any word or phrase 
that refers to a device, technology, organization type, scientific method, 
model, algorithm, application, business concept, process, metric, standard, 
regulation, framework, protocol, system, tool, platform, product, service, data 
type, analytical approach, or any other concept that is specific and meaningful 
within <<{core_area}>> or any of the related interest areas listed above.


Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms (noun phrases 
    / keywords).
-   Multi-word terms are indexed separately from their headwords. Therefore, 
    contexts for an isolated TERM do not include occurrences that belong to its 
    multi-word variants.


INSTRUCTIONS:
-   Use your domain knowledge, the provided core area, interest areas, and the 
    CONTEXT PHRASES below to make the determination.
-   Consider whether the TERM is recognized as technical or domain-specific in 
    <<{core_area}>> or in any other related domain.
-   Do not rely solely on frequency or CONTEXT PHRASES; focus on the TERM's 
    recognized meaning and relevance.
-   If you are unsure or the TERM is ambiguous, default to "no".


OUTPUT:
Return ONLY one word: "yes" or "no". Do not include any explanation, reasoning, or 
punctuation. If your answer contains anything other than "yes" or "no", it will 
be considered invalid.



TERM:
<<{pattern}>>


CONTEXT PHRASES:
{contexts}

"""

# -----------------------------------------------------------------------------

PROMPT_PHASE_1_WITHOUT_CONTEXT_PHRASES = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.


TASK:
Determine whether the candidate TERM is a technical or domain-specific concept,
term, or entity in the current core area <<{core_area}>>, or in any closely 
related technical, scientific, business, analytics, or technology domain.


RELATED INTEREST AREAS:
-   Business analytics (risk analytics, people analytics, health analytics, 
    consumer analytics, retail analytics, fraud analytics, operational 
    research, customer analytics, marketing analytics, supply chain analytics, 
    human resources analytics, workforce analytics, data governance, data 
    privacy)
-   Machine learning and generative AI (deep learning, neural networks, 
    reinforcement learning, supervised/unsupervised learning, generative 
    models)
-   Technology-driven business domains (prop-tech, govtech, adtech, martech, 
    regtech, insurtech, legaltech, fintech, edutech, wealth tech, retailtech, 
    regulatory technology)
-   Teaching and learning analytics (blended learning, educational data mining, 
    adaptive learning, edutech)
-   Business intelligence and big data (big data analytics, chain analytics, 
    blockchain, cloud computing, data warehousing, data lakes)
-   Digital twins (virtual modeling, simulation, cyber-physical systems, IoT 
    integration)
-   Energy economics and sustainable energy (energy modeling, energy markets, 
    renewable energy, forecasting, AI in energy, smart grids)
-   Industry 4.0, Fourth Industrial Revolution, Fifth Industrial Revolution 
    (smart manufacturing, cyber-physical systems, IoT, automation, robotics, 
    human-centric innovation, edge computing, quantum computing)
-   Cybersecurity (information security, network security, data protection, 
    threat intelligence)
-   Biotechnology and bioinformatics (genomics, proteomics, biomedical 
    analytics, health informatics)
-   Smart cities and urban analytics (urban mobility, transportation 
    analytics, infrastructure analytics, sustainability, IoT for cities)
-   Mobility and transportation analytics (traffic modeling, logistics, 
    autonomous vehicles, public transport optimization)

    
DEFINITION:
A technical or domain-specific concept, term, or entity is any word or phrase 
that refers to a device, technology, organization type, scientific method, 
model, algorithm, application, business concept, process, metric, standard, 
regulation, framework, protocol, system, tool, platform, product, service, data 
type, analytical approach, or any other concept that is specific and meaningful 
within <<{core_area}>> or any of the related interest areas listed above.


INSTRUCTIONS:
-   Use your domain knowledge, the provided core area, and interest areas, to 
    make the determination.
-   Consider whether the TERM is recognized as technical or domain-specific in 
    <<{core_area}>> or in any other related domain.
-   Focus on the TERM's recognized meaning and relevance.
-   If you are unsure or the TERM is ambiguous, default to "no".


OUTPUT:
OUTPUT:
Return ONLY one word: "yes" or "no". Do not include any explanation, reasoning, or 
punctuation. If your answer contains anything other than "yes" or "no", it will 
be considered invalid.

TERM:
<<{pattern}>>


"""

# -----------------------------------------------------------------------------

PROMPT_PHASE_2_WITH_CONTEXT_PHRASES = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.


CONTEXT:
Decide whether a candidate TERM should be treated as a stopword for 
bibliometric/tech-mining theme discovery in the core area <<{core_area}>> or 
related interest areas. A stopword is a generic or non-discriminative term that 
does not help surface dominant or emergent themes. A stopword does not have a 
clear and specific meaning in the domain or related core areas.

Important extraction assumption:
-   The corpus has been pre-processed to extract meaningful terms (noun phrases 
    / keywords).
-   Multi-word terms are indexed separately from their headwords. Therefore, 
    contexts for an isolated TERM do not include occurrences that belong to its 
    multi-word variants.

    
NOTE:
Technical or domain-specific terms have already been filtered out by a previous 
step. Only generic, ambiguous, or non-discriminative terms remain for 
evaluation.


TASK:
Return exactly one lowercase word with no punctuation:
- "yes": exclude the TERM as a stopword
- "no": retain the TERM as useful


INSTRUCTIONS:
1.  Use your domain knowledge, the provided core area, interest areas, and the 
    CONTEXT PHRASES below to make your analysis.
2.  List reasons why the TERM should be excluded as a stopword (e.g., it is 
    generic, lacks specific meaning, or does not help identify 
    dominant/emergent themes) in the core area of <<{core_area}>> or in any 
    other related domain.
3.  List reasons why the TERM should be retained (e.g., it is contextually 
    meaningful, helps distinguish themes, or is used in a specific way in 
    the core area of <<{core_area}>> or in any other related domain).
4.  Decide based on the strength and clarity of the arguments. Exclude ("yes") 
    only if the TERM is clearly generic or non-discriminative. If arguments are 
    balanced or ambiguous, default to "no" (retain).
5.  Always return the same answer for the same TERM + contexts.


RELATED INTEREST AREAS:
-   Business analytics (risk analytics, people analytics, health analytics, 
    consumer analytics, retail analytics, fraud analytics, operational 
    research, customer analytics, marketing analytics, supply chain analytics, 
    human resources analytics, workforce analytics, data governance, data 
    privacy)
-   Machine learning and generative AI (deep learning, neural networks, 
    reinforcement learning, supervised/unsupervised learning, generative 
    models)
-   Technology-driven business domains (prop-tech, govtech, adtech, martech, 
    regtech, insurtech, legaltech, fintech, edutech, wealth tech, retailtech, 
    regulatory technology)
-   Teaching and learning analytics (blended learning, educational data mining, 
    adaptive learning, edutech)
-   Business intelligence and big data (big data analytics, chain analytics, 
    blockchain, cloud computing, data warehousing, data lakes)
-   Digital twins (virtual modeling, simulation, cyber-physical systems, IoT 
    integration)
-   Energy economics and sustainable energy (energy modeling, energy markets, 
    renewable energy, forecasting, AI in energy, smart grids)
-   Industry 4.0, Fourth Industrial Revolution, Fifth Industrial Revolution 
    (smart manufacturing, cyber-physical systems, IoT, automation, robotics, 
    human-centric innovation, edge computing, quantum computing)
-   Cybersecurity (information security, network security, data protection, 
    threat intelligence)
-   Biotechnology and bioinformatics (genomics, proteomics, biomedical 
    analytics, health informatics)
-   Smart cities and urban analytics (urban mobility, transportation 
    analytics, infrastructure analytics, sustainability, IoT for cities)
-   Mobility and transportation analytics (traffic modeling, logistics, 
    autonomous vehicles, public transport optimization)


OUTPUT:
Return ONLY one word: "yes" or "no". Do not include any explanation, reasoning, or 
punctuation. If your answer contains anything other than "yes" or "no", it will 
be considered invalid.


TERM:
<<{pattern}>>


CONTEXT PHRASES:
{contexts}

"""

# -----------------------------------------------------------------------------

PROMPT_PHASE_2_WITHOUT_CONTEXT_PHRASES = """
ROLE:
You are an expert in scientometrics and text mining, with experience in co-word 
and tech-mining studies.


CONTEXT:
Decide whether a candidate TERM should be treated as a stopword for 
bibliometric/tech-mining theme discovery in the core area <<{core_area}>> or 
related interest areas. A stopword is a generic or non-discriminative term that 
does not help surface dominant or emergent themes. A stopword does not have a 
clear and specific meaning in the domain or related core areas.

    
NOTE:
Technical or domain-specific terms have already been filtered out by a previous 
step. Only generic, ambiguous, or non-discriminative terms remain for 
evaluation.


TASK:
Return exactly one lowercase word with no punctuation:
- "yes": exclude the TERM as a stopword
- "no": retain the TERM as useful


INSTRUCTIONS:
1.  Use your domain knowledge, the provided core area, and the interest areas,
    to make your analysis.
2.  List reasons why the TERM should be excluded as a stopword (e.g., it is 
    generic, lacks specific meaning, or does not help identify 
    dominant/emergent themes) in the core area of <<{core_area}>> or in any 
    other related domain.
3.  List reasons why the TERM should be retained (e.g., it is contextually 
    meaningful, helps distinguish themes, or is used in a specific way in 
    the core area of <<{core_area}>> or in any other related domain).
4.  Decide based on the strength and clarity of the arguments. Exclude ("yes") 
    only if the TERM is clearly generic or non-discriminative. If arguments are 
    balanced or ambiguous, default to "no" (retain).
5.  Always return the same answer for the same TERM + contexts.


RELATED INTEREST AREAS:
-   Business analytics (risk analytics, people analytics, health analytics, 
    consumer analytics, retail analytics, fraud analytics, operational 
    research, customer analytics, marketing analytics, supply chain analytics, 
    human resources analytics, workforce analytics, data governance, data 
    privacy)
-   Machine learning and generative AI (deep learning, neural networks, 
    reinforcement learning, supervised/unsupervised learning, generative 
    models)
-   Technology-driven business domains (prop-tech, govtech, adtech, martech, 
    regtech, insurtech, legaltech, fintech, edutech, wealth tech, retailtech, 
    regulatory technology)
-   Teaching and learning analytics (blended learning, educational data mining, 
    adaptive learning, edutech)
-   Business intelligence and big data (big data analytics, chain analytics, 
    blockchain, cloud computing, data warehousing, data lakes)
-   Digital twins (virtual modeling, simulation, cyber-physical systems, IoT 
    integration)
-   Energy economics and sustainable energy (energy modeling, energy markets, 
    renewable energy, forecasting, AI in energy, smart grids)
-   Industry 4.0, Fourth Industrial Revolution, Fifth Industrial Revolution 
    (smart manufacturing, cyber-physical systems, IoT, automation, robotics, 
    human-centric innovation, edge computing, quantum computing)
-   Cybersecurity (information security, network security, data protection, 
    threat intelligence)
-   Biotechnology and bioinformatics (genomics, proteomics, biomedical 
    analytics, health informatics)
-   Smart cities and urban analytics (urban mobility, transportation 
    analytics, infrastructure analytics, sustainability, IoT for cities)
-   Mobility and transportation analytics (traffic modeling, logistics, 
    autonomous vehicles, public transport optimization)


OUTPUT:
Return ONLY one word: "yes" or "no". Do not include any explanation, reasoning, or 
punctuation. If your answer contains anything other than "yes" or "no", it will 
be considered invalid.


TERM:
<<{pattern}>>

"""


# -----------------------------------------------------------------------------
def internal__user_input(core_area):

    if core_area is None:
        answer = colorized_input(". Enter the core area > ").strip()
        if answer == "":
            return None, None, None
    else:
        answer = colorized_input(f". Enter the core area [{core_area}] > ").strip()

    if answer != "":
        core_area = answer.upper()

    pattern = colorized_input(". Enter the pattern > ").strip()
    if pattern == "":
        return None, None, None

    n_contexts = colorized_input(
        ". Enter the number of contexts [default: 30] > "
    ).strip()
    if n_contexts == "":
        n_contexts = 30
    else:
        n_contexts = int(n_contexts)

    return core_area, pattern, n_contexts


# -----------------------------------------------------------------------------
def internal__get_contexts(pattern, n_contexts):

    terms = GetValues().with_patterns([pattern]).where_root_directory_is("./").run()
    terms = [term for term in terms if pattern in term]

    complete_contexts = []

    for term in terms:

        contexts = (
            ConcordantSentences()
            #
            .with_abstract_having_pattern(term)
            .where_root_directory_is("./")
            .where_database_is("main")
            .where_record_years_range_is(None, None)
            .where_record_citations_range_is(None, None)
            #
            .run()
        )

        contexts = [c for c in contexts if len(c) > 80]
        contexts = [f"- {c} ." for c in contexts]
        contexts = [c.lower().replace("_", " ") for c in contexts]

        complete_contexts.extend(contexts)

    pattern = pattern.lower().replace("_", " ")
    complete_contexts = [c for c in complete_contexts if pattern in c]

    if len(complete_contexts) < 5:
        return None

    return complete_contexts[:n_contexts]


# -----------------------------------------------------------------------------
def internal__execute_query(core_area, pattern, contexts):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Phase 1: Domain-specific terms
    # ----------------------------------------------------------

    if contexts is None:
        query = PROMPT_PHASE_1_WITHOUT_CONTEXT_PHRASES.format(
            pattern=pattern,
            core_area=core_area,
        )
    else:
        query = PROMPT_PHASE_1_WITH_CONTEXT_PHRASES.format(
            pattern=pattern,
            core_area=core_area,
            contexts="\n".join(contexts),
        )

    try:

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        is_domain_specific = response.output_text
        is_domain_specific = is_domain_specific.strip().lower()
        if is_domain_specific == "yes":
            return "no"

    except openai.OpenAIError as e:
        print(f"Error processing the query: {e}")
        return None

    # Phase 2: Other terms
    # ----------------------------------------------------------

    if contexts is None:
        query = PROMPT_PHASE_2_WITHOUT_CONTEXT_PHRASES.format(
            pattern=pattern,
            core_area=core_area,
        )
    else:
        query = PROMPT_PHASE_2_WITH_CONTEXT_PHRASES.format(
            pattern=pattern,
            core_area=core_area,
            contexts="\n".join(contexts),
        )

    try:

        response = client.responses.create(
            model="gpt-4o",
            input=query,
            temperature=0,
        )

        is_stopword = response.output_text
        is_stopword = is_stopword.strip().lower()

        return is_stopword

    except openai.OpenAIError as e:
        print(f"Error processing the query: {e}")
        return None


# -----------------------------------------------------------------------------
def internal__print_answer(answer):

    text = (
        Fore.LIGHTBLACK_EX
        + "The term "
        + Fore.RESET
        + "{result}"
        + Fore.LIGHTBLACK_EX
        + " is a STOPWORD."
        + Fore.RESET
    )

    if answer.lower() == "yes":
        text = text.format(result="IS")
    else:
        text = text.format(result="IS NOT")

    print()
    print(text)
    print()


# -----------------------------------------------------------------------------
def internal__extend_stopwords(pattern):

    answer = colorized_input(". Extend stopwords with pattern (y/[n])? > ").strip()
    if answer.lower() not in ["n", "no", "not", ""]:
        print()
        return

    pattern = pattern.upper().replace(" ", "_")
    ExtendStopwords().with_patterns([pattern]).where_root_directory_is("./").run()
    print()


# -----------------------------------------------------------------------------
def execute_stopwords_command():

    print()
    # internal__run_diagnostics()
    # return
    core_area = None

    while True:

        core_area, pattern, n_contexts = internal__user_input(core_area)

        if pattern is None:
            print()
            return

        contexts = internal__get_contexts(pattern, n_contexts)
        if not contexts:
            answer = "yes"
        else:
            answer = internal__execute_query(core_area, pattern, contexts)

        internal__print_answer(answer)

        if answer == "yes":
            internal__extend_stopwords(pattern)


# -----------------------------------------------------------------------------
def internal__run_diagnostics():

    patterns = [
        "ELECTRIC_UTILITIES",
        "ENERGY_GENERATION",
        "ENERGY_PRODUCTION",
        "FARMS",
        "INDUSTRY",
        "INSTALLED_CAPACITY",
        "PERFORMANCE",
        "POWER_PLANTS",
        "POWER",
        "TURBINE",
        "WIND_FARMS",
        "WIND_POWER_INDUSTRY",
        "WIND_POWER",
        "WIND_TURBINE",
        #
        "ACCOUNT",
        "AMOUNTS",
        "ANALYZES",
        "APPROACH",
        "BALANCE",
        "BASIS",
        "BENEFIT",
        "COMPARISONS",
        "CONDITION",
        "CONFIGURATION",
        "CONSIDERATIONS",
        "EFFICIENCY",
        "FORMS",
        "GOALS",
        "LOSS",
        "METHOD",
        "MODEL",
        "MODELING",
        "NUMBERS",
        "OBJECTIVES",
        "RESULTS",
        "SCENARIO",
        "SITUATION",
        "SIZES",
        "STUDY_CASE",
        "TRADE_OFF",
        "TYPE",
        "VALUE",
        "YEAR",
    ]

    summary = {}

    for pattern in tqdm(patterns, total=len(patterns), ncols=80):

        contexts = internal__get_contexts(pattern, 30)

        results = []

        for _ in range(5):

            answer = internal__execute_query(
                "economics of wind energy", pattern, contexts
            )
            results.append(answer)

        summary[pattern] = results

    print()
    print("Summary: ")
    print()
    pprint(summary)
    print()
