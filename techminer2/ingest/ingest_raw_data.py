# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _ingest.ingest_raw_data:

Ingest Raw Data
===============================================================================

Import a scopus data file in the working directory.

>>> from techminer2.ingest import ingest_raw_data
>>> ingest_raw_data(
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/", 
...     remove_raw_csv_files=True,
... )
--INFO-- Concatenating raw files in data/regtech/raw-data/cited_by/
--INFO-- Concatenating raw files in data/regtech/raw-data/references/
--INFO-- Concatenating raw files in data/regtech/raw-data/main/
--INFO-- Applying scopus tags to database files
--INFO-- Formatting column names in database files
--INFO-- Repairing authors ID
--INFO-- Repairing bad separators in keywords
--INFO-- Dropping NA columns in database files
--INFO-- Removed columns: {'page_count'}
--INFO-- Processing text columns (remove accents)
--INFO-- Processing text columns (remove stranger chars)
--INFO-- Removing records with `raw_authors` in ['Anon', '[No author name available]']
--INFO-- Removed 1 records
--INFO-- Processing `authors_id` column
--INFO-- Processing `document_type` column
--INFO-- Processing `eissn` column
--INFO-- Processing `global_citations` column
--INFO-- Processing `isbn` column
--INFO-- Processing `issn` column
--INFO-- Processing `raw_authors` column
--INFO-- Processing `source_name` column
--INFO-- Mask `source_abbr` column with `source_name`
--INFO-- Processing `source_abbr` column
--INFO-- Processing `doi` column
--INFO-- Disambiguating `authors` column
--INFO-- Copying `authors` column to `num_authors`
--INFO-- Processing `num_authors` column
--INFO-- Copying `global_references` column to `num_global_references`
--INFO-- Processing `num_global_references` column
--INFO-- Creating `article` column
--INFO-- Processing `raw_author_keywords` column
--INFO-- Processing `raw_index_keywords` column
--INFO-- Concatenating `raw_author_keywords` and `raw_index_keywords` columns to `raw_keywords`
--INFO-- Processing `title` column
--INFO-- Copying `title` column to `raw_title_nlp_phrases`
--INFO-- Processing `raw_title_nlp_phrases` column
--INFO-- Processing `abstract` column
--INFO-- Copying `abstract` column to `raw_abstract_nlp_phrases`
--INFO-- Processing `raw_abstract_nlp_phrases` column
--INFO-- Concatenating `raw_title_nlp_phrases` and `raw_abstract_nlp_phrases` columns to `raw_nlp_phrases`
--INFO-- Processing `raw_nlp_phrases` column
--INFO-- Concatenating `raw_nlp_phrases` and `raw_keywords` columns to `raw_descriptors`
--INFO-- Processing `raw_descriptors` column
--INFO-- Homogenizing local references
--INFO-- 27 local references homogenized
--INFO-- Homogenizing global references
--INFO-- 765 global references homogenized
--INFO-- The data/regtech/global_references.txt thesaurus file was applied to global_references in 'main' database
--INFO-- Creating `local_citations` column in references database
--INFO-- Creating `local_citations` column in documents database
--INFO-- The data/regtech/countries.txt thesaurus file was created
--INFO-- Creating `words.txt` from author/index keywords, and abstract/title nlp phrases
--INFO-- The data/regtech/organizations.txt thesaurus file was created
--INFO-- The data/regtech/countries.txt thesaurus file was applied to affiliations in all databases
--INFO-- Applying `words.txt` thesaurus to author/index keywords and abstract/title words
--INFO-- The data/regtech/organizations.txt thesaurus file was applied to affiliations in all databases
--INFO-- Process finished!!!
--INFO-- data/regtech/databases/_references.zip: 909 imported records
--INFO-- data/regtech/databases/_main.zip: 52 imported records
--INFO-- data/regtech/databases/_cited_by.zip: 387 imported records

>>> import pandas as pd
>>> from pprint import pprint
>>> import textwrap
>>> root_dir = "data/regtech/"
>>> my_list = pd.read_csv(root_dir + "databases/_main.zip", encoding="utf-8", compression="zip").columns.tolist()
>>> wrapped_list = textwrap.fill(", ".join(sorted(my_list)), width=79)
>>> print(wrapped_list)
abstract, abstract_nlp_phrases, affiliations, art_no, article, author_keywords,
authors, authors_id, authors_with_affiliations, coden, correspondence_address,
countries, country_1st_author, descriptors, document_type, doi, eid,
global_citations, global_references, index_keywords, isbn, issn, issue,
keywords, link, local_citations, local_references, nlp_phrases, num_authors,
open_access, organization_1st_author, organizations, page_end, page_start,
publication_stage, raw_abstract_nlp_phrases, raw_author_keywords, raw_authors,
raw_authors_id, raw_countries, raw_descriptors, raw_global_references,
raw_index_keywords, raw_keywords, raw_nlp_phrases, raw_organizations,
raw_title_nlp_phrases, source, source_abbr, source_title, title,
title_nlp_phrases, volume, year





>>> records = pd.read_csv(root_dir + "databases/_main.zip", encoding="utf-8", compression="zip")
>>> print(records[["raw_authors_id", "authors_id"]].head().to_markdown())
|    | raw_authors_id                                                           | authors_id                                                                                                                                            |
|---:|:-------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | 57194137877;57694114300;35369323900;                                     | 000000000000057194137877;000000000000057694114300;000000000000035369323900                                                                            |
|  1 | 58065730600;25928338900;57212494182;                                     | 000000000000058065730600;000000000000025928338900;000000000000057212494182                                                                            |
|  2 | 9633912200;57203071719;                                                  | 000000000000009633912200;000000000000057203071719                                                                                                     |
|  3 | 57211924905;57218104231;56779331500;56645203200;57439248400;56291956400; | 000000000000057211924905;000000000000057218104231;000000000000056779331500;000000000000056645203200;000000000000057439248400;000000000000056291956400 |
|  4 | 57206840410;57226162166;57189220315;                                     | 000000000000057206840410;000000000000057226162166;000000000000057189220315                                                                            |

    
>>> records = pd.read_csv(root_dir + "databases/_main.zip", encoding="utf-8", compression="zip")
>>> print(records["local_references"].dropna().head(10).to_markdown())
|    | local_references                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Baxter LG, 2016, DUKE LAW J, V66, P567;Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85;Ghanem S, 2021, STUD COMPUT INTELL, V954, P139;Singh C, 2020, J MONEY LAUND CONTROL, V24, P464;Turki M, 2020, HELIYON, V6;von Solms J, 2021, J BANK REGUL, V22, P152                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|  3 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|  4 | Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|  5 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Baxter LG, 2016, DUKE LAW J, V66, P567;Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161;Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801;Buckley RP, 2020, J BANK REGUL, V21, P26;Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19;Das SR, 2019, J FINANCIAL DATA SCI, V1, P8;Kavassalis P, 2018, J RISK FINANC, V19, P39;Kurum E, 2020, J FINANC CRIME;Muganyi T, 2022, FINANCIAL INNOV, V8;Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382;Singh C, 2020, J MONEY LAUND CONTROL, V24, P464;Singh C, 2022, J FINANC CRIME, V29, P45;von Solms J, 2021, J BANK REGUL, V22, P152 |
|  6 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|  8 | Singh C, 2020, J MONEY LAUND CONTROL, V24, P464                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|  9 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801;Buckley RP, 2020, J BANK REGUL, V21, P26;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85;Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219;Kurum E, 2020, J FINANC CRIME;Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382;Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135;Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787;Siering M, 2022, DECIS SUPPORT SYST, V158;von Solms J, 2021, J BANK REGUL, V22, P152                                                                                                                      |
| 10 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Baxter LG, 2016, DUKE LAW J, V66, P567;Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801;Buckley RP, 2020, J BANK REGUL, V21, P26;Gasparri G, 2019, FRONTIER ARTIF INTELL, V2;Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219;Kavassalis P, 2018, J RISK FINANC, V19, P39;Kurum E, 2020, J FINANC CRIME;Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382;Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135;Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787;Waye V, 2020, ADELAIDE LAW REV, V40, P363;von Solms J, 2021, J BANK REGUL, V22, P152                                                                                              |
| 11 | Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 12 | Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |


