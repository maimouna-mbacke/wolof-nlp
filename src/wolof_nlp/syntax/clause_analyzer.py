"""Wolof Clause Analyzer - Copular sentences, relative clauses (Martinović)"""

from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum, auto

from ..core.constants import ALL_DETERMINERS, RELATIVE_PRONOUNS

class CopularType(Enum):
    PREDICATIONAL = auto()
    SPECIFICATIONAL = auto()
    IDENTITY = auto()

class ClauseStructure(Enum):
    LA_SENTENCE = auto()
    A_SENTENCE = auto()
    RELATIVE = auto()
    SIMPLE = auto()

@dataclass
class ClauseAnalysis:
    structure: ClauseStructure
    copular_type: Optional[CopularType]
    dp1: Optional[str]
    dp2: Optional[str]
    particle: Optional[str]
    is_relative: bool
    relative_pronoun: Optional[str]

class ClauseAnalyzer:
    def analyze(self, tokens: List[str]) -> ClauseAnalysis:
        words = [t.lower() for t in tokens]
        
        rel_pronoun = self._find_relative(words)
        if rel_pronoun:
            return ClauseAnalysis(
                structure=ClauseStructure.RELATIVE,
                copular_type=None,
                dp1=None, dp2=None,
                particle=None,
                is_relative=True,
                relative_pronoun=rel_pronoun
            )
        
        if 'la' in words:
            return self._analyze_la_sentence(tokens, words)
        
        for i, w in enumerate(words):
            if w.endswith('a') and i == 0 and 'di' in words:
                return self._analyze_a_sentence(tokens, words)
        
        return ClauseAnalysis(
            structure=ClauseStructure.SIMPLE,
            copular_type=None,
            dp1=None, dp2=None, particle=None,
            is_relative=False, relative_pronoun=None
        )
    
    def _find_relative(self, words: List[str]) -> Optional[str]:
        for w in words:
            if w in RELATIVE_PRONOUNS:
                return w
        return None
    
    def _analyze_la_sentence(self, tokens: List[str], words: List[str]) -> ClauseAnalysis:
        la_idx = words.index('la')
        dp1 = tokens[0] if la_idx > 0 else None
        dp2 = tokens[la_idx - 1] if la_idx > 1 else None
        
        dp1_is_definite = self._is_definite(tokens[:la_idx] if la_idx > 0 else [])
        dp2_is_definite = self._is_definite([tokens[la_idx-1]] if la_idx > 0 else [])
        
        if dp1_is_definite and not dp2_is_definite:
            copular_type = CopularType.PREDICATIONAL
        elif not dp1_is_definite and dp2_is_definite:
            copular_type = CopularType.SPECIFICATIONAL
        else:
            copular_type = CopularType.PREDICATIONAL
        
        return ClauseAnalysis(
            structure=ClauseStructure.LA_SENTENCE,
            copular_type=copular_type,
            dp1=dp1, dp2=dp2, particle='la',
            is_relative=False, relative_pronoun=None
        )
    
    def _analyze_a_sentence(self, tokens: List[str], words: List[str]) -> ClauseAnalysis:
        dp1 = tokens[0].rstrip('a') if tokens else None
        di_idx = words.index('di') if 'di' in words else -1
        dp2 = tokens[di_idx + 1] if di_idx >= 0 and di_idx + 1 < len(tokens) else None
        
        return ClauseAnalysis(
            structure=ClauseStructure.A_SENTENCE,
            copular_type=CopularType.IDENTITY,
            dp1=dp1, dp2=dp2, particle='a',
            is_relative=False, relative_pronoun=None
        )
    
    def _is_definite(self, tokens: List[str]) -> bool:
        for t in tokens:
            if t.lower() in ALL_DETERMINERS:
                return True
        return False

def analyze_clause(tokens: List[str]) -> ClauseAnalysis:
    return ClauseAnalyzer().analyze(tokens)