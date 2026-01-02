"""Wolof Sentiment Analysis - Rule-based hybrid approach with morphological awareness"""

from typing import List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
import re

from ..core.tokenizer import WolofTokenizer, TokenType


class Sentiment(Enum):
    POSITIVE = auto()
    NEGATIVE = auto()
    NEUTRAL = auto()


@dataclass
class SentimentResult:
    sentiment: Sentiment
    score: float
    positive_words: List[str] = field(default_factory=list)
    negative_words: List[str] = field(default_factory=list)
    negated_words: List[str] = field(default_factory=list)
    intensified: bool = False


POSITIVE_ROOTS = frozenset([
    'neex', 'baax', 'rafet', 'bëgg', 'begg', 'sant', 'kontaan', 'bég',
    'sopp', 'teranga', 'jàmm', 'jamm', 'fayda', 'ndank', 'yépp',
    'jeggal', 'muñ', 'teraanga', 'mbëggeel', 'xol',
])

NEGATIVE_ROOTS = frozenset([
    'bon', 'ñàkk', 'nakk', 'metti', 'tiit', 'bañ', 'ragal', 'rus',
    'mer', 'sonnu', 'tàgg', 'xéew', 'sàcc', 'naqar', 'yagg', 'dof',
    'feebar', 'sonn', 'xiif', 'jail',
])

ARABIC_POSITIVE = frozenset([
    'amine', 'amin', 'ameen', 'mashallah', 'machallah', 'maachallah',
    'alhamdulillah', 'alxamdulilah', 'barke', 'baraka', 'inshallah',
    'inchallah', 'subhanallah', 'jërëjëf', 'jerejef', 'dieuredieuf',
])

FRENCH_POSITIVE = frozenset([
    'magnifique', 'bravo', 'super', 'excellent', 'incroyable', 'formidable',
    'génial', 'genial', 'parfait', 'merveilleux', 'fantastique', 'bien',
])

FRENCH_NEGATIVE = frozenset([
    'triste', 'dommage', 'nul', 'mauvais', 'terrible', 'horrible',
    'décevant', 'decevant', 'moche', 'pire',
])

INTENSIFIERS = frozenset([
    'lool', 'torop', 'trop', 'bu', 'sax', 'dëgg', 'degg', 'wér', 'yépp',
    'vraiment', 'très', 'tres', 'tellement', 'completely', 'totally',
])

DISCOURSE_FLIPPERS = frozenset([
    'waaye', 'waye', 'mais', 'however', 'but', 'ndax', 'ndaxte', 'konte',
])

POSITIVE_EMOJI = frozenset([
    '❤', '😂', '🙏', '😊', '😍', '🥰', '👍', '🔥', '💪', '👏', '💖', '💕',
    '💗', '💘', '💙', '💚', '💛', '🧡', '💜', '🤍', '✨', '🎉', '😘', '🤣',
])

NEGATIVE_EMOJI = frozenset([
    '😭', '😢', '💔', '😡', '😠', '😤', '😞', '😔', '😿', '🤮', '👎',
])

NEGATION_PATTERN = re.compile(r'^(.+?)(w?oul|w?ul)$', re.IGNORECASE)
DU_PATTERN = re.compile(r'^(du|duma|doo|dunu|dungeen|duñu)$', re.IGNORECASE)


