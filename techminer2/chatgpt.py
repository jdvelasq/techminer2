#
# ChatGPT prompts for bibliometric analysis
#
# This file contains functions for generating prompts for bibliometric analysis
# using ChatGPT.
#


def generate_prompt(table):
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
