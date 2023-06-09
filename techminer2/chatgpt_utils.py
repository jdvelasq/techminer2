"""
This module define the texts for the prompts used in the ChatGPT model 
for the analysis of the data extracted by the techminer2 package.


"""

HEADER = "Your task is generate a short analysis for a research paper. "

#
#  PROMPTS
#
SCIENTPY_BAR_GRAPH_TREND_ANALYSIS = (
    HEADER
    + """\
Your task is to generate a short analysis of top {n_rows} terms with the \
highest average growth rate for a research paper. The average growth rate \
is calculated comparing the number of documents published {period1} with the \
number of documents published {period2} for each item in the field \
'{field}'. Analyze the table below, delimited by triple backticks, in at \
most 30 words. In the table, the column 'OCC' indicates the number of \
documents in which each item of the field '{field}'appears. Use the \
information in the table to draw conclusions about average growth rate and \
relevante of each item in the field. In your analysis, be sure to describe \
in a clear and concise way, any findings or any patterns you observe, and \
identify any outliers or anomalies in the table."""
)


def generate_prompt_bibliographic_indicators(table):
    """Generate a prompt for bibliometric analysis.

    Parameters
    ----------
    table : pandas.DataFrame
        A dataframe with the topics extracted from the specified
        criterion and its associated bibliometric indicators.

    Returns
    -------
    str
        A prompt for bibliometric analysis.

    """
    prompt = f"""\
Analyze the table below, which provides bibliographic indicators for a \
collection of research articles. Identify any notable patterns, trends, or \
outliers in the data, and discuss their implications for the research field. \
Be sure to provide a concise summary of your findings in no more than 150 \
words.

{table.to_markdown()}

"""
    return prompt


def generate_prompt_for_matrix(obj):
    """Generate a prompt for bibliometric analysis."""
    prompt = f"""\
Analyze the table below which contains values for the metric {obj.metric_}. \
The columns of the table correspond to {obj.criterion_for_columns_}, and the \
rows correspond to {obj.criterion_for_rows_}. Identify any notable patterns, \
trends, or outliers in the data, and discuss their implications for the \
research field. Be sure to provide a concise summary of your findings in no \
more than 150 words.

{obj.matrix_.to_markdown()}

"""
    return prompt