>>> records = pd.read_csv(root_dir + "databases/_main.zip", encoding="utf-8", compression="zip")
>>> print(records["global_references"].dropna().head(10).to_markdown())
|    | global_references                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  0 | Anselmi G, 2021, INT REV FINANC ANAL, V76;Baxter LG, 2016, DUKE LAW J, V66, P567;Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85;Elimelech OC, 2022, TECHNOL SOC, V71;Fox S, 2022, TECHNOL SOC, V71;Galaz V, 2021, TECHNOL SOC, V67;Ghanem S, 2021, STUD COMPUT INTELL, V954, P139;Ha LT, 2022, TECHNOL SOC, V68;Hildebrandt M, 2018, PHILOS TRANS R SOC A MATH PHY, V376;Ng PML, 2022, TECHNOL SOC, V70;Otrachshenko V, 2022, TECHNOL SOC, V71;Shah TR, 2022, TECHNOL SOC, V68;Singh C, 2020, J MONEY LAUND CONTROL, V24, P464;Turki M, 2020, HELIYON, V6;Ulbricht L, 2022, REGUL GOVERNANCE, V16, P3;Yeung K, 2018, REGUL GOVERNANCE, V12, P505;Zarsky T, 2016, SCI TECHNOL HUM VALUES, V41, P118;von Solms J, 2021, J BANK REGUL, V22, P152                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|  1 | Aggarwal R, 2011, J FINANC ECON, V100, P154;Aggarwal R, 2015, J FINANC, V70, P2309;Ajinkya B, 2005, J ACCOUNT RES, V43, P343;Baik B, 2010, J FINANC ECON, V97, P81;Bernile G, 2015, REV FINANC STUD, V28, P2009;Bernile G, 2019, REV FINANC ECON, V37, P38;Bodnaruk A, 2009, REV FINANC, V13, P629;Borochin P, 2017, J FINANC ECON, V126, P171;Calluzzo P, 2019, J FINANC ECON, V134, P669;Chen Z/1, 2013, ACCOUNT REV, V88, P1211;Chhaochharia V, 2012, J ACCOUNT ECON, V54, P42;Choe H, 2005, REV FINANC STUD, V18, P795;Coval JD, 1999, J FINANC, V54, P2045;Crane AD, 2019, J FINANC ECON, V133, P175;Del Guercio D, 2008, J FINANC ECON, V90, P84;Duan Y, 2016, J FINANC QUANT ANAL, V51, P489;Dyck A, 2019, J FINANC ECON, V131, P693;Ertimur Y, 2013, J ACCOUNT RES, V51, P951;Faelten A, 2014, J BUS FINANC ACCOUNT, V41, P469;Ferreira MA, 2008, J FINANC ECON, V88, P499;Fried JM, 2020, J FINANC ECON, V138, P777;GORDON LA, 1993, J FINANC, V48, P697;Gao H, 2020, FINANC MANAGE, V49, P1029;Gillan SL, 2000, J FINANC ECON, V57, P275;He JJ, 2019, J FINANC ECON, V134, P400;Hsu GC-M, 2005, CORP GOV, V13, P809;Iliev P, 2015, REV FINANC STUD, V28, P2167;Iliev P, 2015, REV FINANC STUD, V28, P446;Ivkovic Z, 2005, J FINANC, V60, P267;Jiang F/1, 2020, REV FINANC, V24, P733;Kang J-K, 2018, J FINANC ECON, V128, P576;Malenko A, 2019, J FINANC, V74, P2441;McCahery JA, 2016, J FINANC, V71, P2905;Morgan A, 2011, J CORP FINANC, V17, P914;Petersen MA, 2009, REV FINANC STUD, V22, P435;Schmidt C, 2017, J FINANC ECON, V124, P285;Seasholes MS, 2010, J FINANC, V65, P1987;Sialm C, 2020, REV FINANC STUD, V33, P4771;Song S, 2020, CORP GOV: INT REV, V28, P69;Thomas RS, 2007, J CORP FINANC, V13, P368;Varottil U, 2021, COMPARATIVE CORPORATE GOV, P346;Vincenty T, 1975, SURV REV, V23, P88                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|  3 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Ansari S, 2012, RES POLICY, V41, P1357;Berger AN, 2017, REV FINANC STUD, V30, P3416;Ding D, 2018, HANDBBLOCKCHAIN, DIGIT FINANC, P19;Drasch BJ, 2018, J ECON BUS, V100, P26;Goode A, 2018, BIOM TECHNOL TODAY, V2018, P5;Gopalan S, 2020, J ECON BUS, V107;Hasan I, 2009, J BANK FINANC, V33, P157;Hasan MM, 2020, SAGE OPEN, V10;Jagtiani J, 2018, J ECON BUS, V100, P43;Jiang D, 2020, ECON SYST, V44;Lee C-C/1, 2016, J INT MONEY FINANC, V62, P25;Lee I, 2018, BUS HORIZ, V61, P35;Leong C, 2017, INT J INF MANAGE, V37, P92;Levine R, 2005, HANDB ECON GROWTH, V1, P865;Li H, 2019, FINAN RES LETT, V30, P426;Makina D, 2019, EXTENDING FINANC INCLAFR, P299;Meijering E, 2002, PROC IEEE, V90, P319;Min Z, 2018, CHINA ECON J, V11, P25;Muganyi T, 2021, ENVIRON SCI ECOTECHNOL, V7;Pesaran MH, 2008, J ECONOM, V142, P50;Rajan RG, 2003, J FINANC ECON, V69, P5;Ryan RM, 2014, J BANK FINANC, V49, P495;Salampasis D, 2018, HANDBBLOCKCHAIN, DIGIT FINANC, V2, P451;Sun H-P, 2019, TRANSNATL CORP REV, V11, P346;Sun H-P, 2020, ENERGY, V208;Sun H-P, 2021, TECHNOL FORECAST SOC CHANGE, V167;Sun Y, 2020, FINAN RES LETT, V35;Yin W, 2019, J CLEAN PROD, V211, P247;Yiping H, 2014, CHINA ECON REV, V31, P426;Yuan H, 2019, J CLEAN PROD, V237;Zaefarian G, 2017, IND MARK MANAGE, V65, P39;Zhang C, 2015, J INT MONEY FINANC, V59, P287;Zhou W, 2018, HANDBBLOCKCHAIN, DIGIT FINANC, V2, P45                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|  4 | Almeida H, 2011, J FINANC ECON, V102, P526;Andrade G, 2001, J ECON PERSPECT, V15, P103;Baker AC, 2022, J FINANC ECON, V144, P370;Bakke T-E, 2010, REV FINANC STUD, V23, P1941;Bena J, 2014, J FINANC, V69, P1923;Bennett B, 2020, J FINANC ECON, V136, P281;Benveniste LM, 1989, J FINANC ECON, V24, P343;Bertrand M, 2003, J POLIT ECON, V111, P1043;Bird A, 2021, REV FINANC, V25, P745;Bonaime A, 2018, J FINANC ECON, V129, P531;Bond P, 2012, ANNU REV FINANC ECON, V4, P339;Chen Q, 2007, REV FINANC STUD, V20, P619;Chen T, 2015, J FINANC ECON, V115, P383;DIAMOND DW, 1985, J FINANC, V40, P1071;DIAMOND DW, 1991, J FINANC, V46, P1325;Dong M, 2006, J FINANC, V61, P725;Dow J, 1997, J FINANC, V52, P1087;Drake MS, 2015, CONTEMP ACCOUNT RES, V32, P1128;Duarte J, 2020, J FINANC ECON, V135, P795;Duchin R, 2013, J FINANC ECON, V107, P69;Edmans A, 2012, J FINANC, V67, P933;Edmans A, 2017, J FINANC ECON, V126, P74;Erel I, 2021, J FINANC QUANT ANAL, V56, P443;Ferris SP, 2013, J FINANC QUANT ANAL, V48, P137;Fuller K, 2002, J FINANC, V57, P1763;Gao M, 2020, REV FINANC STUD, V33, P1367;Garfinkel JA, 2011, J FINANC ECON, V101, P515;Goel AM, 2010, REV FINANC STUD, V23, P487;Goldstein I, 2015, J FINANC, V70, P1723;Goldstein I, 2019, REV FINANC STUD, V32, P1647;Gormley TA, 2011, REV FINANC STUD, V24, P2781;Gormley TA, 2016, J FINANC ECON, V122, P431;Harford J, 1999, J FINANC, V54, P1969;Harford J, 2005, J FINANC ECON, V77, P529;Hoberg G, 2010, REV FINANC STUD, V23, P3773;Huang Q, 2014, J FINANC ECON, V112, P269;Jayaraman S, 2019, REV FINANC STUD, V32, P2225;Jensen MC, 1983, J FINANC ECON, V11, P5;Jenter D, 2015, J FINANC, V70, P2813;Jiang F/2, 2019, J FINANC QUANT ANAL, V54, P2017;John K, 2015, J FINANC ECON, V118, P49;Lee CMC, 2001, J ACCOUNT ECON, V31, P233;Li FW, 2022, J ECON DYN CONTROL, V141;Luo Y, 2005, J FINANC, V60, P1951;Maksimovic V, 2001, J FINANC, V56, P2019;Masulis RW, 2007, J FINANC, V62, P1851;Mitchell M, 2004, J FINANC, V59, P31;Moeller SB, 2004, J FINANC ECON, V73, P201;Nguyen NH, 2017, J FINANC QUANT ANAL, V52, P613;Ni X, 2021, J CORP FINANC, V71;Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135;Panousi V, 2012, J FINANC, V67, P1113;Rock K, 1986, J FINANC ECON, V15, P187;Roosenboom P, 2014, REV FINANC STUD, V27, P2392;Samuels D, 2021, J ACCOUNT ECON, V71;Shleifer A, 2003, J FINANC ECON, V70, P295;Yim S, 2013, J FINANC ECON, V108, P250;Zhu C/1, 2019, REV FINANC STUD, V32, P2021                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|  5 | Acedo FJ, 2006, J MANAGE STUD, V43, P957;Aksoy M, 2021, J APPL ACCOUNT RES, V22, P706;Alam MZ, 2020, J INNOV ENTREPRENEURSHIP, V9;Alrabiah A, 2018, COGENT ECON FINANCE, V6, P1;Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Apostolou AK, 2009, INT J DISCL GOV, V6, P262;Appio FP, 2014, SCIENTOMETRICS, V101, P623;Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55;Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7;Baldwin AA, 2011, INT J DIGIT ACCOUNT RES, V11, P1;Barberis JN, 2016, NEW ECON WINDOWS, P69;Bartley J, 2011, ACCOUNT HORIZ, V25, P227;Baxter LG, 2016, DUKE LAW J, V66, P567;Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161;Blankespoor E, 2014, REV ACCOUNT STUD, V19, P1468;Bollen J, 2009, PLOS ONE, V4;Bonson E, 2010, J FINANC REGUL COMPLIANCE, V18, P144;Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801;Buckley RP, 2020, J BANK REGUL, V21, P26;Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19;Chao X, 2022, INT REV FINANC ANAL, V80;Chen S, 2021, REV QUANT FINANC ACCOUNT, V56, P479;Chen W/1, 2021, FRONT BUS RES CHINA, V15;Chiu IH-Y, 2021, ROUTLEDGE HANDBFINANCIAL TECH, P1;Choi D, 2021, INT J ACCOUNT INF SYST, V43;Crossan MM, 2010, J MANAGE STUD, V47, P1154;Currie WL, 2018, J INF TECHNOL, V33, P304;Das SR, 2019, J FINANCIAL DATA SCI, V1, P8;Dashottar S, 2021, J BANK REGUL, V22, P39;Donthu N, 2020, J BUS RES, V109, P1;Donthu N, 2021, J BUS RES, V133, P285;Du H, 2013, J INFO SYST, V27, P61;Dunne T, 2013, BR ACCOUNT REV, V45, P167;Elo S, 2008, J ADV NURS, V62, P107;Grassi L, 2022, QUAL RES ACCOUNT MANAGE, V19, P323;Gray GL, 2009, INT J DISCL GOV, V6, P207;Gurzki H, 2017, J BUS RES, V77, P147;Hao L, 2014, INT J ACCOUNT INF MANAGE, V22, P86;Huang JY, 2021, FINANCIAL INNOV, V7;Ilias A, 2019, INT J FINANCIAL RES, V10, P170;Iman N, 2020, COGENT BUS MANAG, V7;Kavassalis P, 2018, J RISK FINANC, V19, P39;Khan MA, 2021, J BUS RES, V125, P295;Kurum E, 2020, J FINANC CRIME;Laguna de Paz JC, 2022, J BANK REGUL;Lee J, 2020, EUR BUS ORG LAW REV, V21, P731;Liu C, 2014, DECIS SUPPORT SYST, V59, P242;Liu C, 2017, DECIS SUPPORT SYST, V93, P42;Meredith K, 2020, DECIS SUPPORT SYST, V139;Merigo JM, 2015, J BUS RES, V68, P2645;Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349;Mishchenko S, 2021, INVESTM MANANGE FINANC INNOV, V18, P191;Moshirian F, 2011, J BANK FINANC, V35, P502;Muganyi T, 2022, FINANCIAL INNOV, V8;Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382;Nath RD, 2021, FINANCIAL INNOV, V7;Nguyen QK, 2016, PROC - INT CONF GREEN TECHNOL, P51;Omarova ST, 2020, J FINANC REGUL, V6, P75;Oswari T, 2017, INT J ECON RES, V14, P219;Pinsker RE, 2016, J EMERG TECHNOL ACCOUNT, V13, P95;Pittaway L, 2004, INT J MANAGE REV, V5-6, P137;Sandelowski M, 1995, RES NURS HEALTH, V18, P371;Sheridan I, 2017, CAP MARK LAW J, V12, P417;Singh C, 2020, J MONEY LAUND CONTROL, V24, P464;Singh C, 2022, J FINANC CRIME, V29, P45;Soloviev VI, 2018, J REV GLOB ECON, V7, P377;Srivastava RP, 2010, INT J ACCOUNT INF SYST, V11, P261;Tranfield D, 2003, BR J MANAGE, V14, P207;Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544;Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256;Yang S/2, 2018, LECT NOTES INF SYS ORGAN, V24, P193;Zavolokina L, 2016, FINANCIAL INNOV, V2;Zeranski S, 2021, INT J DISCL GOV, V18, P315;Zupic I, 2015, ORG RES METHODS, V18, P429;von Solms J, 2021, J BANK REGUL, V22, P152                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  6 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Bastani K, 2019, EXPERT SYS APPL, V127, P256;Cheatham B, 2019, MCKINSEY Q, V2019;Clapham B, 2021, INF SYST FRONT, V23, P477;Clark GL, 1992, J CONSUM MARK, V9, P5;Currie WL, 2018, J INF TECHNOL, V33, P304;Dietterich TG, 1997, AI MAG, V18, P97;Ekelund RB, 1995, J ECON STUD, V22, P33;Fayyad U, 1996, AI MAG, V17, P37;Feuerriegel S, 2020, BUSIN INFO SYS ENG, V62, P379;Foohey P, 2017, LAW CONTEMP PROBL, V80, P177;Goodwin C, 1990, J CONSUM MARK, V7, P39;Gozman DP, 2014, J INF TECHNOL, V29, P44;Gregor S, 2013, MIS QUART MANAGE INF SYST, V37, P337;Groth SS, 2014, DECIS SUPPORT SYST, V62, P32;Hansen T, 2010, INT J RETAIL DISRTIB MANAGE, V38, P6;Hevner AR, 2004, MIS QUART MANAGE INF SYST, V28, P75;Hod S, 2022, COMMUN ACM, V65, P35;Kanapala A, 2019, ARTIF INTELL REV, V51, P371;Khedkar S, 2020, PROCEDIA COMPUT SCI, V167, P449;Kotsiantis SB, 2007, INF, V31, P249;Kuechler B, 2008, EUR J INF SYST, V17, P489;Lausen J, 2020, J ASSOC INF SYST, V21, P1153;McAlister DT, 2003, J BUS RES, V56, P341;Mudambi SM, 2010, MIS QUART MANAGE INF SYST, V34, P185;Murdoch WJ, 2019, PROC NATL ACAD SCI U S A, V116, P22071;Ngai EWT, 2011, DECIS SUPPORT SYST, V50, P559;Nyer PU, 2000, J CONSUM MARK, V17, P9;Otterbacher J, 2010, INT CONF INF KNOWLEDGE MANAGE, P369;Peffers K, 2007, J MANAGE INF SYST, V24, P45;Rai A, 2020, J ACAD MARK SCI, V48, P137;Siering M, 2017, J INF TECHNOL, V32, P251;Siering M, 2018, DECIS SUPPORT SYST, V108, P1;Siering M, 2019, INF SYST J, V29, P456;Siering M, 2021, J ASSOC INF SYST, V22, P156;Stone PJ, 1963, AFIPS CONF PROC - SPRING JT C, P241;Strauss J, 2001, J INTERACT MARK, V15, P63;Susskind AM, 2005, J HOSP TOUR RES, V29, P150;Valentini G, 2002, LECT NOTES COMPUT SCI, V2486 LNCS, P3;West J, 2016, COMPUT SECUR, V57, P47;Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  8 | Bellamy RKE, 2019, IBM J RES DEV, V63;Kingston KG, 2020, AFRICAN J INT COMP LAW, V28, P106;Lee Kuo Chuen D, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P1;Simser J, 2008, J MONEY LAUND CONTROL, V11, P15;Singh C, 2020, J MONEY LAUND CONTROL, V24, P464;Smith KT, 2010, J STRATEG MARK, V18, P201;Wilson HJ, 2017, MIT SLOAN MANAGE REV, V58, P14                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|  9 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Arner DW, 2019, EUR BUS ORG LAW REV, V20, P55;Becker M, 2019, J FINANC REGUL COMPLIANCE, V27, P464;Bellomarini L, 2020, CEUR WORKSHOP PROC, V3020, P43;Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801;Buckley RP, 2020, J BANK REGUL, V21, P26;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85;Chalkidis I, 2021, EACL - CONF EUR CHAPTER ASSOC, P3498;Clarke R, 2022, ELECTRON MARK, V32, P179;Du J, 2020, PROC - INT CONF ECON MANAG MO, P428;Fitrianah D, 2014, INT CONF DIGIT INF COMMUN TEC, P101;Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219;Gozman DP, 2020, MIS Q EXEC, V19, P19;Gozman DP, 2020, MIS Q EXEC, V19, P19;Haakman M, 2021, EMPIR SOFTWARE ENG, V26;Jagadeesh Chandra Bose RP, 2019, PROC - IEEE/ACM INT CONF SOFT, P284;Kurum E, 2020, J FINANC CRIME;Lee J, 2020, EUR BUS ORG LAW REV, V21, P731;Mayer M, 2019, THER INNOV REGUL SCI, V53, P759;Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349;Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349;Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382;Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135;Ostern NK, 2021, BUSIN INFO SYS ENG, V63, P551;Parra Moyano J, 2017, BUSIN INFO SYS ENG, V59, P411;Raso J, 2017, CAN J LAW SOC, V32, P75;Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787;Siering M, 2022, DECIS SUPPORT SYST, V158;Wei Y-C, 2022, CLUSTER COMPUT;Wymeersch E, 2007, EUR BUS ORG LAW REV, V8, P237;Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256;Zetzsche DA, 2020, J FINANC REGUL, V6, P172;von Solms J, 2021, J BANK REGUL, V22, P152                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 10 | Alaassar A, 2021, TECHNOVATION, V103;Alam S, 2021, COMPUT NETWORKS, V198;Allen JG, 2020, MOD LAW REV, V83, P505;Altman J, 2016, AUSTR J SOC ISS, V51, P487;Anagnostopoulos I, 2018, J ECON BUS, V100, P7;Anagnostopoulos I, 2021, INTELL SYST ACCOUNT FINANCE M, V28, P97;Antunes JAP, 2021, FINANCIAL INNOV, V7;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Barykin S, 2020, IOP CONF SER MATER SCI ENG, V918;Baxter LG, 2016, DUKE LAW J, V66, P567;Bellomarini L, 2020, CEUR WORKSHOP PROC, V3020, P43;Bholat D, 2021, OXF REV ECON POLICY, V37, P417;Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801;Brophy R, 2020, J FINANC REGUL COMPLIANCE, V28, P215;Buchanan BG, 2021, OXF REV ECON POLICY, V37, P537;Buckley RP, 2020, J BANK REGUL, V21, P26;Buckmann M, 2021, OXF REV ECON POLICY, V37, P479;Buttigieg CP, 2020, LAW FINANC MARK REV, V14, P5;Chakraborty G, 2020, J PUBLIC AFF, V20;Chen W, 2018, J CLEAN PROD, V201, P123;Chen W/1, 2021, FRONT BUS RES CHINA, V15;Chiu IH-Y, 2017, LAW INNOV TECHNOL, V9, P190;Clarke R, 2019, COMPUT LAW SECUR REV, V35, P398;Craja P, 2020, DECIS SUPPORT SYST, V139;Dahdal A, 2020, LAW FINANC MARK REV, V14, P223;De Chiara A, 2018, J FINANC STAB, V34, P86;De Filippi P, 2016, FIRST MONDAY, V21;Delimatsis P, 2021, J INT ECON LAW, V24, P277;Deshpande A, 2020, CMI CONF CYBERSECUR PRIV - DI;Ding X, 2021, INT REV ECON FINANC, V76, P502;Dresch A, 2015, DESIGN SCIENCE RESEARCH: A ME, P1;Du J, 2020, PROC - INT CONF ECON MANAG MO, P428;Eichengreen B, 2021, J BANK REGUL;ElYacoubi D, 2020, J MONEY LAUND CONTROL, V23, P527;Ellul J, 2021, PROC INT CONF ARTIF INTELL LA, P190;Faria I, 2019, J CULT ECON, V12, P119;Franks PC, 2020, REC MANAGE J, V30, P287;Gasparri G, 2019, FRONTIER ARTIF INTELL, V2;Giudici P, 2018, FRONTIER ARTIF INTELL, V1;Gomber P, 2018, J MANAGE INF SYST, V35, P220;Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219;Goyal N, 2021, REGUL GOVERNANCE, V15, P1020;Gozman DP, 2018, J MANAGE INF SYST, V35, P145;Gozman DP, 2020, MIS Q EXEC, V19, P19;Grout PA, 2021, OXF REV ECON POLICY, V37, P618;Haakman M, 2021, EMPIR SOFTWARE ENG, V26;Haddad C, 2019, SMALL BUS ECON, V53, P81;Imerman MB, 2020, J ASSET MANAGE, V21, P167;Ioannou S, 2019, REV POLIT ECON, V31, P356;Kapsis I, 2020, CAP MARK LAW J, V15, P18;Kapsis I, 2020, EUR BUS LAW REV, V31, P475;Kavassalis P, 2018, J RISK FINANC, V19, P39;Knewtson HS, 2020, MANAG FINANC, V46, P1043;Kondratyeva MN, 2021, IOP CONF SER MATER SCI ENG, V1047;Konigstorfer F, 2020, J BEHAV EXP FINANC, V27;Kowalski M, 2021, TECHNOL FORECAST SOC CHANGE, V166;Kraus NM, 2020, SCI INNO, V16, P92;Kurum E, 2020, J FINANC CRIME;Lee J, 2020, EUR BUS ORG LAW REV, V21, P731;Li C/1, 2020, ACM INT CONF PROC SER, P42;Lin M, 2021, ACM INT CONF PROC SER, P96;Liu R, 2020, INF MANAGE, V57;Lokanan M, 2019, J FINANC REGUL COMPLIANCE, V27, P324;Lui A, 2018, INF COMMUN TECHNOL LAW, V27, P267;Machkour B, 2020, PROCEDIA COMPUT SCI, V177, P496;Marszk A, 2018, TECHNOL FORECAST SOC CHANGE, V133, P51;Masciandaro D, 2020, J FINANC STAB, V46;Micheler E, 2020, EUR BUS ORG LAW REV, V21, P349;Milian EZ, 2019, ELECT COMMER RES APPL, V34;Minto A, 2017, CAP MARK LAW J, V12, P428;Miraz MH, 2019, PROC - INT CONF COMPUT, ELECT, P35;Moraes TKL, 2020, J INFOR TECHNOL TEACH CLASSES, V10, P108;Muhamad W, 2017, INT CONF INF TECHNOL SYST INN, V2018-January, P384;Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382;Ng AW, 2017, J FINANC REGUL COMPLIANCE, V25, P422;Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135;Omarova ST, 2020, J FINANC REGUL, V6, P75;Ozili PK, 2020, DIGIT POLI REGUL GOVERN, V22, P135;Palmie M, 2020, TECHNOL FORECAST SOC CHANGE, V151;Parra Moyano J, 2017, BUSIN INFO SYS ENG, V59, P411;Paul LR, 2021, PROC INT CONF INNOV PRACT TEC, P131;Peters GW, 2018, J OPER RISK, V13, P47;Peters R, 2019, PHARMACEUTICAL CAREDIGITAL RE, P195;Raso J, 2017, CAN J LAW SOC, V32, P75;Rowbottom N, 2021, ACCOUNT ORGAN SOC, V92;Russell SL, 2009, ACCOUNT FORUM, V33, P225;Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787;Ryzhik AV, 2020, J ADV RES LAW ECON, V11, P1032;Salami I, 2018, STUD CONFL TERRORISM, V41, P968;Sangwan V, 2020, STUD ECON FINANC, V37, P71;Savchuk N, 2021, INVESTM MANANGE FINANC INNOV, V18, P312;Sheridan I, 2017, CAP MARK LAW J, V12, P417;Soloviev VI, 2018, J REV GLOB ECON, V7, P377;Soloviev VI, 2018, PROC INT CONF "MANAG LARGE-SC;Troshani I, 2021, AUST ACCOUNT REV, V31, P213;Truby J, 2020, LAW FINANC MARK REV, V14, P110;Wall LD, 2018, J ECON BUS, V100, P55;Waye V, 2020, ADELAIDE LAW REV, V40, P363;Weng T-S, 2020, ACM INT CONF PROC SER, P58;Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544;Witt A, 2021, PROC INT CONF ARTIF INTELL LA, P139;Wojcik D, 2021, PROG HUM GEOGR, V45, P878;Xu Z, 2021, INT CONF INF KNOWLEDGE MANAGE, P4264;Yang D, 2018, EMERG MARK FINANC TRADE, V54, P3256;Yang X, 2020, PROC VLDB ENDOW, V13, P3138;Yao Q, 2018, SCI CHINA INF SCI, V61;Yeung K, 2019, MOD LAW REV, V82, P207;Yuryeva O, 2020, E3S WEB CONF, V210;Zeranski S, 2021, INT J DISCL GOV, V18, P315;Zetzsche DA, 2020, J FINANC REGUL, V6, P172;Zhang L, 2021, DICTA - INT CONF DIGIT IMAGE;Zhang Y/1, 2020, CHIN J COMP LAW, V8, P143;von Solms J, 2021, J BANK REGUL, V22, P152 |
| 11 | Ahdieh R, 2011, BOSTON UNIV LAW REV, V91, P43;Arner DW, 2017, NORTHWEST J INTL LAW BUS, V37, P373;Baker A, 2013, NEW POLIT ECON, V18, P112;Baker A, 2014, TRANSNATL FINANCIAL REGULATIO, P29;Baker A, 2018, REV INT POLIT ECON, V25, P293;Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85;Froud J, 2010, NEW POLIT ECON, V15, P147;Gabor D, 2021, DEV CHANGE, V52, P429;Germain R, 2014, REV INT POLIT ECON, V21, P1095;Gruin J, 2021, COMPET CHANGE, V25, P580;Haldane AG, 2011, NATURE, V469, P351;Jain S, 2020, NEW POLIT ECON, V25, P813;Jasanoff S, 2009, MINERVA, V47, P119;Koker L, 2009, J FINANC CRIME, V16, P334;Kranke M, 2019, NEW POLIT ECON, V24, P816;Langley P, 2021, NEW POLIT ECON, V26, P376;Lenglet M, 2021, TOPOI, V40, P811;Lockwood E, 2015, REV INT POLIT ECON, V22, P719;MacKenzie D, 2014, ECON SOC, V43, P153;MacKenzie D, 2021, REV INT POLIT ECON, V28, P1385;Macartney H, 2022, NEW POLIT ECON, V27, P257;Merz S, 2018, NEW POLIT ECON, V23, P560;Mirowski P, 2007, J ECON BEHAV ORGAN, V63, P209;Nesvetailova A, 2010, MILLENNIUM J INT STUD, V38, P797;Omarova ST, 2020, J FINANC REGUL, V6, P75;Ortiz H, 2021, ANTHROPOL THEOR, V21, P3;Piroska D, 2021, J COMMON MARK STUD, V59, P497;Riles A, 2004, AM ETHNOL, V31, P392;Sadowski J, 2019, BIG DATA SOC, V6;Samman A, 2014, MILLENNIUM J INT STUD, V42, P309;Schindler S, 2022, NEW POLIT ECON;Sinclair TJ, 2000, ENVIRON PLANN C GOV POLICY, V18, P487;Thompson G, 2011, J CULT ECON, V4, P405;Williams JW, 2013, ACCOUNT ORGAN SOC, V38, P544                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |




