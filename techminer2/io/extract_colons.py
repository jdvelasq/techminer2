# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Extract Colons
===============================================================================


Example:
    >>> from techminer2.database.tools import ExtractColons
    >>> text = ExtractColons(
    ...     pattern=None,
    ...     n_chars=20,
    ...     root_directory="examples/structured/",
    ... ).run()
    >>> for t in text[:20]: print(t) # doctest: +NORMALIZE_WHITESPACE
                                                    introduction  :  THE_FLIPPED_CLASSROOM is PEDAGOGICAL_MODEL that consists >>>
                                                       objective  :  to develop A_SYSTEM of activitiesdesigned for THE_TEACHI >>>
                                                         methods  :  A_RESEARCH with A_QUANTITATIVE_APPROACH is presented
                                                         results  :  A_CONCEPTUAL_MAP was obtained as A_PROPOSAL and GUIDE fo >>>
                                                     conclusions  :  the IN_DEPTH_STUDY carried out demonstrated THE_FEASIBIL >>>
                                                      background  :  THE_ADVENT of DIGITAL_TECHNOLOGY has profoundly impacted >>>
                                                      objectives  :  this study aimed to identify THE_KEY_MOTIVATIONAL_COMPON >>>
                                                         methods  :  a qualitative GROUNDED_THEORY ( GT ) approach was used t >>>
    <<< _CATEGORIES influencing THE_ADOPTION of BLENDED_LEARNING  :  LEARNER_PROFESSOR , INFRASTRUCTURE , structural , ENVIRO >>>
                                                     conclusions  :  THE_MODEL provides ACTIONABLE_INSIGHTS for MEDICAL_SCHOO >>>
                                                         context  :  jining MEDICAL_UNIVERSITY has adopted THE_TRADITIONAL_LA >>>
                                                       objective  :  to solve THIS_PROBLEM , we integrated DESIGN_THINKING in >>>
                                                          method  :  A_MIXED_METHODOLOGY ( qualitative and quantitative ) was >>>
    <<< NS and 18 PAIN_POINTS , categorized into FOUR_DIMENSIONS  :  SELF_AWARENESS , TEAMWORK , LEARNING_EFFICIENCY , and CO >>>
                                                      conclusion  :  THE_LARGE_CLASS_FLIPPED_CLASSROOM model integrated with  >>>
                                                         purpose  :  this study aims to investigate TEACHING_METHODOLOGIES ,  >>>
                                 design / methodology / approach  :  using A_QUALITATIVE_DESCRIPTIVE_APPROACH , DATA was coll >>>
                                                        findings  :  EFFECTIVE_STRATEGIES in LARGE_CLASS_STS_COURSE included  >>>
                                          practical implications  :  RECOMMENDATIONS include reducing CLASS_SIZE , enhancing  >>>
                                             originality / value  :  this study contributes to THE_GROWING_BODY of RESEARCH o >>>


"""

from techminer2._internals.mixins import ParamsMixin
from techminer2.concordances import ConcordantProcessedContexts


class ExtractColons(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        return (
            ConcordantProcessedContexts()
            .update(**self.params.__dict__)
            .having_abstract_matching(" : ")
            .run()
        )


## ============================================================================
