import re
from dataclasses import dataclass
from typing import List, Optional, Set, Tuple
from enum import Enum, auto
from .normalizer import WolofNormalizer
from .constants import (
    CLITIC_COMBINATIONS,
    AK_CONTRACTIONS,
    AY_CONTRACTIONS,
    POSSESSIVE_CONTRACTIONS,
    PRENASALIZED,
    GEMINATES,
    SERIAL_VERBS,
    COMMON_VERBS,
    ALL_DETERMINERS,
    FRENCH_COMMON,
    FRENCH_CONTRACTIONS,
    ARABIC_LOANWORDS,
    ENGLISH_COMMON,
    COMMON_WORDS,
    TAM_MARKERS,
    VOWELS,
    CONSONANTS,
    SENEGAL_PLACES,
    WOLOF_NAMES,
)

class TokenType(Enum):
    WORD = auto()
    PUNCTUATION = auto()
    NUMBER = auto()
    EMOJI = auto()
    URL = auto()
    EMAIL = auto()
    HASHTAG = auto()
    MENTION = auto()
    UNKNOWN = auto()

class Language(Enum):
    WOLOF = auto()
    FRENCH = auto()
    ARABIC = auto()
    ENGLISH = auto()
    MIXED = auto()
    UNKNOWN = auto()

@dataclass
class Token:
    text: str
    type: TokenType
    start: int
    end: int
    normalized: Optional[str] = None
    language: Optional[Language] = None
    morphemes: Optional[List[str]] = None
    is_split: bool = False

MORPHEME_MAP = {
    # Progressive forms with -y (always split)
    'damay': ['da', 'ma', 'y'],
    'dangay': ['da', 'nga', 'y'],
    'dafay': ['da', 'fa', 'y'],
    'dañuy': ['da', 'ñu', 'y'],
    'lañuy': ['la', 'ñu', 'y'],
    'dinay': ['di', 'na', 'y'],
    'ngay': ['nga', 'y'],
    'mooy': ['moo', 'di'],
    # Future (split di + person)
    'dinaa': ['di', 'na', 'a'],
    'dinga': ['di', 'nga'],
    'dinanu': ['di', 'na', 'nu'],
    'dingeen': ['di', 'ngeen'],
    'dinañu': ['di', 'na', 'ñu'],
    'dina': ['di', 'na'],
    # Perfect with 1SG (split na + a)
    'naa': ['na', 'a'],
    'nanga': ['na', 'nga'],  # obligative
    'nañu': ['na', 'ñu'],
    # Presentative (split person + ngi)
    'mangui': ['ma', 'ngi'],
    'mangi': ['ma', 'ngi'],
    'mungi': ['mu', 'ngi'],
    'nungi': ['nu', 'ngi'],
    'yangi': ['ya', 'ngi'],
    # NOTE: dafa, dama, danga, moo, yaa, yeena etc. are NOT split per gold standard
    'lanu': ['la', 'nu'],
    'laña': ['la', 'ña'],
    'yeena': ['yee', 'na'],
    'lane': ['lan', 'e'],
    'dootu': ['doot', 'u'],
    'ñaari': ['ñaar', 'i'],
    'ñetti': ['ñett', 'i'],
    'ñeenti': ['ñeent', 'i'],
    'fukki': ['fukk', 'i'],
    'juróomi': ['juróom', 'i'],
}

NEGATION_SUFFIXES = {
    # -uma splits as verb+u + ma (gold: bëgguma -> bëggu ma)
    'uma': ['ma'],  # verb+u stays together, only ma splits off
    # -uloo/-ulo splits as verb+u + loo/lo
    'uloo': ['loo'],
    'ulo': ['lo'],
    # -ul, -unu, -uleen, -uñu stay attached (gold: demul, amul, nekkul)
}

