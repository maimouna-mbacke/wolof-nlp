"""Wolof Lexicon - Word lookup and classification utilities"""

from typing import Optional, Dict, List, Tuple
from collections import Counter

from ..core.constants import (
    POS_CATEGORIES, COMMON_WORDS, ARABIC_LOANWORDS, FRENCH_COMMON, ENGLISH_COMMON,
    NOUN_CLASS_MARKERS, PRONOUNS, NUMBERS, TAM_MARKERS, SENTENCE_PARTICLES
)

class Lexicon:
    def lookup_pos(self, word: str) -> Optional[str]:
        word_lower = word.lower()
        for pos, words in POS_CATEGORIES.items():
            if word_lower in words:
                return pos
        return None
    
    def is_wolof_word(self, word: str) -> bool:
        word_lower = word.lower()
        if word_lower in COMMON_WORDS or word_lower in ARABIC_LOANWORDS:
            return True
        if 'ë' in word_lower or 'ñ' in word_lower or 'ŋ' in word_lower:
            return True
        prenasalized = ['mb', 'nd', 'nj', 'ng', 'nc', 'nk']
        if any(word_lower.startswith(pn) for pn in prenasalized):
            return True
        return False
    
    def detect_noun_class(self, determiner: str) -> Optional[str]:
        det_lower = determiner.lower()
        for cls, markers in NOUN_CLASS_MARKERS.items():
            if det_lower in markers.values():
                return cls
        return None
    
    def detect_tam(self, word: str) -> Optional[str]:
        word_lower = word.lower()
        if word_lower in SENTENCE_PARTICLES:
            return SENTENCE_PARTICLES[word_lower]['type']
        from ..core.constants import SUBJECT_FOCUS, VERB_FOCUS, FUTURE, NEGATIVE_FUTURE
        if word_lower in SUBJECT_FOCUS:
            return 'subject_focus'
        if word_lower in VERB_FOCUS:
            return 'verb_focus'
        if word_lower in FUTURE:
            return 'future'
        if word_lower in NEGATIVE_FUTURE:
            return 'negative_future'
        if word_lower == 'la':
            return 'object_focus'
        return None
    
    def get_pronoun_info(self, word: str) -> Optional[Dict]:
        return PRONOUNS.get(word.lower())
    
    def get_number_value(self, word: str) -> Optional[int]:
        return NUMBERS.get(word.lower())
    
    def word_frequency(self, tokens: List[str], top_n: int = 10) -> List[Tuple[str, int]]:
        cleaned = [t.lower() for t in tokens if len(t) > 1]
        return Counter(cleaned).most_common(top_n)
    
    def compute_language_ratio(self, tokens: List['Token']) -> Dict[str, float]:
        langs = [t.language for t in tokens if hasattr(t, 'language') and t.language]
        if not langs:
            return {}
        total = len(langs)
        counts = Counter(langs)
        return {lang: count/total for lang, count in counts.items()}

def is_wolof_word(word: str) -> bool:
    return Lexicon().is_wolof_word(word)

def detect_noun_class(determiner: str) -> Optional[str]:
    return Lexicon().detect_noun_class(determiner)

def detect_tam(word: str) -> Optional[str]:
    return Lexicon().detect_tam(word)

def word_frequency(tokens: List[str], top_n: int = 10) -> List[Tuple[str, int]]:
    return Lexicon().word_frequency(tokens, top_n)