"""
import glob
import os
import pathlib
import re

import pandas as pd
from textblob import TextBlob

from ..refine.countries.apply_countries_thesaurus import apply_countries_thesaurus
from ..refine.organizations.apply_organizations_thesaurus import apply_organizations_thesaurus
from ..refine.words.apply_thesaurus import apply_thesaurus as apply_words_thesaurus

# from ..reports import abstracts_report
from .create_countries_thesaurus import create_countries_thesaurus
from .create_descriptors_thesaurus import create_descriptors_thesaurus
from .create_organizations_thesaurus import create_organizations_thesaurus
from .homogenize_global_references import homogenize_global_references
from .homogenize_local_references import homogenize_local_references

KEYWORDS_MAX_LENGTH = 50


def ingest_raw_data(
    #
    # DATABASE PARAMS:
    root_dir="./",
    remove_raw_csv_files=True,
    **document_types,
):
    """
    Import a Scopus data file in the working directory.

    Args:
        root_dir (str): The root directory to import the data to.
        disable_progress_bar (bool): Whether to disable the progress bar.
        **document_types: Keyword arguments specifying the document types to import.

    Returns:
        None
    :meta private:
    """

    #
    #
    # Phase 1: Preparing database files
    #
    #
    compress_raw_data(root_dir, remove_raw_csv_files)

    create_working_directories(root_dir)
    create_stopword_txt_file(root_dir)
    create_database_files(root_dir)
    rename_scopus_columns_in_database_files(root_dir)
    format_columns_names_in_database_files(root_dir)
    repair_authors_id_in_database_files(root_dir)
    repair_bad_separators_in_keywords(root_dir)

    discarded_types = [
        key.lower()
        for key, value in document_types.items()
        if isinstance(value, bool) and value is False
    ]

    remove_records(root_dir, "document_type", discarded_types)
    drop_empty_columns_in_database_files(root_dir)

    #
    # Additional Step:
    # Replace journal nanme by journal abbr in references.
    replace_journal_name_in_references(root_dir)

    #
    #
    # Phase 2: Process each column in isolation
    #
    #

    process_text_columns(
        root_dir,
        lambda x: x.str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8"),
        "remove accents",
    )

    process_text_columns(
        root_dir,
        lambda x: x.str.replace("\n", "")
        .str.replace("\r", "")
        .str.replace("&lpar;", "(")
        .str.replace("&rpar;", ")")
        .replace("&colon;", ":"),
        "remove stranger chars",
    )

    remove_records(
        root_dir,
        "raw_authors",
        ["Anon", "[No author name available]"],
    )

    process_column(
        root_dir,
        "authors_id",
        lambda x: x.str.replace(";$", "", regex=True).mask(x == "[No author id available]", pd.NA),
    )

    process_column(
        root_dir,
        "document_type",
        lambda x: x.str.lower().str.replace(" ", "_"),
    )

    process_column(
        root_dir,
        "eissn",
        lambda x: x.astype(str).str.replace("-", "", regex=True).str.upper(),
    )

    process_column(
        root_dir,
        "global_citations",
        lambda x: x.fillna(0).astype(int),
    )

    process_column(
        root_dir,
        "isbn",
        lambda x: x.astype(str).str.replace("-", "", regex=True).str.upper(),
    )

    process_column(
        root_dir,
        "issn",
        lambda x: x.astype(str).str.replace("-", "", regex=True).str.upper(),
    )

    process_column(
        root_dir,
        "raw_authors",
        lambda x: x.mask(x == "[No author name available]", pd.NA)
        .str.replace(",", ";", regex=False)
        .str.replace(".", "", regex=False),
    )

    process_column(
        root_dir,
        "source_name",
        lambda x: x.str.upper().str.replace(r"[^\w\s]", "", regex=True),
    )

    mask_column(
        root_dir,
        "source_abbr",
        "source_name",
    )

    process_column(
        root_dir,
        "source_abbr",
        lambda x: x.str.upper()
        .str.replace(".", "", regex=False)
        .str.replace(" JOURNAL ", " J ")
        .str.replace(" AND ", "")
        .str.replace(" IN ", "")
        .str.replace(" OF ", "")
        .str.replace(" ON ", "")
        .str.replace(" THE ", "")
        .str[:29],
    )

    process_column(
        root_dir,
        "doi",
        lambda x: x.str.replace("https://doi.org/", "", regex=False)
        .str.replace("http://dx.doi.org/", "", regex=False)
        .str.upper(),
    )

    disambiguate_author_names(root_dir)

    copy_to_column(root_dir, "authors", "num_authors")
    process_column(
        root_dir,
        "num_authors",
        lambda x: x.str.split(";").map(len, na_action="ignore").fillna(0).astype(int),
    )

    copy_to_column(root_dir, "global_references", "num_global_references")
    process_column(
        root_dir,
        "num_global_references",
        lambda x: x.str.split(";").str.len().fillna(0).astype(int),
    )

    create__article__column(root_dir)

    #
    #
    # Phase 3: Keywords & noun phrases & abstracts
    #
    #
    # In the context of topic modeling for research abstracts, it is generally
    # more common and beneficial to use "noun phrases" extracted using text
    # mining techniques rather than relying solely on provided "keywords" for
    # the given document.
    #
    # Research abstracts often contain technical and domain-specific
    # language, making it challenging to accurately capture the main topics
    # and themes using only manually assigned or provided keywords. On the
    # other hand, using text mining techniques to extract noun phrases can
    # help uncover more nuanced and contextually relevant phrases that better
    # represent the content of the abstracts.
    #
    # Text mining techniques, such as part-of-speech tagging, noun phrase
    # chunking, or natural language processing algorithms, can identify
    # meaningful noun phrases that may not be explicitly listed as keywords.
    # These extracted noun phrases can provide a more comprehensive
    # representation of the topics present in the research abstracts,
    # allowing for more accurate and informative topic modeling.
    #
    # Therefore, leveraging text mining techniques to extract noun phrases is
    # often preferred over relying solely on provided keywords when
    # conducting topic modeling on research abstracts.
    #

    #
    #
    # Prepare author/index keywords:
    # To upper() and replace spaces with underscores
    # Merge author/index keywords into a single column
    #
    process_column(
        root_dir,
        "raw_author_keywords",
        lambda x: x.str.upper()
        .str.split(";")
        .map(
            lambda w: "; ".join(
                sorted(
                    z.strip()
                    .replace("&", "AND")
                    .replace("   ", "  ")
                    .replace("  ", " ")
                    .replace(" ", "_")
                    .replace("/", "_")
                    .replace("\\", "_")
                    .replace(".", "_")
                    .replace(",", "_")
                    .replace("'", "_")
                    .replace("-", "_")
                    .replace("__", "_")
                    .replace("_(", " (")
                    for z in w
                )
            ),
            na_action="ignore",
        ),
    )
    process_column(
        root_dir,
        "raw_index_keywords",
        lambda x: x.str.upper()
        .str.split(";")
        .map(
            lambda w: "; ".join(
                sorted(
                    z.strip()
                    .replace("&", "AND")
                    .replace("   ", "  ")
                    .replace("  ", " ")
                    .replace(" ", "_")
                    .replace("/", "_")
                    .replace("\\", "_")
                    .replace(".", "_")
                    .replace(",", "_")
                    .replace("'", "_")
                    .replace("-", "_")
                    .replace("__", "_")
                    .replace("_(", " (")
                    for z in w
                )
            ),
            na_action="ignore",
        ),
    )
    concatenate_columns(
        root_dir,
        "raw_keywords",
        "raw_author_keywords",
        "raw_index_keywords",
    )

    #
    # Prepare title:
    # To lower() & remove brackets & remove multiple spaces & strip
    #
    process_column(
        root_dir,
        "title",
        lambda x: x.str.replace(r"\[.*", "", regex=True)
        .str.replace("   ", "  ")
        .str.replace("  ", " ")
        .str.strip()
        .str.lower(),
    )

    #
    # Technological Emergence Indicators using Emergence Score
    # Garner et al. 2017.
    # ------------------------------------------------------------------------
    #
    # Suitable terms for determining emergence are presented both in title and
    # the abstract. This allows to augment the list of terms given by the
    # authors/index keywords
    #

    #
    # Step 1: Create a candidate list of title nlp phrases
    #
    copy_to_column(root_dir, "title", "raw_title_nlp_phrases")
    process_column(
        root_dir,
        "raw_title_nlp_phrases",
        lambda x: x.astype(str)
        .map(lambda z: TextBlob(z).noun_phrases)
        .map(set, na_action="ignore")
        .map(sorted, na_action="ignore")
        .map(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .str.upper()
        .replace("   ", "  ")
        .replace("  ", " ")
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("\\", "_")
        .str.replace(".", "_")
        .str.replace(",", "_")
        .str.replace("'", "_")
        .str.replace("-", "_")
        .str.replace("__", "_")
        .str.replace(";_", "; ")
        .map(lambda x: pd.NA if x == "" else x),
    )

    #
    # Step 2: Create a candidate list of abstract nlp phrases
    #
    process_column(
        root_dir,
        "abstract",
        lambda x: x.mask(x == "[no abstract available]", pd.NA).str.lower(),
    )

    copy_to_column(root_dir, "abstract", "raw_abstract_nlp_phrases")
    process_column(
        root_dir,
        "raw_abstract_nlp_phrases",
        lambda x: x.astype(str)
        .map(lambda z: TextBlob(z).noun_phrases)
        .map(sorted, na_action="ignore")
        .map(set, na_action="ignore")
        .map(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .str.upper()
        .replace("   ", "  ")
        .replace("  ", " ")
        .str.replace(" ", "_")
        .str.replace("/", "_")
        .str.replace("\\", "_")
        .str.replace(".", "_")
        .str.replace(",", "_")
        .str.replace("'", "_")
        .str.replace("-", "_")
        .str.replace("__", "_")
        .str.replace(";_", "; ")
        .map(lambda x: pd.NA if x == "" else x),
    )

    #
    # Step 3: Filter terms in title and abstract nlp phrases
    #
    filter_nlp_phrases(root_dir)

    #
    # Continue normal processing ....
    #
    concatenate_columns(
        root_dir,
        "raw_nlp_phrases",
        "raw_title_nlp_phrases",
        "raw_abstract_nlp_phrases",
    )

    process_column(
        root_dir,
        "raw_nlp_phrases",
        lambda x: x.astype(str)
        .str.split("; ")
        .apply(lambda x: sorted(set(x)))
        .apply(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .apply(lambda x: pd.NA if x == "" else x),
    )

    concatenate_columns(
        root_dir,
        "raw_descriptors",
        "raw_nlp_phrases",
        "raw_keywords",
    )

    process_column(
        root_dir,
        "raw_descriptors",
        lambda x: x.astype(str)
        .str.split("; ")
        .apply(lambda x: sorted(set(x)))
        .apply(lambda x: [z for z in x if z != "nan"])
        .str.join("; ")
        .apply(lambda x: pd.NA if x == "" else x),
    )

    transform_abstract_keywords_to_underscore(root_dir)

    #
    #
    # Phase 4: References
    #
    #
    # create_references(root_dir, disable_progress_bar)
    homogenize_local_references(root_dir)
    homogenize_global_references(root_dir)

    #
    create__local_citations__column_in_references_database(root_dir)
    create__local_citations__column_in_documents_database(root_dir)

    #
    #
    # Phase 5: Thesaurus files
    #
    #
    create_countries_thesaurus(root_dir)
    create_descriptors_thesaurus(root_dir)
    create_organizations_thesaurus(root_dir)

    apply_countries_thesaurus(root_dir)
    apply_words_thesaurus(root_dir)
    apply_organizations_thesaurus(root_dir)

    print("--INFO-- Process finished!!!")

    ## abstracts_report(root_dir=root_dir, file_name="imported_records.txt")
    report_imported_records_per_file(root_dir)


#
#
# End of main function
#
#
def compress_raw_data(root_dir, remove_raw_csv_files):
    """
    :meta private:
    """

    raw_dir = os.path.join(root_dir, "raw-data")

    folders = get_subdirectories(raw_dir)
    for folder in folders:
        csv_files = os.listdir(os.path.join(raw_dir, folder))
        csv_files = [f for f in csv_files if f.endswith(".csv")]
        for csv_file in csv_files:
            csv_file_path = os.path.join(raw_dir, folder, csv_file)
            zip_file_path = os.path.join(raw_dir, folder, csv_file[:-4] + ".zip")
            df = pd.read_csv(csv_file_path, encoding="utf-8")
            df.to_csv(zip_file_path, encoding="utf-8", index=False, compression="zip")
            if remove_raw_csv_files:
                os.remove(csv_file_path)


def replace_journal_name_in_references(root_dir):
    abbrs = []

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data = data[["source", "source_abbr"]]
        data = data.dropna()
        data = data.drop_duplicates()

        abbrs.append(data)
    abbrs = pd.concat(abbrs, ignore_index=True)

    main_path = pathlib.Path(root_dir) / "databases/_main.zip"
    main = pd.read_csv(main_path, encoding="utf-8", compression="zip")

    for source, source_abbr in zip(abbrs.source, abbrs.source_abbr):
        main["raw_global_references"] = main["raw_global_references"].str.replace(
            source, source_abbr, regex=False
        )
    main.to_csv(main_path, sep=",", encoding="utf-8", index=False, compression="zip")


def create_working_directories(root_dir):
    """
    Create the working directories for the Scopus data.

    Args:
        root_dir (str): The root directory to create the directories in.

    Returns:
        None

    :meta private:
    """
    for directory in ["databases", "reports"]:
        directory_path = os.path.join(root_dir, directory)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)


def create_stopword_txt_file(root_dir):
    """
    Create an empty stopwords.txt file if it doesn't exist.

    Args:
        root_dir (str): The root directory containing the processed directory.

    Returns:
        None

    :meta private:
    """
    file_path = os.path.join(root_dir, "stopwords.txt")

    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8"):
            pass


def create_database_files(root_dir):
    """
    Create processed CSV files from raw CSV files.

    Args:
        root_dir (str): The root directory containing the raw and processed directories.

    Returns:
        None

    :meta private:
    """
    raw_dir = os.path.join(root_dir, "raw-data")
    processed_dir = os.path.join(root_dir, "databases")

    folders = get_subdirectories(raw_dir)
    for folder in folders:
        data = concat_raw_zip_files(os.path.join(raw_dir, folder))
        file_name = f"_{folder}.zip"
        file_path = os.path.join(processed_dir, file_name)
        data.to_csv(file_path, sep=",", encoding="utf-8", index=False, compression="zip")

    file_path = os.path.join(root_dir, "databases/_DO_NOT_TOUCH_.txt")
    with open(file_path, "w", encoding="utf-8"):
        pass


def get_subdirectories(directory):
    """
    Get a list of subdirectories in a directory.

    Args:
        directory (str): The directory to get the subdirectories from.

    Returns:
        A list of subdirectories.

    :meta private:
    """
    subdirectories = os.listdir(directory)
    subdirectories = [f for f in subdirectories if os.path.isdir(os.path.join(directory, f))]
    return subdirectories


def concat_raw_zip_files(path, quiet=False):
    """
    Concatenate raw ZIP files in a directory.

    Args:
        path (str): The path to the directory containing the raw CSV files.
        quiet (bool): Whether to suppress output.

    Returns:
        A pandas DataFrame containing the concatenated data.

    :meta private:
    """
    if not quiet:
        print(f"--INFO-- Concatenating raw files in {path}/")

    files = get_zip_files(path)
    if not files:
        raise FileNotFoundError(f"No ZIP files found in {path}")

    data = []
    for file_name in files:
        file_path = os.path.join(path, file_name)
        data.append(pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip"))

    data = pd.concat(data, ignore_index=True)
    data = data.drop_duplicates()

    return data


def get_zip_files(directory):
    """
    Get a list of ZIP files in a directory.

    Args:
        directory (str): The directory to get the CSV files from.

    Returns:
        A list of ZIP files.

    :meta private:
    """
    csv_files = os.listdir(directory)
    csv_files = [f for f in csv_files if f.endswith(".zip")]
    return csv_files


def rename_scopus_columns_in_database_files(root_dir):
    """Rename Scopus columns in the processed CSV files.

    The name equivalences are stored in a repository file.




    :meta private:
    """
    print("--INFO-- Applying scopus tags to database files")

    owner = "jdvelasq"
    repo = "techminer2"
    path = "settings/scopus2tags.csv"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{path}"

    tags = pd.read_csv(url, encoding="utf-8")
    tags["scopus"] = tags["scopus"].str.strip()
    tags["techminer"] = tags["techminer"].str.strip()
    scopus2tags = dict(zip(tags["scopus"], tags["techminer"]))

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data.rename(columns=scopus2tags, inplace=True)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def filter_nlp_phrases(root_dir):
    """Filter nlp phrases in abstract and title

    :meta private:
    """

    def get_nlp_phrases(column):
        databases_dir = pathlib.Path(root_dir) / "databases"
        files = list(databases_dir.glob("_*.zip"))
        nlp_phrases = set()
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            if column not in data.columns:
                continue
            file_nlp_phrases = data[column].dropna()
            file_nlp_phrases = (
                file_nlp_phrases.dropna()
                .str.split(";")
                .explode()
                .str.strip()
                .drop_duplicates()
                .to_list()
            )
            nlp_phrases.update(file_nlp_phrases)
        return nlp_phrases

    def apply_filter_to_nlp_phrases(column, selected_nlp_phrases):
        """Apply filter to nlp phrases to the specicied column"""

        databases_dir = pathlib.Path(root_dir) / "databases"
        files = list(databases_dir.glob("_*.zip"))

        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            if column not in data.columns:
                continue
            data[column] = (
                data[column]
                .astype(str)
                .str.split("; ")
                .map(lambda x: [w.strip() for w in x])
                .map(lambda x: [w for w in x if w in selected_nlp_phrases])
                .map(lambda x: [w for w in x if w != "nan"])
                .map(lambda x: "; ".join(sorted(x)))
                .map(lambda x: pd.NA if x == "" else x)
            )
            data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    #
    # Main code:
    #

    # Obtain the raw nlp phrases
    raw_keywords = get_nlp_phrases("raw_keywords")
    raw_title_nlp_phrases = get_nlp_phrases("raw_title_nlp_phrases")
    raw_abstract_nlp_phrases = get_nlp_phrases("raw_abstract_nlp_phrases")

    # nlp phrases appearing in the title and abstract
    selected_nlp_phrases = raw_title_nlp_phrases & raw_abstract_nlp_phrases

    # adds raw keywords
    selected_nlp_phrases.update(raw_keywords)

    apply_filter_to_nlp_phrases(
        "raw_title_nlp_phrases",
        selected_nlp_phrases,
    )

    apply_filter_to_nlp_phrases(
        "raw_abstract_nlp_phrases",
        selected_nlp_phrases,
    )


def format_columns_names_in_database_files(root_dir: str) -> None:
    """
    Format column names in database files.

    Args:
        root_dir: The root directory containing the processed CSV files.

    Returns:
        None

    :meta private:
    """
    print("--INFO-- Formatting column names in database files")

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data = format_column_names(data)
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def format_column_names(data: pd.DataFrame) -> pd.DataFrame:
    """
    Format column names in a pandas DataFrame.

    Args:
        data: The pandas DataFrame to format.

    Returns:
        The pandas DataFrame with formatted column names.

    :meta private:
    """
    return data.rename(
        columns={col: col.replace(".", "").replace(" ", "_").lower() for col in data.columns}
    )


def repair_authors_id_in_database_files(root_dir: str) -> None:
    """
    Repair authors IDs in the processed CSV files.

    Args:
        root_dir: The root directory containing the processed CSV files.

    Returns:
        None

    :meta private:
    """
    print("--INFO-- Repairing authors ID")

    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    max_length = get_max_authors_id_length(files)
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        data["authors_id"] = repair_authors_id(data["raw_authors_id"], max_length)
        data.to_csv(file, index=False, encoding="utf-8", compression="zip")


def get_max_authors_id_length(files: list) -> int:
    """
    Get the maximum length of authors IDs in a list of ZIP files.

    Args:
        files: A list of ZIP files.

    Returns:
        The maximum length of authors IDs.

    :meta private:
    """
    lengths = []
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        ids = data["raw_authors_id"].copy()
        ids = ids.str.rstrip(";")
        ids = ids.str.split(";")
        ids = ids.explode()
        ids = ids.drop_duplicates()
        ids = ids.str.strip()
        ids = ids.str.len()
        lengths.append(ids.max())
    return max(lengths)


def repair_authors_id(authors_id: pd.Series, max_length: int) -> pd.Series:
    """
    Repair authors IDs in a pandas Series.

    Args:
        authors_id: The pandas Series containing authors IDs.
        max_length: The maximum length of authors IDs.

    Returns:
        The pandas Series with repaired authors IDs.

    :meta private:
    """

    max_length = int(max_length)

    return (
        authors_id.str.rstrip(";")
        .str.split(";")
        .map(lambda x: [i.strip() for i in x] if x is not pd.NA else x, na_action="ignore")
        .map(
            lambda x: [i.rjust(max_length, "0") for i in x] if x is not pd.NA else x,
            na_action="ignore",
        )
        .str.join(";")
    )


def repair_bad_separators_in_keywords(root_dir):
    """Repair keywords with bad separators in the processed CSV files.

    In Scopus, keywords are separated by semicolons. However, some records
    contain keywords separated by commas. This function repairs these
    keywords.

    Args:
        root_dir: The root directory containing the processed CSV files.

    Returns:
        None

    :meta private:
    """
    print("--INFO-- Repairing bad separators in keywords")
    processed_dir = pathlib.Path(root_dir) / "databases"
    files = list(processed_dir.glob("_*.zip"))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        for column in ["raw_index_keywords", "raw_authors_keywords"]:
            if column in data.columns:
                data[column] = repair_keywords_in_column(data[column])
        data.to_csv(file, index=False, encoding="utf-8", compression="zip")


def repair_keywords_in_column(raw_keywords: pd.Series) -> pd.Series:
    """Repair keywords in a pandas Series.


    :meta private:
    """
    keywords = raw_keywords.copy()
    keywords = keywords.dropna()
    keywords = keywords.str.split("; ").explode().str.strip().drop_duplicates()
    keywords = keywords[keywords.str.len() > KEYWORDS_MAX_LENGTH]
    if len(keywords) > 0:
        for keyword in keywords:
            print(f"--WARNING-- Keyword with bad separator: {keyword}")
            raw_keywords = raw_keywords.str.replace(keyword, keyword.replace(",", ";"))
    return raw_keywords


def remove_records(root_dir, col_name, values_to_remove):
    """Remove records with a given value in a given column.

    Args:
        root_dir (str): root directory.
        col_name (str): column name.
        values_to_remove (list): values to remove.

    :meta private:
    """
    if len(values_to_remove) == 0:
        return
    print(f"--INFO-- Removing records with `{col_name}` in {values_to_remove}")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        org_length = len(data)
        data = data[~data[col_name].isin(values_to_remove)]
        new_length = len(data)
        if org_length != new_length:
            print(f"--INFO-- Removed {org_length - new_length} records")
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def drop_empty_columns_in_database_files(root_dir):
    """Drop NA columns in database files.

    :meta private:
    """

    print("--INFO-- Dropping NA columns in database files")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        original_cols = data.columns.copy()
        data = data.dropna(axis=1, how="all")
        if len(data.columns) != len(original_cols):
            removed_cols = set(original_cols) - set(data.columns)
            print(f"--INFO-- Removed columns: {removed_cols}")
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def process_text_columns(root_dir, process_func, msg):
    """Process text columns in all database files.

    Args:
        root_dir (str): root directory.
        process_func (function): function to be applied to each column.

    :meta private:
    """
    print(f"--INFO-- Processing text columns ({msg})")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        cols = data.select_dtypes(include=["object"]).columns
        for col in cols:
            data[col] = process_func(data[col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def process_column(root_dir, column_name, process_func):
    """Process a column in all database files.

    Args:
        root_dir (str): root directory.
        column_name (str): column name.
        process_func (function): function to be applied to the column.

    Returns:
        None

    :meta private:
    """
    print(f"--INFO-- Processing `{column_name}` column")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if column_name in data.columns:
            data[column_name] = process_func(data[column_name])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def mask_column(root_dir, masked_col, rep_col):
    """Mask a column in all database files.

    :meta private:
    """
    print(f"--INFO-- Mask `{masked_col}` column with `{rep_col}`")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if masked_col in data.columns and rep_col in data.columns:
            data[masked_col].mask(data[masked_col].isnull(), data[rep_col])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def disambiguate_author_names(root_dir):
    """Create the authors column.

    :meta private:
    """

    #
    def load_authors_names():
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        data = [
            pd.read_csv(file, encoding="utf-8", compression="zip")[["raw_authors", "authors_id"]]
            for file in files
        ]
        data = pd.concat(data)
        data = data.dropna()
        return data

    #
    def build_dict_names(data):
        data = data.copy()

        data = data.assign(authors_and_ids=data.raw_authors + "#" + data.authors_id)
        data.authors_and_ids = data.authors_and_ids.str.split("#")
        data.authors_and_ids = data.authors_and_ids.apply(
            lambda x: (x[0].split(";"), x[1].split(";"))
        )
        data.authors_and_ids = data.authors_and_ids.apply(lambda x: list(zip(x[0], x[1])))
        data = data.explode("authors_and_ids")
        data.authors_and_ids = data.authors_and_ids.apply(lambda x: (x[0].strip(), x[1].strip()))
        data = data.reset_index(drop=True)
        data = data[["authors_and_ids"]]
        data["author"] = data.authors_and_ids.apply(lambda x: x[0])
        data["author_id"] = data.authors_and_ids.apply(lambda x: x[1])
        data = data.drop(columns=["authors_and_ids"])
        data = data.drop_duplicates()
        data = data.sort_values(by=["author"])
        data = data.assign(counter=data.groupby(["author"]).cumcount())
        data = data.assign(author=data.author + "/" + data.counter.astype(str))
        data.author = data.author.str.replace("/0", "")
        author_id2name = dict(zip(data.author_id, data.author))
        return author_id2name

    def repair_names(author_id2name):
        files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
        # total_items = len(files)
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            data = data.assign(authors=data.authors_id.copy())
            data["authors"] = data["authors"].str.split(";")
            data["authors"] = data["authors"].map(
                lambda x: [author_id2name[id] for id in x], na_action="ignore"
            )
            data["authors"] = data["authors"].str.join("; ")
            data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

    #
    print("--INFO-- Disambiguating `authors` column")
    data = load_authors_names()
    author_id2name = build_dict_names(data)
    repair_names(author_id2name)


def copy_to_column(root_dir, src, dest):
    """Copy a column in all database files.

    :meta private:
    """
    print(f"--INFO-- Copying `{src}` column to `{dest}`")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if src in data.columns:
            data[dest] = data[src]
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def concatenate_columns(root_dir, dest, column_name1, column_name2):
    """Concatenate two columns in all database files.

    :meta private:
    """
    print(f"--INFO-- Concatenating `{column_name1}` and `{column_name2}` columns to `{dest}`")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        if column_name1 in data.columns and column_name2 in data.columns:
            src = data[column_name1].astype(str).str.split("; ")
            dst = data[column_name2].astype(str).str.split("; ")
            con = src + dst
            con = con.map(lambda x: [z for z in x if z != "nan"])
            con = con.map(lambda x: sorted(set(x)), na_action="ignore")
            con = con.map(lambda x: "; ".join(x), na_action="ignore")
            con = con.map(lambda x: x if x != "" else pd.NA)
            data[dest] = con

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


def create__article__column(root_dir):
    """Create a WoS style reference column.

    :meta private:
    """
    #
    # First Author, year, source_abbr, 'V'volumne, 'P'page_start, ' DOI ' doi
    #
    print("--INFO-- Creating `article` column")

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        #
        wos_ref = data.authors.map(
            lambda x: x.split("; ")[0].strip() if not pd.isna(x) else "[Anonymous]"
        )
        wos_ref += ", " + data.year.map(str)
        wos_ref += ", " + data.source_abbr
        wos_ref += data.volume.map(
            lambda x: ", V" + str(x).replace(".0", "") if not pd.isna(x) else ""
        )
        wos_ref += data.page_start.map(
            lambda x: ", P" + str(x).replace(".0", "") if not pd.isna(x) else ""
        )
        # wos_ref += data.doi.map(lambda x: ", DOI " + str(x) if not pd.isna(x) else "")
        data["article"] = wos_ref.copy()
        data = data.drop_duplicates(subset=["article"])
        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")


# def create_references(directory, disable_progress_bar=False):
#     """Create references from `documents.csv` or `_references.csv` file.

