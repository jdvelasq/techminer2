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
    N...

    >>> import textwrap
    >>> from techminer2.database.tools import RecordMapping
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

    >>> texts = [mapping[i]["AB"] for i in range(len(mapping))]
    >>> texts = [textwrap.fill(text, width=90) for text in texts]
    >>> texts = [line for text in texts for line in text.splitlines()]
    >>> texts = [text for text in texts if "." in text and ":" in text]
    >>> for text in texts: print(text)
    in NURSING_CURRICULA . objectives : THE_AIMS of THIS_SYSTEMATIC_REVIEW were to examine how
    THIS_STYLE of TEACHING . data sources : FIVE_DATABASES were searched and resulted in
    THE_RETRIEVAL of 21 papers : PUBMED , CINAHL , EMBASE , SCOPUS and ERIC . review methods :
    ALL_INCLUDED_STUDIES . results : THIS_SYSTEMATIC_REVIEW screened 21 titles and ABSTRACTS
    THE_INCLUDED_STUDIES . FIVE_STUDIES were identified and THEMES identified were :
    THE_FLIPPED_CLASSROOM . conclusions : use of THE_FLIPPED_CLASSROOM in
    TEACHING_CLINICAL_SKILLS is limited . design : MIXED_METHODS_SYSTEMATIC_REVIEW , which
    follows the joanna briggs institute user guide version 5. data sources :
    results : NINETEEN_PUBLISHED_PAPERS were identified . SEVENTEEN_PAPERS reported on
    THE_E_LEARNING_INTERVENTIONS used varied throughout ALL_THE_STUDIES . conclusion :
    purpose : BLENDED_LEARNING is rapidly emerging as A_DOMAIN for PRACTICE and RESEARCH .
    A_LEADING_MALAYSIAN_HIGHER_EDUCATION_INSTITUTION . methodology : the study employed
    also used to IDENTIFY_RESPONSES based on STUDENTS ' DEMOGRAPHIC_PROFILES . findings :
    on GENDER , AGE , ETHNICITY , FIELD of STUDY , and LEVEL of EDUCATION . significance :
    LEARNING_COURSES in A_UNIVERSITY_CONTEXT . implications for practice :
    DRY_EYE_SYMPTOMS in A_UNIVERSITY_BASED_POPULATION . background : to assess THE_PREVALENCE
    . methods : this study was performed using A_WEB_BASED_QUESTIONNAIRE that was distributed
    OSDI_QUESTIONNAIRE . results : A_TOTAL of 676 UNIVERSITY_STUDENTS with an average age_of
    SYMPTOMATIC_DRY_EYE_DISEASE . conclusion : THE_SYNCHRONOUS_HYBRID_LEARNING_ENVIRONMENT
    in A_BLENDED_LEARNING_ENVIRONMENT . method : THE_RESEARCH consists of TWO_STUDIES : STUDY
    CHINA . results : FINDINGS revealed that INTRINSIC_MOTIVATION , EXTRINSIC_MOTIVATION ,
    ACADEMIC_PERFORMANCE . discussion : in FUTURE_BLENDED_LEARNING_PRACTICES , it is essential
    or ' flipped ' . objectives : THE_PRIMARY_OBJECTIVES of THIS_REVIEW were to assess
    THEIR_COURSE_SATISFACTION . search methods : we identified RELEVANT_STUDIES by searching
    STUDY . intervention : we included ANY_EDUCATIONAL_INTERVENTION that included
    HPE ) sector ( E . g . , engineering , ECONOMICS ) . outcomes : THE_INCLUDED_STUDIES used
    QUALITATIVE_RESEARCH . data collection and analysis : TWO_MEMBERS of THE_REVIEW_TEAM
    THE_INCLUDED_STUDIES . main results : we found 5873 potentially RELEVANT_RECORDS , of
    interval [ ci ] = 0.25 to 0.90 , 2 : 1.16. i2 : 98 % . p < 0.00001 , 44 STUDIES , n = 7813
    , 2 : 0.76. i2 : 97 % . p < 0.00001 , 33 STUDIES , n = 5924 ) . all being LOW_CERTAINTY of
    compared to TRADITIONAL_CLASS_LEARNING ( smd = 0.48 , 95 % ci = 0.15 to 0.82 , 2 : 0.19 ,
    i2:89 % , p < 0.00001 , 8 STUDIES n = 1696 ) . all being LOW_CERTAINTY of EVIDENCE .
    promote LEARNING through A_WORK jointly led by TEACHERS_AND_STUDENTS . objective : to
    THE_RESEARCH_METHODOLOGY_COURSE . methodology : a prospective , longitudinal ,
    QUASI_EXPERIMENTAL_RESEARCH_DESIGN . place : HEALTH_SCIENCES_FACULTY , at
    A_PRIVATE_UNIVERSITY . participants : 81 UNDERGRADUATE_STUDENTS . interventions :
    OPEN_SOURCE_LEARNING_MANAGEMENT_SYSTEM . results : 93.8 % stated that THE_TEACHER and
    THE_FINAL_EXAM . conclusion : THE_FLIPPED_CLASSROOM_MODEL proved to be effective to
    made use of THE_FLIPPED_CLASSROOM_MODEL to deliver THE_TRAINING . evidence :
    and TIME_CONSTRAINTS within THE_CLINICAL_SETTING . discussion : EDUCATIONAL_NEEDS and
    PRIMARY_STUDIES . findings and originality : THE_MAJORITY of AUTHORS examined
    LANGUAGE_ACQUISITION . value : THE_RESULTS clarify for EDUCATORS that
    with ACCOUNT taken of UNIVERSITY_SPECIFIC_CHARACTER . methodology :
    SYSTEM_DEVELOPMENT . results : the developed by THE_AUTHOR_MODEL_RESULT in
    ORGANIZATIONAL_CHANGEABILITY of THE_EDUCATIONAL_ENVIRONMENT . applications of this study :
    AN_UNDERGRADUATE_COMPUTER_SCIENCE_COURSE . background : HANDS on WORK in
    design : the study compares THE_APPLICATION of FC and A_TRADITIONAL_METHODOLOGY . it
    encompasses TWO_ACADEMIC_COURSES and involves 434 STUDENTS and SIX_LECTURERS . findings :
    improve STUDENT_PERFORMANCE_VERSUS_TRADITIONAL_LECTURER led TEACHING_METHODS . objective :
    ONLINE_ONLY_DELIVERY affects THE_EFFICACY of THE_FLIPPED_CLASSROOM_APPROACH . method :
    DIFFERENT_METHODS . results : OVERALL_GRADES on THE_MODULE did not differ significantly
    by TEACHING entirely ONLINE . conclusion : THE_KEY_ADVANTAGES of
    of CLASSROOM_CONTEXT . teaching implications : using FLIPPED_CLASSROOMS can be
    into traditional , FACE_TO_FACE , UNDERGRADUATE_ENGINEERING_COURSES . background : MOOCS
    AN_OPEN_PROBLEM . research question : what is THE_MOST_EFFECTIVE_MOOC_BLENDING_STRATEGY
    THE_MBF_DESIGN_PRINCIPLES can be implemented in PRACTICE . findings : THE_RESULTS suggest
    europe ' s COMPETENCIES . materials and methods : the research was modelled in
    . results : it was seen that THE_FLIPPED_CLASSROOM_MODEL had A_MORE_POSITIVE_EFFECT on
    higher in FAVOUR of THE_FLIPPED_CLASSROOM_MODEL . conclusion : this study provides
    THEIR_ADAPTATION_CHALLENGES . methods : THE_PRESENT_STUDY was A_MIXED_METHOD accomplished
    THEIR_FIRST_EXPERIENCE and OPINION of THE_FC . results : A_TOTAL of 234 QUESTIONNAIRES
    and i got THE_CHANCE to answer ' ' ( st . 6 ) . conclusion : THE_RESULTS showed that
    , including FACE_TO_FACE_LEARNING combined with ONLINE_LEARNING . objectives :
    following year ' s INTERNSHIP_SUBJECT . design : ANALYTICAL_STUDY of RETROSPECTIVE_COHORTS
    . settings : PHYSIOTHERAPY_UNIVERSITY_DEGREE_PROGRAM . participants :
    THREE_HUNDRED_STUDENTS working towards attaining PHYSIOTHERAPY_DEGREES . methods :
    ASYNCHRONOUS_ONLINE_COMPLEMENTARY_TRAINING during LOCKDOWN . results : THE_RESULTS show
    CLINICAL_PRACTICE_COMPETENCIES in PHYSIOTHERAPY_STUDENTS . contribution of the paper :
    TWO_EMERGING_UK_HIGHER_EDUCATION_INSTITUTIONS ( HEIS ) . design / methodology / approach :
    descriptively analysed . findings : the findings revealed that there is some
    THE_USE of BLENDED_TECHNOLOGY and A_FLIPPED_CLASSROOM . practical implications : the study
    and point to OPPORTUNITIES for IMPROVED_STUDENT_EXPERIENCE . originality / value : where
    purpose : in the era of INDUSTRY 4.0 , THE_RELEVANCE of WEBINAR_TUTORIALS , A_FORM of
    approach : this study employs A_MIXED_METHODS_APPROACH . in THE_FIRST_PHASE ,
    while QUANTITATIVE_DATA were evaluated using MANCOVA . findings : the findings demonstrate
    and MODULES . research limitations / implications : SOME_LIMITATIONS in this study need to
    also affected THE_INDEPENDENT_VARIABLES . practical implications : this study emphasizes
    social implications : THE_SOCIAL_IMPLICATIONS of THIS_STUDY are noteworthy . in the
    SOCIETAL_RESILIENCE in THE_FACE of TECHNOLOGICAL_ADVANCEMENTS . originality / value :
    THE_BLENDED_LEARNING_CURRICULA and ITS_INFLUENTIAL_FACTORS . objectives : to explore
    ITS_INFLUENTIAL_FACTORS . design : A_CONVERGENT_PARALLEL_MIXED_METHODS was used . DATA
    : the study was carried out in THE_NURSING_SCHOOL at A_UNIVERSITY in CHINA . PARTICIPANTS
    including STUDENTS undertaking ENTRY to THE_BLENDED_LEARNING_CURRICULA . methods : in
    to understand PARTICIPANTS ' COGNITIVE_ENGAGEMENT_EXPERIENCES . results :
    SOCIAL_INTERACTION ( = 0.358 , p < 0.001 ) . conclusions : THE_COGNITIVE_ENGAGEMENT of
    THE_INDIVIDUAL_AND_COLLABORATIVE_STUDY_HOURS needed to prepare for TBL . methods : we
    SELF_PERCEIVED_LEARNING . conclusions : THREE_WEEKS of LECTURES were replaced by TBL
    PROFESSIONAL_EXPECTATIONS . scholarly critique : this paper examines
    THE_TRANSITIONAL_AND_DEVELOPMENTAL_PATHWAY to achieve COMPETENCE . conclusion : working
    providing A_SOLID_FOUNDATION for UNDERSTANDING THE_CONTEXT of the study . method :
    HIGHER_EDUCATION . originality / value : THIS_STUDY stands out for
    ( he ) CONTEXT . design / methodology / approach : in A_RESEARCH_METHODS_MODULE , 140
    was VIDEO recorded within BOTH_THE_REAL_AND_VIRTUAL_SPACES . findings : ATTENDANCE was
    ultimately LEARNING_/_PRODUCTIVITY_OUTCOMES . originality / value : THIS_STUDY
    THE_FLIPPED_CLASSROOM_MODEL . materials and methods :
    THE_DIFFERENCES between THE_TWO_GROUPS . results : both LEARNING_MODEL_COHORTS filled out
    NO_STATISTICALLY_SIGNIFICANT_DIFFERENCE between THE_TWO_GROUPS . conclusions :
    on STUDENTS ' AVERSION_TO_LEARNING . subjects and methods : the study selected
    . results : THE_EFFECT of THE_FLIPPED_CLASSROOM_CIVICS_TEACHING_MODEL combined with
    THE_SUBJECTIVE_AVERSION to LEARNING is slightly weaker . conclusions :
    PERSONALITY_TEACHING_EFFICACY . findings : this study has proven THE_EFFECTS of
    applications : it need to WORK on A_TEACHING_PROCESS that aims to ENHANCE_CREATIVITY .
    carry out . objective : to develop A_SYSTEM of activitiesdesigned for THE_TEACHING of
    ACADEMIC_POSTGRADUATE_STUDIES . methods : A_RESEARCH with A_QUANTITATIVE_APPROACH is
    correlational , experimental and CROSS_SECTIONAL_TYPE . results : A_CONCEPTUAL_MAP was
    designed that showed THE_USE of VARIOUS_FORMATS and NAMES . conclusions : the
    INCREASED_STUDENT_SATISFACTION and improved OUTCOMES in MEDICAL_EDUCATION . objectives :
    BLENDED_LEARNING within MEDICAL_UNIVERSITIES . methods : a qualitative GROUNDED_THEORY (
    TRANSFERABILITY , and DEPENDABILITY . results : INTERVIEWS with 14 FACULTY_MEMBERS
    FACULTY_ENGAGEMENT in BLENDED_LEARNING . conclusions : THE_MODEL provides
    LEARNING_OUTCOMES are not satisfactory . objective : to solve THIS_PROBLEM , we integrated
    DESIGN_THINKING into THE_LARGE_CLASS flipped TEACHING . method : A_MIXED_METHODOLOGY (
    QUESTIONNAIRES , and CLASSROOM_ASSESSMENTS . results : ANALYSIS of 24 EMPATHY_MAPS
    LEARNING_BURDEN ( p 0.05 ) . conclusion : THE_LARGE_CLASS_FLIPPED_CLASSROOM model
    THE_NORMALE_LECTURE_MODEL at Y_UNIVERSITY . design / methodology / approach : using
    DATA_COLLECTION . findings : EFFECTIVE_STRATEGIES in LARGE_CLASS_STS_COURSE included
    INCREASED_STRESS and ANXIETY in LARGE_CLASS_SETTINGS . practical implications :
    LARGE_CLASSES . originality / value : this study contributes to THE_GROWING_BODY of
    as NO_EXCLUSIVE_TOOL focuses on HEALTH_SCIENCES_FACULTY_MEMBERS . materials and methods :
    . results : THE_FBL_TOOL has A_CRONBACH_ALPHA_COEFFICIENT of 0.867.
    A_SIGNIFICANT_POSITIVE_RELATIONSHIP with ITS_RESPECTIVE_FBL_FACTOR . conclusion : this
    EQUITABLE_AND_EFFECTIVE_EDUCATIONAL_OUTCOMES . objective : the objective of this study was
    A_SECONDARY_ANALYSIS of PUBLICLY_AVAILABLE_DATA . design : THIS_STUDY involved
    PROGRAM_LEVEL_DATA . main outcomes and measures : KEY_VARIABLES included INSTITUTION_TYPE
    PROGRAM_OUTCOMES . results : there are 33 HDPT_PROGRAMS at 25 UNIQUE_INSTITUTIONS in
    consistent with NATIONAL_AVERAGES . conclusion and relevance : HDPT_PROGRAMS demonstrate
    ENDED_QUESTIONS , were designed to gather INSIGHTS from EACH_GROUP . findings :
    DESIGN_INNOVATIVE_LEARNING_MODULES to ENHANCE_STUDENT_ENGAGEMENT . originality / value :
    AUSTRALIA_AND_NEW_ZEALAND , as documented in UNIVERSITY_WEBSITES . background :
    THESE_HYBRID_MASTER_DEGREES . methods : WEBSITES of MEMBERS of THE_COUNCIL of DEANS of
    CONTENT_ANALYSIS were used to generate THE_FINDINGS . results :
    MEDICAL_STUDENT_ORTHOPAEDIC_KNOWLEDGE . design : ORTHOACCESS 2.0 is a 16 week ,
    EMERGING_THEMES . setting : LECTURES were presented weekly in PERSON for STUDENTS at
    posted to THE_WEBSITE . participants : ORTHOACCESS 2.0 was hosted from JUNE to OCTOBER
    attended at_least 8/16 CASE_DISCUSSIONS . results : in THE_POST_CURRICULUM_SURVEY , 68 %
    n=44 ) . conclusions : this FLIPPED_CLASSROOM , BLENDED_LEARNING_CURRICULUM has improved
    FLIPPED_CLASSROOM model for THE_EMPOWERMENT of NEW_GRADUATE_NURSES ( NGNS ) . design :
    SINGLE_CENTER , PARALLEL_GROUP , RANDOMIZED_CONTROLLED_TRIAL . methods : the study was
    randomly assigned to THE_INTERVENTION_GROUP ( n : 32 ) and CONTROL_GROUP ( n : 32 ) .
    chi squared , and T_TESTS . results : the study determined that
    THE_INTERVENTION_GROUP was higher . conclusion : THE_EDUCATION_PROGRAM developed to
    OPINIONS . results : THE_MAJORITY of STUDENTS found FLIPPED_CLASSROOMS to be more
    as A_FLIPPED_CLASSROOM . conclusion : FLIPPED_CLASSROOM_TEACHING is acceptable and finds
    EXTRA_TIME and ENERGY by THE_FACILITATORS , especially initially . clinical significance :
    aim : to DESIGN and validate THE_FLIPPED_LEARNING_ASSESSMENT_SCALE . A_TOOL for assessing
    STUDENTS ' experience of FLIPPED_LEARNING . background : frequently , UNIVERSITY_STUDENTS
    THE_LEARNING_PROCESS . design : CROSS_SECTIONAL_DESCRIPTIVE_STUDY . methods :
    results : A_TOTAL of 455 STUDENTS completed THE_QUESTIONNAIRE . 373 women and 82 men . the
    acceptable , implying that THE_MODEL was validated . conclusion :
    ' experience of FLIPPED_LEARNING . impact : FLIPPED_LEARNING has been
    THIS_TEACHING_AND_LEARNING_METHODOLOGY . patient or public contribution : none . 2024 the
    IN_SERVICE_TRAINING_OF_EMPLOYEES , 2020 . materials and methods : A_QUALITATIVE_STUDY
    . results : flipped LEARNING_PROCESS in MAZANDARAN_UNIVERSITY_OF_MEDICAL_SCIENCES has 12
    QUALITY_OF_EDUCATION , and LEARNING_QUALITY . conclusion : acknowledging FLIPPED_LEARNING
    THE_SUBJECT_SUBJECT_MODEL in THE_CONDITIONS of BLENDED_LEARNING . methodology : we have
    presented on THE_MOODLE_PLATFORM . result : to comply with THE_SUBJECT_SUBJECT_MODEL of
    PREPARATION of THE_COURSE . applications : this research can be used for THE_UNIVERSITIES
    , TEACHERS and EDUCATION_STUDENTS . novelty / originality : in this research , THE_MODEL



"""
