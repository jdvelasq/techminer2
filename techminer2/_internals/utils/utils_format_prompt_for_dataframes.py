# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=missing-docstring
"""Format chatbot prompt for dataframes."""
import textwrap

TEXTWRAP_WIDTH = 73


def _utils_format_prompt_for_dataframes(
    main_text: str,
    df_text: str,
):
    """:meta private:"""

    prompt = textwrap.fill(main_text, width=TEXTWRAP_WIDTH)
    prompt = prompt.replace("\n", " \\\n")
    return prompt + f"\n\nTable:\n```\n{df_text}\n```\n"