#     :meta private:
#     """
#     create_references_from_documents_csv_file(directory, disable_progress_bar)

#     #
#     # Formats only references in the documents.csv file. Creates a thesurus
#     # for homogenizing the references.

#     # references_path = os.path.join(directory, "databases/_references.csv")
#     # if os.path.exists(references_path):
#     #     create_references_from_references_csv_file(directory, disable_progress_bar)
#     # else:
#     #     create_references_from_documents_csv_file(directory, disable_progress_bar)


# def create_references_from_documents_csv_file(directory, disable_progress_bar=False):
#     """Create references from `documents.csv` file.

#     :meta private:
#     """

#     print("--INFO-- Creating references from  `_main.csv` file.")

#     documents_path = os.path.join(directory, "databases/_main.csv")
#     documents = pd.read_csv(documents_path)

#     # references como aparecen en los articulos
#     raw_cited_references = documents.raw_global_references.copy()
#     raw_cited_references = raw_cited_references.str.lower()
#     raw_cited_references = raw_cited_references.str.split(";")
#     raw_cited_references = raw_cited_references.explode()
#     raw_cited_references = raw_cited_references.str.strip()
#     raw_cited_references = raw_cited_references.dropna()
#     raw_cited_references = raw_cited_references.drop_duplicates()
#     raw_cited_references = raw_cited_references.reset_index(drop=True)

