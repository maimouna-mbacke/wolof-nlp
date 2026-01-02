"""Wolof Morphology Analyzer - Derivational and inflectional analysis"""

from dataclasses import dataclass
from typing import List, Optional, Dict
from enum import Enum, auto

from ..core.constants import (
    NEGATION_SUFFIXES, IMPERATIVE_SUFFIXES, CAUSATIVE_SUFFIXES, CAUSATIVE_LO_SUFFIXES,
    BENEFACTIVE_SUFFIXES, REFLEXIVE_SUFFIXES, RECIPROCAL_SUFFIXES, REPETITIVE_SUFFIXES,
    NOMINALIZATION_SUFFIXES, INTENSIVE_SUFFIXES, REVERSIVE_SUFFIXES, PAST_SUFFIXES,
    TAM_MARKERS, OBJECT_CLITICS, ALL_DETERMINERS, VOWELS, GEMINATES,
    SUBJECT_FOCUS, VERB_FOCUS, PRESENTATIVE, PERFECT, FUTURE, NEGATIVE_FUTURE,
    IMPERFECTIVE, SEMI_AUXILIARIES, AK_CONTRACTIONS, AY_CONTRACTIONS
)

class MorphemeType(Enum):
    ROOT = auto()
    TAM = auto()
    SUBJECT_FOCUS = auto()
    VERB_FOCUS = auto()
    PRESENTATIVE = auto()
    PERFECT = auto()
    FUTURE = auto()
    NEGATIVE = auto()
    IMPERFECTIVE = auto()
    SUBJECT = auto()
    OBJECT = auto()
    NEGATION = auto()
    IMPERATIVE = auto()
    PAST = auto()
    CAUSATIVE = auto()
    CAUSATIVE_LO = auto()
    BENEFACTIVE = auto()
    REFLEXIVE = auto()
    RECIPROCAL = auto()
    REPETITIVE = auto()
    NOMINALIZATION = auto()
    INTENSIVE = auto()
    REVERSIVE = auto()
    DETERMINER = auto()
    CONTRACTION = auto()
    UNKNOWN = auto()

@dataclass
class Morpheme:
    text: str
    type: MorphemeType
    gloss: Optional[str] = None
    
    @property
    def form(self):
        return self.text
    
    @property
    def label(self):
        return self.type.name
    
    def __repr__(self):
        if self.gloss:
            return f"{self.text}:{self.type.name}({self.gloss})"
        return f"{self.text}:{self.type.name}"

