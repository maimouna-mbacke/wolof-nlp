"""Wolof Temporal Expression Analyzer - Based on Moore's research on space-time metaphors"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum, auto

from ..core.constants import TEMPORAL_SPATIAL

class TemporalMetaphor(Enum):
    MOVING_EGO = auto()
    MOVING_TIME = auto()
    SEQUENCE = auto()

class TemporalReference(Enum):
    PAST = auto()
    PRESENT = auto()
    FUTURE = auto()
    SEQUENCE_BEFORE = auto()
    SEQUENCE_AFTER = auto()

@dataclass
class TemporalExpression:
    word: str
    spatial_meaning: str
    temporal_meaning: str
    metaphor: TemporalMetaphor
    reference: TemporalReference

class TemporalAnalyzer:
    def __init__(self):
        self.temporal_words = TEMPORAL_SPATIAL
    
    def analyze_word(self, word: str) -> Optional[TemporalExpression]:
        word_lower = word.lower()
        if word_lower not in self.temporal_words:
            return None
        
        info = self.temporal_words[word_lower]
        metaphor = TemporalMetaphor[info['metaphor']]
        reference = self._get_reference(word_lower, metaphor)
        
        return TemporalExpression(
            word=word_lower,
            spatial_meaning=info['spatial'],
            temporal_meaning=info['temporal'],
            metaphor=metaphor,
            reference=reference
        )
    
    def analyze_sentence(self, tokens: List[str]) -> List[TemporalExpression]:
        results = []
        for token in tokens:
            expr = self.analyze_word(token)
            if expr:
                results.append(expr)
        return results
    
    def _get_reference(self, word: str, metaphor: TemporalMetaphor) -> TemporalReference:
        past_words = {'gannaaw', 'paase'}
        future_words = {'kanam', 'ñów'}
        present_words = {'fekk', 'jot', 'tollu'}
        sequence_before = {'jiitu'}
        sequence_after = {'topp', 'tegu'}
        
        if word in past_words:
            return TemporalReference.PAST
        elif word in future_words:
            return TemporalReference.FUTURE
        elif word in present_words:
            return TemporalReference.PRESENT
        elif word in sequence_before:
            return TemporalReference.SEQUENCE_BEFORE
        elif word in sequence_after:
            return TemporalReference.SEQUENCE_AFTER
        return TemporalReference.PRESENT

def analyze_temporal(word: str) -> Optional[TemporalExpression]:
    return TemporalAnalyzer().analyze_word(word)