#     # record in document.csv ---> reference
#     searching_thesaurus = {t: None for t in raw_cited_references.tolist()}
#     found_thesaurus = {}

#     # marcador para indicar si la referencia fue encontrada
#     references = documents.copy()
#     references["found"] = False

#     # busqueda por doi
#     print("--INFO-- Searching `references` using DOI")
#     i_counter = 0
#     with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
#         for doi, article in zip(references.doi, references.article):
#             for key in searching_thesaurus.keys():
#                 if searching_thesaurus[key] is None:
#                     if not pd.isna(doi) and doi in key:
#                         searching_thesaurus[key] = article
#                         found_thesaurus[key] = article
#                         references.loc[references.doi == doi, "found"] = True

#             i_counter += 1
#             if i_counter >= 100:
#                 searching_thesaurus = {k: v for k, v in searching_thesaurus.items() if v is None}
#                 i_counter = 0
#             pbar.update(1)

#     # Reduce la base de búsqueda
#     references = references[~references.found]

#     # Busqueda por (año, autor y tttulo)
#     i_counter = 0
#     print("--INFO-- Searching `references` using (year, title, author)")
#     with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
#         for article, year, authors, title in zip(
#             references.article,
#             references.year,
#             references.authors,
#             references.title,
#         ):
#             year = str(year)
#             author = authors.split()[0].lower()
#             title = (
#                 title.lower()
#                 .replace(".", "")
#                 .replace(",", "")
#                 .replace(":", "")
#                 .replace(";", "")
#                 .replace("-", " ")
#                 .replace("'", "")
#             )

