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
Internet BANKing, mobile BANKing, atm,cash deposit machines, instant payment services,
online trading in stock markets, online funds transfers, e-wallets,wealth management, peer
to peer lending, blockchain TECHNOLOGY are various fintech products and services... This
consequently puts the FINANCIAL SERVICEs industry under additional pressure and constant
growing competition from the financial sector participants, from large TECHNOLOGY
companies such as google, apple, facebook, amazon, from large fintech companies such as
paypal, moven, transferwise, mobile network operators and other existing and potential
market players... To address these questions, the paper examines how the decision of the
united kingdom to leave the european union has influenced the financial TECHNOLOGY
(fintech) industry in london, applying data collected from in-depth interviews, covering
different groups of stakeholders in londons fintech industry, such as angel investors,
BANKs, legal advisers, lobby organizations and private companies.
<BLANKLINE>
The research on data science and ai in fintech involves many latest progress made in smart
fintech for bankingtech, tradetech, lendtech, insurtech, wealthtech, paytech, risktech,
CRYPTOCURRENCIES, and blockchain, and the dsai techniques including complex system
methods, quantitative methods, intelligent interactions, recognition and responses, data
analytics, deep learning, federated learning, privacy-preserving processing, augmentation,
optimization, and system intelligence enhancement... The application of a series of
ARTIFICIAL INTELLIGENCE technologies such as data mining, accurate profiling, MACHINE
LEARNING, neural networks, will provide financial products, service channels, service
methods, risk management, credit financing and investment decision-making have brought
about a new round of changes... These research streams are related to CRYPTOCURRENCIES,
SMART CONTRACTs, financial technology, financial industry stability, service, innovation,
regulatory technology (regtech), and MACHINE LEARNING and deep learning innovations.
<BLANKLINE>
The most important factors that influence the level of satisfaction when using fintech
services were considered: comfort and ease of use, legal regulations, ease of account
opening, mobile payments features, crowdfunding options, international money transfers
features, reduced costs associated with transactions, PEER-TO-PEER lending, insurances
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



"""

from .abstract_summarization import abstract_summarization
from .co_occurrence_network_communities import co_occurrence_network_communities


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
        abstract_summarization(
            texts=list_of_keywords,
            n_phrases=n_phrases,
            directory=directory,
        )
        print()
