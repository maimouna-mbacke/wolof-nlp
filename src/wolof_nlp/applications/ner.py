"""Wolof Named Entity Recognition - Pattern-based with gazetteer fallback"""

from typing import List, Optional, Tuple
from dataclasses import dataclass
import re

from ..core.tokenizer import WolofTokenizer, TokenType


@dataclass
class NamedEntity:
    text: str
    label: str
    start: int
    end: int
    confidence: float = 0.8


SENEGAL_PLACES = frozenset([
    'dakar', 'thiès', 'thies', 'kaolack', 'ziguinchor', 'saint-louis', 'ndar',
    'touba', 'mbour', 'rufisque', 'diourbel', 'louga', 'tambacounda', 'kolda',
    'matam', 'fatick', 'kaffrine', 'kédougou', 'kedougou', 'sédhiou', 'sedhiou',
    'sénégal', 'senegal', 'gambie', 'gambia', 'mauritanie', 'mali', 'guinée',
    'guinee', 'france', 'paris', 'usa', 'america', 'maroc', 'italie', 'espagne',
    'london', 'londres', 'new york', 'abidjan', 'bamako', 'conakry', 'banjul',
    'casamance', 'sine', 'saloum', 'fouta', 'walo', 'cayor', 'baol', 'djolof',
    'gorée', 'goree', 'lac rose', 'petite côte', 'cap vert', 'almadies',
])

WOLOF_FIRST_NAMES = frozenset([
    'samba', 'demba', 'fatou', 'fatu', 'awa', 'moussa', 'musa', 
    'ibrahima', 'amadou', 'amadu', 'ousmane', 'usmane',
    'mariama', 'aïssatou', 'aissatou', 'aisatu', 'aminata', 
    'modou', 'modu', 'mamadou', 'mamadu', 'abdoulaye', 'abdulaye',
    'aliou', 'aliu', 'oumar', 'umar', 'binta', 'coumba', 'kumba', 
    'daba', 'ndeye', 'ndey', 'pape', 'cheikh',
    'sokhna', 'soxna', 'adja', 'mor', 'mbaye', 'lamine', 'malick', 
    'youssou', 'yusu', 'babacar', 'babakar',
    'abdou', 'abdu', 'alassane', 'alasan', 'khady', 'xadi', 
    'mame', 'biram', 'thierno', 'cerno', 'assane', 'asan', 'djibril', 'jibril',
])

WOLOF_SURNAMES = frozenset([
    'ba', 'seck', 'mbaye', 'fall', 'ndiaye', 'faye', 'sall', 'diop', 'thiam',
    'gueye', 'sy', 'cissé', 'cisse', 'diouf', 'wade', 'diagne', 'mbacké',
    'mbacke', 'diaw', 'sarr', 'niang', 'kane', 'dia', 'tall', 'samb', 'lo',
    'ndoye', 'gning', 'sene', 'bodian', 'diatta', 'sonko', 'sow', 'camara',
])

RELIGIOUS_TITLES = frozenset([
    'serigne', 'sëriñ', 'seriñe', 'cheikh', 'sheikh', 'oustaz', 'ustaz',
    'imam', 'mame', 'sokhna', 'adja', 'el hadj', 'elhadj', 'hadj', 'hajj',
])

ORGANIZATIONS = frozenset([
    'tfm', 'rts', '2stv', 'sen tv', 'sentv', 'walf', 'gfm', 'iradio',
    'sonatel', 'orange', 'free', 'expresso', 'auchan', 'eiffage',
    'mouride', 'mouridiyya', 'tidiane', 'tidjane', 'layène', 'layene',
    'ucad', 'ugb', 'uasz', 'ept', 'esp', 'iam', 'bhs', 'cbao', 'sgbs',
])

TV_SHOWS = frozenset([
    'pod et marichou', 'maîtresse', 'maitresse', 'wiri wiri', 'adja',
    'mbettel', 'nafi', 'mœurs', 'moeurs', 'golden', 'dikoon', 'buur',
])

TITLE_PATTERN = re.compile(
    r'\b(serigne|sëriñ|seriñe|cheikh|sheikh|oustaz|ustaz|mame|sokhna|el\s*hadj)\s+([A-ZÀÁÂÃÄÅÈÉÊËÌÍÎÏÒÓÔÕÖÙÚÛÜ][a-zàáâãäåèéêëìíîïòóôõöùúûü]+)',
    re.IGNORECASE
)