#             for key in searching_thesaurus.keys():
#                 if searching_thesaurus[key] is None:
#                     text = key
#                     text = (
#                         text.lower()
#                         .replace(".", "")
#                         .replace(",", "")
#                         .replace(":", "")
#                         .replace(";", "")
#                         .replace("-", " ")
#                         .replace("'", "")
#                     )

#                     if author in text and str(year) in text and title[:29] in text:
#                         searching_thesaurus[key] = article
#                         references.loc[references.article == article, "found"] = True
#                         found_thesaurus[key] = article

#                     elif author in text and str(year) in text and title[-29:] in text:
#                         searching_thesaurus[key] = article
#                         references.loc[references.article == article, "found"] = True
#                         found_thesaurus[key] = article

#             i_counter += 1
#             if i_counter >= 100:
#                 searching_thesaurus = {k: v for k, v in searching_thesaurus.items() if v is None}
#                 i_counter = 0
#             pbar.update(1)

#     # Reduce la base de búsqueda
#     references = references[~references.found]

#     # Busqueda por titulo
#     print("--INFO-- Searching `references` using (title)")
#     i_counter = 0
#     with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
#         for article, title in zip(
#             references.article,
#             references.title,
#         ):
#             title = (
#                 title.lower()
#                 .replace(".", "")
#                 .replace(",", "")
#                 .replace(":", "")
#                 .replace(";", "")
#                 .replace("-", " ")
#                 .replace("'", "")
#             )

