"""Format chatbot prompt for paragraphs."""

import textwrap

TEXTWRAP_WIDTH = 73


def _utils_format_prompt_for_paragraphs(main_text, secondary_text, paragraphs):
    """Generate prompt for table analysis."""

    text = ""
    counter = 0
    for i_paragraph, (paragraph, title) in enumerate(zip(paragraphs, paragraphs.index)):
        #
        #
        if paragraph is None:
            continue
        #
        # Header counter
        counter += 1
        if counter > 5:
            counter = 1
            if i_paragraph < len(paragraphs) - 1:
                text += "-" * 75 + "\n\n"
                text += secondary_text
                text += "--\n\n"

        else:
            text += "--\n\n"

        #
        # Text:
        paragraph_text = textwrap.fill(paragraph, width=TEXTWRAP_WIDTH)
        text += f"Record-No: {i_paragraph+1}\n"
        text += f"Artile: {title}\n"
        text += f"Text:```\n{paragraph_text}\n```\n\n"

    return main_text + text
