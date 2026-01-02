"""Wolof Sentence Parser - Based on Martinović's analysis of clause structure"""

from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum, auto

from ..core.constants import (
    SUBJECT_FOCUS, VERB_FOCUS, PRESENTATIVE, PERFECT, FUTURE, NEGATIVE_FUTURE,
    PROHIBITIVE, SUBJECT_CLITICS, OBJECT_CLITICS, INTERROGATIVES, SENTENCE_PARTICLES
)
from ..core.tokenizer import WolofTokenizer, Token, TokenType

class ClauseType(Enum):
    V_RAISING = auto()
    WH_RAISING = auto()
    NEUTRAL = auto()
    SUBJECT_FOCUS = auto()
    VERB_FOCUS = auto()
    COMPLEMENT_FOCUS = auto()
    COPULAR = auto()
    IMPERATIVE = auto()
    CONDITIONAL = auto()
    UNKNOWN = auto()

class FocusType(Enum):
    NONE = auto()
    SUBJECT = auto()
    VERB = auto()
    COMPLEMENT = auto()

@dataclass
class SentenceAnalysis:
    clause_type: ClauseType
    focus_type: FocusType
    sentence_particle: Optional[str]
    subject: Optional[str]
    verb: Optional[str]
    focused_element: Optional[str]
    is_negative: bool
    is_question: bool
    has_clitic_doubling: bool
    
    def __repr__(self):
        return f"SentenceAnalysis(type={self.clause_type.name}, focus={self.focus_type.name})"

class SentenceParser:
    def __init__(self):
        self.tokenizer = WolofTokenizer(normalize=True, detect_language=True)
    
    def parse(self, sentence: str) -> SentenceAnalysis:
        tokens = self.tokenizer.tokenize(sentence)
        word_tokens = [t for t in tokens if t.type == TokenType.WORD]
        
        if not word_tokens:
            return self._empty_analysis()
        
        words = [t.text.lower() for t in word_tokens]
        
        is_question = any(w in INTERROGATIVES for w in words) or sentence.strip().endswith('?')
        is_negative = self._detect_negation(words)
        particle = self._find_sentence_particle(words)
        focus_type, focused_elem = self._detect_focus(words, word_tokens)
        clause_type = self._determine_clause_type(words, particle, focus_type, is_question)
        subject = self._find_subject(word_tokens, clause_type)
        verb = self._find_verb(word_tokens, clause_type)
        has_clitic = self._has_clitic_doubling(words)
        
        return SentenceAnalysis(
            clause_type=clause_type,
            focus_type=focus_type,
            sentence_particle=particle,
            subject=subject,
            verb=verb,
            focused_element=focused_elem,
            is_negative=is_negative,
            is_question=is_question,
            has_clitic_doubling=has_clitic
        )
    
    def _empty_analysis(self) -> SentenceAnalysis:
        return SentenceAnalysis(
            clause_type=ClauseType.UNKNOWN,
            focus_type=FocusType.NONE,
            sentence_particle=None,
            subject=None,
            verb=None,
            focused_element=None,
            is_negative=False,
            is_question=False,
            has_clitic_doubling=False
        )
    
    def _find_sentence_particle(self, words: List[str]) -> Optional[str]:
        for w in words:
            if w in SENTENCE_PARTICLES:
                return w
            for marker in SUBJECT_FOCUS | VERB_FOCUS | PRESENTATIVE | FUTURE | NEGATIVE_FUTURE:
                if w == marker or w.startswith(marker):
                    return w
        return None
    
    def _detect_focus(self, words: List[str], tokens: List[Token]) -> Tuple[FocusType, Optional[str]]:
        for i, w in enumerate(words):
            if w in VERB_FOCUS:
                return FocusType.VERB, None
            
            if w in SUBJECT_FOCUS or (w.endswith('a') and i == 0 and len(words) > 1 and w not in VERB_FOCUS):
                if 'a' in w and i < len(words) - 1:
                    return FocusType.SUBJECT, tokens[0].text if i == 0 else None
            
            if w == 'la' and i > 0:
                return FocusType.COMPLEMENT, tokens[i-1].text if i > 0 else None
        
        return FocusType.NONE, None
    
    def _determine_clause_type(self, words: List[str], particle: Optional[str], 
                               focus_type: FocusType, is_question: bool) -> ClauseType:
        if is_question and any(w in INTERROGATIVES for w in words):
            return ClauseType.WH_RAISING
        
        if focus_type == FocusType.SUBJECT:
            return ClauseType.SUBJECT_FOCUS
        
        if focus_type == FocusType.VERB:
            return ClauseType.VERB_FOCUS
        
        if focus_type == FocusType.COMPLEMENT:
            return ClauseType.COMPLEMENT_FOCUS
        
        if particle:
            if particle in VERB_FOCUS:
                return ClauseType.V_RAISING
            if particle in PRESENTATIVE:
                return ClauseType.V_RAISING
            if particle in FUTURE or particle in NEGATIVE_FUTURE:
                return ClauseType.V_RAISING
            if particle == 'na' or particle in PERFECT:
                return ClauseType.NEUTRAL
            if particle in PROHIBITIVE or particle.startswith('bu') or particle.startswith('su'):
                return ClauseType.CONDITIONAL
        
        if any(w.endswith('al') for w in words[:2]):
            return ClauseType.IMPERATIVE
        
        return ClauseType.UNKNOWN
    
    def _detect_negation(self, words: List[str]) -> bool:
        neg_markers = {'du', 'duma', 'doo', 'dunu', 'duñu', 'bul', 'bañ'}
        neg_suffixes = ['ul', 'uma', 'uloo', 'unu', 'uleen', 'uñu', 'wul']
        
        if any(w in neg_markers for w in words):
            return True
        if any(any(w.endswith(suf) for suf in neg_suffixes) for w in words):
            return True
        return False
    
    def _find_subject(self, tokens: List[Token], clause_type: ClauseType) -> Optional[str]:
        if not tokens:
            return None
        
        if clause_type in [ClauseType.SUBJECT_FOCUS, ClauseType.V_RAISING]:
            first = tokens[0].text.lower()
            if first not in VERB_FOCUS and first not in PRESENTATIVE:
                return tokens[0].text
        
        return None
    
    def _find_verb(self, tokens: List[Token], clause_type: ClauseType) -> Optional[str]:
        for t in tokens:
            w = t.text.lower()
            if w not in (SUBJECT_FOCUS | VERB_FOCUS | PRESENTATIVE | FUTURE | 
                        NEGATIVE_FUTURE | SUBJECT_CLITICS | OBJECT_CLITICS):
                if not any(w == det for det in ['bi', 'gi', 'ji', 'ki', 'yi', 'ñi']):
                    return t.text
        return None
    
    def _has_clitic_doubling(self, words: List[str]) -> bool:
        has_clitic = any(w in SUBJECT_CLITICS for w in words)
        has_full_noun = len([w for w in words if len(w) > 3]) > 1
        return has_clitic and has_full_noun

def parse_sentence(sentence: str) -> SentenceAnalysis:
    return SentenceParser().parse(sentence)