class MorphologyAnalyzer:
    FRENCH_PATTERNS = {'ment$', 'tion$', 'eur$', 'eux$', 'ique$', 'able$', 'ible$'}
    FRENCH_WORDS = {'meriku', 'pendant', 'vraiment', 'toujours', 'beaucoup', 'quelque'}
    
    def _is_likely_french(self, word: str) -> bool:
        """Check if word is likely French to avoid false morphological analysis."""
        import re
        w = word.lower()
        if w in self.FRENCH_WORDS:
            return True
        for pattern in self.FRENCH_PATTERNS:
            if re.search(pattern, w):
                return True
        if re.search(r'(eau|ou[^s]|oi|qu|ph)', w):
            return True
        return False
    
    def analyze(self, word: str) -> List[Morpheme]:
        word_lower = word.lower()
        
        if self._is_likely_french(word_lower):
            return [Morpheme(word_lower, MorphemeType.ROOT)]
        
        tam_result = self._check_tam_marker(word_lower)
        if tam_result:
            return tam_result
        
        if word_lower in ALL_DETERMINERS:
            return [Morpheme(word_lower, MorphemeType.DETERMINER)]
        
        if word_lower in OBJECT_CLITICS:
            return [Morpheme(word_lower, MorphemeType.OBJECT)]
        
        contraction_result = self._expand_contraction(word_lower)
        if contraction_result:
            return contraction_result
        
        result = self._analyze_verb(word_lower)
        if result:
            return result
        
        nomin_result = self._analyze_nominalization(word_lower)
        if nomin_result:
            return nomin_result
        
        deriv_result = self._analyze_derivational(word_lower)
        if deriv_result:
            return deriv_result
        
        return [Morpheme(word_lower, MorphemeType.ROOT)]
    
    def _check_tam_marker(self, word: str) -> Optional[List[Morpheme]]:
        if word in SUBJECT_FOCUS:
            return [Morpheme(word, MorphemeType.SUBJECT_FOCUS, "it's X who")]
        if word in VERB_FOCUS:
            return [Morpheme(word, MorphemeType.VERB_FOCUS, "X does")]
        if word in PRESENTATIVE:
            return [Morpheme(word, MorphemeType.PRESENTATIVE, "X is here")]
        if word in FUTURE:
            return [Morpheme(word, MorphemeType.FUTURE, "X will")]
        if word in NEGATIVE_FUTURE:
            return [Morpheme(word, MorphemeType.NEGATIVE, "X won't")]
        if word in IMPERFECTIVE:
            return [Morpheme(word, MorphemeType.IMPERFECTIVE, "ongoing")]
        if word in SEMI_AUXILIARIES:
            return [Morpheme(word, MorphemeType.TAM, "auxiliary")]
        if word in PERFECT:
            return [Morpheme(word, MorphemeType.PERFECT, "completed")]
        return None
    
    def _expand_contraction(self, word: str) -> Optional[List[Morpheme]]:
        if word in AK_CONTRACTIONS:
            parts = AK_CONTRACTIONS[word]
            return [Morpheme(parts[0], MorphemeType.ROOT), Morpheme(parts[1], MorphemeType.CONTRACTION, "and")]
        if word in AY_CONTRACTIONS:
            parts = AY_CONTRACTIONS[word]
            return [Morpheme(parts[0], MorphemeType.ROOT), Morpheme(parts[1], MorphemeType.CONTRACTION, "plural")]
        return None
    
    def _analyze_nominalization(self, word: str) -> Optional[List[Morpheme]]:
        for suffix in sorted(NOMINALIZATION_SUFFIXES, key=len, reverse=True):
            if word.endswith(suffix) and len(word) > len(suffix) + 2:
                root = word[:-len(suffix)]
                if suffix == 'kat':
                    return [Morpheme(root, MorphemeType.ROOT), Morpheme(suffix, MorphemeType.NOMINALIZATION, "agent")]
                elif suffix == 'in':
                    return [Morpheme(root, MorphemeType.ROOT), Morpheme(suffix, MorphemeType.NOMINALIZATION, "patient")]
                elif suffix == 'waay' and root and root[-1] in VOWELS:
                    return [Morpheme(root, MorphemeType.ROOT), Morpheme(suffix, MorphemeType.NOMINALIZATION, "abstract noun")]
                elif suffix == 'aay' and root and root[-1] not in VOWELS:
                    return [Morpheme(root, MorphemeType.ROOT), Morpheme(suffix, MorphemeType.NOMINALIZATION, "abstract noun")]
                elif suffix == 'ay':
                    return [Morpheme(root, MorphemeType.ROOT), Morpheme(suffix, MorphemeType.NOMINALIZATION, "abstract noun")]
        return None
    
    def _analyze_verb(self, word: str) -> Optional[List[Morpheme]]:
        morphemes = []
        remaining = word
        
        for suffix in sorted(NEGATION_SUFFIXES, key=len, reverse=True):
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 2:
                morphemes.append(Morpheme(suffix, MorphemeType.NEGATION, "not"))
                remaining = remaining[:-len(suffix)]
                break
        
        for suffix in sorted(PAST_SUFFIXES, key=len, reverse=True):
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 2:
                morphemes.insert(0, Morpheme(suffix, MorphemeType.PAST, "past"))
                remaining = remaining[:-len(suffix)]
                break
        
        for clitic in sorted(OBJECT_CLITICS, key=len, reverse=True):
            if remaining.endswith(clitic) and len(remaining) > len(clitic) + 2:
                morphemes.insert(0, Morpheme(clitic, MorphemeType.OBJECT))
                remaining = remaining[:-len(clitic)]
                break
        
        tam_found = None
        for tam in sorted(['naa', 'nga', 'na', 'nanu', 'ngeen', 'nañu'], key=len, reverse=True):
            if remaining.endswith(tam) and len(remaining) > len(tam) + 1:
                tam_found = tam
                remaining = remaining[:-len(tam)]
                break
        
        remaining = self._strip_derivational(remaining, morphemes)
        
        if tam_found:
            morphemes.insert(0, Morpheme(tam_found, MorphemeType.TAM, "perfect"))
        
        if remaining:
            morphemes.insert(0, Morpheme(remaining, MorphemeType.ROOT))
        
        if len(morphemes) > 1:
            return morphemes
        return None
    
    def _analyze_derivational(self, word: str) -> Optional[List[Morpheme]]:
        morphemes = []
        remaining = word
        
        for suffix in ['éku', 'iku', 'ku', 'u']:
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 1:
                root = remaining[:-len(suffix)]
                if suffix in ['ku', 'iku', 'éku'] and root and root[-1] in VOWELS:
                    morphemes.append(Morpheme(suffix, MorphemeType.REFLEXIVE, "oneself"))
                    remaining = root
                    break
                elif suffix == 'u' and root and root[-1] not in VOWELS and not root.endswith(tuple(GEMINATES)):
                    morphemes.append(Morpheme(suffix, MorphemeType.REFLEXIVE, "oneself"))
                    remaining = root
                    break
        
        for suffix in sorted(RECIPROCAL_SUFFIXES, key=len, reverse=True):
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 2:
                morphemes.insert(0, Morpheme(suffix, MorphemeType.RECIPROCAL, "each other"))
                remaining = remaining[:-len(suffix)]
                break
        
        for suffix in sorted(REPETITIVE_SUFFIXES, key=len, reverse=True):
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 2:
                root = remaining[:-len(suffix)]
                if suffix == 'waat' and root and root[-1] in VOWELS:
                    morphemes.insert(0, Morpheme(suffix, MorphemeType.REPETITIVE, "again"))
                    remaining = root
                    break
                elif suffix == 'aat' and root and (root[-1] not in VOWELS or root[-1] == 'y'):
                    morphemes.insert(0, Morpheme(suffix, MorphemeType.REPETITIVE, "again"))
                    remaining = root
                    break
        
        for suffix in sorted(CAUSATIVE_LO_SUFFIXES, key=len, reverse=True):
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 2:
                morphemes.insert(0, Morpheme(suffix, MorphemeType.CAUSATIVE_LO, "make someone"))
                remaining = remaining[:-len(suffix)]
                break
        
        for suffix in sorted(CAUSATIVE_SUFFIXES, key=len, reverse=True):
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 2:
                morphemes.insert(0, Morpheme(suffix, MorphemeType.CAUSATIVE, "cause/for"))
                remaining = remaining[:-len(suffix)]
                break
        
        if morphemes:
            morphemes.insert(0, Morpheme(remaining, MorphemeType.ROOT))
            return morphemes
        return None
    
    def _strip_derivational(self, word: str, morphemes: List[Morpheme]) -> str:
        remaining = word
        
        for suffix in ['éku', 'iku', 'ku', 'u']:
            if remaining.endswith(suffix) and len(remaining) > len(suffix) + 1:
                root = remaining[:-len(suffix)]
                if suffix in ['ku', 'iku', 'éku'] and root and root[-1] in VOWELS:
                    morphemes.insert(0, Morpheme(suffix, MorphemeType.REFLEXIVE, "oneself"))
                    remaining = root
                    break
                elif suffix == 'u' and root and root[-1] not in VOWELS and not root.endswith(tuple(GEMINATES)):
                    morphemes.insert(0, Morpheme(suffix, MorphemeType.REFLEXIVE, "oneself"))
                    remaining = root
                    break
        
        return remaining
    
    def get_root(self, word: str) -> str:
        morphemes = self.analyze(word)
        for m in morphemes:
            if m.type == MorphemeType.ROOT:
                return m.text
        return word
    
    def get_derivation_chain(self, word: str) -> List[str]:
        morphemes = self.analyze(word)
        if len(morphemes) <= 1:
            return [word]
        chain = []
        current = ""
        for m in morphemes:
            current += m.text
            chain.append(current)
        return chain

def analyze_morphology(word: str) -> List[Morpheme]:
    return MorphologyAnalyzer().analyze(word)

def get_root(word: str) -> str:
    return MorphologyAnalyzer().get_root(word)