#             for key in searching_thesaurus.keys():
#                 text = key
#                 text = (
#                     text.lower()
#                     .replace(".", "")
#                     .replace(",", "")
#                     .replace(":", "")
#                     .replace(";", "")
#                     .replace("-", " ")
#                     .replace("'", "")
#                 )

#                 if title in text:
#                     searching_thesaurus[key] = article
#                     found_thesaurus[key] = article
#                     references.loc[references.article == article, "found"] = True

#             i_counter += 1
#             if i_counter >= 100:
#                 searching_thesaurus = {k: v for k, v in searching_thesaurus.items() if v is None}
#                 i_counter = 0
#             pbar.update(1)
#     #
#     # Crea la columna de referencias locales
#     #
#     documents["local_references"] = documents.raw_global_references.copy()
#     documents["local_references"] = documents["local_references"].str.lower()
#     documents["local_references"] = documents["local_references"].str.split(";")
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [t.strip() for t in x] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [found_thesaurus.get(t, "") for t in x] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [t for t in x if t is not None] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].str.join("; ")
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: pd.NA if x == "" else x
#     )
#     #
#     documents.to_csv(documents_path, index=False)


# def create_references_from_references_csv_file(directory, disable_progress_bar=False):
#     """Create the references from the references.csv file.

#     :meta private:
#     """