DO_NOT_SPLIT = frozenset([
    'wala', 'walla', 'waaye', 'yàlla', 'yalla', 'allah',
    'tuuti-tuuti', 'ndank-ndank',
    'yeena', 'moo', 'yaa', 'dafa', 'dama', 'danga', 'dañu',
    'ñaari', 'ñetti', 'ñeenti', 'fukki',
    'duma', 'doo', 'dunu', 'duñu',
    'modou', 'modu', 'mamadou', 'mamadu', 'abdoulaye', 'abdulaye', 
    'ibrahima', 'ousmane', 'usmane', 'fatou', 'fatu', 'aminata',
    'samba', 'demba', 'awa', 'moussa', 'musa', 'amadou', 'amadu',
    'mariama', 'aissatou', 'aisatu', 'aliou', 'aliu',
    'oumar', 'umar', 'binta', 'coumba', 'kumba', 'ndeye', 'ndey',
    'pape', 'cheikh', 'sokhna', 'soxna',
    'adja', 'mor', 'mbaye', 'lamine', 'malick', 'youssou', 'yusu',
    'babacar', 'babakar', 'abdou', 'abdu',
    'alassane', 'alasan', 'khady', 'xadi', 'mame', 'biram', 
    'thierno', 'cerno', 'assane', 'asan', 'djibril', 'jibril',
    'seydou', 'seydu', 'boubacar', 'bubakar', 'aida', 'astou', 'astu',
    'yacine', 'yasin', 'rokhaya', 'roxaya', 'seynabou', 'seynabou',
    'dieynaba', 'jeynaba', 'nogaye', 'aby', 'adama', 'bamba', 'fallou', 'falu', 'serigne', 'seriñ',
    'motax', 'loolu', 'sonnu',
])

# Words that normalize to different form
NORMALIZE_WORDS = {
    'lane': 'lan',  # question word variant
}

