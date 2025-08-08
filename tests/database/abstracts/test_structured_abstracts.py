# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
#
"""

Example:
    >>> from techminer2.database.ingest import IngestScopus
    >>> IngestScopus(root_directory="examples/structured/").run() # doctest: +ELLIPSIS

    >>> import textwrap
    >>> from techminer2.tools import RecordMapping
    >>> mapping = (
    ...     RecordMapping()
    ...     #
    ...     .where_root_directory_is("examples/structured/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     .where_records_ordered_by("global_cited_by_highest")
    ...     .run()
    ... )

    >>> for i in range(10):
    ...     print(textwrap.fill(mapping[i]["AB"], width=90))
    ...     print()
    background : THE_FLIPPED_CLASSROOM has generated interest in HIGHER_EDUCATION providing
    A_STUDENT_CENTRED_APPROACH to LEARNING . this has THE_POTENTIAL to engage NURSING_STUDENTS
    in WAYS that address THE_NEEDS of today ' sstudents and THE_COMPLEXITY of
    CONTEMPORARY_HEALTHCARE . calls for EDUCATIONAL_REFORM , particularly in
    HEALTHCARE_PROGRAMS such_as NURSING , highlight THE_NEED for STUDENTS to PROBLEM solve ,
    reason and apply THEORY into PRACTICE . THE_DRIVERS towards STUDENT_BASED_LEARNING have
    manifested in TEAM , PROBLEM and CASE_BASED_LEARNING models . though there has been
    A_SHIFT towards THE_FLIPPED_CLASSROOM , comparatively little is known about how it is used
    in NURSING_CURRICULA . objectives : THE_AIMS of THIS_SYSTEMATIC_REVIEW were to examine how
    THE_FLIPPED_CLASSROOM has been applied in NURSING_EDUCATION and OUTCOMES associated with
    THIS_STYLE of TEACHING . data sources : FIVE_DATABASES were searched and resulted in
    THE_RETRIEVAL of 21 papers : PUBMED , CINAHL , EMBASE , SCOPUS and ERIC . review methods :
    after SCREENING for INCLUSION_/_EXCLUSION_CRITERIA , EACH_PAPER was evaluated using
    A_CRITICAL_APPRAISAL_TOOL . DATA_EXTRACTION and ANALYSIS were completed on
    ALL_INCLUDED_STUDIES . results : THIS_SYSTEMATIC_REVIEW screened 21 titles and ABSTRACTS
    resulting_in NINE_INCLUDED_STUDIES . ALL_AUTHORS critically appraised THE_QUALITY of
    THE_INCLUDED_STUDIES . FIVE_STUDIES were identified and THEMES identified were :
    ACADEMIC_PERFORMANCE_OUTCOMES , and STUDENT_SATISFACTION implementing
    THE_FLIPPED_CLASSROOM . conclusions : use of THE_FLIPPED_CLASSROOM in
    HIGHER_EDUCATION_NURSING_PROGRAMMES yielded NEUTRAL_OR_POSITIVE_ACADEMIC_OUTCOMES and
    MIXED_RESULTS for SATISFACTION . ENGAGEMENT of STUDENTS in THE_FLIPPED_CLASSROOM_MODEL was
    achieved when ACADEMICS informed and rationalised THE_PURPOSE of
    THE_FLIPPED_CLASSROOM_MODEL to STUDENTS . however , NO_STUDIES in THIS_REVIEW identified
    THE_EVALUATION of THE_PROCESS of implementing THE_FLIPPED_CLASSROOM . STUDIES examining
    THE_PROCESS and ONGOING_EVALUATION and REFINEMENT of THE_FLIPPED_CLASSROOM in
    HIGHER_EDUCATION_NURSING_PROGRAMMES are warranted . 2015 elsevier ltd .
    <BLANKLINE>
    aim : to determine whether THE_USE of AN_ONLINE_OR_BLENDED_LEARNING_PARADIGM has
    THE_POTENTIAL to enhance THE_TEACHING of CLINICAL_SKILLS in UNDERGRADUATE_NURSING .
    background : THE_NEED to adequately SUPPORT and develop STUDENTS in CLINICAL_SKILLS is now
    arguably more important than previously considered due_to REDUCTIONS in
    PRACTICE_OPPORTUNITIES . ONLINE_AND_BLENDED_TEACHING_METHODS are being developed to try
    and meet THIS_REQUIREMENT , but KNOWLEDGE about THEIR_EFFECTIVENESS in
    TEACHING_CLINICAL_SKILLS is LIMITED . design : MIXED_METHODS_SYSTEMATIC_REVIEW , which
    follows the joanna briggs institute user guide version 5. data sources :
    COMPUTERIZED_SEARCHES of FIVE_DATABASES were undertaken for THE_PERIOD 1995 august 2013 .
    review methods : critical appraisal and data extraction were undertaken using joanna
    briggs institute tools for experimental / observational STUDIES and
    INTERPRETATIVE_AND_CRITICAL_RESEARCH . A_NARRATIVE_SYNTHESIS was used to REPORT_RESULTS .
    results : NINETEEN_PUBLISHED_PAPERS were identified . SEVENTEEN_PAPERS reported on
    ONLINE_APPROACHES and ONLY_TWO_PAPERS reported on A_BLENDED_APPROACH . THE_SYNTHESIS of
    FINDINGS focused on THE_FOLLOWING_FOUR_AREAS : PERFORMANCE_/_CLINICAL_SKILL , KNOWLEDGE ,
    SELF_EFFICACY_/_CLINICAL_CONFIDENCE_AND_USER_EXPERIENCE_/_SATISFACTION .
    THE_E_LEARNING_INTERVENTIONS used varied throughout ALL_THE_STUDIES . conclusion :
    THE_AVAILABLE_EVIDENCE suggests that ONLINE_LEARNING for TEACHING_CLINICAL_SKILLS is no
    less effective than TRADITIONAL_MEANS . highlighted by THIS_REVIEW is THE_LACK of
    AVAILABLE_EVIDENCE on THE_IMPLEMENTATION of A_BLENDED_LEARNING_APPROACH to
    TEACHING_CLINICAL_SKILLS in UNDERGRADUATE_NURSE_EDUCATION . FURTHER_RESEARCH is required
    to assess THE_EFFECTIVENESS of THIS_TEACHING_METHODOLOGY . 2014 john wiley and sons ltd .
    <BLANKLINE>
    purpose : BLENDED_LEARNING is rapidly emerging as A_DOMAIN for PRACTICE and RESEARCH .
    across DISCIPLINES and CONTEXTS , at INDIVIDUAL_INSTRUCTOR and INSTITUTION_LEVELS ,
    EDUCATORS are experimenting with THE_BLENDED_LEARNING_MODEL of INSTRUCTION .
    THE_CURRENT_GENERATION of LEARNERS have been referred to as ' digitalnatives ' in
    REFL_ECTION of THEIR_APPARENT_EASE and FAMILIARITY with DIGITAL_TECHNOLOGY . however ,
    QUESTIONS remain about how READY_STUDENTS are for A_BLENDED_LEARNING_MODEL of INSTRUCTION
    . THE_PURPOSE of the study was to investigate STUDENTS ' readiness for
    A_BLENDED_LEARNING_MODEL of INSTRUCTION in
    A_LEADING_MALAYSIAN_HIGHER_EDUCATION_INSTITUTION . methodology : the study employed
    A_NON_EXPERIMENTAL_QUANTITATIVE_RESEARCH_DESIGN . DATA were gathered from A_SAMPLE of 235
    UNDERGRADUATE and 131 POSTGRADUATE_STUDENTS using
    THE_BLENDED_LEARNING_READINESS_ENGAGEMENT_QUESTIONNAIRE ( BLREQ ) . THE_DATA was analysed
    using the WINSTEPS_RASCH_MODEL_MEASUREMENT_SOFTWARE to determine the
    VALIDITY_AND_RELIABILITY of THE_INSTRUMENT . DIFFERENTIAL_ITEM_FUNCTIONING_ANALYSIS was
    also used to IDENTIFY_RESPONSES based on STUDENTS ' DEMOGRAPHIC_PROFILES . findings :
    FINDINGS identified that STUDENTS were ready for BLENDED_LEARNING . FURTHER_ANALYSIS
    indicated that there were DIFFERENCES in STUDENTS ' readiness for BLENDED_LEARNING based
    on GENDER , AGE , ETHNICITY , FIELD of STUDY , and LEVEL of EDUCATION . significance :
    this study provides INSIGHTS on STUDENTS ' readiness towards BLENDED_LEARNING ,
    particularly in THE_MALAYSIAN_CONTEXT , DISCUSSES_IMPLICATIONS for
    BLENDED_LEARNING_PRACTICES in HIGHER_EDUCATION_INSTITUTIONS , and offers RECOMMENDATIONS
    for FUTURE_RESEARCH . 2013 , universiti utara malaysia .
    <BLANKLINE>
    for EFFECTIVE_FLIPPED_LEARNING , beyond simply switching THE_SEQUENCE of LECTURES and
    HOMEWORK , it is important to understand and implement THE_FUNDAMENTAL_DESIGN_PRINCIPLES
    of FLIPPED_LEARNING . A_NEW_NOTION is proposed called FLIPPED_LEARNING_DESIGN_FIDELITY ,
    defined as THE_DEGREE to which A_CLASS is faithfully designed to be close to
    AN_IDEAL_FLIPPED_LEARNING_CLASS operationalised with FOUR_PROXY_INDICATORS of
    THE_F_L_I_PTM_MODEL ( FLEXIBLE_ENVIRONMENT , LEARNING_CULTURE , INTENTIONAL_CONTENT , and
    PROFESSIONAL_EDUCATOR ) . THIS_STUDY empirically examines THE_EFFECT of
    BOTH_LEARNER_RELATED_FACTOR ( SELF_REGULATED_LEARNING ) and DESIGN_RELATED_FACTOR (
    DESIGN_FIDELITY ) on LEARNING_OUTCOMES ( SATISFACTION , CONTINUANCE_INTENTION ) in
    A_UNIVERSITY_FLIPPED_COURSE . we hypothesised that FLIPPED_LEARNING_DESIGN_FIDELITY and
    SELF_REGULATED_LEARNING affect STUDENT_SATISFACTION and INTENTION to_continue
    participating in A_FLIPPED_LEARNING_COURSE . THE_PARTICIPANTS were 134 KOREAN_STUDENTS of
    A_UNIVERSITY_COURSE taught in A_FLIPPED_LEARNING_MODE . THE_RESULTS revealed that
    THE_LEVEL of FLIPPED_LEARNING_DESIGN_FIDELITY had A_SIGNIFICANT_EFFECT on SATISFACTION ,
    but did not affect CONTINUANCE_INTENTION . in_addition , THE_LEVEL of
    SELF_REGULATED_LEARNING had A_SIGNIFICANT_EFFECT on SATISFACTION and CONTINUANCE_INTENTION
    . drawn from THE_KEY_FINDINGS , we suggest IMPLICATIONS for THE_DESIGN of
    FLIPPED_LEARNING_COURSES in A_UNIVERSITY_CONTEXT . implications for practice :
    INSTRUCTIONAL_DESIGNERS and INSTRUCTORS can apply THE_CONCEPT of
    FLIPPED_LEARNING_DESIGN_FIDELITY to fully implement THE_FOUR_PILLARS of
    THE_F_L_I_PTM_MODEL . SELF_REGULATED_STUDENTS are likely to be satisfied with
    FLIPPED_LEARNING and want to_continue taking FLIPPED_LEARNING_COURSES . 2021 . articles
    published in the australasian journal of educational technology ( AJET ) are available
    under creative commons attribution NON commercial NO_DERIVATIVES_LICENCE ( cc by nc nd 4.0
    ) . AUTHORS retain COPYRIGHT in THEIR_WORK and GRANT_AJET_RIGHT of FIRST_PUBLICATION under
    cc by nc nd 4.0 .
    <BLANKLINE>
    clinical relevance : THE_SYNCHRONOUS_HYBRID_LEARNING_ENVIRONMENT is associated with
    INCREASED_TIME spent by STUDENTS working with vdt and INCREASED_PREVALENCE of
    DRY_EYE_SYMPTOMS in A_UNIVERSITY_BASED_POPULATION . background : to assess THE_PREVALENCE
    of DRY_EYE_SYMPTOMS using the OCULAR_SURFACE_DISEASE_INDEX_QUESTIONNAIRE in
    UNIVERSITY_STUDENTS and to identify whether FACTORS such_as
    THE_SYNCHRONOUS_HYBRID_LEARNING_ENVIRONMENT as A_PREVENTIVE_MEASURE of covid 19 ,
    VIDEO_DISPLAY_TERMINAL_USE , GENDER or CONTACT_LENS_WEAR_INFLUENCE_DRY_EYE_SYMPTOMATOLOGY
    . methods : this study was performed using A_WEB_BASED_QUESTIONNAIRE that was distributed
    to UNIVERSITY_STUDENTS to ASSESS_QUESTIONS related to CLASS_ATTENDANCE , to THE_USE of
    VIDEO_DISPLAY_TERMINALS , THE_NEED for OPTICAL_CORRECTION and , finally ,
    THE_OSDI_QUESTIONNAIRE . results : A_TOTAL of 676 UNIVERSITY_STUDENTS with an average
    age_of 20.7 2.9 years completed THE_QUESTIONNAIRE , of which 72.6 % ( 491 ) were FEMALES
    and 27.4 % ( 185 ) were MALES . only 10.2 % of THE_PARTICIPANTS attended
    FACE_TO_FACE_CLASSES . of THE_PARTICIPANTS , 35.5 % were CONTACT_LENS_WEARERS .
    THE_MEAN_OSDI_SCORE of the study population was 27.68 20.09 and THE_PREVALENCE of
    SYMPTOMATIC_DRY_EYE_DISEASE ( OSDI_SCORE above 22 ) was 51.8 % . FEMALE_GENDER ( x2 ( 3 )
    = 38.605 , p < 0.001 ) , ONLINE_CLASS_ATTENDANCE ( x2 ( 1 ) = 20.31. p < 0.001 ) ,
    increased HOURS of ONLINE_CLASS_ATTENDANCE ( x2 ( 2 ) = 26.84 , p < 0.001 ) and
    CONTACT_LENS_WEAR ( x2 ( 2 ) = 15.264 , p < 0.05 ) were associated with A_HIGHER_INCIDENCE
    of SYMPTOMATIC_DRY_EYE_DISEASE . conclusion : THE_SYNCHRONOUS_HYBRID_LEARNING_ENVIRONMENT
    increases the TIME_STUDENTS spend working with VIDEO_DISPLAY_TERMINALS and THE_PREVALENCE
    of DRY_EYE_SYMPTOMS . FEMALE_GENDER and CONTACT_LENS_WEAR were also associated with
    A_HIGHER_PREVALENCE of DRY_EYE_SYMPTOMS . it should not be ignored THAT_DRY_EYE could also
    affect ACADEMIC_PERFORMANCE . 2021 optometry australia .
    <BLANKLINE>
    introduction : this study aims to explore THE_RELATIONSHIPS among PSYCHOLOGICAL_CAPITAL ,
    LEARNING_MOTIVATION , EMOTIONAL_ENGAGEMENT , and ACADEMIC_PERFORMANCE for COLLEGE_STUDENTS
    in A_BLENDED_LEARNING_ENVIRONMENT . method : THE_RESEARCH consists of TWO_STUDIES : STUDY
    1 primarily focuses on validating , developing , revising , and analyzing
    THE_PSYCHOMETRIC_PROPERTIES of THE_SCALE using FACTOR_ANALYSIS , while STUDY 2 employs
    STRUCTURAL_EQUATION_MODELING ( SEM ) to test THE_HYPOTHESES of RELATIONSHIPS of
    INCLUDED_VARIABLES and draw CONCLUSIONS based on 745 DATA collected in A_UNIVERSITY in
    CHINA . results : FINDINGS revealed that INTRINSIC_MOTIVATION , EXTRINSIC_MOTIVATION ,
    EMOTIONAL_ENGAGEMENT , and PSYCHOLOGICAL_CAPITAL all IMPACT_ACADEMIC_PERFORMANCE .
    EXTRINSIC_LEARNING_MOTIVATION has SIGNIFICANT_POSITIVE_DIRECT_EFFECTS on
    INTRINSIC_LEARNING_MOTIVATION , EMOTIONAL_ENGAGEMENT , and PSYCHOLOGICAL_CAPITAL .
    INTRINSIC_MOTIVATION_MEDIATES_THE_RELATIONSHIP between EXTRINSIC_MOTIVATION and
    ACADEMIC_PERFORMANCE . discussion : in FUTURE_BLENDED_LEARNING_PRACTICES , it is essential
    to CULTIVATE_STUDENTS ' INTRINSIC_LEARNING_MOTIVATION while maintaining A_CERTAIN_LEVEL of
    EXTERNAL_LEARNING_MOTIVATION . it is also crucial to stimulate and maintain STUDENTS '
    EMOTIONAL_ENGAGEMENT , enhance THEIR_SENSE of IDENTITY and belonging , and recognize
    THE_ROLE of PSYCHOLOGICAL_CAPITAL in LEARNING to boost STUDENTS ' confidence , RESILIENCE
    , and POSITIVE_EMOTIONS . copyright 2024 liu , ma and chen .
    <BLANKLINE>
    background : THE_FLIPPED_CLASSROOM ' approach is AN_INNOVATIVE_APPROACH in
    EDUCATIONAL_DELIVERY_SYSTEMS . in A_TYPICAL_FLIPPED_CLASS_MODEL , WORK that_is typically
    done as HOMEWORK in THE_DIDACTIC_MODEL is interactively undertaken in THE_CLASS with
    THE_GUIDANCE of THE_TEACHER , whereas listening to A_LECTURE or
    WATCHING_COURSE_RELATED_VIDEOS is undertaken at HOME . THE_ESSENCE of A_FLIPPED_CLASSROOM
    is that THE_ACTIVITIES carried out during TRADITIONAL_CLASS_TIME and SELF_STUDY_TIME are
    reversed or flipped ' . objectives : THE_PRIMARY_OBJECTIVES of THIS_REVIEW were to assess
    THE_EFFECTIVENESS of THE_FLIPPED_CLASSROOM_INTERVENTION for
    UNDERGRADUATE_HEALTH_PROFESSIONAL_STUDENTS on THEIR_ACADEMIC_PERFORMANCE , and
    THEIR_COURSE_SATISFACTION . search methods : we identified RELEVANT_STUDIES by searching
    MEDLINE ( OVID ) , APA_PSYCINFO , EDUCATION_RESOURCES_INFORMATION_CENTER ( ERIC )
    as_well_as several more ELECTRONIC_DATABASES , registries , SEARCH_ENGINES , WEBSITES ,
    and ONLINE_DIRECTORIES . THE_LAST_SEARCH_UPDATE was performed in APRIL 2022 . selection
    criteria : included STUDIES had to meet THE_FOLLOWING_CRITERIA : PARTICIPANTS :
    UNDERGRADUATE_HEALTH_PROFESSIONAL_STUDENTS , regardless_of THE_TYPE of HEALTHCARE_STREAMS
    ( e.g. , MEDICINE , PHARMACY ) , duration of THE_LEARNING_ACTIVITY , or the country of
    STUDY . intervention : we included ANY_EDUCATIONAL_INTERVENTION that included
    THE_FLIPPED_CLASSROOM as A_TEACHING_AND_LEARNING_TOOL in UNDERGRADUATE_PROGRAMS ,
    regardless_of THE_TYPE of HEALTHCARE_STREAMS ( e.g. , MEDICINE , PHARMACY ) . we also
    included STUDIES that aimed to improve STUDENT_LEARNING and / or STUDENT_SATISFACTION if
    they included THE_FLIPPED_CLASSROOM for UNDERGRADUATE_STUDENTS . we excluded STUDIES on
    STANDARD_LECTURES and SUBSEQUENT_TUTORIAL_FORMATS . we also excluded STUDIES on
    FLIPPED_CLASSROOM_METHODS , which did not belong to the HEALTH_PROFESSIONAL_EDUCATION (
    HPE ) sector ( e.g. , engineering , economics ) . outcomes : THE_INCLUDED_STUDIES used
    PRIMARY_OUTCOMES such_as ACADEMIC_PERFORMANCE as judged by
    FINAL_EXAMINATION_GRADES_/_SCORES or OTHER_FORMAL_ASSESSMENT_METHODS at
    THE_IMMEDIATE_POST_TEST , as_well_as STUDENT_SATISFACTION with the METHOD_OF_LEARNING .
    study design : we included randomised CONTROLLED_TRIALS ( RCTS ) ,
    QUASI_EXPERIMENTAL_STUDIES ( QES ) , and TWO_GROUP_COMPARISON_DESIGNS . although we had
    planned to include CLUSTER_LEVEL_RCTS , NATURAL_EXPERIMENTS , and
    REGRESSION_DISCONTINUITY_DESIGNS , these were not available . we did not include
    QUALITATIVE_RESEARCH . data collection and analysis : TWO_MEMBERS of THE_REVIEW_TEAM
    independently screened THE_SEARCH_RESULTS to ASSESS_ARTICLES for THEIR_ELIGIBILITY for
    INCLUSION . THE_SCREENING involved AN_INITIAL_SCREENING of THE_TITLE and ABSTRACTS , and
    subsequently , the FULL_TEXT of SELECTED_ARTICLES . DISCREPANCIES between
    THE_TWO_INVESTIGATORS were settled through DISCUSSION or CONSULTATION with A_THIRD_AUTHOR
    . TWO_MEMBERS of THE_REVIEW_TEAM then extracted THE_DESCRIPTIONS and DATA from
    THE_INCLUDED_STUDIES . main results : we found 5873 potentially RELEVANT_RECORDS , of
    which we screened 118 of them in FULL_TEXT , and included 45 STUDIES ( 11 RCTS , 19 QES ,
    and 15 two GROUP_OBSERVATIONAL_STUDIES ) that met THE_INCLUSION_CRITERIA . SOME_STUDIES
    assessed MORE_THAN_ONE_OUTCOME . we included 44 STUDIES on ACADEMIC_PERFORMANCE and
    EIGHT_STUDIES on STUDENTS ' SATISFACTION_OUTCOMES in THE_META_ANALYSIS . THE_MAIN_REASONS
    for excluding STUDIES were that they had not implemented A_FLIPPED_CLASS_APPROACH or
    THE_PARTICIPANTS were not UNDERGRADUATE_STUDENTS in HEALTH_PROFESSIONAL_EDUCATION .
    A_TOTAL of 8426 UNDERGRADUATE_STUDENTS were included in 45 STUDIES that were identified
    for THIS_ANALYSIS . THE_MAJORITY of THE_STUDIES were conducted by STUDENTS from
    MEDICAL_SCHOOLS ( 53.3 % , 24/45 ) , NURSING_SCHOOLS ( 17.8 % , 8/45 ) , PHARMACY_SCHOOLS
    ( 15.6 % , 7/45 ) . medical , NURSING , and DENTISTRY_SCHOOLS ( 2.2 % , 1/45 ) , and
    OTHER_HEALTH_PROFESSIONAL_EDUCATION_PROGRAMS ( 11.1 % , 5/45 ) . among_these 45 STUDIES
    identified , 16 ( 35.6 % ) were conducted in THE_UNITED_STATES , SIX_STUDIES in CHINA ,
    FOUR_STUDIES in TAIWAN , three in INDIA , TWO_STUDIES each in AUSTRALIA and CANADA ,
    followed by NINE_SINGLE_STUDIES from BRAZIL , german , IRAN , NORWAY , SOUTH_KOREA , SPAIN
    , THE_UNITED_KINGDOM , SAUDI_ARABIA , and TURKEY . based on OVERALL_AVERAGE_EFFECT_SIZES ,
    there was BETTER_ACADEMIC_PERFORMANCE in THE_FLIPPED_CLASS_METHOD of LEARNING compared to
    TRADITIONAL_CLASS_LEARNING ( standardised mean difference [ smd ] = 0.57 , 95 % confidence
    interval [ CI ] = 0.25 to 0.90 , 2 : 1.16. i2 : 98 % . p < 0.00001 , 44 STUDIES , n = 7813
    ) . in A_SENSITIVITY_ANALYSIS that excluded ELEVEN_STUDIES with IMPUTED_DATA from
    THE_ORIGINAL_ANALYSIS of 44 STUDIES , ACADEMIC_PERFORMANCE in THE_FLIPPED_CLASS_METHOD of
    LEARNING was better than TRADITIONAL_CLASS_LEARNING ( smd = 0.54 , 95 % CI = 0.24 to 0.85
    , 2 : 0.76. i2 : 97 % . p < 0.00001 , 33 STUDIES , n = 5924 ) . all being LOW_CERTAINTY of
    EVIDENCE . overall , STUDENT_SATISFACTION with FLIPPED_CLASS_LEARNING was positive
    compared to TRADITIONAL_CLASS_LEARNING ( smd = 0.48 , 95 % CI = 0.15 to 0.82 , 2 : 0.19 ,
    i2:89 % , p < 0.00001 , 8 STUDIES n = 1696 ) . all being LOW_CERTAINTY of EVIDENCE .
    authors ' conclusions : in THIS_REVIEW , we aimed to find EVIDENCE of
    THE_FLIPPED_CLASSROOM_INTERVENTION ' seffectiveness for
    UNDERGRADUATE_HEALTH_PROFESSIONAL_STUDENTS . we found ONLY_A_FEW_RCTS , and the
    RISK_OF_BIAS in THE_INCLUDED_NON_RANDOMISED_STUDIES was high . overall , implementing
    FLIPPED_CLASSES may improve ACADEMIC_PERFORMANCE , and may SUPPORT_STUDENT_SATISFACTION in
    UNDERGRADUATE_HEALTH_PROFESSIONAL_PROGRAMS . however , THE_CERTAINTY of EVIDENCE was low
    for BOTH_ACADEMIC_PERFORMANCE and STUDENTS ' SATISFACTION with THE_FLIPPED_METHOD of
    LEARNING compared to THE_TRADITIONAL_CLASS_LEARNING . future well designed
    SUFFICIENTLY_POWERED_RCTS with low RISK_OF_BIAS that REPORT according to
    THE_CONSORT_GUIDELINES are needed . 2023 the authors . CAMPBELL_SYSTEMATIC_REVIEWS
    published by john wiley and sons ltd on BEHALF of THE_CAMPBELL_COLLABORATION .
    <BLANKLINE>
    introduction : TEACHERS are currently trying to change THE_TRADITIONAL_MODEL to one based
    on LEARNING_NEEDS of THE_STUDENTS . THE_FLIPPED_LEARNING_MODEL seeks to promote LEARNING
    through A_WORK jointly led by TEACHERS_AND_STUDENTS . objective : to analyze
    THE_IMPLEMENTATION of THE_FLIPPED_LEARNING_MODEL in THE_ACHIEVEMENT of GOALS in
    THE_RESEARCH_METHODOLOGY_COURSE . methodology : a prospective , longitudinal ,
    QUASI_EXPERIMENTAL_RESEARCH_DESIGN . place : HEALTH_SCIENCES_FACULTY , at
    A_PRIVATE_UNIVERSITY . participants : 81 UNDERGRADUATE_STUDENTS . interventions :
    A_CONVENIENCE_NON_PROBABILITY_SAMPLE was selected . then , THE_FLIPPED_LEARNING_MODEL was
    implemented . THE_FIRST_ANALYSIS was performed in THE_THIRD_WEEK of CLASSES , and the
    second one in THE_FIFTEENTH_WEEK , using A_VALID_INSTRUMENT with A_TOTAL_RELIABILITY_INDEX
    of 0.79. THE_EDOOME_EDUCATIONAL_PLATFORM was also used . it has CHARACTERISTICS of an
    OPEN_SOURCE_LEARNING_MANAGEMENT_SYSTEM . results : 93.8 % stated that THE_TEACHER and
    THE_STUDENTS develop THE_CLASS , 29.6 % previously STUDY_THE_CONTENTS , and 39.5 % make
    A_SUMMARY of THE_CLASS , meaning that THE_COLLABORATIVE_WORK predominates . 74.0 % stated
    that THE_FLIPPED_LEARNING facilitated THEIR_LEARNING and obtained BETTER_GRADES in
    THE_FINAL_EXAM . conclusion : THE_FLIPPED_CLASSROOM_MODEL proved to be effective to
    achieve LEARNING_GOALS in THE_RESEARCH_METHODOLOGY_COURSE , and ITS_IMPLEMENTATION is
    becoming A_NEED for THE_UNIVERSITY_EDUCATION_SYSTEM . 2018 film and HISTORY . all rights
    reserved .
    <BLANKLINE>
    introduction : THE_ONGOING_CHANGES in HEALTH_CARE_DELIVERY have resulted in THE_REFORM of
    EDUCATIONAL_CONTENT and METHODS of TRAINING in POSTGRADUATE_MEDICAL_LEADERSHIP_EDUCATION .
    HEALTH_CARE_LAW and MEDICAL_ERRORS are DOMAINS in MEDICAL_LEADERSHIP where
    MEDICAL_RESIDENTS_DESIRE_TRAINING . however , THE_POTENTIAL_VALUE of THE_FLIPPED_CLASSROOM
    as A_PEDAGOGICAL_TOOL for LEADERSHIP_TRAINING within POSTGRADUATE_MEDICAL_EDUCATION has
    not been fully explored . there fore , we designed A_LEARNING_MODULE for_this_purpose and
    made use of THE_FLIPPED_CLASSROOM_MODEL to deliver THE_TRAINING . evidence :
    THE_FLIPPED_CLASSROOM_MODEL reverses THE_ORDER of LEARNING : BASIC_CONCEPTS are learned
    individually outside_of CLASS so_that MORE_TIME is spent applying KNOWLEDGE to DISCUSSIONS
    and PRACTICAL_SCENARIOS during CLASS . ADVANTAGES include HIGH_LEVELS of INTERACTION ,
    OPTIMAL_UTILIZATION of STUDENT_AND_EXPERT_TIME and DIRECT_APPLICATION to THE_PRACTICE
    setting . DISADVANTAGES include THE_NEED for HIGH_LEVELS of SELF_MOTIVATION and
    TIME_CONSTRAINTS within THE_CLINICAL_SETTING . discussion : EDUCATIONAL_NEEDS and
    EXPECTATIONS vary within VARIOUS_GENERATIONS and call for NOVEL_TEACHING_MODALITIES .
    hence , THE_CHOICE of INSTRUCTIONAL_METHODS should be driven not only by
    THEIR_INTRINSIC_VALUES but also by THEIR_ALIGNMENT with the LEARNERS ' preference .
    THE_FLIPPED_CLASSROOM_MODEL is AN_EDUCATIONAL_MODALITY that resonates with
    MILLENNIAL_STUDENTS . it helps them to PROGRESS quickly beyond THE_MERE_UNDERSTANDING of
    THEORY to HIGHER_ORDER_COGNITIVE_SKILLS such_as EVALUATION and APPLICATION of KNOWLEDGE in
    PRACTICE . hence , THE_SUCCESSFUL_APPLICATION of THIS_MODEL would allow THE_TRANSLATION of
    HIGHLY_THEORETICAL_TOPICS to THE_PRACTICE setting within POSTGRADUATE_MEDICAL_EDUCATION .
    2017 lucardie et al .
    <BLANKLINE>
    purpose : we systematically reviewed THE_EMPIRICAL_LITERATURE that REPORTS_RESEARCH in
    THE_SPECIFIC_CONTEXT of TEACHING_EFL to identify what is known about THE_EFFICACY of using
    FLIPPED_LEARNING to teach EFL , THE_ROBUSTNESS of THIS_EVIDENCE , and to explicate
    THE_STRENGTHS and WEAKNESSES of THE_PEDAGOGY in TEACHING_EFL . design / methodology /
    approach : adapting THE_SYSTEMATIC_LITERATURE_REVIEW_METHOD and combining it with
    CONTENT_ANALYSIS of QUALITATIVE_FINDINGS we narrowed OUR_SEARCH to 40 ARTICLES that were
    PRIMARY_STUDIES . findings and originality : THE_MAJORITY of AUTHORS examined
    STUDENT_PERCEPTIONS of THEIR_LEARNING . one third investigated THE_USE of FLIPPED_LEARNING
    on THE_ACQUISITION and DEVELOPMENT of EFL_KNOWLEDGE , SKILLS and ABILITIES . that STUDENTS
    like LEARNING in A_FLIPPED_LEARNING_ENVIRONMENT is THE_STRONGEST_FINDING emerging . many
    linking it to THE_FACILITATION of SELF_REGULATED_LEARNING_BEHAVIORS . however ,
    RESEARCH_EVIDENCE for FLIPPED_LEARNING ' scontribution to IMPORTANT_EDUCATIONAL_OUTCOMES
    is not robust and this remains A_PROBLEM for UNDERSTANDING where or how to target
    THE_IMPACT or VALUE of THIS_PEDAGOGY . nonetheless , OTHER_ENCOURAGING_FINDINGS include
    that using FLIPPED_LEARNING to teach EFL was linked to ITS_CAPACITY to improve
    IDIOMATIC_KNOWLEDGE , ORAL_AND_WRITING_PERFORMANCE , MOTIVATION , and
    HIGHER_ORDER_THINKING_SKILLS . FUTURE_RESEARCH should FOCUS on improving RESEARCH_DESIGN
    and REPORTING for FLIPPED_LEARNING_INTERVENTIONS , and FOCUS on investigating
    KEY_EFL_LEARNING_SKILLS particularly reading which is comparatively understudied despite
    ITS_IMPORTANCE to LANGUAGE_ACQUISITION . value : THE_RESULTS clarify for EDUCATORS that
    FLIPPED_LEARNING ' scapacity to influence THE_ACQUISITION of KEY_LEARNING_SKILLS remains
    largely unproven . 2024 the author ( s ) . published by informa uk limited , trading as
    taylor and francis group .
    <BLANKLINE>


    >>> for i in range(10, 20):
    ...     print(textwrap.fill(mapping[i]["AB"], width=90))
    ...     print()
    purpose of the study : the article brings forward THE_DEFINITION , based on THE_ANALYSIS
    of both domestic and FOREIGN_SCIENTISTS ' views . STRUCTURE_COMPONENTS of BLENDED_LEARNING
    with ACCOUNT taken of UNIVERSITY_SPECIFIC_CHARACTER . methodology :
    BLENDED_LEARNING_PROCESS is presented as A_MODEL consisting of 9 SUCCESSIVE_STAGES , each
    of them represents A_LOGICAL_SEQUENCE of MEASURES ensuring THE_DYNAMICS of
    SYSTEM_DEVELOPMENT . results : the developed by THE_AUTHOR_MODEL result in
    THE_RECOMMENDATION to proceed to BLENDED_LEARNING which is conceptually based on
    THE_CONSTRUCTIVE_POTENTIAL of A_TEACHER , on searching WAYS of ITS_BUILDING on THE_BASIS
    of communicative , PERSON centered and INTERACTIVE_APPROACHES , increasing
    ORGANIZATIONAL_CHANGEABILITY of THE_EDUCATIONAL_ENVIRONMENT . applications of this study :
    this research can be used for THE_UNIVERSITIES , TEACHERS , and STUDENTS . novelty /
    originality of this study : in this research , THE_MODEL of THE_BLENDED_LEARNING in
    UNIVERSITY_EDUCATION is presented in A_COMPREHENSIVE_AND_COMPLETE_MANNER .
    ABROSIMOVA_ET_AL .
    <BLANKLINE>
    contribution : this article presents AN_EXPERIENCE_REPORT on THE_APPLICATION of
    FLIPPED_CLASSROOM ( FC ) to THE_LABORATORY_SESSIONS ( HENCEFORTH_LAB_SESSIONS ) of
    AN_UNDERGRADUATE_COMPUTER_SCIENCE_COURSE . background : HANDS on WORK in
    COMPUTER_SCIENCE_LAB_SESSIONS is typically preceded by TECHNICAL_INSTRUCTIONS on how to
    install , CONFIGURE , and use THE_SOFTWARE_AND_HARDWARE_TOOLS needed during THE_LAB . in
    THE_COURSE under STUDY , THIS_INITIAL_EXPLANATION took between 14 % and 50 % of
    THE_LAB_TIME , reducing drastically THE_TIME available for ACTUAL_PRACTICE . it was also
    observed that STUDENTS missing any of THE_LABS had TROUBLE catching up . intended outcomes
    : THE_APPLICATION of FC is expected to increase THE_TIME for HANDS_ON_ACTIVITIES , and
    improve STUDENTS ' PERFORMANCE and MOTIVATION . THIS_IMPROVEMENT is expected to be more
    noticeable in THOSE_STUDENTS who are unable to attend ALL_LAB_SESSIONS . application
    design : the study compares THE_APPLICATION of FC and A_TRADITIONAL_METHODOLOGY . it
    encompasses TWO_ACADEMIC_COURSES and involves 434 STUDENTS and SIX_LECTURERS . findings :
    THE_FC is suitable for LAB_SESSIONS in COMPUTER_SCIENCE . among OTHER_RESULTS , flipping
    THE_LABS resulted in 24 more minutes of PRACTICAL_AND_COLLABORATIVE_WORK on average at
    EACH_LAB_SESSION . it was observed A_SIGNIFICANT_IMPROVEMENT in THE_MOTIVATION of STUDENTS
    , with 9 out of every 10 STUDENTS preferring it over TRADITIONAL_METHODOLOGIES . also ,
    THE_FC made it much easier for STUDENTS to catch up after missing A_LAB , making
    THE_FINAL_GRADES less dependent on LAB_ATTENDANCE . 1963 2012 ieee .
    <BLANKLINE>
    background : THE_FLIPPED_CLASSROOM_METHOD requires that STUDENTS engage with HOMEWORK
    before coming to THE_CLASSROOM so_that CLASS_TIME can be spent on
    ACTIVE_AND_COLLABORATIVE_LEARNING_EXERCISES . RESEARCH has demonstrated that this can
    improve STUDENT_PERFORMANCE_VERSUS_TRADITIONAL_LECTURER led TEACHING_METHODS . objective :
    during the COVID_19_PANDEMIC , THE_VAST_MAJORITY of TEACHING has been entirely ONLINE
    such_that even in CLASS ' TIME has been virtual . THE_CURRENT_ARTICLE examined whether
    ONLINE_ONLY_DELIVERY affects THE_EFFICACY of THE_FLIPPED_CLASSROOM_APPROACH . method :
    GRADES for A_RESEARCH_METHODS and STATISTICS_MODULE and A_STATISTICS_PORTFOLIO_ASSIGNMENT
    were compared across CONSECUTIVE_COHORTS of UNDERGRADUATE_PSYCHOLOGY_STUDENTS taught by
    DIFFERENT_METHODS . results : OVERALL_GRADES on THE_MODULE did not differ significantly
    across TEACHING_METHODS but STUDENT_PERFORMANCE on STATISTICS_TESTS did .
    FLIPPED_CLASSROOMS , whether accompanied by on CAMPUS or SYNCHRONOUS_ONLINE_CLASSES , led
    to SIGNIFICANTLY_BETTER_PERFORMANCE than TRADITIONAL_METHODS . NO_DETRIMENT was observed
    by TEACHING entirely ONLINE . conclusion : THE_KEY_ADVANTAGES of
    THE_FLIPPED_CLASSROOM_METHOD appear driven by ACTIVE_LEARNING which can occur irrespective
    of CLASSROOM_CONTEXT . teaching implications : using FLIPPED_CLASSROOMS can be
    A_USEFUL_TOOL , particularly in SUBJECTS where STUDENTS may otherwise be less engaged with
    THE_CONTENT . the author ( s ) 2021 .
    <BLANKLINE>
    contribution : this work studies how to integrate MASSIVE_OPEN_ONLINE_COURSES ( MOOCS )
    into traditional , FACE_TO_FACE , UNDERGRADUATE_ENGINEERING_COURSES . background : MOOCS
    emerged as AN_INNOVATIVE_TREND in ONLINE_LEARNING with DISTINCTIVE_AND_ATTRACTIVE_FEATURES
    , such_as EASE_OF_ACCESS and COST_EFFECTIVENESS for LARGE_AUDIENCES . for_this_reason ,
    they have attracted A_LOT of ATTENTION for THEIR_POTENTIAL in contributing to
    GLOBAL_CHALLENGES in CONTEMPORARY_ENGINEERING_EDUCATION . however , THE_INTEGRATION of
    MOOCS into traditional , on CAMPUS_COURSES and PROGRAMS in HIGHER_EDUCATION remains
    AN_OPEN_PROBLEM . research question : what is THE_MOST_EFFECTIVE_MOOC_BLENDING_STRATEGY
    for traditional , on CAMPUS_ENGINEERING_PROGRAMS ? methodology : to answer THIS_QUESTION ,
    FIRST_A_LITERATURE_REVIEW was conducted on THE_UTILIZATION of MOOCS within
    FACE_TO_FACE_UNDERGRADUATE_EDUCATION . based on THIS_LITERATURE_REVIEW , this
    WORK_ADVOCATES for the mooc based flipped ( MBF ) CLASSROOM as THE_STRATEGY with
    THE_HIGHEST_POTENTIAL for MOOC_BASED_BLENDING . THE_MAIN_PEDAGOGICAL_AND_DESIGN_PRINCIPLES
    of THIS_METHODOLOGY are described and A_CASE_STUDY is presented on A_COHORT of STUDENTS (
    n= 23 ) enrolled in A_DIGITAL_SIGNAL_PROCESSING_COURSE within
    AN_UNDERGRADUATE_ELECTRONICS_ENGINEERING_PROGRAM . this is A_POSITION_PAPER based on
    EVIDENCE from THE_LITERATURE , but THE_CASE_STUDY is used to_illustrate how
    THE_MBF_DESIGN_PRINCIPLES can be implemented in PRACTICE . findings : THE_RESULTS suggest
    that THE_MBF_METHODOLOGY is A_GROWING_TREND in UNDERGRADUATE_ENGINEERING_EDUCATION with
    THE_POTENTIAL to FACILITATE_STUDENT ' SACTIVE_LEARNING in synchronous
    FACE_TO_FACE_SESSIONS while fostering the ADOPTION_AND_USAGE of MOOCS . 1963 2012 ieee .
    <BLANKLINE>
    introduction : THE_LAST_TWO_DECADES have seen A_SHIFT towards BLENDED_LEARNING in
    EDUCATION due_to TECHNOLOGICAL_ADVANCEMENTS . this study focuses on DENTAL_EDUCATION ,
    comparing TWO_BLENDED_LEARNING_MODELS enriched VIRTUAL_AND_FULLY_ONLINE_FLIPPED_CLASSROOM
    in_terms_of ACADEMIC_ACHIEVEMENT , aligning with THE_ASSOCIATION for DENTAL_EDUCATION in
    europe ' scompetencies . materials and methods : the research was modelled in
    A_QUANTITATIVE_DESIGN with A_PREPOST_TEST_CONTROL_GROUP_EXPERIMENTAL_DESIGN . the study
    was conducted at EGE_UNIVERSITY_FACULTY of DENTISTRY in TURKEY for 4 weeks with the
    experimental ( n = 44 ) and control ( n = 39 ) GROUPS divided into TWO_GROUPS by
    IMPARTIAL_ASSIGNMENT . to THE_EXPERIMENTAL_GROUP , THE_THEORETICAL_PART of THE_COURSE was
    tried to be conveyed before EACH_LESSON with VIDEO_LESSONS prepared with EDPUZZLE
    containing REINFORCEMENT_QUESTIONS and a question set consisting of CASE_QUESTIONS .
    THE_PRACTICAL_LEARNING_OBJECTIVES of THE_COURSE were tried to be gained through
    THE_DISCUSSION of THE_PREVIOUSLY_PRESENTED_CASE_QUESTIONS in THE_ONLINE_SYNCHRONOUS_COURSE
    . as TOOLS for collecting DATA , A_UNIQUE_ACADEMIC_ACHIEVEMENT_TEST ,
    A_COURSE_EVALUATION_FORM and A_SEMI_STRUCTURED_QUALITATIVE_DATA_COLLECTION_FORM were used
    . results : it was seen that THE_FLIPPED_CLASSROOM_MODEL had A_MORE_POSITIVE_EFFECT on
    STUDENTS ' ACADEMIC_ACHIEVEMENT than THE_ENRICHED_VIRTUAL_CLASSROOM_MODEL .
    THE_GENERAL_SATISFACTION_LEVELS of THE_PARTICIPANTS regarding THESE_TWO_MODELS are also
    higher in FAVOUR of THE_FLIPPED_CLASSROOM_MODEL . conclusion : this study provides
    SIGNIFICANT_FINDINGS for EDUCATIONAL_INSTITUTIONS , POLICYMAKERS and EDUCATORS about
    THE_IMPACT of FULLY_ONLINE_TEACHING_METHODS on ACADEMIC_ACHIEVEMENT . in THIS_CONTEXT ,
    THE_FLIPPED_CLASSROOM_METHOD can be preferred both in CASES where EDUCATION is blocked and
    in DENTAL_EDUCATION_INSTITUTIONS that want to ENSURE_DIGITAL_TRANSFORMATION efficiently
    and partially remotely . 2023 JOHN_WILEY and SONS_A_/_S . published by john wiley and sons
    ltd .
    <BLANKLINE>
    background and objective : THE_FLIPPED_CLASSROOM ( FC ) approach has become increasingly
    predominant and popular in MEDICAL_EDUCATION . this study aimed to explore THE_USEFULNESS
    and THE_SCOPE of FC based on MEDICAL_STUDENTS ' experience , with
    THEIR_ADAPTATION_CHALLENGES . methods : THE_PRESENT_STUDY was A_MIXED_METHOD accomplished
    during THE_ACADEMIC_YEARS 2019 20 , involving FOURTH_YEAR_STUDENTS at THE_COLLEGE of
    MEDICINE in RIYADH , SAUDI_ARABIA . A_SELF_ADMINISTERED_QUESTIONNAIRE was used to seek
    THEIR_FIRST_EXPERIENCE and OPINION of THE_FC . results : A_TOTAL of 234 QUESTIONNAIRES
    were distributed to THE_STUDENTS , and 214 STUDENTS completed THE_SURVEY ( RESPONSE_RATE
    of 91.45 % ) . out of THIS_TOTAL , 68.2 % were MALES and 31.8 % were FEMALES . most of
    THE_STUDENTS agreed 156 ( 72.9 % ) that THE_FLIPPED_CLASSROOM was more engaging than
    THE_TRADITIONAL_LECTURE , among them 100 ( 68.5 % ) MALES and 56 ( 82.3 ) FEMALES agreed .
    almost ~79 % of STUDENTS liked FC as it enabled them knowing THE_MATERIAL in ADVANCE , and
    THE_CLASS_TIME was spent clarifying THE_FACTS and PRINCIPLES with ACTIVE_INTERACTION , as
    commented during FOCUS_GROUP_DISCUSSION_MORE_CHANCE for discussing with THE_DOCTORS , and
    i got THE_CHANCE to answer ( st . 6 ) . conclusion : THE_RESULTS showed THAT_THE_STUDENTS
    like THE_FC more than THE_CONVENTIONAL_CLASSROOM . SUGGESTIONS were given by STUDENTS to
    improve THE_ACTIVE_LEARNING_SESSIONS within THE_FC_MODALITY . 2022 , professional medical
    publications . all rights reserved .
    <BLANKLINE>
    introduction : the COVID_19_PANDEMIC has led to THE_CREATION of
    DIFFERENT_TEACHING_ADAPTATIONS shared in HEALTH_DEGREES , such_as BLENDED_TEACHING_METHODS
    , including FACE_TO_FACE_LEARNING combined with ONLINE_LEARNING . objectives :
    ONE_OBJECTIVE was to compare THE_ACADEMIC_PERFORMANCE_SCORES aligned to
    WORKED_COMPETENCIES during PHYSIOTHERAPY_INTERNSHIPS between TWO_GROUPS : one exposed to
    A_BLENDED_LEARNING_EDUCATIONAL_MODEL and another exposed to a FACE_TO_FACE_TEACHING system
    during INTERNSHIPS . ANOTHER_OBJECTIVE was to STUDY_THE_CORRELATION of THE_MARKS of the
    following year ' SINTERNSHIP_SUBJECT . design : ANALYTICAL_STUDY of RETROSPECTIVE_COHORTS
    . SETTINGS : PHYSIOTHERAPY_UNIVERSITY_DEGREE_PROGRAM . participants :
    THREE_HUNDRED_STUDENTS working towards attaining PHYSIOTHERAPY_DEGREES . methods :
    TWO_GROUPS were studied : THE_NON_EXPOSED_COHORT , which had 100 % FACE_TO_FACE_ATTENDANCE
    at THE_CLINICAL_CENTER , and THE_EXPOSED_COHORT , which experienced B_LEARNING and had 50
    % ATTENDANCE at THE_CLINICAL_PRACTICE_CENTER and 50 % COMPLETION of
    ASYNCHRONOUS_ONLINE_COMPLEMENTARY_TRAINING during LOCKDOWN . results : THE_RESULTS show
    that both in THE_EXPOSED_COHORT and in THE_NON_EXPOSED_COHORT , the qualifications and ,
    therefore , THE_COMPETENCE_DEVELOPMENT achieved by THE_STUDENTS were similar .
    A_STRONGER_CORRELATION with SKILLS_ACTIVITIES developed in THE_EXPOSED_COHORT in RELATION
    to THE_FINAL_MARK of the following year ' SINTERNSHIP_SUBJECT has been found . discussion
    and conclusions : for ALL_THE_COMPETENCIES developed during CS_II , PARTICIPANTS obtained
    THE_SAME_GRADES in BOTH_GROUPS , so it is concluded that THE_ONLINE_ACTIVITIES implemented
    during CONFINEMENT mixed with FACE_TO_FACE_TEACHING were useful for THE_ACHIEVEMENT of
    THESE_SKILLS . thus , B_LEARNING is A_GOOD_METHOD for developing
    CLINICAL_PRACTICE_COMPETENCIES in PHYSIOTHERAPY_STUDENTS . CONTRIBUTION of THE_PAPER :
    BLENDED_TEACHING ( B_TEACHING ) is useful for developing INTERNSHIP_COMPETENCIES . it is
    necessary to align THE_ACTIVITIES developed in INTERNSHIPS with THE_EVALUATED_SKILLS .
    2023 by the authors .
    <BLANKLINE>
    purpose : this study aims to explore THE_PERCEPTIONS of ACCOUNTANCY_STUDENTS on the
    USE_OF_TECHNOLOGY , BLENDED_LEARNING and FLIPPED_CLASSROOM in
    TWO_EMERGING_UK_HIGHER_EDUCATION_INSTITUTIONS ( HEIS ) . design / methodology / approach :
    THE_PRIMARY_DATA for the study were collected using A_QUESTIONNAIRE_SURVEY and
    descriptively analysed . findings : the findings revealed that there is some
    USE_OF_TECHNOLOGY in_terms_of THE_BLACKBOARD and POWERPOINT_PRESENTATIONS but BLOGS and
    WIKIS have VERY_LIMITED_USE . AN_ASPECT that does not seem to be integrated fully yet is
    THE_USE of BLENDED_TECHNOLOGY and A_FLIPPED_CLASSROOM . practical implications : the study
    FINDINGS offer A_PICTURE of HOW_TECHNOLOGY , BLENDED_LEARNING and
    THE_FLIPPED_CLASSROOM_TECHNIQUE were utilised with ACCOUNTANCY_STUDENTS prior_to
    THE_CORONAVIRUS_DISEASE 2019 ( covid 19 ) PANDEMIC . THIS_INFORMATION is valuable for
    ACCOUNTING_EDUCATORS and by EXTENSION to OTHER_ASPECTS of BUSINESS_STUDIES_DISCIPLINES in
    providing A_COMPARISON between the PRE_COVID 19 scenario and the current one and thus
    enabling an evaluation of advancement in the application of these teaching strategies
    as_a_result of the pressure imposed by SOCIAL_DISTANCING . SUCH_INTELLIGENCE will
    facilitate THE_IDENTIFICATION of AREAS where enhancing LEARNING_OUTCOMES has been possible
    and point to OPPORTUNITIES for IMPROVED_STUDENT_EXPERIENCE . originality / value : where
    covid 19 brought about SIGNIFICANT_STRUCTURAL_CHANGE in TEACHING_AND_LEARNING in
    THE_HE_ENVIRONMENT , this study represents a PRE_COVID 19 CONSIDERATION of
    STUDENT_PERCEPTIONS on BLENDED_LEARNING and FLIPPED_CLASSROOM . THIS_STUDY thus has
    THE_POTENTIAL to anchor FUTURE_RELEVANT_STUDIES that consider the POST_COVID 19
    environment . 2023 , emerald publishing limited .
    <BLANKLINE>
    purpose : in the era of INDUSTRY 4.0 , THE_RELEVANCE of WEBINAR_TUTORIALS , A_FORM of
    DISTANCE_LEARNING , is paramount . THESE_TUTORIALS can catalyze SELF_REGULATED_LEARNING ,
    CRITICAL_THINKING_AND_COMMUNICATION_SKILLS , especially for
    PROSPECTIVE_AND_IN_SERVICE_TEACHERS pursuing HIGHER_EDUCATION . this paper aims to develop
    A_CONCEPTUAL_FRAMEWORK and REPORT_THE_RESULTS of implementing A_FLIPPED_CLASSROOM with
    WHITEBOARD_ANIMATION and MODULES . THIS_INNOVATIVE_APPROACH seeks to ENHANCE_STUDENTS '
    SELF_REGULATION , CRITICAL_THINKING_AND_COMMUNICATION_ABILITIES . design / methodology /
    approach : this study employs A_MIXED_METHODS_APPROACH . in THE_FIRST_PHASE ,
    A_HYPOTHETICAL_MODEL and CONCEPTUAL_FRAMEWORK for THE_FLIPPED_CLASSROOM with
    WHITEBOARD_ANIMATION and MODULES were developed to ENHANCE_SELF_REGULATION ,
    CRITICAL_THINKING_AND_COMMUNICATION_SKILLS . THE_RESULTING_CONCEPTUAL_FRAMEWORK was then
    implemented through A_QUASI_EXPERIMENT using A_NON_EQUIVALENT_CONTROL_GROUP_DESIGN
    involving 83 ELEMENTARY_SCHOOL_TEACHERS enrolled in
    THE_ELEMENTARY_SCHOOL_SCIENCE_EDUCATION_COURSE ( pdgk4202 ) , divided into
    THREE_TREATMENT_GROUPS . QUALITATIVE_DATA were collected through OBSERVATIONS of
    THE_LEARNING_PROCESS , DOCUMENTATION of STUDENT_WORKSHEET_COMPLETION and INTERVIEWS with
    STUDENTS . QUESTIONNAIRES and TESTS were used as INSTRUMENTS for
    QUANTITATIVE_DATA_COLLECTION . QUALITATIVE_DATA were analyzed using DESCRIPTIVE_METHODS ,
    while QUANTITATIVE_DATA were evaluated using MANCOVA . findings : the findings demonstrate
    SIGNIFICANT_IMPROVEMENTS in STUDENTS ' SELF_REGULATION , CRITICAL_THINKING_SKILLS and
    COMMUNICATION_ABILITIES after implementing THE_FLIPPED_CLASSROOM with WHITEBOARD_ANIMATION
    and MODULES . research limitations / implications : SOME_LIMITATIONS in this study need to
    be recognized . THESE_LIMITATIONS include THE_SPECIFIC_SAMPLE_TYPE of
    ELEMENTARY_SCHOOL_TEACHERS who went back to COLLEGE to take SCIENCE_LEARNING_COURSES in
    ELEMENTARY_SCHOOL . TEACHERS have VARIOUS_DIVERSITY that may affect THE_DEPENDENT_VARIABLE
    , such_as AGE , EDUCATIONAL_BACKGROUND , FACILITIES , INTERNET_SIGNAL_STABILITY at
    THEIR_LEARNING_LOCATION and TEACHING_EXPERIENCE . this study was conducted in
    A_SPECIFIC_CONTEXT ( using THE_FLIPPED_CLASSROOM_MODEL at UT ) , so THE_RESULTS may need
    to be more generalizable to other EDUCATIONAL_CONTEXTS with DIFFERENT_FACILITIES , SYSTEMS
    and POLICIES . in_addition , THE_MEASUREMENT of SELF_REGULATION_AND_COMMUNICATION_SKILLS ,
    particularly with QUESTIONNAIRES , relies on SELF_REPORT , which can be biased due_to
    SOCIALLY_DESIRABLE_RESPONSES or INACCURATE_SELF_ASSESSMENT . although THE_MANCOVA_TEST
    showed SIGNIFICANT_RESULTS , it is possible that OTHER_VARIABLES not controlled for in
    this study ( e . g . INTRINSIC_MOTIVATION , SOCIAL_SUPPORT from FAMILY or COLLEAGUES )
    also affected THE_INDEPENDENT_VARIABLES . practical implications : this study emphasizes
    THE_IMPORTANCE of ADAPTING_WEBINAR_TUTORIALS for INDUSTRY 4.0 and enhancing
    SELF_REGULATED_LEARNING , CRITICAL_THINKING_AND_COMMUNICATION_SKILLS , particularly for
    WORKING_STUDENTS and TEACHERS . it offers A_PRACTICAL_FRAMEWORK for EDUCATORS and
    SUGGESTS_WAYS to improve ONLINE_LEARNING_MATERIALS . THE_IMPLEMENTATION_RESULTS show
    SIGNIFICANT_SKILL_ENHANCEMENT . THESE_FINDINGS have PRACTICAL_IMPLICATIONS for EDUCATORS ,
    INSTITUTIONS and INSTRUCTIONAL_DESIGNERS , guiding THE_DEVELOPMENT of
    EFFECTIVE_DISTANCE_LEARNING_STRATEGIES and CURRICULUM_IMPROVEMENTS in THE_DIGITAL_AGE .
    social implications : THE_SOCIAL_IMPLICATIONS of THIS_STUDY are noteworthy . in the
    context of INDUSTRY 4.0 , ADAPTING_WEBINAR_TUTORIALS to promote SELF_REGULATED_LEARNING ,
    CRITICAL_THINKING_AND_COMMUNICATION_SKILLS is essential not only for
    THE_EDUCATIONAL_SECTOR but also for THE_BROADER_SOCIETY . it equips
    PROSPECTIVE_AND_IN_SERVICE_TEACHERS , who are pivotal in shaping FUTURE_GENERATIONS , with
    THE_NECESSARY_SKILLS to navigate A_RAPIDLY_CHANGING_DIGITAL_LANDSCAPE . furthermore ,
    enhancing SELF_REGULATION and CRITICAL_THINKING_ABILITIES among employed
    STUDENTS_CONTRIBUTES to A_MORE_INFORMED_AND_ADAPTABLE_WORKFORCE , fostering
    SOCIETAL_RESILIENCE in THE_FACE of TECHNOLOGICAL_ADVANCEMENTS . originality / value :
    THE_UNIQUENESS of THIS_STUDY stems from THE_CREATIVE_MODIFICATION of A_WEBINAR_TUTORIAL ,
    which specifically targets THE_URGENT_REQUIREMENT for enhancing ABILITIES among TEACHERS
    and UNIVERSITY_STUDENTS . THE_CONCEPTUAL_FRAMEWORK serves as A_VALUABLE_TOOL for EDUCATORS
    , and THE_FINDINGS of THIS_STUDY confirm ITS_EFFECTIVENESS in enhancing SELF_REGULATION ,
    CRITICAL_THINKING_ABILITIES and COMMUNICATION_PROFICIENCY . furthermore ,
    THE_RECOMMENDATIONS offered also furnish PRACTICAL_INSIGHTS to improve THIS_MODEL . 2024 ,
    GEDE_SUWARDIKA , AGUS_TATANG_SOPANDI , i . PUTU_OKTAP_INDRAWAN and KADEK_MASAKAZU .
    <BLANKLINE>
    background : BLENDED_LEARNING is being integrated into UNDERGRADUATE_NURSING_EDUCATION at
    ALL_LEVELS and from ALL_DIRECTIONS . COGNITIVE_ENGAGEMENT is not only an embodiment and
    guarantee of STUDENTS ' ENGAGEMENT into THE_CURRICULUM from A_COGNITIVE_LEVEL ,
    DEEP_ENGAGEMENT and HIGH_LEVEL_THINKING , but also an IMPORTANT_INDICATOR of whether
    STUDENTS are effectively engaged in THE_BLENDED_LEARNING_CURRICULA . however , NO_STUDIES
    have been seen to investigate THE_COGNITIVE_ENGAGEMENT of NURSING_UNDERGRADUATES in
    THE_BLENDED_LEARNING_CURRICULA and ITS_INFLUENTIAL_FACTORS . objectives : to explore
    NURSING_UNDERGRADUATES ' COGNITIVE_ENGAGEMENT during THE_BLENDED_LEARNING_CURRICULA and
    ITS_INFLUENTIAL_FACTORS . design : A_CONVERGENT_PARALLEL_MIXED_METHODS was used . DATA
    were collected between NOVEMBER 2021 and may 2022 , inclusive . settings and participants
    : the study was carried out in THE_NURSING_SCHOOL at A_UNIVERSITY in CHINA . PARTICIPANTS
    including STUDENTS undertaking ENTRY to THE_BLENDED_LEARNING_CURRICULA . methods : in
    THE_QUANTITATIVE_COMPONENT ( n = 142 ) , PARTICIPANTS ' COGNITIVE_ENGAGEMENT was
    investigated and FACTORS associated with it were examined using UNIVARIATE_ANALYSIS ,
    CORRELATION_ANALYSIS and MULTIPLE_REGRESSION_ANALYSIS . during_this_period , personal ,
    SEMI_STRUCTURED_INTERVIEWS were conducted with A_SUBSET of THESE_PARTICIPANTS ( n = 15 )
    to understand PARTICIPANTS ' COGNITIVE_ENGAGEMENT_EXPERIENCES . results :
    THE_COGNITIVE_ENGAGEMENT of NURSING_UNDERGRADUATES was at A_MODERATE_LEVEL and
    THE_COGNITIVE_ENGAGEMENT_EXPERIENCES were reflected in THE_FOUR_THEMES of RECONSTITUTION ,
    CONNECTION , ELABORATION and RETENTION . THE_INFLUENTIAL_FACTORS of COGNITIVE_ENGAGEMENT
    were LEARNING_ACTIVITIES ( = 0.226 , p = 0.004 ) , autonomy ( = 0.158 , p = 0.047 ) ,
    ACADEMIC_SELF_EFFICACY ( = 0.311 , p < 0.001 , = 0.271 , p < 0.001 ) and
    SOCIAL_INTERACTION ( = 0.358 , p < 0.001 ) . conclusions : THE_COGNITIVE_ENGAGEMENT of
    NURSING_UNDERGRADUATES in THE_BLENDED_LEARNING_CURRICULA_NEEDS to be improved . to
    maximize PROMOTE_COGNITIVE_ENGAGEMENT of NURSING_UNDERGRADUATES in
    THE_BLENDED_LEARNING_CURRICULA , EDUCATORS should DESIGN_DIVERSE_LEARNING_ACTIVITIES ,
    engage in HIGH_QUALITY_SOCIAL_INTERACTIONS with STUDENTS , and MAXIMIZE_STUDENTS '
    autonomy and SELF_EFFICACY . 2023 elsevier ltd
    <BLANKLINE>


    >>> for i in range(20, 30):
    ...     print(textwrap.fill(mapping[i]["AB"], width=90))
    ...     print()
    context : TEAM_BASED_LEARNING ( TBL ) is A_FLIPPED_CLASSROOM_APPROACH requiring STUDENTS
    to STUDY before CLASS . FULLY_FLIPPED_CURRICULA usually have fewer in CLASS_HOURS .
    however , for PRACTICAL_REASONS , SEVERAL_PROGRAMS implement A_FEW_WEEKS of TBL without
    adjusting THE_SEMESTER_TIMETABLE . STUDENTS fear that they will be overloaded by
    THE_INDIVIDUAL_AND_COLLABORATIVE_STUDY_HOURS needed to prepare for TBL . methods : we
    implemented THREE_CONSECUTIVE_WEEKS of TBL in a 15 WEEK_LECTURE based COURSE on
    THE_RENAL_SYSTEM . in CLASS_TIME and ASSESSMENTS were unchanged for ALL_COURSES .
    FOUR_HUNDRED_FIFTY_NINE_FIRST_YEAR_UNDERGRADUATE_MEDICAL_STUDENTS ( 229 in 2018 . 230 in
    2019 ) were invited to COMPLETE_WEEKLY_LOGS of
    THEIR_INDIVIDUAL_AND_COLLABORATIVE_STUDY_HOURS during LECTURES and TBL , along_with
    QUESTIONNAIRES on COGNITIVE_LOAD and PERCEPTION of THE_COURSE . OUR_PROGRAM changed from a
    to e grading in 2018 to PASS_FAIL_GRADING in 2019 RESULTS : PARTICIPANTS ( n = 324 ) spent
    A_SIMILAR_NUMBER of HOURS studying for TBL_VS . LECTURES with A_MEAN of 3.1 H_/_WEEK .
    COLLABORATIVE_STUDY was MINIMAL_OUTSIDE_CLASS ( MEDIAN 0.1 H_/_WEEK ) . RESULTS remained
    similar with PASS_FAIL_GRADING . if in CLASS_TIME were reduced , 18 % of PARTICIPANTS said
    they would have used freed up TIME to STUDY for TBL . studying for TBL generated
    SIMILAR_EXTRANEOUS_COGNITIVE_LOAD and LOWER_INTRINSIC_LOAD compared to studying for
    LECTURES . STUDENTS were less stressed , and maintained HIGH_LEVELS of MOTIVATION and
    SELF_PERCEIVED_LEARNING . conclusions : THREE_WEEKS of LECTURES were replaced by TBL
    without reducing in CLASS_TIME . STUDENTS did not REPORT_OVERLOAD in STUDY_HOURS or in
    COGNITIVE_LOAD . 2021 , international association of medical science educators .
    <BLANKLINE>
    aim : this paper describes and discusses THE_DEVELOPMENT and IMPLEMENTATION of
    SEQUENTIAL_BLENDED_LEARNING_STRATEGIES in ONE_AUSTRALIAN_POST_GRADUATE_NURSING_PROGRAM
    designed to SUPPORT_STUDENT_TRANSITION to THE_NURSE_PRACTITIONER ( NP ) role . background
    : despite THE_AVAILABILITY of NP_PRACTICE_STANDARDS and ROLE_DESCRIPTIONS , THE_DIVERSITY
    and COMPLEXITY of NP_PRACTICE can make it difficult for STUDENTS commencing
    POST_GRADUATE_NP_PROGRAMS to comprehend WHAT_WAYS they need to develop to meet
    PROFESSIONAL_EXPECTATIONS . scholarly critique : this paper examines
    THIS_CONTEMPORARY_POST_GRADUATE_EDUCATION_ISSUE . BLENDED_LEARNING_STRATEGIES provided
    AN_OPPORTUNITY to address THE_REQUIREMENTS , DIVERSITY and COMPLEXITY of NP_PRACTICE early
    in THE_NP_PROGRAM . STUDENTS were confronted with THE_GAP between THEIR_CURRENT_LEVEL of
    COMPETENCE and NP_COMPETENCE , and supported to plan and travel
    THE_TRANSITIONAL_AND_DEVELOPMENTAL_PATHWAY to achieve COMPETENCE . conclusion : working
    with STUDENTS from early on in THEIR_DEGREE enables them to progressively and more clearly
    envision THE_GAP between THEIR_CURRENT_LEVEL of COMPETENCE and that required of
    THE_AUSTRALIAN_NP_ROLE . adopting A_SEQUENTIAL_BLENDED_LEARNING_APPROACH is ONE_WAY to
    engage STUDENTS in preparing for THEIR_FUTURE_ROLE . CONSIDERATION of
    DESIGN_ELEMENTS_INTEGRAL to BLENDED_LEARNING_APPROACHES is important , including A_NEED
    for AUTHENTICITY and SUPPORT . preparing nps who fully comprehend THE_NATURE and SCOPE of
    THEIR_PRACTICE is both vital for SAFETY and of STRATEGIC_IMPORTANCE to
    THE_NURSING_PROFESSION . EXAMPLES of how to FACILITATE_STUDENT_UNDERSTANDING of
    THE_NP_ROLE are needed to inform EDUCATIONAL_PRACTICE . 2015 australian college of nursing
    ltd .
    <BLANKLINE>
    objective : the_aim_of THIS_RESEARCH is to evaluate THE_IMPLEMENTATION of
    THE_FLIPPED_CLASSROOM and COLLABORATIVE_WORK in UNIVERSITY_MARKETING_STUDENTS ,
    in_terms_of ACADEMIC_PERFORMANCE , THE_DEVELOPMENT of CROSS_CURRICULAR_COMPETENCIES ,
    STUDENT_SATISFACTION and MOTIVATION , and THE_EFFECTIVE_USE of
    INFORMATION_AND_COMMUNICATION_TECHNOLOGIES in THE_LEARNING_PROCESS . theoretical framework
    : THE_MAIN_CONCEPTS and ACADEMIC_LITERATURE that underpin THE_RESEARCH are presented ,
    providing A_SOLID_FOUNDATION for UNDERSTANDING_THE_CONTEXT of the study . method :
    THE_METHODOLOGY adopted for THIS_RESEARCH is quantitative in NATURE , with
    A_CROSS_SECTIONAL_DESIGN , and EXPLORATORY_AND_DESCRIPTIVE_SCOPE . DATA_COLLECTION was
    conducted using A_QUESTIONNAIRE composed of FIVE_DIMENSIONS , in_order_to cover
    ALL_ASPECTS inherent to THE_MIXED_INCLUSIVE_STRATEGY that combines THE_FLIPPED_CLASSROOM
    and COLLABORATIVE_WORK in THE_UNIVERSITY_CLASSROOM . results and discussion : THE_RESULTS
    suggest that THE_FLIPPED_CLASSROOM and COLLABORATIVE_WORK have A_GENERALLY_POSITIVE_IMPACT
    on HIGHER_EDUCATION , in LINE with much of THE_CURRENT_SCIENTIFIC_LITERATURE . however ,
    it is also evident that CAREFUL_CONSIDERATION of IMPLEMENTATION and CONTEXT is necessary
    to maximize THEIR_EFFECTIVENESS . VARIATIONS in OUTCOMES , depending on FACTORS such_as
    DISCIPLINE , COURSE_DESIGN , and THE_DIGITAL_SKILLS of THE_PARTICIPANTS , are
    CRUCIAL_ASPECTS that must be considered . THESE_FINDINGS underline THE_IMPORTANCE of
    A_BALANCED_AND_ADAPTIVE_APPROACH in THE_APPLICATION of INNOVATIVE_METHODOLOGIES in
    HIGHER_EDUCATION . originality / value : THIS_STUDY stands out for
    ITS_RIGOROUS_EXPLORATION of how THE_INTEGRATION of THE_FLIPPED_CLASSROOM and
    COLLABORATIVE_WORK in HIGHER_EDUCATION enhances SOFT_SKILLS and ACADEMIC_PERFORMANCE ,
    contrasting with TRADITIONAL_METHODOLOGIES . it underscores THE_RELEVANCE of adapting
    EDUCATIONAL_STRATEGIES to maximize THE_EFFECTIVENESS of ICT in
    A_CONTEMPORARY_AND_DIVERSIFIED_LEARNING_CONTEXT . ITS_VALUE lies in providing
    EMPIRICAL_EVIDENCE that supports THE_IMPLEMENTATION of THESE_INNOVATIVE_METHODOLOGIES ,
    promoting MORE_INCLUSIVE_AND_EFFECTIVE_LEARNING_ENVIRONMENTS . 2024 anpad associacao
    nacional de pos graduacao e pesquisa them administracao . all rights reserved .
    <BLANKLINE>
    purpose : this paper aims to investigate HOW_MIXED_REALITY ( MR ) can be used to
    ENHANCE_INCLUSIVITY in SYNCHRONOUS_WORKING_ACTIVITIES where GROUPS of PEOPLE may be
    present either FACE_TO_FACE or ONLINE focusing_on BLENDED_LEARNING in THE_HIGHER_EDUCATION
    ( he ) CONTEXT . design / methodology / approach : in A_RESEARCH_METHODS_MODULE , 140
    UNIVERSITY_MASTER ' SLEVEL_STUDENTS were given THE_OPTION to attend and engage in
    SEMINARS_/_PRACTICAL_SESSIONS either in A_REAL_LECTURE_ROOM or ONLINE through
    A_VIRTUAL_VERSION of AN_EQUIVALENT_ENVIRONMENT , accessible on EVERYDAY_DEVICES .
    THE_MR_PLATFORM provided TWO_WAY_VIDEO_WINDOWS enabling ALL_STUDENTS on THE_MODULE to
    freely interact with STAFF and THEIR_PEERS . ATTENDANCE was recorded throughout
    THE_SEMESTER and SURVEY_DATA was captured after_all SESSIONS ( 33 % RESPONSE_RATE ) .
    in_addition , STUDENT_ACTIVITY was VIDEO recorded within BOTH_THE_REAL_AND_VIRTUAL_SPACES
    . findings : ATTENDANCE was high throughout THE_SEMESTER and STUDENTS were very positive
    about THIS_NOVEL_APPROACH to THEIR_EDUCATION . STUDENTS chose to either engage purely in
    PERSON , ONLINE or as A_MIXTURE of the two . PERFORMANCE on THE_MODULE was not impacted by
    THIS_DECISION . THE_SURVEY highlighted SEVERAL_FACTORS that impacted on STUDENTS ' choice
    of LEARNING_SPACE , including those related to INTRINSIC_CHARACTERISTICS of
    INDIVIDUAL_STUDENTS ( e . g . desire for TRADITIONAL_/_NOVEL_SOCIAL_INTERACTIONS ) and
    those related to EXTRINSIC_INFLUENCES ( e . g . WEATHER and TRAVEL_DEMANDS ) .
    VIDEO_ANALYSIS revealed NUMEROUS_DIFFERENCES in THE_BEHAVIOURS exhibited across
    THE_VIRTUAL_AND_REAL_SPACES , related to INDIVIDUAL_VERSUS_TEAM_MENTALITIES . practical
    implications : CONCLUSIONS are drawn regarding how MR can be used in he and
    POTENTIALLY_OTHER_WORK related CONTEXTS to ENHANCE_ENGAGEMENT , a SENSE_OF_COMMUNITY and
    ultimately LEARNING_/_PRODUCTIVITY_OUTCOMES . originality / value : THIS_STUDY
    investigated how a large ( > 100 ) cohort of STUDENTS responded to
    AN_MR_BLENDED_LEARNING_EXPERIENCE across A_WHOLE_SEMESTER . in_this_respect , to the best
    of THE_AUTHOR ' sknowledge , this is THE_FIRST_STUDY to consider SUCH_ISSUES at_this scale
    in A_UNIVERSITY_EDUCATION_SETTING . 2024 , emerald publishing limited .
    <BLANKLINE>
    introduction : THE_CURRENT_STUDY was conducted to compare THE_EFFECTS of
    THE_LECTURE_METHOD of TEACHING and THE_FLIPPED_CLASSROOM_MODEL based on bloom ' staxonomy
    of EDUCATIONAL_OBJECTIVES on THE_TEACHING of ENDODONTICS_CURRICULUM to
    UNDERGRADUATE_STUDENTS majoring in STOMATOLOGY , and to develop
    A_STANDARDIZED_TEACHING_PROCESS based on THE_FLIPPED_CLASSROOM_MODEL . materials and
    methods : A_STANDARDIZED_FLIPPED_CLASSROOM_MODEL based on bloom ' staxonomy of
    EDUCATIONAL_OBJECTIVES was established . TWO_GROUPS of UNDERGRADUATE_STUDENTS majoring in
    STOMATOLOGY received INSTRUCTION in A_PORTION of THE_ENDODONTICS_CURRICULUM using
    EITHER_THE_LECTURE_METHOD or FLIPPED_CLASSROOM model of TEACHING .
    A_TEACHING_QUESTIONNAIRE was administered to evaluate THE_STUDENTS ' mastery of
    THEORETICAL_KNOWLEDGE , UNDERSTANDING of LEARNING_OBJECTIVES , SATISFACTION of
    TEACHING_METHOD , and LEARNING_INTEREST . the spss 26.0 software was used for
    STATISTICAL_ANALYSIS , and THE_T_TEST was used to compare THE_DIFFERENCES between
    THE_TWO_GROUPS . results : both LEARNING_MODEL_COHORTS filled out
    ASSESSMENT_QUESTIONNAIRES upon COMPLETION of THE_PILOT_CURRICULUM . compared with
    THE_RESPONSES from STUDENTS in THE_LECTURE based GROUP , THE_SELF_RATING of
    THEORETICAL_KNOWLEDGE reported by STUDENTS in THE_FLIPPED_CLASSROOM_COHORT increased by
    10.9 % , from 7.1 0.8 to 7.9 0.7 ( t = 2.912 , p < 0.006 ) . STUDENTS ' TEST_SCORES in
    THE_FLIPPED_CLASSROOM_GROUP increased by 17.1 % , from 7.0 0.8 to 8.2 0.7 ( t = 4.284 , p
    < 0.001 ) . STUDENTS ' UNDERSTANDING of IDEOLOGICAL_AND_HUMANISTIC_OBJECTIVES as_well_as
    MEDICAL_ETHICS were both significantly improved by 11.4 % ( t = 2.267 , p = 0.009 ) and
    13.9 % ( t = 2.600 , p = 0.014 ) , respectively . STUDENTS ' SATISFACTION with
    THE_TEACHING_MODEL and CLASS_DURATION increased significantly , by 11.1 % ( t = 2.782 , p
    = 0.009 ) and 14.3 % ( t = 2.449 , p < 0.020 ) , respectively . STUDENTS '
    LEARNING_INTEREST increased by 17.1 % ( t = 3.101 , p = 0.004 ) . THE_LENGTH of STUDY_TIME
    prior_to CLASS under THE_FLIPPED_CLASSROOM_MODEL was longer than when using
    THE_TRADITIONAL_LECTURE_METHOD ( t = 3.165 , p = 0.003 ) , but THE_FLIPPED_CLASSROOM_MODEL
    shortened REVIEW_TIME after CLASS ( t = 4.038 , p = 0.001 ) . STUDENTS ' self reported
    UNDERSTANDING of TEACHING_OBJECTIVES improved by 8.3 % ( t = 1.762 , p = 0.083 ) , and
    SATISFACTION with THE_PREVIEW_METHOD and CURRICULUM increased by 8.1 % ( t = 1.804 , p =
    0.081 ) and 11.1 % ( t = 1.861 , p = 0.072 ) , respectively . there was
    NO_STATISTICALLY_SIGNIFICANT_DIFFERENCE between THE_TWO_GROUPS . conclusions :
    THE_FLIPPED_CLASSROOM_TEACHING_MODEL based on bloom ' staxonomy of EDUCATIONAL_OBJECTIVES
    , combined with HUMANISTIC_TEACHING_OBJECTIVES , can improve THE_EFFICACY of INSTRUCTION ,
    and merits popularizing and applying in THE_TEACHING of UNDERGRADUATE_STUDENTS majoring in
    STOMATOLOGY . copyright 2025 wei and peng .
    <BLANKLINE>
    background : SOCIAL_PSYCHOLOGY has A_VERY_IMPORTANT_ROLE in analyzing INDIVIDUAL_BEHAVIOR
    , GROUP_BEHAVIOR and INTERPERSONAL_RELATIONSHIPS . based on THE_ANALYSIS of
    SOCIAL_PSYCHOLOGY and UNIVERSITY_STUDENTS ' AVERSION_TO_LEARNING , the study proposes
    A_FLIPPED_CLASSROOM_CIVICS_TEACHING_MODEL , and analyzes in DEPTH_THE_EFFECT of THE_MODEL
    on STUDENTS ' AVERSION_TO_LEARNING . subjects and methods : the study selected
    UNIVERSITY_STUDENTS from FIVE_UNIVERSITIES as THE_RESEARCH_SUBJECTS to analyses THE_EFFECT
    of THE_FLIPPED_CLASSROOM_CIVICS_TEACHING_MODEL combined with SOCIAL_PSYCHOLOGY on STUDENTS
    ' AVERSION_TO_LEARNING . THE_MODEL_REFORM includes TEACHING_THEORY and OBJECTIVES ,
    TEACHING_PREPARATION , TEACHING_PROCESS , STUDENTS ' FEEDBACK and TEACHING_REFLECTION ,
    which are represented by patternl pattern4 respectively . in_order_to better assess
    THE_ALLEVIATION_EFFECT , the study combined EXPERT_ADVICE to assign A_CERTAIN_WEIGHT to
    BOTH_SUBJECTIVE_AND_OBJECTIVE_PSYCHOLOGY , and took THE_FINAL_RESULT as THE_FINAL_OUTCOME
    . results : THE_EFFECT of THE_FLIPPED_CLASSROOM_CIVICS_TEACHING_MODEL combined with
    SOCIAL_PSYCHOLOGY on improving THE_PSYCHOLOGICAL_EFFECTS of STUDENTS '
    AVERSION_TO_LEARNING is significant , mainly in_terms_of THE_LOW_QUALITY of LEARNING and
    EDUCATION and THE_EXISTENCE of BAD_SOCIAL_CLIMATE in SOCIETY , while THE_IMPROVEMENT in
    THE_SUBJECTIVE_AVERSION to LEARNING is slightly weaker . conclusions :
    SOCIAL_PSYCHOLOGY_PLAYS_AN_IMPORTANT_ROLE in THE_ANALYSIS of INDIVIDUAL_BEHAVIOR ,
    GROUP_BEHAVIOR and INTERPERSONAL_RELATIONSHIPS . THE_FLIPPED_CLASSROOM_MODEL of
    TEACHING_CIVICS combined with SOCIAL_PSYCHOLOGY can positively improve STUDENTS '
    AVERSION_TO_LEARNING . MEDICINSKA_NAKLADA_ZAGREB , CROATIA .
    <BLANKLINE>
    background / objectives : this study aims to analyze THE_EFFECTS of APPLICATION_CLASSES
    based on FLIPPED_LEARNING for strengthening CAPABILITY of CREATIVITY .
    PERSONALITY_EDUCATION in THE_COURSE of TEACHER_TRAINING in THE_UNIVERSITY . methods /
    statistical analysis : for THIS_STUDY , it was conducted the before and after SURVEYS on
    FLIPPED_LEARNING_BASED_CLASS covering 112 STUDENTS attending EDUCATIONAL_METHOD and
    TECHNOLOGY ' COURSE in UNIVERSITY a in DAEJEON . CREATIVITY and
    PERSONALITY_DIAGNOSTIC_TOOL was used to measure CREATIVITY and PERSONALITY_CAPABILITY
    which is categorized mainly as CREATIVITY , PERSONALITY and CREATIVITY and
    PERSONALITY_TEACHING_EFFICACY . findings : this study has proven THE_EFFECTS of
    FLIPPED_LEARNING aiming to improve PRELIMINARY_INSTRUCTOR ' screativity and
    PERSONALITY_EDUCATIONAL_CAPABILITIES . according to THE_RESULTS , it is effective
    first_of_all to lead THE_STUDENTS to STUDY_THE_MATERIAL_ONLINE ahead , and then lead them
    to VARIOUS_ACTUAL_ACTIVITIES aiming to increase THE_CREATIVITY and
    PERSONALITY_EDUCATIONAL_CAPABILITY in_order_to improve THE_CREATIVITY , PERSONALITY and
    THE_CREATIVITY and PERSONALITY_TEACHING_EFFICACY of THE_PRELIMINARY_INSTRUCTOR . first ,
    it is critical to induce PERCEPTION_SHIFTS of PRELIMINARY_INSTRUCTORS regarding CURRICULA
    for TEACHING_PROFESSION . second , change in THE_OPERATION of UNIVERSITY_CURRICULA for
    TEACHING is required alongside THE_CHANGE of PERCEPTION of THE_INSTRUCTORS . third , to
    DESIGN_A_CONSTRUCTIVE_ACTIVITY for enhancing CREATIVITY and PERSONALITY_CAPABILITIES ,
    A_FOUNDATION_SYSTEM is required to actually put THE_IDEAS in PRACTICE . improvements /
    applications : it need to WORK on A_TEACHING_PROCESS that aims to ENHANCE_CREATIVITY .
    PERSONALITY_CAPABILITY on VARIOUS_SUBJECTS as_well_as to FOCUS on THE_THEORIES of
    CURRICULA for TEACHING . 2017 , institute of advanced scientific research , inc . . all
    rights reserved .
    <BLANKLINE>
    introduction : THE_FLIPPED_CLASSROOM is PEDAGOGICAL_MODEL that consists of reversing
    THE_TRADITIONAL_ORDER of LEARNING_ACTIVITIES in THE_CLASSROOM . at_the_same_time ,
    THE_TEACHING of STATISTICS in POSTGRADUATE_STUDIES is A_CHALLENGE for TEACHERS when faced
    with PROFESSIONALS who do not address THESE_TOPICS regularly , which requires THE_SEARCH
    for motivating LEARNING_METHODOLOGIES for THEIR_FURTHER_APPLICATION in THE_RESEARCH they
    carry out . objective : to develop A_SYSTEM of activitiesdesigned for THE_TEACHING of
    STATISTICS applied to RESEARCH using THE_FLIPPED_CLASSROOM_METHODOLOGY for
    ACADEMIC_POSTGRADUATE_STUDIES . methods : A_RESEARCH with A_QUANTITATIVE_APPROACH is
    presented . A_SET of PROCESSES is carried out with AN_EVIDENTIARY_PURPOSE , of a
    correlational , experimental and CROSS_SECTIONAL_TYPE . results : A_CONCEPTUAL_MAP was
    obtained as A_PROPOSAL and guide for THE_ACTIVITY_SYSTEM . A_SYSTEM of ACTIVITIES was
    designed that showed THE_USE of VARIOUS_FORMATS and NAMES . conclusions :
    THE_IN_DEPTH_STUDY carried out demonstrated THE_FEASIBILITY of using
    THE_FLIPPED_CLASSROOM_METHODOLOGY in THE_STATISTICAL_TRAINING of POSTGRADUATE_STUDENTS and
    THE_POSSIBILITY of ITS_GENERALIZATION . ITS_APPLICATION and DESIGN_REFLECT_THE_POTENTIAL
    of THE_ACTIVITY_SYSTEM for THE_DEVELOPMENT of STATISTICAL_SKILLS . 2025 , editorial
    ciencias medicas . all rights reserved .
    <BLANKLINE>
    background : THE_ADVENT of DIGITAL_TECHNOLOGY has profoundly impacted THE_FIELD of
    EDUCATION , effectively removing LIMITATIONS and enhancing THE_LEARNING_ENVIRONMENT .
    BLENDED_LEARNING , which combines FACE_TO_FACE_INSTRUCTION with ONLINE_COMPONENTS ,
    ADDRESSES_BARRIERS to LEARNING and FOSTERS_HIGHER_ORDER_COGNITIVE_SKILLS , resulting_in
    INCREASED_STUDENT_SATISFACTION and IMPROVED_OUTCOMES in MEDICAL_EDUCATION . objectives :
    this study aimed to identify THE_KEY_MOTIVATIONAL_COMPONENTS and construct
    A_COMPREHENSIVE_MODEL that can effectively SUPPORT_FACULTY_MEMBERS in implementing
    BLENDED_LEARNING within MEDICAL_UNIVERSITIES . methods : a qualitative GROUNDED_THEORY (
    GT ) approach was used to explore THIS_PHENOMENON . FACULTY_MEMBERS from
    MEDICAL_UNIVERSITIES in REGION 4 were recruited using PURPOSEFUL_SAMPLING . DATA were
    collected through SEMI_STRUCTURED_INTERVIEWS conducted between NOVEMBER 2023 and MARCH
    2024 . A_THREE_STAGE_CODING_PROCESS open , axial , and selective was applied to analyze
    THE_DATA . RIGOR was ensured through MEASURES addressing CREDIBILITY , CONFIRMABILITY ,
    TRANSFERABILITY , and DEPENDABILITY . results : INTERVIEWS with 14 FACULTY_MEMBERS
    revealed FIVE_PRIMARY_CATEGORIES influencing THE_ADOPTION of BLENDED_LEARNING :
    LEARNER_PROFESSOR , INFRASTRUCTURE , structural , ENVIRONMENTAL_FACTORS , and
    RULES_AND_REGULATIONS . THESE_FINDINGS informed THE_DEVELOPMENT of
    A_MOTIVATIONAL_FRAMEWORK that highlights CRITICAL_COMPONENTS for promoting
    FACULTY_ENGAGEMENT in BLENDED_LEARNING . conclusions : THE_MODEL provides
    ACTIONABLE_INSIGHTS for MEDICAL_SCHOOLS to enhance EDUCATIONAL_OUTCOMES and
    INNOVATE_TEACHING_PRACTICES in HEALTHCARE_EDUCATION . 2025 , abbasi et al .
    <BLANKLINE>
    context : jining MEDICAL_UNIVERSITY has adopted THE_TRADITIONAL_LARGE_CLASS_TEACHING_MODE
    in ITS_HISTOLOGY_AND_EMBRYOLOGY_COURSE . in THIS_MODE , STUDENTS ' participation and
    LEARNING_OUTCOMES are not satisfactory . objective : to solve THIS_PROBLEM , we integrated
    DESIGN_THINKING into THE_LARGE_CLASS_FLIPPED_TEACHING . method : A_MIXED_METHODOLOGY (
    qualitative and quantitative ) was employed . PARTICIPANTS were from THE_UNIVERSITY '
    SCLINICAL_MEDICINE_PROGRAM , randomly assigned to THE_EXPERIMENTAL_AND_CONTROL_GROUPS .
    THE_EXPERIMENTAL_GROUP received INTEGRATED_FLIPPED_CLASSROOM_INSTRUCTIONS , whereas
    THE_CONTROL_GROUP received TRADITIONAL_LARGE_CLASS_TEACHING . DATA were collected using
    AN_EMPATHY_CANVAS , QUESTIONNAIRES , and CLASSROOM_ASSESSMENTS . results : ANALYSIS of 24
    EMPATHY_MAPS identified 32 LEARNING_GAINS and 18 PAIN_POINTS , categorized into
    FOUR_DIMENSIONS : SELF_AWARENESS , TEAMWORK , LEARNING_EFFICIENCY , and
    COMPREHENSIVE_COMPETENCIES . SURVEY_RESULTS showed 89.3 % of STUDENTS found
    THIS_TEACHING_MODEL_ENHANCED_KNOWLEDGE_COMPREHENSION , 85.3 % reported
    NO_INCREASED_LEARNING_BURDEN , and 80 % acknowledged IMPROVED_COMPREHENSIVE_ABILITIES .
    SIGNIFICANT_GENDER_DIFFERENCES emerged in RESOURCE_PREFERENCES ( MALES favored
    INTERACTIVE_RESOURCES while FEMALES preferred structured MATERIALS ) and perceived
    LEARNING_BURDEN ( p 0.05 ) . conclusion : THE_LARGE_CLASS_FLIPPED_CLASSROOM_MODEL
    integrated with DESIGN_THINKING has THE_POTENTIAL to ENHANCE_LEARNING_OUTCOMES and
    COMPREHENSIVE_LITERACY without imposing AN_ADDITIONAL_BURDEN . this MODEL_SHOWS_POTENTIAL
    for APPLICATION in THE_TEACHING of HISTOLOGY and EMBRYOLOGY . however , FURTHER_VALIDATION
    is needed to confirm ITS_APPLICABILITY across DIFFERENT_CONTENT_AREAS and
    LEARNING_ENVIRONMENTS . the author ( s ) 2025 .
    <BLANKLINE>



    >>> for i in range(30, 40):
    ...     print(textwrap.fill(mapping[i]["AB"], width=90))
    ...     print()
    purpose : this study aims to investigate TEACHING_METHODOLOGIES , BEST_PRACTICES , and
    CHALLENGES encountered in delivering a SCIENCE , TECHNOLOGY , and SOCIETY_COURSE using
    THE_NORMALE_LECTURE_MODEL at Y_UNIVERSITY . design / methodology / approach : using
    A_QUALITATIVE_DESCRIPTIVE_APPROACH , DATA was collected through SURVEYS distributed to 202
    first YEAR_STUDENTS enrolled in AN_STS_COURSE . ETHICAL_CLEARANCE was secured prior_to
    DATA_COLLECTION . findings : EFFECTIVE_STRATEGIES in LARGE_CLASS_STS_COURSE included
    A_COMBINATION of LECTURES , COLLABORATIVE_GROUP_ACTIVITIES , ASYNCHRONOUS_ASSIGNMENTS ,
    and DIGITAL_TOOLS , such_as QUIZIZZ , to ENHANCE_ENGAGEMENT and provide structured ,
    INTERACTIVE_LEARNING_EXPERIENCES . STUDENTS_PERCEIVE_BEST_PRACTICES , such_as
    COLLABORATIVE_AND_INTERDISCIPLINARY_PROJECTS and ACTIVE_LEARNING_METHODS .
    STUDENTS_FACE_CHALLENGES such_as LIMITED_INTERACTION with INSTRUCTORS , fast paced
    CONTENT_DELIVERY , TECHNOLOGICAL_ISSUES , LACK of HANDS_ON_ACTIVITIES , and increased
    STRESS and ANXIETY in LARGE_CLASS_SETTINGS . practical implications : RECOMMENDATIONS
    include reducing CLASS_SIZE , enhancing INTERACTIVE_AND_PRACTICAL_ACTIVITIES , providing
    CLEAR_COMMUNICATION and FEEDBACK , and optimizing TECHNOLOGY_USE to FOSTER_ENGAGEMENT and
    improve LEARNING_OUTCOMES in LARGE_CLASSES . originality / value : this study contributes
    to THE_GROWING_BODY of RESEARCH on LARGE_CLASS_PEDAGOGY in
    THE_PHILIPPINE_HIGHER_EDUCATION_CONTEXT , offering INSIGHTS into adapting BLENDED_LEARNING
    for DIVERSE_AND_LARGE_CLASS_SIZES . this study focuses on A_SINGLE_INSTITUTION and COURSE
    , which limits ITS_GENERALIZABILITY . 2025 , JAYSON_L . DE_VERA , NILO_JAYOMA_CASTULO ,
    VIC_MARIE_I . CAMACHO , THADDEUS_OWEN_D . ayuste and BRANDO_C . PALOMAR .
    <BLANKLINE>
    background : FACULTY_MEMBERS ' perceptions of BLENDED_LEARNING are critical to developing
    EFFECTIVE_STRATEGIES to improve ITS_QUALITY and prepare for ITS_IMPLEMENTATION under
    THE_NEW_NORMAL_CONDITIONS . this study introduces A_NEW_FBL_SCALE to address THIS_ISSUE ,
    as NO_EXCLUSIVE_TOOL focuses on HEALTH_SCIENCES_FACULTY_MEMBERS . materials and methods :
    THE_DEVELOPMENT_AND_PSYCHOMETRIC_EVALUATION of THE_FBL_SCALE was chosen as the study
    DESIGN . TWO_HUNDRED_AND_FORTY_FACULTY_MEMBERS employed in
    SELECTED_HEALTH_SCIENCE_COLLEGES of IMAM_ABDULRAHMAN_BIN_FAISAL_UNIVERSITY in SAUDI_ARABIA
    were randomly selected and administered THE_FBL_TOOL . THE_TOOL consists of 25 items with
    FOUR_SUBSCALES that MEASURE_FACULTY ' perceptions of CONVENIENCE , ENGAGEMENT in
    BLENDED_LEARNING , SATISFACTION , and STUDENT_LEARNING_PROGRESS on
    A_FIVE_POINT_LIKERT_SCALE . RELIABILITY was examined using cronbach
    ALPHA_RELIABILITY_AND_VALIDITY was determined using CONFIRMATORY_FACTOR_ANALYSIS . results
    : THE_FBL_TOOL has A_CRONBACH_ALPHA_COEFFICIENT of 0.867.
    STRUCTURAL_EQUATION_MODELING_ANALYSIS revealed that EACH_ITEM had
    A_SIGNIFICANT_POSITIVE_RELATIONSHIP with ITS_RESPECTIVE_FBL_FACTOR . conclusion : this
    study provides a 25 ITEM_FBL_TOOL with FOUR_SUBSCALES consisting of cbl , EBL , sbl and pb
    , which is well suited to ASSESS_FACULTY_MEMBERS ' views on BLENDED_LEARNING specifically
    in THE_SAUDI_ARABIAN_CONTEXT under THE_NEW_NORMAL_CONDITIONS .
    THESE_FACTORS_ENABLE_POLICYMAKERS to ASSESS_FACULTY_MEMBERS ' perceptions of
    BLENDED_LEARNING and develop APPROPRIATE_STRATEGIES that improve THE_OVERALL_QUALITY of
    EDUCATION through the effective USE_OF_TECHNOLOGY . the author ( s ) 2025 .
    <BLANKLINE>
    importance : HYBRID_DOCTOR of PHYSICAL_THERAPY_PROGRAMS , which combine ONLINE and
    IN_PERSON_INSTRUCTION , are becoming AN_INCREASINGLY_COMMON_MODEL for delivering
    PHYSICAL_THERAPIST_EDUCATION . UNDERSTANDING_THEIR_CHARACTERISTICS , TRENDS , and
    IMPLICATIONS is critical to guiding THEIR_DEVELOPMENT and ensuring
    EQUITABLE_AND_EFFECTIVE_EDUCATIONAL_OUTCOMES . objective : the objective of this study was
    to examine CHARACTERISTICS and TRENDS in HYBRID_EDUCATION_PROGRAMS through
    A_SECONDARY_ANALYSIS of PUBLICLY_AVAILABLE_DATA . design : THIS_STUDY involved
    A_SECONDARY_ANALYSIS of PUBLICLY_AVAILABLE_DATA on HDPT_PROGRAMS in THE_UNITED_STATES .
    setting / participants / intervention : the study included accredited , CANDIDATE , and
    developing HDPT_PROGRAMS in THE_UNITED_STATES and involved DESCRIPTIVE_ANALYSES of
    PROGRAM_LEVEL_DATA . main outcomes and measures : KEY_VARIABLES included INSTITUTION_TYPE
    , INSTITUTION and PROGRAM_CHARACTERISTICS , ADMISSIONS and ENROLLMENT_DATA , and
    PROGRAM_OUTCOMES . results : there are 33 HDPT_PROGRAMS at 25 UNIQUE_INSTITUTIONS in
    THE_UNITED_STATES , located in 21 states .
    HDPT_PROGRAMS_ENROLL_A_MORE_RACIALLY_AND_ETHNICALLY_DIVERSE_BODY compared to
    NATIONAL_AVERAGES . MEAN_HDPT_PROGRAM_COHORT_SIZE was 32 % larger than NATIONAL_AVERAGE .
    MEAN_FIRST_TIME_PASS_RATE for THE_NATIONAL_PHYSICAL_THERAPY_EXAMINATION ( NPTE ) for
    HDPT_GRADUATES was reported at 71 % , while ULTIMATE_PASS_RATES , GRADUATION_RATES , and
    EMPLOYMENT_RATES ranged from 96 % to 99 % . MEAN_PROGRAM_DURATION and COSTS were
    consistent with NATIONAL_AVERAGES . conclusion and relevance : HDPT_PROGRAMS demonstrate
    POTENTIAL to broaden ACCESS and DIVERSITY in THE_PHYSICAL_THERAPY_PROFESSION .
    STANDARDIZED_DATA_COLLECTION and FURTHER_RESEARCH are essential to exploring
    THESE_CHALLENGES and supporting DEVELOPMENT of accessible , equitable , and
    HIGH_QUALITY_HYBRID_EDUCATION_PATHWAYS in PHYSICAL_THERAPY . the author ( s ) 2025 .
    published by oxford university press on behalf of the american physical therapy
    association . all rights reserved .
    <BLANKLINE>
    purpose : this study aims to explore THE_CONTEMPORARY_RELEVANCE and POTENTIAL_APPLICATIONS
    of HYBRID_LEARNING in BANGLADESH , focusing_on PERSPECTIVES from TEACHERS , STUDENTS and
    PARENTS . drawing on PREVIOUS_RESEARCH highlighting THE_POSITIVE_IMPACT of HYBRID_LEARNING
    globally , THIS_STUDY discovers ITS_IMPLICATIONS for STUDENT_CONVENIENCE , SATISFACTION ,
    ENGAGEMENT and PERFORMANCE within THE_CONTEXT of A_DEVELOPING_COUNTRY , BANGLADESH .
    design / methodology / approach : THIS_STUDY utilized A_QUALITATIVE_APPROACH , employing
    in DEPTH , SEMI_STRUCTURED_INTERVIEWS to explore THE_HYBRID_LEARNING_MODEL in BANGLADESH .
    PARTICIPANTS were divided into THREE_CLUSTERS : STUDENTS ( 80 ) , EDUCATORS ( 50 ) and
    PARENTS ( 34 ) . PERSONALIZED_QUESTIONNAIRES , comprising both open
    ENDED_AND_CLOSED_ENDED_QUESTIONS , were designed to gather INSIGHTS from EACH_GROUP .
    findings : THE_RESEARCH_FINDINGS demonstrate THE_EFFECTIVENESS of HYBRID_LEARNING in
    CRISIS_MANAGEMENT , FLEXIBILITY and INCLUSIVITY , particularly in BANGLADESH '
    SEDUCATIONAL_LANDSCAPE . HYBRID_MODELS provide A_PRACTICAL_SOLUTION during
    POLITICAL_UNREST , ensuring UNINTERRUPTED_EDUCATION through A_COMBINATION of ONLINE and
    FACE_TO_FACE_CLASSES . PARTICIPANTS expressed SATISFACTION with THE_FLEXIBILITY offered by
    HYBRID_LEARNING , emphasizing ITS_ACCESSIBILITY for DIVERSE_LEARNERS and
    WORKING_PROFESSIONALS . moreover , while HYBRID_LEARNING holds PROMISE for enhancing
    SATISFACTION and ACADEMIC_PERFORMANCE , FURTHER_EVALUATION is needed to gauge
    ITS_LONG_TERM_EFFECTIVENESS and IMPACT_ON_LEARNING_OUTCOMES . the research highlights
    THE_TRANSFORMATIVE_POTENTIAL of HYBRID_LEARNING in EXECUTIVE_EDUCATION , catering to
    THE_DIVERSE_NEEDS of STUDENTS and fostering INCLUSIVITY in EDUCATION . it also revealed
    THE_IMPORTANCE of COMMUNICATION , COLLABORATION and ENGAGEMENT in HYBRID_EDUCATION .
    research limitations / implications : this study will help EDUCATORS understand
    THE_DIVERSE_NEEDS of STUDENTS , enabling them to effectively
    DESIGN_INNOVATIVE_LEARNING_MODULES to ENHANCE_STUDENT_ENGAGEMENT . originality / value :
    THE_ORIGINALITY and VALUE of THIS_RESEARCH_LIE in ITS_COMPREHENSIVE_EXPLORATION of
    THE_IMPLEMENTATION and IMPACT of HYBRID_LEARNING in the context of A_DEVELOPING_COUNTRY .
    2025 , emerald publishing limited .
    <BLANKLINE>
    aim : to map THE_RESEARCH_PROJECT_COMPONENT of NURSING_HYBRID_MASTER_DEGREES in
    AUSTRALIA_AND_NEW_ZEALAND , as documented in UNIVERSITY_WEBSITES . background :
    MASTER_DEGREES are completed by MANY_NURSES internationally . THESE_DEGREES take
    MANY_FORMATS , one of which combines COURSEWORK and RESEARCH . little is known about
    THE_COMPONENTS , STRUCTURES and INTENDED_OUTCOMES of THE_RESEARCH_PROJECT_COMPONENT of
    THESE_HYBRID_MASTER_DEGREES . methods : WEBSITES of MEMBERS of THE_COUNCIL of DEANS of
    NURSING and MIDWIFERY of AUSTRALIA_AND_NEW_ZEALAND were systematically searched for
    DETAILS of THE_RESEARCH_PROJECT_COMPONENTS of HYBRID_MASTER_DEGREES . ALL_CONTENT was
    downloaded and HYPERLINKS searched for INFORMATION about THE_RESEARCH_COMPONENT .
    A_PRESET_TEMPLATE was used to guide THE_EXTRACTION of THE_WEBSITE_CONTENT related to
    THE_STRUCTURE and COMPONENTS of THE_RESEARCH_PATHWAYS . DESCRIPTIVE_STATISTICS and
    CONTENT_ANALYSIS were used to generate THE_FINDINGS . results :
    TWENTY_SEVEN_UNIVERSITY_WEBSITES contained CONTENT of HYBRID_NURSING_MASTER_DEGREES .
    THE_VOLUME and FORMAT of THE_WEBSITE_INFORMATION varied greatly . there was VARIATION in
    THE_PROPORTION of THE_RESEARCH_COMPONENT in THE_DEGREE ( range 8 % 50 % . MEDIAN 33.3 % )
    , THE_TYPE of RESEARCH undertaken ( primary , secondary or both ) , THE_FINAL_OUTPUT (
    thesis , REPORT or MANUSCRIPT ) and ITS_SIZE ( range 200025,000 words ) .
    LEARNING_OUTCOMES ( n = 178 ) , where included , varied in FOCUS and CONTENT . conclusion
    : FINDINGS indicate THE_RESEARCH_PATHWAY_COMPONENTS of HYBRID_NURSING_MASTER_DEGREES
    across AUSTRALASIA vary widely . INFORMATION provided on MANY_UNIVERSITY_WEBSITES was
    insufficient for NURSES to confidently choose A_PROGRAM that would align with
    THEIR_CAREER_GOALS . 2025 the authors
    <BLANKLINE>
    objective : due_to LIMITED_MUSCULOSKELETAL_EDUCATION , STUDENTS pursuing
    ORTHOPAEDIC_SURGERY often feel unprepared for RESIDENCY . CLINICAL_ROTATIONS provide
    SOME_EDUCATION . however , prior_to THE_DEVELOPMENT of
    THE_ORTHO_ACTING_INTERN_COORDINATED_CLINICAL_EDUCATION and SURGICAL_SKILLS_CURRICULUM in
    2019 , NO_STANDARDIZED_DIDACTIC_CURRICULUM existed . over TIME , STUDENTS desired
    interactive , CASE_BASED_LEARNING_OPPORTUNITIES . OUR_OBJECTIVE was to
    DESIGN_A_FLIPPED_CLASSROOM , BLENDED_LEARNING_CURRICULUM and evaluate ITS_ABILITY to
    improve MEDICAL_STUDENT_ORTHOPAEDIC_KNOWLEDGE . design : ORTHOACCESS 2.0 is a 16 week ,
    OPEN_ACCESS_CURRICULUM consisting of DIDACTIC_LECTURES , CASE_DISCUSSIONS , and
    LEARNING_RESOURCES . THE_CURRICULUM was evaluated using PRE_CURRICULUM ,
    POST_CASE_DISCUSSION , and POST_CURRICULUM_SURVEYS . LIKERT_ITEM_QUESTIONS were evaluated
    with PAIRED_WILCOXON_SIGNED_RANK_ANALYSIS . FREE_TEXT_RESPONSES were reviewed for
    EMERGING_THEMES . setting : LECTURES were presented weekly in PERSON for STUDENTS at
    ORTHOACCESS_INSTITUTIONS with PRE_RECORDED_LECTURES available for NON rotating STUDENTS .
    FACULTY led VIRTUAL_CASE_DISCUSSIONS consisted of 3 CASE_PRESENTATIONS and BREAKOUT_ROOMS
    for DISCUSSION . LEARNING_RESOURCES ( e.g. , ANKI_CARDS , SCUT_SHEETS ) were posted to
    THE_WEBSITE . participants : ORTHOACCESS 2.0 was hosted from JUNE to OCTOBER 2023 with 35
    participating INSTITUTIONS . all 226 STUDENT_REGISTRANTS completed
    THE_PRE_CURRICULUM_SURVEY and 69 completed THE_POST_CURRICULUM_SURVEY . FORTY_STUDENTS
    attended at_least 8/16 CASE_DISCUSSIONS . results : in THE_POST_CURRICULUM_SURVEY , 68 %
    of PARTICIPANTS reported QUITE_OR_EXTREMELY_STRONG_ORTHOPEDIC_KNOWLEDGE , compared to 23 %
    beforehand ( p < 0.001 ) . POSTCASE_DISCUSSION_SURVEYS revealed SIGNIFICANT_INCREASES in
    KNOWLEDGE associated with EACH_LECTURE_AND_CASE_DISCUSSION ( p < 0.001 ) .
    THE_GREATEST_STUDENT reported BENEFITS were THE_BROAD_COVERAGE of ORTHOPEDIC_TOPICS ( n=41
    ) and LEARNING how to think like AN_ORTHOPAEDIC_SURGEON ( n=20 ) . THE_GREATEST_BARRIER to
    ATTENDANCE was CLINICAL_OBLIGATIONS during CASE_DISCUSSIONS ( n=44 ) . conclusions :
    THIS_FLIPPED_CLASSROOM , BLENDED_LEARNING_CURRICULUM has improved
    MEDICAL_STUDENT_FOUNDATIONAL_ORTHOPAEDIC_KNOWLEDGE nationally . THIS_MODEL may be valuable
    for OTHER_SPECIALTIES with LIMITED_UNDERGRADUATE_MEDICAL_EXPOSURE . 2024 association of
    PROGRAM_DIRECTORS in SURGERY
    <BLANKLINE>
    purpose : to evaluate THE_EFFECTIVENESS of THE_EDUCATION_PROGRAM developed based on
    THE_STRUCTURAL_EMPOWERMENT ( SE ) and PSYCHOLOGICAL_EMPOWERMENT ( PE ) theories and
    FLIPPED_CLASSROOM model for THE_EMPOWERMENT of NEW_GRADUATE_NURSES ( NGNS ) . design :
    single center , PARALLEL_GROUP , RANDOMIZED_CONTROLLED_TRIAL . methods : the study was
    conducted between JUNE 2021 and SEPTEMBER 2023 in TWO_PHASES : developing
    THE_EDUCATION_PROGRAM to EMPOWER_NGNS and evaluating ITS_EFFECTIVENESS .
    AN_EDUCATION_PROGRAM consisting of TWO_PARTS , ONLINE and FACE_TO_FACE , was developed .
    THE_ONLINE_PART consists of EIGHT_MODULES implemented for TWO_WEEKS . the FACE_TO_FACE
    part was implemented for TWO_DAYS and included THE_IN_CLASS_ACTIVITIES . NGNS were
    randomly assigned to THE_INTERVENTION_GROUP ( n : 32 ) and CONTROL_GROUP ( n : 32 ) .
    AN_EDUCATION_PROGRAM was applied to THE_INTERVENTION_GROUP , whereas THE_CONTROL_GROUP
    continued THEIR_ROUTINE_ORIENTATION_PROGRAM . A_RANGE of OUTCOME_MEASURES of SE , PE , and
    EDUCATION_PROGRAMS ' EFFECTIVENESS were evaluated . DATA were analyzed using descriptive ,
    chi squared , and T_TESTS . results : the study determined that
    THE_INTERVENTION_AND_CONTROL_GROUPS showed HOMOGENEOUS_DISTRIBUTION in the pretest .
    A_STATISTICALLY_SIGNIFICANT_DIFFERENCE was identified between
    THE_INTERVENTION_AND_CONTROL_GROUPS regarding THE_MEAN_SCORES of PE and SE three months
    following THE_IMPLEMENTATION of THE_EDUCATION_PROGRAM , and THE_TOTAL_MEAN_SCORE of
    THE_INTERVENTION_GROUP was higher . conclusion : THE_EDUCATION_PROGRAM developed to
    EMPOWER_NGNS was A_HIGHLY_EFFECTIVE_INTERVENTION in increasing NURSES ' perceptions of SE
    and PE . there is A_NEED to carry out STUDIES and ACTIVITIES to disseminate THIS_PROGRAM .
    clinical relevance : THE_FINDINGS of this study will guide EDUCATORS , RESEARCHERS , and
    ADMINISTRATORS in FUTURE_STRATEGIES and INNOVATIVE_PROGRAMS for empowering NGNS . 2024 the
    author ( s ) . journal of nursing scholarship published by wiley periodicals llc on behalf
    of sigma theta tau international .
    <BLANKLINE>
    aim and background : despite THE_VAST_HETEROGENEITY of TEACHING_METHODS , there remains
    A_DILEMMA on what works best for TEACHING_MEDICAL_STUDENTS . FLIPPED_CLASSROOM_TEACHING is
    A_LEARNER_ORIENTED_ACTIVE_TEACHING_LEARNING_METHODOLOGY with A_FOCUS on inculcating
    DIFFERENT_ASPECTS of KNOWLEDGE_ATTAINMENT in LEARNERS including APPLICATION , ANALYSIS ,
    EVALUATION , and SYNTHESIS of KNOWLEDGE . this study aimed to assess THE_ACCEPTABILITY of
    THE_FLIPPED_CLASSROOM_MODEL for TEACHING_UNDERGRADUATE_MEDICAL_STUDENTS . materials and
    methods : this was a mixed METHOD_QUALITATIVE_ANALYSIS conducted over 3 months utilizing
    ANONYMIZED_PREVALIDATED_QUESTIONNAIRE for LEARNERS and FOCUSED_GROUP_DISCUSSION ( FGD )
    for FACILITATORS . A_TOTAL of 50 STUDENTS were enrolled for THE_FLIPPED_CLASSROOM_SESSIONS
    and FEEDBACK was taken with A_COMBINATION of OPEN_AND_CLOSED_ENDED_QUESTIONS .
    FOCUSED_GROUP_DISCUSSION was carried out to discuss THE_MERITS and CONSTRAINTS of
    THE_TEACHING_METHODOLOGY . RESULTS were compiled as FREQUENCY_DISTRIBUTION and
    THE_QUALITATIVE_DATA was analyzed using PRE_FORMED_CODES to identify RECURRING_THEMES and
    OPINIONS . results : THE_MAJORITY of STUDENTS found FLIPPED_CLASSROOMS to be more
    interactive and easier to comprehend in_comparison with TRADITIONAL_TEACHING_METHODS .
    about 72 % of STUDENTS experienced HIGHER_CONFIDENCE_LEVELS after THE_SUBJECT was taken up
    as A_FLIPPED_CLASSROOM . conclusion : FLIPPED_CLASSROOM_TEACHING is acceptable and finds
    HIGH_SATISFACTION_LEVELS_AMONGST_MEDICAL_STUDENTS . it involves AN_INVESTMENT of
    EXTRA_TIME and ENERGY by THE_FACILITATORS , especially initially . clinical significance :
    THIS_PILOT_PROJECT helps to understand THE_NEED for innovating and integrating
    VARIOUS_TEACHING_TECHNIQUES for BETTER_ACADEMIC_OUTCOMES as_well_as STUDENT_SATISFACTION
    and promotes FURTHER_RESEARCH with A_HIGHER_SAMPLE_SIZE to fortify
    THESE_ACTIVE_TEACHING_METHODS in THE_WORLD of EDUCATION . the author ( s ) . 2024 open
    access .
    <BLANKLINE>
    aim : to DESIGN and validate THE_FLIPPED_LEARNING_ASSESSMENT_SCALE . A_TOOL for assessing
    STUDENTS ' experience of FLIPPED_LEARNING . background : frequently , UNIVERSITY_STUDENTS
    are introduced to NEW_CONTENT during LECTURES . in_contrast , ACTIVE_LEARNING_ACTIVITIES ,
    such_as FLIPPED_LEARNING , are designed as AN_INSTRUCTIONAL_METHOD to ENGAGES_STUDENTS in
    THE_LEARNING_PROCESS . design : CROSS_SECTIONAL_DESCRIPTIVE_STUDY . methods :
    A_CROSS_SECTIONAL_STUDY was carried out in THREE_PHASES ( ( 1 ) ITEM_SELECTION ,
    REPHRASING and TRANSLATION . ( 2 ) CONTENT_ANALYSIS through EXPERT_PANEL and ( 3 )
    CONFIRMATORY_FACTOR_ANALYSIS ) . THE_FINAL_VERSION of THE_SCALE was piloted on
    A_SUFFICIENT_SAMPLE of UNDERGRADUATE_STUDENT_NURSES from THREE_SPANISH_UNIVERSITIES .
    results : A_TOTAL of 455 STUDENTS completed THE_QUESTIONNAIRE . 373 women and 82 men . the
    TOTAL_CRONBACH ' SALPHA_VALUE for THE_COMPLETE_INSTRUMENT was 0.893. cronbach ALPHA for
    EACH_SEPARATE_DIMENSION ranged between 0.660 and 0.897. GOODNESS_OF_FIT values were
    acceptable , implying that THE_MODEL was validated . conclusion :
    THE_FLIPPED_LEARNING_APPROACH has become increasingly popular in ACADEMIC_SETTINGS .
    evaluating THE_STUDENTS ' flipped LEARNING_EXPERIENCE is important to ANALYSE_ASPECTS
    such_as ACCEPTABILITY and EFFECTIVENESS of THIS_METHODOLOGY .
    THE_FLIPPED_LEARNING_ASSESSMENT_SCALE is A_VALID_AND_RELIABLE_TOOL for analysing STUDENTS
    ' experience of FLIPPED_LEARNING . impact : FLIPPED_LEARNING has been
    A_USEFUL_PEDAGOGICAL_MODEL very for cultivating STUDENT_SKILLS in PROBLEM solving ,
    CRITICAL_THINKING , TEAMWORK and SELF_ACTIVE_LEARNING in NURSING_EDUCATION . A_KEY_ISSUES
    , such_as STUDENT_SATISFACTION , has been explored further before implementing this
    TEACHING_AND_LEARNING_METHODOLOGY . patient or public contribution : none . 2024 the
    author ( s ) . NURSING open published by john wiley and sons ltd .
    <BLANKLINE>
    background and purpose : LACK of LEARNING_MOTIVATION , large AMOUNT_OF_INFORMATION that
    must be learned in A_SHORT_TIME , and LACK of up to DATE_CONTENT are among THE_LIMITATIONS
    of EFFECTIVE_LEARNING . FLIPPED_LEARNING is suggested as A_SOLUTION in which
    DIRECT_TEACHING in CLASSROOM_ENVIRONMENT is replaced by TEACHING and INDIVIDUAL_LEARNING
    using educational TOOLS_AND_TECHNOLOGIES . in this study , we investigated
    FLIPPED_LEARNING_PROCESS in MAZANDARAN_UNIVERSITY_OF_MEDICAL_SCIENCES , aiming
    IN_SERVICE_TRAINING of EMPLOYEES , 2020 . materials and methods : A_QUALITATIVE_STUDY
    using GROUNDED_THEORY_APPROACH was performed . THE_PARTICIPANTS ( n=16 ) included
    ELITE_UNIVERSITY_EXPERTS and MEMBERS of THE_EDUCATION_AND_EMPOWERMENT_COMMITTEES in
    MAZANDARAN , BABOL , and TEHRAN_UNIVERSITIES of MEDICAL_SCIENCES . they were selected via
    PURPOSEFUL_SAMPLING . IN_DEPTH_INTERVIEWS were done and DATA were analyzed by MAXQDA 2018
    . results : FLIPPED_LEARNING_PROCESS in MAZANDARAN_UNIVERSITY_OF_MEDICAL_SCIENCES has 12
    dimensions , including LEARNING_MOTIVATION , INDIVIDUAL_FACTORS , FACTORS of
    ORGANIZATIONAL_CULTURE , STRUCTURAL_FACTORS , ESTABLISHMENT of FLIPPED_LEARNING ,
    facilitating MEASUREMENTS , ORGANIZATIONAL_BARRIERS and CHALLENGES ,
    NON_ORGANIZATIONAL_BARRIERS and CHALLENGES , PLANNING , AWARENESS , the
    QUALITY_OF_EDUCATION , and LEARNING_QUALITY . conclusion : acknowledging FLIPPED_LEARNING
    , as AN_INDEPENDENT_APPROACH , by SENIOR_MANAGERS , providing and improving THE_QUALITY of
    E_LEARNING_INFRASTRUCTURE and FACILITIES , and improving MANAGEMENT_CAPABILITIES and
    PERFORMANCES through RECRUITING_PROFESSORS who are familiar with THIS_PHENOMENON can be of
    GREAT_BENEFIT in implementing THIS_APPROACH . 2021 , mazandaran university of medical
    sciences . all rights reserved .
    <BLANKLINE>


    >>> for i in range(40, len(mapping)):
    ...     print(textwrap.fill(mapping[i]["AB"], width=90))
    ...     print()
    purpose : THE_ARTICLE conducts the study IMPLEMENTATION of THE_SUBJECT_SUBJECT_MODEL in
    THE_CONDITIONS of MIXED_LEARNING . the article deals with THE_DEVELOPMENT of
    THE_SUBJECT_SUBJECT_MODEL in THE_CONDITIONS of BLENDED_LEARNING . methodology : we have
    shown THE_IMPORTANT_ROLE of BLENDED_LEARNING in THE_MAINTENANCE and DEVELOPMENT of
    THE_SUBJECT_SUBJECT_MODEL of INTERACTION between STUDENTS and TEACHERS .
    THE_IMPLEMENTATION of SUBJECT_SUBJECT_INTERACTION was considered on THE_EXAMPLE of the
    DISCIPLINE ' ' general and PROFESSIONAL_PEDAGOGY ' ' , THE_ELECTRONIC_COURSE of which is
    presented on THE_MOODLE_PLATFORM . result : to comply with THE_SUBJECT_SUBJECT_MODEL of
    INTERACTION between THE_TEACHER and STUDENTS , it is important to periodically monitor
    THE_DEVELOPED_ELECTRONIC_COURSES within THE_FRAMEWORK of BLENDED_LEARNING . therefore ,
    THE_AUTHORS propose THE_CRITERIA by which it should be carried out and THE_MAIN_STAGES of
    PREPARATION of THE_COURSE . applications : this research can be used for THE_UNIVERSITIES
    , TEACHERS and EDUCATION_STUDENTS . novelty / originality : in this research , THE_MODEL
    of THE_SUBJECT_SUBJECT_MODEL in THE_CONDITIONS of MIXED_LEARNING is presented in
    A_COMPREHENSIVE_AND_COMPLETE_MANNER . ZANFIR
    <BLANKLINE>

"""
