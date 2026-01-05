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
    >>> IngestScopus(root_directory="examples/punctuation/", ).run() # doctest: +ELLIPSIS
    N...


    >>> from techminer2.database.tools import Query
    >>> df = (
    ...     Query()
    ...     #
    ...     .with_query_expression("SELECT tokenized_abstract, abstract FROM database;")
    ...     #
    ...     .where_root_directory("examples/punctuation/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )

    >>> import textwrap
    >>> for _, row in df.iterrows():
    ...     print(textwrap.fill(row['tokenized_abstract'], width=90))
    ...     print()
    ...     print(textwrap.fill(row['abstract'], width=90))
    ...     print()
    this paper studies the profit distribution of wind power , thermal power and electric
    vehicles in the power market , based on the cooperative game theory , the combined
    operation mode of wind turbine , thermal power unit and electric vehicle for electric
    vehicle charging and eliminating wind is designed . the optimal scheduling model under the
    three party alliance , two party alliance and non alliance mode is constructed with the
    goal of maximizing the profit of the alliance . the profit results of different operating
    modes are used as the basis for distribution , adopting shapley value , banzhaf value ,
    and solidarity value allocation strategy for three party alliance profit distribution ,
    and set the core theory and mdp indicators to determine the possibility of cooperation and
    the intensity of cooperation intention under each allocation strategy . the mixed integer
    programming technique and cplex optimization software are used to simulate the simulation
    . the results show that the three party joint model can promote the consumption and
    development of wind power , and the cooperation under the shapely value allocation
    strategy can be established . the cooperation intentions of all members of the alliance
    are strong . 2018 ieee .
    <BLANKLINE>
    this paper studies THE_PROFIT_DISTRIBUTION of WIND_POWER , THERMAL_POWER and
    ELECTRIC_VEHICLES in THE_POWER_MARKET , based on THE_COOPERATIVE_GAME_THEORY ,
    THE_COMBINED_OPERATION_MODE of WIND_TURBINE , THERMAL_POWER_UNIT and ELECTRIC_VEHICLE for
    ELECTRIC_VEHICLE_CHARGING and eliminating WIND is designed . THE_OPTIMAL_SCHEDULING_MODEL
    under THE_THREE_PARTY_ALLIANCE , TWO_PARTY_ALLIANCE and NON_ALLIANCE_MODE is constructed
    with THE_GOAL of maximizing THE_PROFIT of THE_ALLIANCE . THE_PROFIT_RESULTS of
    DIFFERENT_OPERATING_MODES are used as THE_BASIS for DISTRIBUTION , adopting SHAPLEY_VALUE
    , BANZHAF_VALUE , and SOLIDARITY_VALUE_ALLOCATION_STRATEGY for
    THREE_PARTY_ALLIANCE_PROFIT_DISTRIBUTION , and set THE_CORE_THEORY and MDP_INDICATORS to
    determine THE_POSSIBILITY of COOPERATION and THE_INTENSITY of COOPERATION_INTENTION under
    EACH_ALLOCATION_STRATEGY . THE_MIXED_INTEGER_PROGRAMMING_TECHNIQUE and
    CPLEX_OPTIMIZATION_SOFTWARE are used to simulate THE_SIMULATION . THE_RESULTS show that
    THE_THREE_PARTY_JOINT_MODEL can promote THE_CONSUMPTION and DEVELOPMENT of WIND_POWER ,
    and THE_COOPERATION under THE_SHAPELY_VALUE_ALLOCATION_STRATEGY can be established .
    THE_COOPERATION_INTENTIONS of ALL_MEMBERS of THE_ALLIANCE are strong . 2018 ieee .
    <BLANKLINE>
    the wind energy market is in continuous development since the last decade . this market
    accounts more than 600 gw of installed wind turbines in 2018 , with 14 gw of onshore wind
    turbines installed in france . with the new act of 17 august 2015 on energy transition for
    green growth , france committed fully to energy transformation , with an objective of
    national renewable energy share of 35 % in 2030 . thus , incentives and many provisions
    were applied to enhance public and private investments in mature renewable energy sources
    . within these energy sources , the wind energy market gets a new twist in pricing
    policies and new actors have emerged . the purpose of this paper is to describe the
    current state of art of pricing policies and describe the role of the industry ' s recent
    actors ( wind farm managers and manufacturers , aggregators , cre ... ) . these policies
    are then discussed to outline their opportunities and challenges in the french wind energy
    market . 2019
    <BLANKLINE>
    THE_WIND_ENERGY_MARKET is in CONTINUOUS_DEVELOPMENT since THE_LAST_DECADE . THIS_MARKET
    accounts more than 600 gw of INSTALLED_WIND_TURBINES in 2018 , with 14 gw of
    ONSHORE_WIND_TURBINES installed in FRANCE . with THE_NEW_ACT of 17 august 2015 on
    ENERGY_TRANSITION for GREEN_GROWTH , FRANCE committed fully to ENERGY_TRANSFORMATION ,
    with AN_OBJECTIVE of NATIONAL_RENEWABLE_ENERGY_SHARE of 35 % in 2030 . thus , INCENTIVES
    and MANY_PROVISIONS were applied to enhance PUBLIC_AND_PRIVATE_INVESTMENTS in
    MATURE_RENEWABLE_ENERGY_SOURCES . within THESE_ENERGY_SOURCES , THE_WIND_ENERGY_MARKET
    gets A_NEW_TWIST in PRICING_POLICIES and NEW_ACTORS have emerged . the purpose of this
    paper is to describe THE_CURRENT_STATE of ART of PRICING_POLICIES and describe THE_ROLE of
    the industry ' s RECENT_ACTORS ( WIND_FARM_MANAGERS and MANUFACTURERS , AGGREGATORS , cre
    ... ) . THESE_POLICIES are then discussed to outline their OPPORTUNITIES_AND_CHALLENGES in
    THE_FRENCH_WIND_ENERGY_MARKET . 2019
    <BLANKLINE>
    taiwan ' s energy transformation to change the power structure is a new energy policy for
    economic development , industrial upgrading and environmental preservation . this study
    investigates the possibility of evaluating the economic spillover effects and co2
    emissions to evaluate new energy policy objectives by investing in solar and wind power
    generation systems . the research results show that the short term solar investment in
    economic effects is superior to wind power generation , and the economic spillover
    increases the scale of co2 emissions . the main reason is that the high ratio of equipment
    for wind power generation comes from imports and reduces the spillover effect . observing
    the economic spillover effects of individual industries , solar investment has the largest
    increase in ' ' sewage treatment sector and resource recovery ' ' sectors , while wind
    investment has the largest increase in ' ' machinery related industries . ' ' the scale of
    co2 emissions in individual industries , solar investment has increased the most emissions
    by ' ' chemical ' ' sectors , and wind investment has increased by ' ' service industries
    . ' ' however , from a long term perspective , the industrial upgrading through economic
    restructuring and the low emission coefficient of wind power will greatly improve the
    economic spillover effect of wind investment and improve the environment . 2019 ,
    econjournals . all rights reserved .
    <BLANKLINE>
    taiwan ' s ENERGY_TRANSFORMATION to change THE_POWER_STRUCTURE is A_NEW_ENERGY_POLICY for
    ECONOMIC_DEVELOPMENT , INDUSTRIAL_UPGRADING and ENVIRONMENTAL_PRESERVATION . this study
    investigates THE_POSSIBILITY of evaluating THE_ECONOMIC_SPILLOVER_EFFECTS and co2
    emissions to evaluate NEW_ENERGY_POLICY_OBJECTIVES by investing in
    SOLAR_AND_WIND_POWER_GENERATION_SYSTEMS . THE_RESEARCH_RESULTS show that
    THE_SHORT_TERM_SOLAR_INVESTMENT in ECONOMIC_EFFECTS is superior to WIND_POWER_GENERATION ,
    and THE_ECONOMIC_SPILLOVER increases THE_SCALE of co2 emissions . THE_MAIN_REASON is that
    THE_HIGH_RATIO of EQUIPMENT for WIND_POWER_GENERATION comes from IMPORTS and reduces
    THE_SPILLOVER_EFFECT . observing THE_ECONOMIC_SPILLOVER_EFFECTS of INDIVIDUAL_INDUSTRIES ,
    SOLAR_INVESTMENT has THE_LARGEST_INCREASE in ' ' SEWAGE_TREATMENT_SECTOR and
    RESOURCE_RECOVERY ' ' sectors , while WIND_INVESTMENT has THE_LARGEST_INCREASE in ' '
    MACHINERY_RELATED_INDUSTRIES . ' ' THE_SCALE of co2 emissions in INDIVIDUAL_INDUSTRIES ,
    SOLAR_INVESTMENT has increased THE_MOST_EMISSIONS by ' ' chemical ' ' sectors , and
    WIND_INVESTMENT has increased by ' ' SERVICE_INDUSTRIES . ' ' however , from
    A_LONG_TERM_PERSPECTIVE , THE_INDUSTRIAL_UPGRADING through ECONOMIC_RESTRUCTURING and
    THE_LOW_EMISSION_COEFFICIENT of WIND_POWER will greatly improve
    THE_ECONOMIC_SPILLOVER_EFFECT of WIND_INVESTMENT and improve THE_ENVIRONMENT . 2019 ,
    econjournals . all rights reserved .
    <BLANKLINE>
    the influence of repair technology of wind turbine blades on the levelized costs of energy
    ( lcoe ) is analyzed . the contribution of minor and major failure to the operational
    expenditures ( opex ) of wind turbines is estimated . it is demonstrated that the minor
    failure , mainly , surface erosion , is the largest contributor to the unplanned repair ,
    12 times higher than structural failure . the shortening of material curing procedure can
    lead to the significant reduction of repair costs , and lcoe , and expand the so called '
    ' repair window . ' ' the analysis of the role of defects and voids in adhesives on the
    post repair lifetime of wind turbine blades and energy costs is carried out . using the
    continuum damage mechanics approach , it is demonstrated that the voids in adhesives
    drastically reduce the post repair lifetime of wind turbine blades . 2020 john wiley and
    sons , ltd .
    <BLANKLINE>
    THE_INFLUENCE of REPAIR_TECHNOLOGY of WIND_TURBINE_BLADES on THE_LEVELIZED_COSTS of ENERGY
    ( LCOE ) is analyzed . THE_CONTRIBUTION of MINOR_AND_MAJOR_FAILURE to
    THE_OPERATIONAL_EXPENDITURES ( OPEX ) of WIND_TURBINES is estimated . it is demonstrated
    that THE_MINOR_FAILURE , mainly , SURFACE_EROSION , is THE_LARGEST_CONTRIBUTOR to
    THE_UNPLANNED_REPAIR , 12 times higher than STRUCTURAL_FAILURE . THE_SHORTENING of
    MATERIAL_CURING_PROCEDURE can lead to THE_SIGNIFICANT_REDUCTION of REPAIR_COSTS , and LCOE
    , and expand the so called ' ' REPAIR_WINDOW . ' ' THE_ANALYSIS of THE_ROLE of DEFECTS and
    VOIDS in ADHESIVES on THE_POST_REPAIR_LIFETIME of WIND_TURBINE_BLADES and ENERGY_COSTS is
    carried out . using THE_CONTINUUM_DAMAGE_MECHANICS_APPROACH , it is demonstrated that
    THE_VOIDS in ADHESIVES drastically reduce THE_POST_REPAIR_LIFETIME of WIND_TURBINE_BLADES
    . 2020 john wiley and sons , ltd .
    <BLANKLINE>
    with the large scale and cluster development of offshore wind farms , it has become an
    inevitable trend for the development of offshore wind farm integration to form an
    intensive mode of interconnection of offshore power transmission network and land power
    network . aiming at the problem of fixed cost allocation for offshore wind farm
    integration system under multi stakeholder investment . , this paper proposes a fixed cost
    allocation method for offshore wind farm integration system considering the correlation of
    wind power output . first , considering the correlation between wind speeds in offshore
    wind farms , the pso is used to optimize the weight coefficient of the mixed copula
    function , and a wind speed correlation model based on the mixed copula function is
    established . secondly , for the fixed cost allocation problem of the offshore wind farm
    integration system , the fixed cost allocation method based on the shapley value solution
    of cooperative game is used to establish the cooperative game model of the fixed cost
    allocation of the offshore wind farm integration system . taking the ieee30 node standard
    test system as an case , the simulation results of the case verify the effectiveness and
    superiority of the proposed method . 2022 ieee .
    <BLANKLINE>
    with THE_LARGE_SCALE_AND_CLUSTER_DEVELOPMENT of OFFSHORE_WIND_FARMS , it has become
    AN_INEVITABLE_TREND for THE_DEVELOPMENT of OFFSHORE_WIND_FARM_INTEGRATION to form
    AN_INTENSIVE_MODE of INTERCONNECTION of OFFSHORE_POWER_TRANSMISSION_NETWORK and
    LAND_POWER_NETWORK . aiming at THE_PROBLEM of FIXED_COST_ALLOCATION for
    OFFSHORE_WIND_FARM_INTEGRATION_SYSTEM under MULTI_STAKEHOLDER_INVESTMENT . , this paper
    proposes A_FIXED_COST_ALLOCATION_METHOD for OFFSHORE_WIND_FARM_INTEGRATION_SYSTEM
    considering THE_CORRELATION of WIND_POWER_OUTPUT . first , considering THE_CORRELATION
    between WIND_SPEEDS in OFFSHORE_WIND_FARMS , THE_PSO is used to optimize
    THE_WEIGHT_COEFFICIENT of THE_MIXED_COPULA_FUNCTION , and A_WIND_SPEED_CORRELATION_MODEL
    based on THE_MIXED_COPULA_FUNCTION is established . secondly , for
    THE_FIXED_COST_ALLOCATION_PROBLEM of THE_OFFSHORE_WIND_FARM_INTEGRATION_SYSTEM ,
    THE_FIXED_COST_ALLOCATION_METHOD based on THE_SHAPLEY_VALUE_SOLUTION of COOPERATIVE_GAME
    is used to establish THE_COOPERATIVE_GAME_MODEL of THE_FIXED_COST_ALLOCATION of
    THE_OFFSHORE_WIND_FARM_INTEGRATION_SYSTEM . taking the ieee30 node STANDARD_TEST_SYSTEM as
    AN_CASE , THE_SIMULATION_RESULTS of THE_CASE verify THE_EFFECTIVENESS and SUPERIORITY of
    the proposed method . 2022 ieee .
    <BLANKLINE>
    catamount energy corporation ( cec ) was formed in 1986 as a non regulated subsidiary of
    central vermont public service , the largest utility in vermont . in may 2004 , cec
    announced a new wge partnership with marubeni corp . , a giant japanese industrial
    conglomerate . one of the justifications for wind generated electricity ( wge ) was that
    the world faced considerable uncertainty in terms of its future supplies of fossil fuels ,
    notably oil , and that this uncertainty would directly impact utilities ' ability to meet
    future demands for electricity . critics of wge ' s economics note that wherever it is
    used , it is accompanied by massive state subsidies . referring to denmark ' s wge
    experience , one american based critic claimed that the danish energy commission
    subsidizes nearly 30 % of the true cost of producing wind power in that country . the
    company was seeking regulatory approval for the development of a 27 turbine wind farm to
    produce wge atop glebe mountain , in south central vermont . 2006 by georgetown university
    , pew case study center , usa .
    <BLANKLINE>
    CATAMOUNT_ENERGY_CORPORATION ( CEC ) was formed in 1986 as A_NON_REGULATED_SUBSIDIARY of
    CENTRAL_VERMONT_PUBLIC_SERVICE , THE_LARGEST_UTILITY in VERMONT . in may 2004 , CEC
    announced A_NEW_WGE_PARTNERSHIP with MARUBENI_CORP . ,
    A_GIANT_JAPANESE_INDUSTRIAL_CONGLOMERATE . one of THE_JUSTIFICATIONS for
    WIND_GENERATED_ELECTRICITY ( WGE ) was that THE_WORLD faced CONSIDERABLE_UNCERTAINTY
    in_terms_of ITS_FUTURE_SUPPLIES of FOSSIL_FUELS , NOTABLY_OIL , and that THIS_UNCERTAINTY
    would directly IMPACT_UTILITIES ' ability to meet FUTURE_DEMANDS for ELECTRICITY . CRITICS
    of WGE_ECONOMICS_NOTE that wherever it is used , it is accompanied by
    MASSIVE_STATE_SUBSIDIES . referring to denmark ' s WGE_EXPERIENCE ,
    ONE_AMERICAN_BASED_CRITIC claimed that THE_DANISH_ENERGY_COMMISSION subsidizes nearly 30 %
    of THE_TRUE_COST of producing WIND_POWER in_that country . THE_COMPANY was seeking
    REGULATORY_APPROVAL for THE_DEVELOPMENT of a 27 turbine WIND_FARM to produce
    WGE_ATOP_GLEBE_MOUNTAIN , in SOUTH_CENTRAL_VERMONT . 2006 by georgetown university , pew
    case study center , usa .
    <BLANKLINE>
    this paper aims to improve the limitations of traditional economic evaluation methods of
    offshore wind power . the offshore wind power operation and maintenance process
    considering meteorological accessibility is first analyzed based on the impact of
    meteorological conditions . then , we propose the method of calculating economic
    evaluation indexes including downtime , power loss , wind farms availability , operation
    and maintenance cost . the benefit simulation model of offshore wind power operation and
    maintenance is established based on anylogic platform . the real time status of wind
    turbines , ships and personnel and the statistics of various economic evaluation indexes
    are simulated to evaluate the economic benefits of operation and maintenance of offshore
    wind power farms . finally , the case results show that the proposed model can simulate
    the operation and maintenance process of offshore wind power farms and accurately
    calculate the key indicators such as downtime , power loss , wind farm availability ,
    operation and maintenance cost . the impact of offshore meteorological conditions on the
    economic effect is truthfully reflected , which provides technical reference for the
    operation and maintenance of offshore wind power farms . 2023 science press . all rights
    reserved .
    <BLANKLINE>
    this paper aims to improve THE_LIMITATIONS of TRADITIONAL_ECONOMIC_EVALUATION_METHODS of
    OFFSHORE_WIND_POWER . THE_OFFSHORE_WIND_POWER_OPERATION_AND_MAINTENANCE_PROCESS
    considering METEOROLOGICAL_ACCESSIBILITY is first analyzed based on THE_IMPACT of
    METEOROLOGICAL_CONDITIONS . then , we propose THE_METHOD of calculating
    ECONOMIC_EVALUATION_INDEXES including DOWNTIME , POWER_LOSS , WIND_FARMS_AVAILABILITY ,
    OPERATION_AND_MAINTENANCE_COST . THE_BENEFIT_SIMULATION_MODEL of offshore
    WIND_POWER_OPERATION_AND_MAINTENANCE is established based on ANYLOGIC_PLATFORM .
    THE_REAL_TIME_STATUS of WIND_TURBINES , SHIPS and PERSONNEL and THE_STATISTICS of
    VARIOUS_ECONOMIC_EVALUATION_INDEXES are simulated to evaluate THE_ECONOMIC_BENEFITS of
    OPERATION_AND_MAINTENANCE of OFFSHORE_WIND_POWER_FARMS . finally , THE_CASE results show
    that THE_PROPOSED_MODEL can simulate THE_OPERATION_AND_MAINTENANCE_PROCESS of
    OFFSHORE_WIND_POWER_FARMS and accurately calculate THE_KEY_INDICATORS such_as DOWNTIME ,
    POWER_LOSS , WIND_FARM_AVAILABILITY , OPERATION_AND_MAINTENANCE_COST . THE_IMPACT of
    OFFSHORE_METEOROLOGICAL_CONDITIONS on THE_ECONOMIC_EFFECT is truthfully reflected , which
    provides TECHNICAL_REFERENCE for the OPERATION_AND_MAINTENANCE of
    OFFSHORE_WIND_POWER_FARMS . 2023 science press . all rights reserved .
    <BLANKLINE>
    with the recent introduction of wind power generation of various scales due to its promise
    as a green energy resource , effectively managing the risk of fluctuations in wind power
    generation revenues has become an important issue . against this background , this study
    introduces several weather derivatives based on wind speed and temperature as underlying
    assets and examines their effectiveness . in particular , we propose new standardized
    derivatives with higher order monomial payoff functions , such as ' ' wind speed cubic
    derivatives ' ' and ' ' wind speed and temperature cross derivatives . ' ' in contrast to
    the existing nonparametric derivatives , the minimum variance hedging problem to find the
    optimal contract amount of these standardized derivatives is reduced to estimating a
    linear regression . we also develop a market trading model to put the proposed
    standardized derivatives into practical use and clarify the real world implications of
    standardizing weather derivatives . furthermore , to make trading more efficient , we
    propose a ' ' product selection ' ' strategy utilizing the ' ' variable selection ' '
    approach of lasso regression . empirical analysis confirms hedging effectiveness
    comparable to existing nonparametric derivatives and reveals the effectiveness of the
    proposed derivatives standardization scheme as well as their trading strategies . the
    author ( s ) , under exclusive license to springer nature switzerland ag 2023 .
    <BLANKLINE>
    with THE_RECENT_INTRODUCTION of WIND_POWER_GENERATION of VARIOUS_SCALES due_to ITS_PROMISE
    as A_GREEN_ENERGY_RESOURCE , effectively managing THE_RISK of FLUCTUATIONS in
    WIND_POWER_GENERATION_REVENUES has become AN_IMPORTANT_ISSUE . against THIS_BACKGROUND ,
    this study introduces SEVERAL_WEATHER_DERIVATIVES based on WIND_SPEED and TEMPERATURE as
    UNDERLYING_ASSETS and examines THEIR_EFFECTIVENESS . in_particular , we propose
    NEW_STANDARDIZED_DERIVATIVES with HIGHER_ORDER_MONOMIAL_PAYOFF_FUNCTIONS , such_as ' '
    WIND_SPEED_CUBIC_DERIVATIVES ' ' and ' ' WIND_SPEED and TEMPERATURE_CROSS_DERIVATIVES . '
    ' in_contrast to THE_EXISTING_NONPARAMETRIC_DERIVATIVES ,
    THE_MINIMUM_VARIANCE_HEDGING_PROBLEM to find THE_OPTIMAL_CONTRACT_AMOUNT of
    THESE_STANDARDIZED_DERIVATIVES is reduced to estimating A_LINEAR_REGRESSION . we also
    develop A_MARKET_TRADING_MODEL to put THE_PROPOSED_STANDARDIZED_DERIVATIVES into
    PRACTICAL_USE and clarify THE_REAL_WORLD_IMPLICATIONS of standardizing WEATHER_DERIVATIVES
    . furthermore , to make TRADING more efficient , we propose a ' ' PRODUCT_SELECTION ' '
    strategy utilizing the ' ' VARIABLE_SELECTION ' ' APPROACH of LASSO_REGRESSION .
    EMPIRICAL_ANALYSIS_CONFIRMS_HEDGING_EFFECTIVENESS comparable to
    EXISTING_NONPARAMETRIC_DERIVATIVES and reveals THE_EFFECTIVENESS of
    THE_PROPOSED_DERIVATIVES_STANDARDIZATION_SCHEME as_well_as THEIR_TRADING_STRATEGIES . the
    author ( s ) , under exclusive license to springer nature switzerland ag 2023 .
    <BLANKLINE>
    the strong uncertainty of wind power output seriously hinders the accurate implementation
    of the electricity market reporting plan , and the resulting deviation power may make the
    wind energy storage combined system ( wcs ) bear high deviation penalty and wind
    curtailment loss . in order to reduce the economic loss caused by the wrong bidding
    decision , a multi time scale market bidding model of wcs is established . based on the
    existing market mechanism of the united states , the benefit and cost models of wcs
    participating in the energy market and frequency regulation auxiliary service market are
    established . in order to improve the accuracy of wcs ' s bidding strategy , a
    quantitative model is carried out for the uncertainty of wind power output based on the
    copula function , based on which part of the energy storage output capacity is reserved ,
    so as to reduce the economic risk caused by the deviation power . with the goal of
    maximizing the expected net income of wcs , the day ahead bidding strategies for energy
    market and frequency regulation auxiliary service market are formulated , and the bidding
    decisions are revised on the basis of ultra short term wind power forecast data in the
    intra day stage . a multi time scale market participation strategy of wcs is proposed
    considering the uncertainty of wind power output . taking a practical wcs in china as an
    example , the results show that the proposed strategy can effectively improve the economic
    benefits of wcs and avoid the waste of resources . 2024 electric power automation
    equipment press . all rights reserved .
    <BLANKLINE>
    THE_STRONG_UNCERTAINTY of WIND_POWER_OUTPUT seriously hinders THE_ACCURATE_IMPLEMENTATION
    of THE_ELECTRICITY_MARKET_REPORTING_PLAN , and THE_RESULTING_DEVIATION_POWER may make
    THE_WIND_ENERGY_STORAGE_COMBINED_SYSTEM ( WCS ) bear HIGH_DEVIATION_PENALTY and
    WIND_CURTAILMENT_LOSS . in_order_to reduce THE_ECONOMIC_LOSS caused by
    THE_WRONG_BIDDING_DECISION , A_MULTI_TIME_SCALE_MARKET_BIDDING_MODEL of WCS is established
    . based on THE_EXISTING_MARKET_MECHANISM of THE_UNITED_STATES ,
    THE_BENEFIT_AND_COST_MODELS of WCS participating in
    THE_ENERGY_MARKET_AND_FREQUENCY_REGULATION_AUXILIARY_SERVICE_MARKET are established .
    in_order_to improve THE_ACCURACY of WCS ' s BIDDING_STRATEGY , A_QUANTITATIVE_MODEL is
    carried out for THE_UNCERTAINTY of WIND_POWER_OUTPUT based on THE_COPULA_FUNCTION , based
    on WHICH_PART of THE_ENERGY_STORAGE_OUTPUT_CAPACITY is reserved , so_as_to reduce
    THE_ECONOMIC_RISK caused by THE_DEVIATION_POWER . with THE_GOAL of maximizing
    THE_EXPECTED_NET_INCOME of WCS , THE_DAY ahead bidding STRATEGIES for ENERGY_MARKET and
    FREQUENCY_REGULATION_AUXILIARY_SERVICE_MARKET are formulated , and THE_BIDDING_DECISIONS
    are revised on THE_BASIS of ULTRA_SHORT_TERM_WIND_POWER_FORECAST_DATA in
    THE_INTRA_DAY_STAGE . A_MULTI_TIME_SCALE_MARKET_PARTICIPATION_STRATEGY of WCS is proposed
    considering THE_UNCERTAINTY of WIND_POWER_OUTPUT . taking A_PRACTICAL_WCS in CHINA as
    AN_EXAMPLE , THE_RESULTS show that THE_PROPOSED_STRATEGY can effectively improve
    THE_ECONOMIC_BENEFITS of WCS and avoid the WASTE_OF_RESOURCES . 2024 electric power
    automation equipment press . all rights reserved .
    <BLANKLINE>
    in the context of large scale and medium and long distance offshore wind power development
    , a compre hensive economic comparison has been made between fractional frequency
    transmission system ( ffts ) and other transmission systems . an economic evaluation model
    based on the levelized cost of electricity ( lcoe ) for the ffts system . this model takes
    into account the lifecycle , initial resource investment , operational losses , routine
    mainte nance , decommissioning costs , and tax liabilities . by using an offshore wind
    farm as a case study , the paper ana lyzes the economic intervals of the ffts and economic
    variability under various scenarios . the findings reveal that , for a 500 mw offshore
    wind farm , the economic interval extends from 80 to 250 kilometers . moreover , this
    range ex hibits a notable degree of stability and demonstrates superior economic viability
    in contrast to traditional transmis sion systems across multiple scenarios . 2024
    editorial department of zhejiang electric power . all rights reserved .
    <BLANKLINE>
    in the context of LARGE_SCALE_AND_MEDIUM_AND_LONG_DISTANCE_OFFSHORE_WIND_POWER_DEVELOPMENT
    , A_COMPRE_HENSIVE_ECONOMIC_COMPARISON has been made between
    FRACTIONAL_FREQUENCY_TRANSMISSION_SYSTEM ( FFTS ) and OTHER_TRANSMISSION_SYSTEMS .
    AN_ECONOMIC_EVALUATION_MODEL based on the LEVELIZED_COST_OF_ELECTRICITY ( LCOE ) for
    THE_FFTS_SYSTEM . THIS_MODEL takes into ACCOUNT THE_LIFECYCLE ,
    INITIAL_RESOURCE_INVESTMENT , OPERATIONAL_LOSSES , ROUTINE_MAINTE_NANCE ,
    DECOMMISSIONING_COSTS , and TAX_LIABILITIES . by using AN_OFFSHORE_WIND_FARM as
    A_CASE_STUDY , the PAPER_ANA_LYZES THE_ECONOMIC_INTERVALS of
    THE_FFTS_AND_ECONOMIC_VARIABILITY under VARIOUS_SCENARIOS . the findings reveal that , for
    a 500 mw OFFSHORE_WIND_FARM , THE_ECONOMIC_INTERVAL extends from 80 to 250 kilometers .
    moreover , this RANGE_EX_HIBITS a NOTABLE_DEGREE of STABILITY and demonstrates
    SUPERIOR_ECONOMIC_VIABILITY in_contrast to TRADITIONAL_TRANSMIS_SION_SYSTEMS across
    MULTIPLE_SCENARIOS . 2024 editorial department of zhejiang electric power . all rights
    reserved .
    <BLANKLINE>
    wind farm clusters can enhance their operational profitability while supporting grid
    frequency regulation by participating in frequency regulation markets through the leasing
    of energy storage . to achieve this , a game theoretic optimization bidding model is
    proposed for leasing energy storage of wind farm clusters , considering fre quency
    regulation performance indicator assessment . the model consists of two layers : the upper
    layer models the bidding process in the frequency regulation market with multiple
    participants , while the lower layer models a leader follower game between energy storage
    lessors and wind farm clusters regarding leasing price and capacity . in this game , the
    energy storage operator acts as the leader , setting the leasing price in response to the
    leasing plan of wind farm clusters , and the wind farm clusters , as the follower , adjust
    the leasing plan according to the price . addition ally , an evolutionary threshold public
    goods game model is embedded within the wind farm clusters to address the cooperation
    dilemma caused by selfish behavior among individual members . by united solution of the
    model , the bidding strategy for leasing energy storage capacity and participating in the
    frequency regulation market is obtained . the case study results demonstrate that the
    proposed strategy effectively resolves the cooperation dilemma and en hances the overall
    profitability of the wind farm clusters . 2024 editorial department of zhejiang electric
    power . all rights reserved .
    <BLANKLINE>
    WIND_FARM_CLUSTERS can enhance THEIR_OPERATIONAL_PROFITABILITY while supporting
    GRID_FREQUENCY_REGULATION by participating in FREQUENCY_REGULATION_MARKETS through
    THE_LEASING of ENERGY_STORAGE . to achieve this ,
    A_GAME_THEORETIC_OPTIMIZATION_BIDDING_MODEL is proposed for LEASING_ENERGY_STORAGE of
    WIND_FARM_CLUSTERS , considering FRE_QUENCY_REGULATION_PERFORMANCE_INDICATOR_ASSESSMENT .
    THE_MODEL consists of TWO_LAYERS : the UPPER_LAYER_MODELS THE_BIDDING_PROCESS in
    THE_FREQUENCY_REGULATION_MARKET with MULTIPLE_PARTICIPANTS , while the lower LAYER_MODELS
    A_LEADER_FOLLOWER_GAME between ENERGY_STORAGE_LESSORS and WIND_FARM_CLUSTERS regarding
    LEASING_PRICE and CAPACITY . in THIS_GAME , THE_ENERGY_STORAGE_OPERATOR acts as THE_LEADER
    , setting THE_LEASING_PRICE in response to THE_LEASING_PLAN of WIND_FARM_CLUSTERS , and
    THE_WIND_FARM_CLUSTERS , as THE_FOLLOWER , adjust THE_LEASING_PLAN according to THE_PRICE
    . ADDITION_ALLY , AN_EVOLUTIONARY_THRESHOLD_PUBLIC_GOODS_GAME_MODEL is embedded within
    THE_WIND_FARM_CLUSTERS to address THE_COOPERATION_DILEMMA caused by SELFISH_BEHAVIOR among
    INDIVIDUAL_MEMBERS . by UNITED_SOLUTION of THE_MODEL , THE_BIDDING_STRATEGY for
    LEASING_ENERGY_STORAGE_CAPACITY and participating in THE_FREQUENCY_REGULATION_MARKET is
    obtained . THE_CASE_STUDY_RESULTS demonstrate that THE_PROPOSED_STRATEGY effectively
    resolves THE_COOPERATION_DILEMMA and EN_HANCES THE_OVERALL_PROFITABILITY of
    THE_WIND_FARM_CLUSTERS . 2024 editorial department of zhejiang electric power . all rights
    reserved .
    <BLANKLINE>




    # >>> import textwrap
    # >>> from techminer2.database.tools import RecordMapping
    # >>> mapping = (
    # ...     RecordMapping()
    # ...     #
    # ...     .where_root_directory("examples/punctuation/")
    # ...     .where_database("main")
    # ...     .where_record_years_range(None, None)
    # ...     .where_record_citations_range(None, None)
    # ...     .where_records_match(None)
    # ...     .where_records_ordered_by("global_cited_by_highest")
    # ...     .run()
    # ... )

    # >>> import re
    # >>> texts = [mapping[i]["AB"] for i in range(len(mapping))]
    # >>> texts = [textwrap.fill(text, width=90) for text in texts]
    # >>> texts = [line for text in texts for line in text.splitlines()]
    # >>> texts = [
    # ...     text
    # ...     for text in texts
    # ...     if re.search(r"[A-Z],[A-Z]", text)] or re.search(r"[A-Z]\. ", text)
    # ... ]
    # >>> for text in texts: print(text)




"""
