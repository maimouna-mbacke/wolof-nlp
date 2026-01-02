"""Wolof POS Tagger - Morphology-first with context rules"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
import re

from ..core.constants import (
    COMMON_VERBS, COMMON_NOUNS, COMMON_ADJECTIVES, COMMON_ADVERBS,
    TAM_MARKERS, ALL_DETERMINERS, CONJUNCTIONS, PREPOSITIONS,
    INTERROGATIVES, DISCOURSE_MARKERS, PRONOUNS, NUMBERS,
    SUBJECT_CLITICS, OBJECT_CLITICS, SUBJECT_FOCUS, VERB_FOCUS,
    PRESENTATIVE, PERFECT, FUTURE, NEGATIVE_FUTURE,
    SENEGAL_PLACES, WOLOF_NAMES,
)
from ..core.tokenizer import WolofTokenizer, TokenType


@dataclass
class POSToken:
    text: str
    pos: str
    confidence: float
    morphology: Optional[str] = None


FRENCH_PATTERNS = re.compile(r'.*(tion|ment|eur|eux|oir|age|ais|ait|ez|ence|ance|able|ible|ique)$', re.IGNORECASE)

FRENCH_COMMON = frozenset([
    'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'le', 'la', 'les',
    'un', 'une', 'des', 'de', 'du', 'au', 'aux', 'et', 'ou', 'mais', 'donc',
    'car', 'ni', 'que', 'qui', 'quoi', 'dont', 'où', 'est', 'sont', 'être',
    'avoir', 'fait', 'faire', 'dit', 'dire', 'voir', 'peut', 'veut', 'sais',
    'très', 'trop', 'bien', 'mal', 'plus', 'moins', 'avec', 'pour', 'dans',
    'sur', 'sous', 'par', 'sans', 'chez', 'vers', 'entre', 'comme', 'quand',
    'comment', 'pourquoi', 'oui', 'non', 'merci', 'bonjour', 'bonsoir',
    'vraiment', 'toujours', 'jamais', 'encore', 'aussi', 'même', 'tout',
    'cette', 'ces', 'mon', 'ton', 'son', 'notre', 'votre', 'leur', 'ce', 'cet',
])

VERB_NEGATION_PATTERN = re.compile(r'^(.+?)(w?oul|w?ul)$', re.IGNORECASE)
AGENT_NOUN_PATTERN = re.compile(r'^(.+?)(kat)$', re.IGNORECASE)
ABSTRACT_NOUN_PATTERN = re.compile(r'^(.+?)(aay|waay|in)$', re.IGNORECASE)
RECIPROCAL_PATTERN = re.compile(r'^(.+?)(ante|andoo|aante)$', re.IGNORECASE)
CAUSATIVE_PATTERN = re.compile(r'^(.+?)(al|loo|lu|andi)$', re.IGNORECASE)
REFLEXIVE_PATTERN = re.compile(r'^(.+?)(u|ku|iku)$', re.IGNORECASE)
REPETITIVE_PATTERN = re.compile(r'^(.+?)(aat|waat)$', re.IGNORECASE)


class POSTagger:
    
    def __init__(self):
        self.tokenizer = WolofTokenizer(normalize=True)
    
    def _is_french(self, word: str) -> bool:
        w = word.lower()
        if w in FRENCH_COMMON:
            return True
        if FRENCH_PATTERNS.match(w) and len(w) > 4:
            return True
        return False
    
    def _classify_by_morphology(self, word: str) -> Tuple[Optional[str], float, Optional[str]]:
        w = word.lower()
        
        if VERB_NEGATION_PATTERN.match(w):
            return 'VERB.NEG', 0.88, 'negation'
        
        if AGENT_NOUN_PATTERN.match(w):
            return 'NOUN.AGENT', 0.90, 'agent'
        
        if ABSTRACT_NOUN_PATTERN.match(w):
            return 'NOUN.ABSTRACT', 0.85, 'abstract'
        
        if RECIPROCAL_PATTERN.match(w) and len(w) > 5:
            return 'VERB.RECIP', 0.82, 'reciprocal'
        
        if REPETITIVE_PATTERN.match(w) and len(w) > 5:
            return 'VERB.REP', 0.80, 'repetitive'
        
        return None, 0.0, None
    
    def _classify_by_context(self, tokens: List, index: int) -> Tuple[Optional[str], float]:
        if index == 0:
            return None, 0.0
        
        prev_token = tokens[index - 1]
        prev_word = prev_token.text.lower() if prev_token.type == TokenType.WORD else ''
        
        if prev_word in TAM_MARKERS:
            return 'VERB', 0.78
        
        if prev_word in ALL_DETERMINERS:
            return 'NOUN', 0.75
        
        if prev_word in PREPOSITIONS:
            return 'NOUN', 0.70
        
        if prev_word in SUBJECT_FOCUS or prev_word in VERB_FOCUS:
            return 'VERB', 0.80
        
        if prev_word in PRESENTATIVE:
            return 'VERB', 0.82
        
        return None, 0.0
    
    def _classify_by_lexicon(self, word: str) -> Tuple[str, float]:
        w = word.lower()
        
        if w in TAM_MARKERS:
            return 'TAM', 0.99
        if w in SUBJECT_FOCUS:
            return 'TAM.SBJF', 0.99
        if w in VERB_FOCUS:
            return 'TAM.VRBF', 0.99
        if w in PRESENTATIVE:
            return 'TAM.PRSV', 0.99
        if w in PERFECT:
            return 'TAM.PFV', 0.99
        if w in FUTURE:
            return 'TAM.FUT', 0.99
        if w in NEGATIVE_FUTURE:
            return 'TAM.NEGF', 0.99
        if w in ALL_DETERMINERS:
            return 'DET', 0.99
        if w in SENEGAL_PLACES:
            return 'PROPN.LOC', 0.95
        if w in WOLOF_NAMES:
            return 'PROPN.PER', 0.95
        if w in COMMON_VERBS:
            return 'VERB', 0.95
        if w in COMMON_NOUNS:
            return 'NOUN', 0.95
        if w in COMMON_ADJECTIVES:
            return 'ADJ', 0.95
        if w in COMMON_ADVERBS:
            return 'ADV', 0.95
        if w in PREPOSITIONS:
            return 'PREP', 0.95
        if w in CONJUNCTIONS:
            return 'CONJ', 0.95
        if w in INTERROGATIVES:
            return 'INTER', 0.95
        if w in DISCOURSE_MARKERS:
            return 'DISC', 0.90
        if w in PRONOUNS:
            return 'PRON', 0.95
        if w in NUMBERS:
            return 'NUM', 0.99
        if w in SUBJECT_CLITICS or w in OBJECT_CLITICS:
            return 'CLIT', 0.95
        
        return 'UNK', 0.0
    
    def tag(self, text: str) -> List[POSToken]:
        tokens = self.tokenizer.tokenize(text)
        result = []
        
        for i, token in enumerate(tokens):
            if token.type != TokenType.WORD:
                continue
            
            word = token.text
            
            if self._is_french(word):
                result.append(POSToken(word, 'FWORD', 0.85, 'french'))
                continue
            
            pos, conf, morph = self._classify_by_morphology(word)
            if pos:
                result.append(POSToken(word, pos, conf, morph))
                continue
            
            pos, conf = self._classify_by_lexicon(word)
            if conf >= 0.95:
                result.append(POSToken(word, pos, conf, 'lexicon'))
                continue
            
            ctx_pos, ctx_conf = self._classify_by_context(tokens, i)
            if ctx_pos and ctx_conf > conf:
                result.append(POSToken(word, ctx_pos, ctx_conf, 'context'))
                continue
            
            if conf > 0:
                result.append(POSToken(word, pos, conf, 'lexicon'))
            else:
                result.append(POSToken(word, 'UNK', 0.0, None))
        
        return result
        
        return result
    
    def tag_sentence(self, text: str) -> List[Tuple[str, str]]:
        return [(t.text, t.pos) for t in self.tag(text)]


def tag(text: str) -> List[Tuple[str, str]]:
    return POSTagger().tag_sentence(text)