class WolofTokenizer:
    PUNCTUATION_CHARS = r""".,;:!?()[]{}«»"'"'`-–—…·•"""
    
    TAM_PATTERNS = {
        'naa', 'nga', 'na', 'nanu', 'ngeen', 'nañu',
        'dinaa', 'dinga', 'dina', 'dinanu', 'dingeen', 'dinañu',
        'duma', 'doo', 'du', 'dunu', 'dungeen', 'duñu',
        'dama', 'danga', 'dafa', 'danu', 'dangeen', 'dañu',
        'maa', 'yaa', 'moo', 'noo', 'yeena', 'ñoo',
        'la', 'laa',
    }
    
    CLITIC_SET = {'ma', 'la', 'ko', 'nu', 'leen', 'ñu'}
    
    NUMERALS = {'benn', 'ñaar', 'ñett', 'ñeent', 'juróom', 'juroom', 'fukk', 'téeméer', 'teemeer', 'junni', 'junne'}

    def __init__(self, normalize: bool = True, keep_whitespace: bool = False, 
                 detect_language: bool = True, segment_attached: bool = True):
        self.normalize = normalize
        self.keep_whitespace = keep_whitespace
        self.detect_language_flag = detect_language
        self.segment_attached = segment_attached
        self.normalizer = WolofNormalizer() if normalize else None
        self.wolof_verb_stems = self._build_verb_stem_set()
        self.sorted_negation = sorted(NEGATION_SUFFIXES.items(), key=lambda x: len(x[0]), reverse=True)

    def _build_verb_stem_set(self) -> Set[str]:
        stems = set(COMMON_VERBS)
        for verb in COMMON_VERBS:
            if len(verb) > 2:
                stems.add(verb[:-1])
                stems.add(verb[:-2])
        return stems

    def tokenize(self, text: str) -> List[Token]:
        if not text:
            return []

        try:
            clean_text = self.normalizer.normalize(text) if self.normalize else text
        except Exception:
            clean_text = text

        token_pattern = r"""
            (?:https?://\S+|www\.\S+)                                                    |
            \S+@\S+\.\S+                                                                  |
            \
            @\w+                                                                          |
            (?:[\U0001F300-\U0001F9FF]|[\U0001FA00-\U0001FAFF]|[\U00002600-\U000027BF]|
               [\U0001F600-\U0001F64F]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF])+ |
            \d+(?:[.,:/]\d+)*                                                             |
            \.{2,}|[!?]{2,}                                                              |
            [a-zA-ZàáâãäåèéêëìíîïòóôõöùúûüýÿçœæŋñÑëËŋŊ]+(?:[-'][a-zA-ZàáâãäåèéêëìíîïòóôõöùúûüýÿçœæŋñÑëËŋŊ]+)* |
            [.,;:!?()\[\]{}«»""\'"`'"-–—]                                                |
            \s+                                                                          |
            \S
        """

        raw_tokens = []
        for match in re.finditer(token_pattern, clean_text, re.VERBOSE):
            val = match.group()
            start, end = match.start(), match.end()

            if val.isspace():
                if self.keep_whitespace:
                    raw_tokens.append(Token(val, TokenType.UNKNOWN, start, end))
                continue

            token_type = self._classify_token(val)
            raw_tokens.append(Token(val, token_type, start, end))

        tokens = self._apply_word_tokenization(raw_tokens)
        
        if self.segment_attached:
            tokens = self._segment_attached_writing(tokens)
        
        if self.detect_language_flag:
            tokens = self._apply_language_detection(tokens)
        
        return tokens

    def tokenize_to_strings(self, text: str) -> List[str]:
        return [t.text for t in self.tokenize(text) if t.type == TokenType.WORD]

    def morphemes(self, text: str) -> List[str]:
        if not text:
            return []
        
        try:
            clean_text = self.normalizer.normalize(text) if self.normalize else text
        except Exception:
            clean_text = text

        token_pattern = r"""
            (?:https?://\S+|www\.\S+)                                                    |
            \S+@\S+\.\S+                                                                  |
            \
            @\w+                                                                          |
            (?:[\U0001F300-\U0001F9FF]|[\U0001FA00-\U0001FAFF]|[\U00002600-\U000027BF]|
               [\U0001F600-\U0001F64F]|[\U0001F680-\U0001F6FF]|[\U0001F1E0-\U0001F1FF])+ |
            \d+(?:[.,:/]\d+)*                                                             |
            \.{2,}|[!?]{2,}                                                              |
            [a-zA-ZàáâãäåèéêëìíîïòóôõöùúûüýÿçœæŋñÑëËŋŊ]+(?:[-'][a-zA-ZàáâãäåèéêëìíîïòóôõöùúûüýÿçœæŋñÑëËŋŊ]+)* |
            [.,;:!?()\[\]{}«»""\'"`'"-–—]                                                |
            \s+                                                                          |
            \S
        """

        result = []
        for match in re.finditer(token_pattern, clean_text, re.VERBOSE):
            val = match.group()
            if val.isspace():
                continue
            
            token_type = self._classify_token(val)
            if token_type == TokenType.WORD:
                morphs = self._decompose_to_morphemes(val)
                result.extend(morphs)
            else:
                result.append(val)
        
        return result

    def _decompose_to_morphemes(self, word: str) -> List[str]:
        low = word.lower()
        
        if low in DO_NOT_SPLIT:
            return [word]
        
        if low in MORPHEME_MAP:
            return MORPHEME_MAP[low]
        
        if low in CLITIC_COMBINATIONS:
            return CLITIC_COMBINATIONS[low]
        
        if low in AK_CONTRACTIONS:
            return AK_CONTRACTIONS[low]
        
        if low in AY_CONTRACTIONS:
            return AY_CONTRACTIONS[low]
        
        for suffix, parts in self.sorted_negation:
            if low.endswith(suffix) and len(low) > len(suffix) + 1:
                # For -uma, -uloo: keep the 'u' with the root (bëgguma -> bëggu + ma)
                root = word[:-len(suffix)+1]  # keep the 'u'
                if self._is_valid_wolof_root(root[:-1]):  # validate without u
                    return [root] + parts
        
        if self._is_numeral_connective(low, word):
            parts = self._split_numeral_connective(word)
            if parts:
                return parts
        
        if self._is_serial_verb(low):
            root, conn = self._split_serial_verb(word)
            if root:
                return [root, conn]
        
        if self.segment_attached:
            segments = self._find_attached_segments(low)
            if segments and len(segments) > 1:
                return segments
        
        return [word]

    def _classify_token(self, text: str) -> TokenType:
        if re.match(r'https?://|www\.', text):
            return TokenType.URL
        if '@' in text and '.' in text and not text.startswith('@'):
            return TokenType.EMAIL
        if text.startswith('#'):
            return TokenType.HASHTAG
        if text.startswith('@'):
            return TokenType.MENTION
        if re.match(r'[\U0001F300-\U0001FAFF]', text):
            return TokenType.EMOJI
        if text[0].isdigit():
            return TokenType.NUMBER
        if len(text) == 1 and text in self.PUNCTUATION_CHARS:
            return TokenType.PUNCTUATION
        if re.match(r'[!?.]{2,}', text):
            return TokenType.PUNCTUATION
        if any(c.isalpha() or c in "ŋëñËŊÑ" for c in text):
            return TokenType.WORD
        return TokenType.UNKNOWN

    def _apply_word_tokenization(self, tokens: List[Token]) -> List[Token]:
        refined = []

        for t in tokens:
            if t.type != TokenType.WORD:
                refined.append(t)
                continue

            low = t.text.lower()

            if low in AK_CONTRACTIONS:
                parts = AK_CONTRACTIONS[low]
                for part in parts:
                    refined.append(Token(part, TokenType.WORD, t.start, t.end, language=Language.WOLOF, is_split=True))
                continue

            if low in AY_CONTRACTIONS:
                parts = AY_CONTRACTIONS[low]
                for part in parts:
                    refined.append(Token(part, TokenType.WORD, t.start, t.end, language=Language.WOLOF, is_split=True))
                continue

            if low in POSSESSIVE_CONTRACTIONS:
                full = POSSESSIVE_CONTRACTIONS[low]
                refined.append(Token(full, TokenType.WORD, t.start, t.end, normalized=full, language=Language.WOLOF))
                continue

            if self._is_numeral_connective(low, t.text):
                parts = self._split_numeral_connective(t.text)
                if parts:
                    for part in parts:
                        refined.append(Token(part, TokenType.WORD, t.start, t.end, language=Language.WOLOF, is_split=True))
                    continue

            if self._is_serial_verb(low):
                root, connector = self._split_serial_verb(t.text)
                if root:
                    refined.append(Token(root, TokenType.WORD, t.start, t.end - len(connector), language=Language.WOLOF))
                    refined.append(Token(connector, TokenType.WORD, t.end - len(connector), t.end, language=Language.WOLOF, is_split=True))
                    continue

            refined.append(t)

        return refined

    def _segment_attached_writing(self, tokens: List[Token]) -> List[Token]:
        result = []
        
        for token in tokens:
            if token.type != TokenType.WORD:
                result.append(token)
                continue
            
            text = token.text.lower()
            
            # Skip already split tokens
            if token.is_split:
                result.append(token)
                continue
            
            # Handle word normalization (lane -> lan)
            if text in NORMALIZE_WORDS:
                result.append(Token(text=NORMALIZE_WORDS[text], type=TokenType.WORD, start=token.start, end=token.end, language=Language.WOLOF))
                continue
            
            # Skip words that shouldn't be split
            if text in DO_NOT_SPLIT:
                result.append(token)
                continue
            
            # Check MORPHEME_MAP first for TAM markers like naa, dinaa, damay
            if text in MORPHEME_MAP:
                parts = MORPHEME_MAP[text]
                for part in parts:
                    result.append(Token(text=part, type=TokenType.WORD, start=token.start, end=token.end, language=Language.WOLOF, is_split=True))
                continue
            
            # Check CLITIC_COMBINATIONS
            if text in CLITIC_COMBINATIONS:
                parts = CLITIC_COMBINATIONS[text]
                for part in parts:
                    result.append(Token(text=part, type=TokenType.WORD, start=token.start, end=token.end, language=Language.WOLOF, is_split=True))
                continue
            
            # Skip short/common words
            if len(text) <= 2 or text in COMMON_WORDS or text in ARABIC_LOANWORDS or '-' in token.text:
                result.append(token)
                continue
            
            # Check negation suffixes (-uma, -uloo splits)
            for suffix, parts in self.sorted_negation:
                if text.endswith(suffix) and len(text) > len(suffix) + 1:
                    root = text[:-len(suffix)+1]  # keep the 'u' with root
                    if self._is_valid_wolof_root(root[:-1]):
                        result.append(Token(text=root, type=TokenType.WORD, start=token.start, end=token.end, language=Language.WOLOF, is_split=True))
                        for part in parts:
                            result.append(Token(text=part, type=TokenType.WORD, start=token.start, end=token.end, language=Language.WOLOF, is_split=True))
                        break
            else:
                # Try to find attached segments (amnako -> am na ko)
                segments = self._find_attached_segments(text)
                
                if segments and len(segments) > 1:
                    for seg in segments:
                        result.append(Token(text=seg, type=TokenType.WORD, start=token.start, end=token.end, language=Language.WOLOF, is_split=True))
                else:
                    result.append(token)
            continue
        
        return result

    def _find_attached_segments(self, text: str) -> Optional[List[str]]:
        for tam_len in range(2, 6):
            for i in range(1, len(text) - tam_len + 1):
                potential_tam = text[i:i+tam_len]
                if potential_tam in self.TAM_PATTERNS:
                    verb = text[:i]
                    rest = text[i+tam_len:]
                    
                    if not self._is_valid_wolof_root(verb):
                        continue
                    
                    if not rest:
                        return [verb, potential_tam]
                    
                    if rest in self.CLITIC_SET:
                        return [verb, potential_tam, rest]
                    
                    clitic_parts = self._find_clitic_chain(rest)
                    if clitic_parts:
                        return [verb, potential_tam] + clitic_parts
        
        return None

    def _find_clitic_chain(self, text: str) -> Optional[List[str]]:
        if not text:
            return []
        if text in self.CLITIC_SET:
            return [text]
        for clitic in sorted(self.CLITIC_SET, key=len, reverse=True):
            if text.startswith(clitic):
                rest = text[len(clitic):]
                rest_parts = self._find_clitic_chain(rest)
                if rest_parts is not None:
                    return [clitic] + rest_parts
        return None

    def _apply_language_detection(self, tokens: List[Token]) -> List[Token]:
        for token in tokens:
            if token.type != TokenType.WORD or token.language is not None:
                continue
            
            word = token.text.lower()
            
            if word in FRENCH_COMMON or word in FRENCH_CONTRACTIONS:
                token.language = Language.FRENCH
            elif word in ARABIC_LOANWORDS:
                token.language = Language.ARABIC
            elif word in ENGLISH_COMMON:
                token.language = Language.ENGLISH
            elif word in COMMON_WORDS or word in ALL_DETERMINERS or word in TAM_MARKERS:
                token.language = Language.WOLOF
            elif word in SENEGAL_PLACES or word in WOLOF_NAMES:
                token.language = Language.WOLOF
            else:
                wolof_score, french_score = self._compute_language_scores(word)
                if wolof_score > french_score and wolof_score >= 15:
                    token.language = Language.WOLOF
                elif french_score > wolof_score and french_score >= 15:
                    token.language = Language.FRENCH
                else:
                    token.language = Language.UNKNOWN
        
        return tokens

    def _compute_language_scores(self, word: str) -> Tuple[int, int]:
        w = word.lower()
        wolof_score = 0
        french_score = 0
        
        if 'ë' in w: wolof_score += 50
        if 'ñ' in w: wolof_score += 50
        if 'ŋ' in w: wolof_score += 50
        if re.match(r'^(mb|nd|nj|ng|nc|nq|mp|nt|nk)', w): wolof_score += 40
        if re.search(r'([bcdgjkpqwy])\1', w): wolof_score += 35
        if re.search(r'(aa|ee|ii|oo|uu|ëë)', w): wolof_score += 25
        if re.search(r'(iku|ante|aat|loo|kat|aay|eel|adi)$', w): wolof_score += 30
        if re.match(r'^(dafa|dinaa?|moo|woo?n|ngaa?)', w): wolof_score += 35
        if 'x' in w and not w.startswith('ex'): wolof_score += 20
        if 'q' in w: wolof_score += 20
        if w.endswith('u') and len(w) > 2: wolof_score += 10
        
        if re.search(r'(tion|ment|eur|eux|ais|ait|ez|oir|age)$', w): french_score += 30
        if re.search(r'(eau|ou|oi|ai|ei|au)', w): french_score += 15
        if re.search(r'(ph|ch|gn|qu)', w): french_score += 15
        if re.match(r'^(re|dé|pré|pro|con|com)', w) and len(w) > 4: french_score += 20
        if re.search(r'[éèê]', w) and 'ë' not in w: french_score += 10
        
        return wolof_score, french_score

    def _is_numeral_connective(self, word: str, original: str) -> bool:
        # Only split hyphenated numeral compounds like juróom-ñaari, fukk-i-benn
        # Don't split standalone numerals like ñaari, ñetti
        if '-' in original and original.lower().endswith('i'):
            return True
        return False

    def _split_numeral_connective(self, word: str) -> Optional[List[str]]:
        # Only split hyphenated forms
        if '-' in word and word.lower().endswith('i'):
            return [word[:-1], 'i']
        return None

    def _is_serial_verb(self, word: str) -> bool:
        # Don't treat TAM markers as serial verbs
        if word in MORPHEME_MAP:
            return False
        return word in SERIAL_VERBS or (len(word) > 3 and word.endswith('a') and word[:-1] in self.wolof_verb_stems)

    def _split_serial_verb(self, word: str) -> Tuple[Optional[str], Optional[str]]:
        if word.lower() in SERIAL_VERBS:
            return word[:-1], 'a'
        if word.endswith('a') and word[:-1].lower() in self.wolof_verb_stems:
            return word[:-1], 'a'
        return None, None

    def _is_valid_wolof_root(self, root: str) -> bool:
        if len(root) < 2:
            return False
        low = root.lower()
        if low in self.wolof_verb_stems:
            return True
        has_vowel = any(c in VOWELS for c in low)
        has_consonant = any(c in CONSONANTS for c in low)
        if not (has_vowel and has_consonant):
            return False
        if low[:2] in PRENASALIZED or low[:2] in GEMINATES:
            return True
        cv_pattern = re.match(r'^[bcdfghjklmnñŋpqrstvwxy]+[aeëiouàáéóú][bcdfghjklmnñŋpqrstvwxy]*[aeëiouàáéóú]?[bcdfghjklmnñŋpqrstvwxy]*$', low)
        return bool(cv_pattern)

    def __call__(self, text: str) -> List[Token]:
        return self.tokenize(text)

def tokenize(text: str, normalize: bool = True) -> List[str]:
    return WolofTokenizer(normalize=normalize, segment_attached=False).tokenize_to_strings(text)

def morphemes(text: str, normalize: bool = True) -> List[str]:
    return WolofTokenizer(normalize=normalize, segment_attached=True).tokenize_to_strings(text)