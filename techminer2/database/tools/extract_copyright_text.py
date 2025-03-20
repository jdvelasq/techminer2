# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Extract Copyright Text
===============================================================================


Example:
    >>> from techminer2.database.tools import ExtractCopyrightText
    >>> text = ExtractCopyrightText(
    ...     pattern=None,
    ...     n_chars=90,
    ...     root_directory="example/",
    ... ).run()
    >>> for t in text[:5]: print(t)
    TORS , REGULATORS , etc . ) , who explore THE_FIELD of FINTECH . 2016 , the_author_(_s_) .
    E_SERVICE_OFFERINGS of FINTECH START_UP in A_STRUCTURED_MANNER . 2017 , the_author_(_s_) .
    RIOD short , we cannot rule out that OUR_FINDINGS are spurious . 2017 , the_author_(_s_) .
    ACTIVE_POLICIES can INFLUENCE THE_EMERGENCE of THIS_NEW_SECTOR . 2018 , the_author_(_s_) .
    _SERVICES will develop into MORE_SECURE_SERVICES in_the_future . 2018 , the_author_(_s_) .

"""
from ..._internals.mixins import ParamsMixin
from .record_mapping import RecordMapping  # type: ignore


class ExtractCopyrightText(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        docs = RecordMapping().update(**self.params.__dict__).run()

        texts = [doc["AB"] for doc in docs if isinstance(doc["AB"], str)]
        texts = [text[-self.params.n_chars :] for text in texts]
        texts = [text[::-1] for text in texts]
        texts = sorted(texts)
        texts = [text[::-1] for text in texts]
        if self.params.pattern is not None:
            texts = [text for text in texts if self.params.pattern in text]

        return texts


## ============================================================================