class SentimentAnalyzer:
    
    def __init__(self):
        self.tokenizer = WolofTokenizer(normalize=True)
    
    def _is_verb_negation(self, word: str) -> Tuple[bool, Optional[str]]:
        match = NEGATION_PATTERN.match(word.lower())
        if match:
            root = match.group(1)
            if len(root) >= 2:
                return True, root
        return False, None
    
    def _check_negation_context(self, words: List[str], index: int) -> bool:
        if index > 0:
            prev_word = words[index - 1].lower()
            if DU_PATTERN.match(prev_word):
                return True
        return False
    
    def _extract_emoji_sentiment(self, text: str) -> Tuple[int, int]:
        pos_count = sum(1 for char in text if char in POSITIVE_EMOJI)
        neg_count = sum(1 for char in text if char in NEGATIVE_EMOJI)
        return pos_count, neg_count
    
    def _has_intensifier(self, words: List[str]) -> bool:
        return any(w.lower() in INTENSIFIERS for w in words)
    
    def _find_discourse_flip(self, words: List[str]) -> int:
        for i, word in enumerate(words):
            if word.lower() in DISCOURSE_FLIPPERS:
                return i
        return -1
    
    def analyze(self, text: str) -> SentimentResult:
        tokens = self.tokenizer.tokenize(text)
        words = [t.text for t in tokens if t.type == TokenType.WORD]
        word_list = [w.lower() for w in words]
        
        pos_found = []
        neg_found = []
        negated = []
        
        flip_index = self._find_discourse_flip(words)
        has_flip = flip_index >= 0
        
        before_flip_pos = []
        before_flip_neg = []
        after_flip_pos = []
        after_flip_neg = []
        
        for i, word in enumerate(word_list):
            is_after_flip = has_flip and i > flip_index
            
            is_neg, root = self._is_verb_negation(word)
            if is_neg and root:
                if root in POSITIVE_ROOTS:
                    negated.append(word)
                    if is_after_flip:
                        after_flip_neg.append(word)
                    else:
                        before_flip_neg.append(word)
                    continue
                elif root in NEGATIVE_ROOTS:
                    negated.append(word)
                    if is_after_flip:
                        after_flip_pos.append(word)
                    else:
                        before_flip_pos.append(word)
                    continue
            
            if self._check_negation_context(word_list, i):
                if word in POSITIVE_ROOTS:
                    negated.append(word)
                    if is_after_flip:
                        after_flip_neg.append(word)
                    else:
                        before_flip_neg.append(word)
                    continue
                elif word in NEGATIVE_ROOTS:
                    negated.append(word)
                    if is_after_flip:
                        after_flip_pos.append(word)
                    else:
                        before_flip_pos.append(word)
                    continue
            
            if word in POSITIVE_ROOTS or word in ARABIC_POSITIVE or word in FRENCH_POSITIVE:
                if is_after_flip:
                    after_flip_pos.append(word)
                else:
                    before_flip_pos.append(word)
            elif word in NEGATIVE_ROOTS or word in FRENCH_NEGATIVE:
                if is_after_flip:
                    after_flip_neg.append(word)
                else:
                    before_flip_neg.append(word)
        
        if has_flip and (after_flip_pos or after_flip_neg):
            pos_found = after_flip_pos
            neg_found = after_flip_neg
        else:
            pos_found = before_flip_pos + after_flip_pos
            neg_found = before_flip_neg + after_flip_neg
        
        emoji_pos, emoji_neg = self._extract_emoji_sentiment(text)
        
        has_intensifier = self._has_intensifier(word_list)
        multiplier = 1.5 if has_intensifier else 1.0
        
        pos_score = (len(pos_found) + emoji_pos * 0.5) * multiplier
        neg_score = (len(neg_found) + emoji_neg * 0.5) * multiplier
        
        if pos_score > neg_score:
            sentiment = Sentiment.POSITIVE
            score = min(pos_score / (pos_score + neg_score + 0.1), 1.0)
        elif neg_score > pos_score:
            sentiment = Sentiment.NEGATIVE
            score = min(neg_score / (pos_score + neg_score + 0.1), 1.0)
        else:
            sentiment = Sentiment.NEUTRAL
            score = 0.5
        
        return SentimentResult(
            sentiment=sentiment,
            score=score,
            positive_words=pos_found,
            negative_words=neg_found,
            negated_words=negated,
            intensified=has_intensifier,
        )


def analyze_sentiment(text: str) -> SentimentResult:
    return SentimentAnalyzer().analyze(text)
