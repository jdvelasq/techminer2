"""
Time report
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> time_report(directory)
          num_documents  local_citations  global_citations  \\
pub_year                                                     
2015                  9               52                83   
2016                 28              250               598   
2017                 73             1028              1370   
2018                132              713              1801   
2019                226              513              1493   
2020                411              381              1349   
2021                415              117               325   
2022                  7                0                 0   
-
          mean_global_citations  mean_local_citations  cum_num_documents  \\
pub_year                                                                   
2015                   9.222222              5.777778                  9   
2016                  21.357143              8.928571                 37   
2017                  18.767123             14.082192                110   
2018                  13.643939              5.401515                242   
2019                   6.606195              2.269912                468   
2020                   3.282238              0.927007                879   
2021                   0.783133              0.281928               1294   
2022                   0.000000              0.000000               1301   
-
          cum_global_citations  cum_local_citations  
pub_year                                             
2015                        83                   52  
2016                       681                  302  
2017                      2051                 1330  
2018                      3852                 2043  
2019                      5345                 2556  
2020                      6694                 2937  
2021                      7019                 3054  
2022                      7019                 3054 


"""
from .lib import load_filtered_documents


def time_report(directory):
    report = load_filtered_documents(directory)
    report = report.assign(num_documents=1)
    report = report[
        [
            "pub_year",
            "num_documents",
            "local_citations",
            "global_citations",
        ]
    ].copy()
    report = report.groupby("pub_year", as_index=True).sum()
    report = report.sort_index(ascending=True, axis="index")
    report = report.assign(
        mean_global_citations=report.global_citations / report.num_documents
    )
    report = report.assign(
        mean_local_citations=report.local_citations / report.num_documents
    )
    report = report.assign(cum_num_documents=report.num_documents.cumsum())
    report = report.assign(cum_global_citations=report.global_citations.cumsum())
    report = report.assign(cum_local_citations=report.local_citations.cumsum())

    return report
