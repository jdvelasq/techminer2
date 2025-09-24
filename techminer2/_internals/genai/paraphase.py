# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches

import os

from openai import OpenAI

from techminer2._internals.load_template import internal_load_template


def internal__paraphrase(text):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    template = internal_load_template("internals.genai.paraphrase.txt")
    prompt = template.format(text=text)

    try:
        response = client.responses.create(
            model="gpt-4-turbo",
            input=prompt,
        )
        answer = response.output_text
        return answer

    except Exception as e:
        print(f"Error processing: {e}")
