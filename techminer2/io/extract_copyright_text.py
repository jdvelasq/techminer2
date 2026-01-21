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
    ...     root_directory="examples/fintech/",
    ... ).run()
    >>> for t in text[:5]: print(t)
    TORS , REGULATORS , etc . ) , who explore THE_FIELD of FINTECH . 2016 , the author ( s ) .
    E_SERVICE_OFFERINGS of FINTECH_START_UP in A_STRUCTURED_MANNER . 2017 , the author ( s ) .
    IOD short , we can not rule out that OUR_FINDINGS are spurious . 2017 , the author ( s ) .
    ACTIVE_POLICIES can influence THE_EMERGENCE of THIS_NEW_SECTOR . 2018 , the author ( s ) .
    _SERVICES will develop into MORE_SECURE_SERVICES in_the_future . 2018 , the author ( s ) .


"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.explore.record_mapping import RecordMapping  # type: ignore


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