MULTI_WORD_ENTITIES = {
    'serigne touba': ('Serigne Touba', 'PER', 0.98),
    'cheikh ahmadou bamba': ('Cheikh Ahmadou Bamba', 'PER', 0.99),
    'cheikh ibra': ('Cheikh Ibra', 'PER', 0.95),
    'mame diarra': ('Mame Diarra', 'PER', 0.95),
    'lamp fall': ('Lamp Fall', 'PER', 0.95),
    'baye fall': ('Baye Fall', 'ORG', 0.90),
    'saint louis': ('Saint-Louis', 'LOC', 0.95),
    'saint-louis': ('Saint-Louis', 'LOC', 0.95),
    'new york': ('New York', 'LOC', 0.95),
    'côte d\'ivoire': ('Côte d\'Ivoire', 'LOC', 0.95),
    'cote d\'ivoire': ('Côte d\'Ivoire', 'LOC', 0.95),
    'lac rose': ('Lac Rose', 'LOC', 0.90),
    'pod et marichou': ('Pod et Marichou', 'WORK', 0.95),
    'sen tv': ('Sen TV', 'ORG', 0.95),
}

EXCLUDED_CAPITALS = frozenset([
    'dafa', 'moo', 'noo', 'lan', 'fan', 'kan', 'yaa', 'maa', 'ñoo',
    'dina', 'dinaa', 'du', 'duma', 'ngi', 'je', 'tu', 'il', 'elle',
    'nous', 'vous', 'ils', 'the', 'and', 'for', 'but', 'est', 'sont',
])


class NERTagger:
    
    def __init__(self):
        self.tokenizer = WolofTokenizer(normalize=True)
    
    def _find_multi_word_entities(self, text: str) -> List[NamedEntity]:
        entities = []
        text_lower = text.lower()
        
        for pattern, (canonical, label, conf) in MULTI_WORD_ENTITIES.items():
            start = 0
            while True:
                idx = text_lower.find(pattern, start)
                if idx == -1:
                    break
                entities.append(NamedEntity(
                    text=canonical,
                    label=label,
                    start=idx,
                    end=idx + len(pattern),
                    confidence=conf,
                ))
                start = idx + 1
        
        return entities
    
    def _find_title_patterns(self, text: str) -> List[NamedEntity]:
        entities = []
        
        for match in TITLE_PATTERN.finditer(text):
            full_match = match.group(0)
            entities.append(NamedEntity(
                text=full_match,
                label='PER',
                start=match.start(),
                end=match.end(),
                confidence=0.92,
            ))
        
        return entities
    
    def _classify_word(self, word_lower: str, word_original: str, is_sentence_start: bool) -> Tuple[Optional[str], float]:
        if word_lower in SENEGAL_PLACES:
            return 'LOC', 0.95
        
        if word_lower in WOLOF_FIRST_NAMES:
            return 'PER', 0.88
        
        if word_lower in WOLOF_SURNAMES:
            return 'PER', 0.85
        
        if word_lower in RELIGIOUS_TITLES:
            return 'PER', 0.80
        
        if word_lower in ORGANIZATIONS:
            return 'ORG', 0.92
        
        if word_lower in TV_SHOWS:
            return 'WORK', 0.90
        
        if (word_original[0].isupper() and 
            len(word_original) > 2 and 
            not is_sentence_start and
            word_lower not in EXCLUDED_CAPITALS):
            return 'PER', 0.55
        
        return None, 0.0
    
    def extract(self, text: str) -> List[NamedEntity]:
        entities = []
        used_spans = set()
        
        multi_word = self._find_multi_word_entities(text)
        for ent in multi_word:
            entities.append(ent)
            for i in range(ent.start, ent.end):
                used_spans.add(i)
        
        title_entities = self._find_title_patterns(text)
        for ent in title_entities:
            if not any(i in used_spans for i in range(ent.start, ent.end)):
                entities.append(ent)
                for i in range(ent.start, ent.end):
                    used_spans.add(i)
        
        tokens = self.tokenizer.tokenize(text)
        
        for i, token in enumerate(tokens):
            if token.type != TokenType.WORD:
                continue
            
            if any(j in used_spans for j in range(token.start, token.end)):
                continue
            
            is_sentence_start = i == 0 or (i > 0 and tokens[i-1].text in '.!?')
            
            label, conf = self._classify_word(token.text.lower(), token.text, is_sentence_start)
            
            if label:
                entities.append(NamedEntity(
                    text=token.text,
                    label=label,
                    start=token.start,
                    end=token.end,
                    confidence=conf,
                ))
        
        entities.sort(key=lambda e: e.start)
        return entities


def extract_entities(text: str) -> List[NamedEntity]:
    return NERTagger().extract(text)
