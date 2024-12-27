# flake8: noqa
# pylint: disable=import-outside-toplevel
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Basic Plot."""


class BasicPlotMixin:

    def set_default_title_texts(
        self,
        default_title_text,
        default_xaxes_title_text,
        default_yaxes_title_text,
    ):

        self.plot_params.title_text = (
            default_title_text
            if self.plot_params.title_text is None
            else self.plot_params.title_text
        )
        self.plot_params.xaxes_title_text = (
            default_xaxes_title_text
            if self.plot_params.xaxes_title_text is None
            else self.plot_params.xaxes_title_text
        )
        self.plot_params.yaxes_title_text = (
            default_yaxes_title_text
            if self.plot_params.yaxes_title_text is None
            else self.plot_params.yaxes_title_text
        )

        return self
