#
"""

Smoke tests:
    >>> from techminer2.database.ingest import IngestScopus
    >>> IngestScopus(root_directory="examples/url/").run() # doctest: +ELLIPSIS
    N...


    >>> from techminer2.io import Query
    >>> df = (
    ...     Query()
    ...     #
    ...     .with_query_expression("SELECT tokenized_abstract FROM database;")
    ...     #
    ...     .where_root_directory("examples/url/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> import textwrap
    >>> texts = df.tokenized_abstract.to_list()
    >>> texts = [textwrap.fill(text, width=90) for text in texts]
    >>> texts = [line for text in texts for line in text.splitlines()]
    >>> texts = [text for text in texts if "http" in text]
    >>> for text in texts: print(text)
    https://github.com/asabuncuoglu13/faid-test-financial-sentiment-analysis ) . 2025 ieee .
    https://github.com/DFKI-Interactive-Machine-Learning/ophthalmo-cdss . 2025 copyright for
    available on github : https://github.com/mahdimanian/dragan-btc/ 2025 ieee .
    approximately 50+ diverse examples ( https://openclinical.net/index.phpid=69 ) .
    reduction . the software is available at : https://github.com/eyeshoe/cop-e-cat . 2021
    http://webs.iiitd.edu.in/ . this article is categorized under : application areas > health
    https://www.jmir.org ) , 24.12.2021. this is an open access article distributed under the
    https://creativecommons.org/licenses/by/4.0/ ) , which permits unrestricted use ,
    bibliographic information , a link to the original publication on https://www.jmir.org/ ,
    https://cancer.jmir.org ) , 31.01.2022. this is an open access article distributed under
    https://creativecommons.org/licenses/by/4.0/ ) , which permits unrestricted use ,
    link to the original publication on https://cancer.jmir.org/ , as well as this copyright
    available online and can be accessed through https://m3cs.shinyapps.io/M3Cs/ . for data
    database url : https://m3cs.shinyapps.io/M3Cs/ 2022 the author ( s ) 2022 . published by
    https://www.researchprotocols.org ) , 01.06.2022. this is an open access article
    https://creativecommons.org/licenses/by/4.0/ ) , which permits unrestricted use ,
    information , a link to the original publication on https://www.researchprotocols.org , as
    https://formative.jmir.org ) , 29.06.2022 .
    https://github.com/aekanshgoel/COVID-19-scRNAseq . 2022 owner / author .
    goodfellow et al . in adv neural inf process syst , 2014 . https://doi.org/10.1145/3422622
    https://arxiv.org/abs/1701.07875 ) , and ctgan ( xu et al . in modeling tabular data using
    conditional gan . https://arxiv.org/pdf/1907.00503 ) independently for baseline comparison
    registration https://osf.io/veqha/?view-only=f560d4892d7c459ea4cff6dcdfacb086 author ( s )
    available at https://github.com/hammoudiproject/SuperpixelGridMasks . 2023 , the author (
    reference beraadslaging nr . 22/014 van 11 january 2022 , available via https://www.ehealt
    chictr2100052773 ) on 11 may 2021 , http://www.chictr.org.cn/showproj.aspx?proj=136659 .
    up . the system is available online at https://kidsfractureexpert.com/ . the author ( s )
    available at https://github.com/hxfj/Facial-Landmark-based-BMI-Analysis.git.Clinical
    in jmir public health and surveillance ( https://publichealth.jmir.org ) , 20.12.2023.
    attribution license ( https://creativecommons.org/licenses/by/4.0/ ) , which permits
    https://publichealth.jmir.org , as well as this copyright and license information must be
    https://www.chictr.org.cn/showproj.html?proj=191398 , chictr2300071478 . copyright 2024 xu
    our code can be accessed through https://github.com/koa-fin/sep . 2024 owner / author .
    https://github.com/anupb08/vendornews-analytics . 2024 copyright for this paper by its
    of our developed method is publicly available at https://gitee.com/andyham-andy.ham/lest-
    https://styluspub.presswarehouse.com/client/MLI . 2023 by bpb publications . all rights
    online demo is available at http://vdemo.dbmind.cn . 2024 , vldb endowment . all rights
    open science framework under doi 10.17605/osf.io/92sk4 ( available at https://osf.io/92SK4
    published in jmir ai ( https://ai.jmir.org ) , 06.02.2025. this is an open access article
    https://github.com/cubenlp/FinDABench . findabench aims to provide a measure for in depth
    synergy with human analytical insights . https://chatgpt.com/g/g-bS4Q76v0I-quantum 2024




    >>> import textwrap
    >>> from techminer2.explore import RecordMapping
    >>> mapping = (
    ...     RecordMapping()
    ...     #
    ...     .where_root_directory("examples/url/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("global_cited_by_highest")
    ...     .run()
    ... )

    >>> texts = [mapping[i]["AB"] for i in range(len(mapping))]
    >>> texts = [textwrap.fill(text, width=90) for text in texts]
    >>> texts = [line for text in texts for line in text.splitlines()]
    >>> texts = [text for text in texts if "http" in text]
    >>> for text in texts: print(text)
    goodfellow et al . in adv neural inf process syst , 2014 . https://doi.org/10.1145/3422622
    https://arxiv.org/abs/1701.07875 ) , and ctgan ( xu et al . in modeling TABULAR_DATA using
    CONDITIONAL_GAN . https://arxiv.org/pdf/1907.00503 ) independently for BASELINE_COMPARISON
    DIMENSION_REDUCTION . THE_SOFTWARE is available at : https://github.com/eyeshoe/cop-e-cat
    research ( https://www.jmir.org ) , 24.12.2021. this is an open access article distributed
    https://creativecommons.org/licenses/by/4.0/ ) , which permits unrestricted use ,
    https://www.jmir.org/ , as_well_as this copyright and license information must be included
    https://github.com/koa-fin/sep . 2024 owner / author .
    https://cancer.jmir.org ) , 31.01.2022. this is an open access article distributed under
    https://creativecommons.org/licenses/by/4.0/ ) , which permits unrestricted use ,
    link to the original publication on https://cancer.jmir.org/ , as_well_as this copyright
    https://github.com/hammoudiproject/superpixelgridmasks . 2023 , the author ( s ) , under
    https://openclinical.net/index.phpid=69 ) . CONCLUSION_OPENCLINICAL . NET is A_SHOWCASE
    http://vdemo.dbmind.cn . 2024 , vldb endowment . all rights reserved .
    related to HEALTHCARE http://webs.iiitd.edu.in/ . this article is categorized under :
    https://www.researchprotocols.org ) , 01.06.2022. this is an open access article
    https://creativecommons.org/licenses/by/4.0/ ) , which permits unrestricted use ,
    https://www.researchprotocols.org , as_well_as this copyright and license information must
    research ( https://formative.jmir.org ) , 29.06.2022 .
    https://m3cs.shinyapps.io/m3cs/ . for DATA_DRIVEN_CLINICAL_SIGNIFICANCE_APPROACH , 538
    INCORPORATE_MIRNA in THE_CLINICAL_POLICY . database url : https://m3cs.shinyapps.io/m3cs/
    http://www.chictr.org.cn/showproj.aspx?proj=136659 . trial registration number
    https://github.com/aekanshgoel/covid-19-scrnaseq . 2022 owner / author .
    https://ai.jmir.org ) , 06.02.2025. this is an open access article distributed under the
    https://gitee.com/andyham-andy.ham/lest-forecasting-framework . 2024 elsevier inc .
    JANUARY 2022 , available via https://www.ehealth.fgov.be/ehealthplatform/file/view/ax54cwc
    https://github.com/hxfj/facial-landmark-based-bmi-analysis.git.clinical relevance this
    https://osf.io/92sk4 ) . author ( s ) ( or their employer ( s ) ) 2025 . re use permitted
    https://chatgpt.com/g/g-bs4q76v0i-quantum 2024 ieee .
    published in JMIR_PUBLIC_HEALTH and SURVEILLANCE ( https://publichealth.jmir.org ) ,
    commons attribution license ( https://creativecommons.org/licenses/by/4.0/ ) , which
    https://publichealth.jmir.org , as_well_as this copyright and license information must be
    https://www.chictr.org.cn/showproj.html?proj=191398 , chictr2300071478 . copyright 2024 xu
    https://osf.io/veqha/?view-only=f560d4892d7c459ea4cff6dcdfacb086 author ( s ) ( or their
    https://github.com/asabuncuoglu13/faid-test-financial-sentiment-analysis ) . 2025 ieee .
    for OUR_CDSS is available here : https://github.com/dfki-interactive-machine-
    the proposed method is available on GITHUB : https://github.com/mahdimanian/dragan-btc/
    https://github.com/cubenlp/findabench . FINDABENCH_AIMS to provide A_MEASURE for
    are available at https://github.com/anupb08/vendornews-analytics . 2024 copyright for this
    https://styluspub.presswarehouse.com/client/mli . 2023 by bpb publications . all rights
    https://kidsfractureexpert.com/ . the author ( s ) 2023 .






"""
