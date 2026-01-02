"""Wolof Orthography Normalizer - Converts popular spellings to CLAD standard"""

import re
from .constants import ORTHOGRAPHY_MAP, WORD_NORMALIZATIONS, FRENCH_COMMON


class WolofNormalizer:
    
    FRENCH_SKIP = frozenset([
        'toujours', 'peut-être', 'peut', 'être', 'thanks', 'always', 'never',
        'maybe', 'really', 'actually', 'seriously', 'obviously', 'honestly',
        'because', 'parfait', 'super', 'génial', 'terrible', 'excellent',
        'formidable', 'incroyable', 'magnifique', 'absolument', 'exactement',
        'vraiment', 'tellement', 'beautiful', 'wonderful', 'amazing',
    ])
    
    FRENCH_SUFFIX_PATTERN = re.compile(r'(tion|ment|eur|eux|oir|age|ais|ait|ez|ence|ance)$', re.IGNORECASE)
    
    def __init__(self):
        self._build_patterns()
    
    def _build_patterns(self):
        sorted_keys = sorted(ORTHOGRAPHY_MAP.keys(), key=len, reverse=True)
        self.ortho_pattern = re.compile('(' + '|'.join(re.escape(k) for k in sorted_keys) + ')', re.IGNORECASE)
        sorted_words = sorted(WORD_NORMALIZATIONS.keys(), key=len, reverse=True)
        self.word_pattern = re.compile(r'\b(' + '|'.join(re.escape(w) for w in sorted_words) + r')\b', re.IGNORECASE)
    
    def _is_french_word(self, word: str) -> bool:
        w = word.lower()
        if w in FRENCH_COMMON or w in self.FRENCH_SKIP:
            return True
        if self.FRENCH_SUFFIX_PATTERN.search(w) and len(w) > 5:
            return True
        return False
    
    def normalize(self, text: str) -> str:
        result = self._normalize_words(text)
        result = self._normalize_orthography_smart(result)
        result = self._normalize_modern_variants(result)
        return result
    
    def _normalize_words(self, text: str) -> str:
        def replace_word(match):
            word = match.group(1)
            if self._is_french_word(word):
                return word
            normalized = WORD_NORMALIZATIONS.get(word.lower(), word)
            if word[0].isupper():
                normalized = normalized.capitalize()
            return normalized
        return self.word_pattern.sub(replace_word, text)
    
    def _normalize_orthography_smart(self, text: str) -> str:
        words = re.findall(r'\b\w+\b|\W+', text)
        result = []
        for word in words:
            if re.match(r'\w+', word) and not self._is_french_word(word):
                normalized = self.ortho_pattern.sub(
                    lambda m: ORTHOGRAPHY_MAP.get(m.group(1).lower(), m.group(1)), 
                    word
                )
                result.append(normalized)
            else:
                result.append(word)
        return ''.join(result)
    
    def _normalize_modern_variants(self, text: str) -> str:
        words = text.split()
        result = []
        for word in words:
            if self._is_french_word(word):
                result.append(word)
            else:
                w = word
                w = re.sub(r'\bou(?=[aeiëou])', 'u', w, flags=re.IGNORECASE)
                w = re.sub(r'(?<=[aeiëou])ou\b', 'u', w, flags=re.IGNORECASE)
                result.append(w)
        return ' '.join(result)
    
    def __call__(self, text: str) -> str:
        return self.normalize(text)


def normalize(text: str) -> str:
    return WolofNormalizer().normalize(text)
