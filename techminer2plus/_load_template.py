"""
Load an HTML template.

"""

import os.path

from jinja2 import Template


def load_template(template_name):
    """Load an HTML template and render it with the data.

    Args:
        namepath (str): Path to the HTML template.


    Returns:
        str: HTML template.

    """
    module_path = os.path.dirname(__file__)
    template_path = os.path.join(module_path, "_templates", template_name)
    template = open(template_path, "r", encoding="utf-8").read()
    return Template(template)
