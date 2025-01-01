# flake8: noqa
# pylint: disable=too-few-public-methods
"""Defines co-citation network param filters."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CoCitationNetworkParams:
    """:meta private:"""

    unit_of_analysis: str = "cited_sources"
    top_n: int = 30
    citations_threshold: int = 0
    custom_terms: Optional[str] = None


class CoCitationNetworkParamsMixin:
    """:meta private:"""

    def set_citation_network_params(self, **kwargs):
        """:meta private:"""
        for key, value in kwargs.items():
            if hasattr(self.item_params, key):
                setattr(self.item_params, key, value)
            else:
                raise ValueError(f"Invalid parameter for AxesParams: {key}")
        return self
