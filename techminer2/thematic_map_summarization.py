"""
Thematic Map / Summarization
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> thematic_map_summarization(
...     'author_keywords', 
...     min_occ=4, 
...     n_keywords=5,
...     n_phrases=3,
...     directory=directory,
... )
The research on data science and ai in FINTECH involves many latest progress made in smart
FINTECH for BANKingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
cryptocurrencies, and blockchain, and the dsai techniques including complex system
methods, quantitative methods, intelligent interactions, recognition and responses, data
analytics, deep learning, federated learning, privacy-preserving processing, augmentation,
optimization, and system intelligence enhancement... From the theoretical point of view,
our research indicates, that besides key growth driving factors, outlined in existing
literature, such as strategy, prerequisites for rapid growth, business model choice,
international business networks, entrepreneur's characteristics, product development or
theoretical frameworks for development, especially within the international market, the
quality of digital logistics performance of FINTECH companies seem to matter... Internet
BANKing, mobile BANKing, atm,cash deposit machines, instant payment services, online
trading in stock markets, online funds transfers, e-wallets,wealth management, peer to
peer lending, blockchain technology are various FINTECH products and services.
<BLANKLINE>
Overall, the interconnectedness of the cross-sector fintech beyond the fintech sectors
drives the fuzzy boundaries between ECOSYSTEMs, established business models, terminology
definitions, ECOSYSTEM actors roles and relationships, which appear to become more
heterogeneous and changeable over time... Several factors are included in the analysis,
controlling for the hedonics of the fintech, including the business model, availability of
and access to finance, and business ECOSYSTEM framework... We conceptualise three
practices, as building blocks at the ECOSYSTEM level, through which incumbents and new
entrants shape financial inclusion: (1) innovative and collaborative practices, (2)
protectionist and equitable practices, and (3) legitimising and sustaining practices.
<BLANKLINE>
The most important factors that influence the level of satisfaction when using fintech
services were considered: comfort and ease of use, legal regulations, ease of account
opening, mobile payments features, crowdfunding options, international money transfers
features, reduced costs associated with transactions, PEER-TO-PEER LENDING, insurances
options, online brokerage, cryptocoins options and exchange options... The application of
a series of artificial intelligence technologies such as data mining, accurate profiling,
machine learning, neural networks, will provide financial products, service channels,
service methods, RISK management, credit financing and investment decision-making have
brought about a new round of changes... This study mainly focuses on how different
cognitive factors such as perceived expenditure, ease of time, level of RISK, service
quality, frequent use of automated tools, socio cultural factors, perceived TRUST,
perceived usability and perceived convenience to use influence the users motive to adopt
and utilise the financial technology.
<BLANKLINE>
From the theoretical point of view, our research indicates, that besides key growth
driving factors, outlined in existing literature, such as strategy, prerequisites for
rapid growth, business model choice, international business networks, entrepreneur's
characteristics, product development or theoretical frameworks for development, especially
within the international market, the quality of DIGITAL logistics performance of fintech
companies seem to matter... The most important factors that influence the level of
satisfaction when using fintech services were considered: comfort and ease of use, legal
regulations, ease of account opening, mobile payments features, CROWDFUNDING options,
international money transfers features, reduced costs associated with transactions, peer-
to-peer lending, insurances options, online brokerage, cryptocoins options and exchange
options... These research streams are related to cryptocurrencies, smart contracts,
financial technology, financial industry stability, service, innovation, regulatory
technology (REGTECH), and machine learning and deep learning innovations.
<BLANKLINE>
The research on data science and ai in fintech involves many latest progress made in smart
fintech for bankingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
CRYPTOCURRENCIES, and blockchain, and the dsai techniques including complex system
methods, quantitative methods, intelligent interactions, recognition and responses, data
analytics, deep learning, federated learning, privacy-preserving processing, augmentation,
optimization, and system intelligence enhancement... From the theoretical point of view,
our research indicates, that besides key growth driving factors, outlined in existing
literature, such as strategy, prerequisites for rapid growth, business model choice,
international business networks, entrepreneur's characteristics, product development or
theoretical frameworks for development, especially within the international market, the
quality of digital logistics performance of fintech companies seem to matter... The most
important factors that influence the level of satisfaction when using fintech services
were considered: comfort and ease of use, legal regulations, ease of account opening,
mobile payments features, crowdfunding options, international money transfers features,
reduced costs associated with transactions, peer-to-peer lending, insurances options,
online brokerage, cryptocoins options and exchange options.
<BLANKLINE>


"""


from .co_occurrence_network_summarization import co_occurrence_network_summarization


def thematic_map_summarization(
    column,
    min_occ=2,
    max_occ=None,
    n_keywords=5,
    n_phrases=10,
    directory="./",
):

    return co_occurrence_network_summarization(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization="association",
        clustering_method="louvain",
        manifold_method=None,
        n_keywords=n_keywords,
        n_phrases=n_phrases,
        directory=directory,
    )
