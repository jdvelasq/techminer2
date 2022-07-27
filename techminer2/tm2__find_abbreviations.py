"""
Find Abbreviations
===============================================================================

Finds string abbreviations in the keywords of a thesaurus.


>>> directory = "data/regtech/"

>>> from techminer2 import tm2__find_abbreviations
>>> tm2__find_abbreviations(
...     "keywords.txt",
...     directory=directory,
... )
artificial intelligence
    artificial intelligence
    artificial intelligence (ai)
artificial intelligence (ai) governance
    artificial intelligence (ai) governance
ai
    ai
    ai strategy
aml
    aml
anti money laundering (aml)
    anti money laundering (aml)
    anti money laundering
anti-money laundering
    anti-money laundering
    anti-money laundering (aml)
banking regulation
    banking regulation
    bank regulation
    bank regulation (basel iii)
    bank regulations
    bank regulators
basel iii
    basel iii
communication channel
    communication channel
    communication channels (information theory)
information theory
    information theory
competition
    competition
    competition (economics)
    competitiveness
economics
    economics
compliance
    compliance
    compliance (grc)
    compliance approach
grc
    grc
contracts
    contracts
    contract
    contracting
    contracts (htlc)
hashed timelock contracts (htlc)
    hashed timelock contracts (htlc)
corporate social responsibility
    corporate social responsibility
    corporate social responsibilities (csr)
csr
    csr
dao
    dao
decentralized autonomous organization
    decentralized autonomous organization
    decentralized autonomous organization (dao)
dapp
    dapp
    dapps
distributed applications
    distributed applications
    distributed applications (dapps)
distributed ledger technology
    distributed ledger technology
    distributed ledger technologies
    distributed ledger technology (dlt)
dlt
    dlt
financial technology
    financial technology
    financial technologies
    financial technology (fintech)
    financial technologies (fintech)
fintech
    fintech
    fintechs
gdpr
    gdpr
general data protection regulations
    general data protection regulations
    general data protection regulation
    general data protection regulation (gdpr)
ict
    ict
information and communication technologies
    information and communication technologies
    information and communication technology
    information and communication technology (ict)
    information and communications technologies (icts)
    information and communications technology
information technology
    information technology
    information technologies
    information technology (it)
it
    it
ico
    ico
    icos
initial coin offerings
    initial coin offerings
    initial coin offering
    initial coin offering (ico)
internet of things
    internet of things
    internet of things (iot)
    internet of thing (iot)
iot
    iot
know your customer (kyc) compliance
    know your customer (kyc) compliance
youre your customer (kyc)
    youre your customer (kyc)
laundering
    laundering
legalization (laundering) of proceeds
    legalization (laundering) of proceeds
natural language processing
    natural language processing
    natural language processing (nlp)
nlp
    nlp
computers
    computers
    computer
    computational methods
neural networks
    neural networks
    neural network
    neural networks (computer)
partial least square structural equation modeling
    partial least square structural equation modeling
    partial least squares structural equation modeling (pls-sem)
pls-sem
    pls-sem
p2p
    p2p
peer-to-peer (p2p) lending risk evaluation
    peer-to-peer (p2p) lending risk evaluation
peer-to-peer lending
    peer-to-peer lending
    peer-to-peer (p2p) lending
proof of work
    proof of work
    proof of work (pow)
proof-of-work (pow)
    proof-of-work (pow)
recurrent neural network (rnn)
    recurrent neural network (rnn)
    recurrent neural networks
rnn
    rnn
regtech
    regtech
regulatory technology
    regulatory technology
    regulatory technology (regtech)
    regulatory technologies
    regulatory technologies (regtech)
rdf
    rdf
resource description framework (rdf)
    resource description framework (rdf)
    resources description frameworks
regulation
    regulation
    regulations
standardization
    standardization
    standards
    standard (regulation)
    standard model
    standard models
team software process (tsp)
    team software process (tsp)
tsp
    tsp
tam
    tam
technology acceptance model
    technology acceptance model
    technology acceptance model (tam)
the unified theory of acceptance and use of technology(utaut)
    the unified theory of acceptance and use of technology(utaut)
    unified theory of acceptance and use of technology
    unified theory of acceptance and use technology (utaut)
utaut
    utaut
tism
    tism
total interpretive structural modeling (tism)
    total interpretive structural modeling (tism)
mathematical models
    mathematical models
    mathematical techniques
    mathematics
trees (mathematics)
    trees (mathematics)




"""
from os.path import isfile, join

import pandas as pd

from ._thesaurus import load_file_as_dict


def tm2__find_abbreviations(
    thesaurus_file,
    directory="./",
):
    """Find abbreviations and reorder the thesaurus to reflect the search."""

    def extract_abbreviation(x):
        if "(" in x:
            abbreviation = x[x.find("(") + 1 : x.find(")")]
            return abbreviation
        return None

    # ----< Load and reverse the thesaurus >------------------------------------------------------
    th_file = join(directory, "processed", thesaurus_file)
    if isfile(th_file):
        th = load_file_as_dict(th_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(th_file))
    reversed_th = {value: key for key, values in th.items() for value in values}

    # ----< search for abbreviations >-------------------------------------------------------------
    df = pd.DataFrame(
        {
            "text": reversed_th.keys(),
            "key": reversed_th.values(),
        }
    )
    df["abbreviation"] = df["text"].map(extract_abbreviation)

    # ----< filter by each abbreviation >----------------------------------------------------------
    abbreviations = df.abbreviation.dropna().drop_duplicates()

    results = []
    for abbreviation in abbreviations.to_list():

        keywords = df[
            df.text.map(lambda x: x == abbreviation)
            | df.text.str.contains("(" + abbreviation + ")", regex=False)
            | df.text.map(lambda x: x == "(" + abbreviation + ")")
            | df.text.str.contains("\b" + abbreviation + "\b", regex=True)
        ]

        keywords = keywords.key.drop_duplicates()

        if len(keywords) > 1:
            results.append(keywords.to_list())

    # ----< remove found keywords >-----------------------------------------------------------------
    results = [value for result in results for value in result]
    findings = {key: th[key] for key in results}
    for key in findings.keys():
        th.pop(key)

    # ----< save the thesaurus >--------------------------------------------------------------------
    with open(th_file, "w", encoding="utf-8") as file:

        for key in findings.keys():
            print(key)
            file.write(key + "\n")
            for item in findings[key]:
                file.write("    " + item + "\n")
                print("    " + item)

        for key in sorted(th.keys()):
            file.write(key + "\n")
            for item in th[key]:
                file.write("    " + item + "\n")
