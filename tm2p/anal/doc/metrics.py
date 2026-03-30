"""
Metrics
===============================================================================


Smoke tests:
    >>> from tm2p import ItemOrderBy
    >>> from tm2p.anal.doc import Metrics
    >>> df = (
    ...     Metrics()
    ...     #
    ...     # FIELD:
    ...     .having_items_in_top(10)
    ...     .having_items_ordered_by(ItemOrderBy.GCS)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     #
    ...     .run()
    ... )
    >>> type(df).__name__
    'DataFrame'
    >>> df.shape[0] > 1
    True
    >>> df.shape[1] > 1
    True
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                                                                             REC_ID                                                                                                                                                                                               TITLE_RAW                                                                  AUTH_NORM  GCS  LCS  YEAR
    0                                           Al-Sartawi A, 2024, J FINANC REP ACC, DOI 10.1108/JFRA-01-2024-0010                                                                   The diffusion of financial technology-enabled innovation in GCC-listed banks and its relationship with profitability and market value                                                               Al-Sartawi A  125    0  2024
    1  Singh B, 2024, HARNESSING BLOCKCHAIN-DIGIT TWIN FUSION SUSTAIN INVEST, P265, DOI 10.4018/9798369318782.ch011                                                              Revealing green finance mobilization: Harnessing FinTech and blockchain innovations to surmount barriers and foster new investment avenues                                                         Singh B; Kaunert C  110    0  2024
    2                                   Aloulou M, 2024, J FINANC REP ACC, V22, P289, DOI 10.1108/JFRA-05-2023-0224                                                                                Does FinTech adoption increase the diffusion rate of digital financial inclusion? A study of the banking industry sector                               Aloulou M; Grati R; Al-Qudah AA; Al-Okaily M  105    0  2024
    3                                     Roh T, 2024, ELECTRON COMMER RES, V24, P3, DOI 10.1007/s10660-021-09527-3                                                                                                                       What makes consumers trust and adopt fintech? An empirical investigation in China                                            Roh T; Yang YS; Xiao S; Park BI  102    0  2024
    4                                    Qin L, 2024, INT REV ECON FINANC, V89, P33, DOI 10.1016/j.iref.2023.07.056                                                                                                    Empirical evidence of fintech and green environment: Using the green finance as a mediating variable                               Qin L; Aziz G; Hussan MW; Qadeer A; Sarwar S   99    0  2024
    5                                      Sampat B, 2024, INT J BANK MARK, V42, P38, DOI 10.1108/IJBM-07-2022-0328                                                                                              The dark side of FinTech in financial services: a qualitative enquiry into FinTech developers’ perspective                                              Sampat B; Mogaji E; Nguyen NP   98    0  2024
    6                                           Liu K, 2024, RESOUR POLIC, V89, DOI 10.1016/j.resourpol.2023.104557                                                                            Exploring the Nexus between Fintech, natural resources, urbanization, and environment sustainability in China: A QARDL study  Liu K; Mahmoud HA; Liu L; Halteh K; Arnone G; Khajimuratov NK; Alzoubi HM   95    0  2024
    7                                               Wang C, 2024, BUS STRATEG ENV, V33, P5776, DOI 10.1002/bse.3778                                                                                                          The impact of Fintech on corporate carbon emissions: Towards green and sustainable development                                  Wang C; Wang L; Zhao S; Yang C; Albitar K   87    0  2024
    8                                 Hasan F, 2024, ELECTRON COMMER RES, V24, P629, DOI 10.1007/s10660-023-09734-0                                                                                                 A comparative analysis between FinTech and traditional stock markets: using Russia and Ukraine war data                                Hasan F; Al-Okaily M; Choudhury T; Kayani U   86    0  2024
    9                                         Sadiq M, 2024, RESOUR POLIC, V88, DOI 10.1016/j.resourpol.2023.104494  Role of fintech, green finance, and natural resource rents in sustainable climate change in China. Mediating role of environmental regulations and government interventions in the pre-post COVID eras          Sadiq M; Paramaiah C; Joseph R; Dong Z; Nawaz MA; Khajimuratov NK   84    0  2024


    >>> from pprint import pprint
    >>> pprint(df.columns.tolist())


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access import load_filtered_main_csv_zip

from .column import AUTH, GCS, LCS, REC_ID, TITLE, YEAR


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        df = load_filtered_main_csv_zip(params=self.params)
        df = df[
            [
                REC_ID,
                TITLE,
                AUTH,
                GCS,
                LCS,
                YEAR,
            ]
        ].dropna()
        top_n = int(self.params.top_n) if self.params.top_n is not None else 0
        df = df.head(top_n)
        df = df.reset_index(drop=True)

        return df