#     references_path = os.path.join(directory, "databases/_references.csv")

#     if not os.path.exists(references_path):
#         print(f"--WARN-- The  file {references_path} does not exists.")
#         print("--WARN-- Some functionalities are disabled.")
#         return

#     references = pd.read_csv(references_path)

#     documents_path = os.path.join(directory, "databases/_main.csv")
#     documents = pd.read_csv(documents_path)

#     # references como aparecen en los articulos
#     raw_cited_references = documents.global_references.copy()
#     raw_cited_references = raw_cited_references.str.lower()
#     raw_cited_references = raw_cited_references.str.split(";")
#     raw_cited_references = raw_cited_references.explode()
#     raw_cited_references = raw_cited_references.str.strip()
#     raw_cited_references = raw_cited_references.dropna()
#     raw_cited_references = raw_cited_references.drop_duplicates()
#     raw_cited_references = raw_cited_references.reset_index(drop=True)

#     # raw_cited_reference --> article
#     thesaurus = {t: None for t in raw_cited_references.tolist()}

#     # marcador para indicar si la referencia fue encontrada
#     references["found"] = False

#     # busqueda por doi
#     print("--INFO-- Searching `references` using DOI")
#     with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
#         for doi, article in zip(references.doi, references.article):
#             for key in thesaurus.keys():
#                 if thesaurus[key] is None:
#                     if not pd.isna(doi) and doi in key:
#                         thesaurus[key] = article
#                         references.loc[references.doi == doi, "found"] = True
#             pbar.update(1)

#     # Reduce la base de búsqueda
#     references = references[~references.found]

#     # Busqueda por (año, autor y tttulo)
#     print("--INFO-- Searching `references` using (year, title, author)")
#     with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
#         for article, year, authors, title in zip(
#             references.article,
#             references.year,
#             references.authors,
#             references.title,
#         ):
#             if pd.isna(authors) or pd.isna(year) or pd.isna(title) or pd.isna(article):
#                 continue

#             year = str(year)
#             author = authors.split()[0].lower()
#             title = (
#                 title.lower()
#                 .replace(".", "")
#                 .replace(",", "")
#                 .replace(":", "")
#                 .replace(";", "")
#                 .replace("-", " ")
#                 .replace("'", "")
#             )

#             for key in thesaurus.keys():
#                 if thesaurus[key] is None:
#                     text = key
#                     text = (
#                         text.lower()
#                         .replace(".", "")
#                         .replace(",", "")
#                         .replace(":", "")
#                         .replace(";", "")
#                         .replace("-", " ")
#                         .replace("'", "")
#                     )

#                     if author in text and str(year) in text and title[:29] in text:
#                         thesaurus[key] = article
#                         references.loc[references.article == article, "found"] = True
#                     elif author in text and str(year) in text and title[-29:] in text:
#                         thesaurus[key] = article
#                         references.loc[references.article == article, "found"] = True

#             pbar.update(1)

#     # Reduce la base de búsqueda
#     references = references[~references.found]

#     # Busqueda por titulo
#     print("--INFO-- Searching `references` using (title)")
#     with tqdm(total=len(references), disable=disable_progress_bar) as pbar:
#         for article, title in zip(
#             references.article,
#             references.title,
#         ):
#             if isinstance(title, str):
#                 title = (
#                     title.lower()
#                     .replace(".", "")
#                     .replace(",", "")
#                     .replace(":", "")
#                     .replace(";", "")
#                     .replace("-", " ")
#                     .replace("'", "")
#                 )

#                 for key in thesaurus.keys():
#                     text = key
#                     text = (
#                         text.lower()
#                         .replace(".", "")
#                         .replace(",", "")
#                         .replace(":", "")
#                         .replace(";", "")
#                         .replace("-", " ")
#                         .replace("'", "")
#                     )
#                     if title in text:
#                         thesaurus[key] = article
#                         references.loc[references.article == article, "found"] = True

#             pbar.update(1)
#     #
#     # Crea la columna de referencias locales
#     #
#     documents["local_references"] = documents.global_references.copy()
#     documents["local_references"] = documents["local_references"].str.lower()
#     documents["local_references"] = documents["local_references"].str.split(";")
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [t.strip() for t in x] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [thesaurus.get(t, "") for t in x] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [t for t in x if t is not None] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].str.join("; ")
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: pd.NA if x == "" else x
#     )
#     #
#     # NOTA: realmente local_references contiene las referencias globales
#     # en formato WoS
#     documents["global_references"] = documents["local_references"].copy()

#     #
#     # Se filtran local references para que contengan unicamente records
#     # que estan en la base de datos principal
#     local_documents = documents.article.copy()
#     documents["local_references"] = documents["local_references"].str.split(";")
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [t.strip() for t in x] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: [t for t in x if t in local_documents.tolist()] if isinstance(x, list) else x
#     )
#     documents["local_references"] = documents["local_references"].map(
#         lambda x: "; ".join(x) if isinstance(x, list) else x
#     )

#     #
#     documents.to_csv(documents_path, index=False)


def create__local_citations__column_in_references_database(directory):
    """Create `local_citations` column in references database

    :meta private:
    """

    references_path = os.path.join(directory, "databases", "_references.zip")
    if not os.path.exists(references_path):
        return

    print("--INFO-- Creating `local_citations` column in references database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(directory, "databases", "_main.zip")
    documents = pd.read_csv(documents_path, compression="zip")
    local_references = documents.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each reference in references database

    references = pd.read_csv(references_path, compression="zip")
    references["local_citations"] = references.article
    references["local_citations"] = references["local_citations"].map(values_dict)
    references["local_citations"] = references["local_citations"].fillna(0)

    # saves the new column in the references database
    references.to_csv(references_path, index=False, compression="zip")


def create__local_citations__column_in_documents_database(root_dir):
    """Create `local_citations` column in documents database

    :meta private:
    """

    print("--INFO-- Creating `local_citations` column in documents database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(root_dir, "databases", "_main.zip")
    documents = pd.read_csv(documents_path, compression="zip")
    local_references = documents.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each document in documents database
    documents["local_citations"] = documents.article
    documents["local_citations"] = documents["local_citations"].map(values_dict)
    documents["local_citations"] = documents["local_citations"].fillna(0)

    # saves the new column in the references database
    documents.to_csv(documents_path, index=False, compression="zip")


def report_imported_records_per_file(root_dir):
    """Report the number of imported records per file.

    Args:
        root_dir (str): root directory.

    :meta private:
    """

    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        data = pd.read_csv(file, encoding="utf-8", compression="zip")
        print(f"--INFO-- {file}: {len(data.index)} imported records")


def transform_abstract_keywords_to_underscore(root_dir):
    """Transform keywords in abstracts to uppercase

    :meta private:
    """

    def get_raw_descriptors():
        """Returns a pandas Series with all NLP phrases in the database files"""
        processed_dir = pathlib.Path(root_dir) / "databases"
        files = list(processed_dir.glob("_*.zip"))
        descriptors = []
        for file in files:
            data = pd.read_csv(file, encoding="utf-8", compression="zip")
            if "raw_nlp_phrases" not in data.columns:
                continue
            candidate_descriptors = data["raw_descriptors"].copy()
            candidate_descriptors = candidate_descriptors.dropna().str.replace("_", " ").str.lower()
            descriptors.append(candidate_descriptors)
        descriptors = pd.concat(descriptors)
        descriptors = descriptors.str.split("; ").explode().str.strip().drop_duplicates()
        # nlp_phrases = nlp_phrases[nlp_phrases.str.contains(" ")]
        return descriptors

    def clean(descriptors):
        """Remove abbreviations from NLP phrases"""

        descriptors = descriptors.copy()

        # remove abbreviations
        descriptors = descriptors.str.replace(r"\(.*\)", "", regex=True).replace(
            r"\[].*\]", "", regex=True
        )

        # strage characters
        descriptors = (
            descriptors.str.replace(r'"', "", regex=True)
            .str.replace("'", "", regex=False)
            .str.replace("#", "", regex=False)
            .str.replace("!", "", regex=False)
            .str.strip()
        )

        descriptors = descriptors[descriptors != ""]
        return descriptors

    def sort_by_num_words(descriptors):
        """Sort keywords by number of words"""

        descriptors = descriptors.copy()
        frame = descriptors.to_frame()
        frame["length"] = frame[descriptors.name].str.split(" ").map(len)
        frame = frame.sort_values(["length", descriptors.name], ascending=[False, True])
        descriptors = frame[descriptors.name].copy()
        return descriptors

    def replace_in_abstracts_and_titles(root_dir, descriptors):
        """Replace keywords in abstracts"""

        descriptors = descriptors.copy()
        descriptors = descriptors.to_list()
        descriptors = [re.escape(text) for text in descriptors]
        descriptors = "|".join(descriptors)
        regex = r"\b(" + descriptors + r")\b"

        documents_path = pathlib.Path(root_dir) / "databases/_main.zip"
        documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")
        for col in ["abstract", "title"]:
            hyphenated_words = documents[col].str.findall(r"\b\w+-\w+\b").sum()
            hyphenated_words = list(set(hyphenated_words))
            hyphenated_words = r"\b(" + "|".join(hyphenated_words) + r")\b"
            #
            documents[col] = (
                documents[col]
                .str.replace("-", " ", regex=False)
                .str.replace(regex, lambda x: x.group().upper().replace(" ", "_"), regex=True)
            )
            documents[col] = documents[col].str.replace(
                hyphenated_words.replace("-", " "),
                lambda x: x.group().replace(" ", "-"),
                regex=True,
            )

        documents.to_csv(documents_path, index=False, compression="zip")

    #
    # Main code:
    #
    descriptors = get_raw_descriptors()
    descriptors = clean(descriptors)
    descriptors = sort_by_num_words(descriptors)
    replace_in_abstracts_and_titles(root_dir, descriptors)
