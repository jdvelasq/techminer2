"""
This package module provides functions for selecting and processing documents.
"""

from .document_metrics import document_metrics
from .select_documents import select_documents

# Define what is available for public use
__all__ = [
    "document_metrics",
    "select_documents",
]

# Placeholder for future imports
# from .another_module import another_function
