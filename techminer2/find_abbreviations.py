"""
Find Abbreviations
===============================================================================

Finds string abbreviations in the keywords of a thesaurus.

>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> find_abbreviations(
...     "words.txt",
...     directory=directory,
... )
aml
    aml
anti money laundering
    anti money laundering
    anti money laundering (aml)
antimoney laundering
    antimoney laundering
    antimoney laundering (aml)
ai
    ai
    ai strategy
artificial intelligence
    artificial intelligence
    artificial intelligence (ai)
artificial intelligence (ai) governance
    artificial intelligence (ai) governance
artificial neural network
    artificial neural network
    neural network
    neural networks
    neural networks (computer)
computational methods
    computational methods
    computer
    computers
bank regulation
    bank regulation
    bank regulation (basel iii)
    bank regulations
    bank regulators
    banking regulation
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
    compliance.
grc
    grc
contract
    contract
    contracting
    contracts
    contracts (htlc)
hashed timelock contracts (htlc)
    hashed timelock contracts (htlc)
corporate social responsibilities (csr)
    corporate social responsibilities (csr)
    corporate social responsibility
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
distributed ledger technologies
    distributed ledger technologies
    distributed ledger technology
    distributed ledger technology (dlt)
dlt
    dlt
financial technologies
    financial technologies
    financial technologies (fintech)
    financial technology
    financial technology (fintech)
fintech
    fintech
    fintechs
gdpr
    gdpr
general data protection regulation
    general data protection regulation
    general data protection regulation (gdpr)
    general data protection regulations
ict
    ict
information and communication technologies
    information and communication technologies
    information and communication technology
    information and communication technology (ict)
    information and communications technologies (icts)
    information and communications technology
information technologies
    information technologies
    information technology
    information technology (it)
it
    it
ico
    ico
    icos
initial coin offering
    initial coin offering
    initial coin offering (ico)
    initial coin offerings
internet of thing (iot)
    internet of thing (iot)
    internet of things
    internet of things (iot)
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
    legalization of proceeds
natural language processing
    natural language processing
    natural language processing (nlp)
nlp
    nlp
partial least square structural equation modeling
    partial least square structural equation modeling
    partial least squares structural equation modeling (plssem)
plssem
    plssem
p2p
    p2p
peertopeer (p2p) lending
    peertopeer (p2p) lending
    peertopeer lending
peertopeer (p2p) lending risk evaluation
    peertopeer (p2p) lending risk evaluation
proof of work
    proof of work
    proof of work (pow)
proofofwork (pow)
    proofofwork (pow)
recurrent neural network (rnn)
    recurrent neural network (rnn)
    recurrent neural networks
rnn
    rnn
regtech
    regtech
    regtech.
regulatory technologies (regtech)
    regulatory technologies (regtech)
    regulatory technology
    regulatory technology (regtech)
rdf
    rdf
resource description framework (rdf)
    resource description framework (rdf)
    resources description frameworks
regulation
    regulation
    regulations
standard
    standard (regulation)
    standard model
    standard models
    standardization
    standards
    standard
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

from .thesaurus import load_file_as_dict


def find_abbreviations(
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
