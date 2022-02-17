"""
Co-occurrence Network / Summarization
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> co_occurrence_network_summarization(
...     'author_keywords', 
...     min_occ=4, 
...     n_keywords=5,
...     n_phrases=3,
...     directory=directory,
... )
The research on data science and ai in FINTECH involves many latest progress made in smart
FINTECH for bankingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
cryptocurrencies, and blockchain, and the dsai techniques including complex system
methods, quantitative methods, intelligent interactions, recognition and responses, data
analytics, deep learning, federated learning, privacy-preserving processing, augmentation,
optimization, and system intelligence enhancement... From the theoretical point of view,
our research indicates, that besides key growth driving factors, outlined in existing
literature, such as strategy, prerequisites for rapid growth, business model choice,
international business networks, entrepreneur's characteristics, product development or
theoretical frameworks for development, especially within the international market, the
quality of digital logistics performance of FINTECH companies seem to matter... The most
important factors that influence the level of satisfaction when using FINTECH services
were considered: comfort and ease of use, legal regulations, ease of account opening,
mobile payments features, crowdfunding options, international money transfers features,
reduced costs associated with transactions, PEER-TO-PEER LENDING, insurances options,
online brokerage, cryptocoins options and exchange options.
<BLANKLINE>
The research on data science and ai in fintech involves many latest progress made in smart
fintech for BANKingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
cryptocurrencies, and blockchain, and the dsai techniques including complex system
methods, quantitative methods, intelligent interactions, recognition and responses, data
analytics, deep learning, federated learning, privacy-preserving processing, augmentation,
optimization, and system intelligence enhancement... From the theoretical point of view,
our research indicates, that besides key growth driving factors, outlined in existing
literature, such as strategy, prerequisites for rapid growth, business model choice,
international business networks, entrepreneur's characteristics, product development or
theoretical frameworks for development, especially within the international market, the
quality of digital logistics performance of fintech companies seem to matter... The most
important factors that influence the level of satisfaction when using fintech services
were considered: comfort and ease of use, legal REGULATIONs, ease of account opening,
mobile payments features, crowdfunding options, international money transfers features,
reduced costs associated with transactions, peer-to-peer lending, insurances options,
online brokerage, cryptocoins options and exchange options.
<BLANKLINE>
The research on data science and ai in fintech involves many latest progress made in smart
fintech for bankingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
CRYPTOCURRENCIES, and BLOCKCHAIN, and the dsai techniques including complex system
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
The research on data science and ai in fintech involves many latest progress made in smart
fintech for bankingtech, tradetech, lendtech, insurtech, wealthtech, paytech, RISKtech,
cryptocurrencies, and blockchain, and the dsai techniques including complex system
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
reduced costs associated with transactions, PEER-TO-PEER lending, insurances options,
online brokerage, cryptocoins options and exchange options.
<BLANKLINE>



"""

from .co_occurrence_network_communities import co_occurrence_network_communities
from .keywords_summarization import keywords_summarization


def co_occurrence_network_summarization(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    n_keywords=5,
    n_phrases=10,
    directory="./",
):

    cm = co_occurrence_network_communities(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
        directory=directory,
    )

    cm = cm.head(n_keywords).transpose()

    for row in cm.iterrows():

        list_of_keywords = []

        for word in row[1]:
            word = word.split(" ")
            word = word[:-1]
            word = " ".join(word)
            list_of_keywords.append(word)

        keywords_summarization(
            column=column,
            keywords=list_of_keywords,
            n_phrases=n_phrases,
            sufix="_" + row[0],
            directory=directory,
        )

        print()
