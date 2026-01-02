"""Wolof Interlinear Glosser - Morphological decomposition with Leipzig conventions"""

from typing import List, Optional
from dataclasses import dataclass
import re

from ..core.tokenizer import WolofTokenizer, TokenType
from ..morphology.analyzer import MorphologyAnalyzer
from ..lexicon.dictionary import Dictionary


@dataclass
class GlossedWord:
    wolof: str
    morphemes: str
    gloss: str
    translation: str


@dataclass
class InterlinearGloss:
    original: str
    words: List[GlossedWord]
    
    def to_string(self) -> str:
        lines = [[], [], [], []]
        for w in self.words:
            width = max(len(w.wolof), len(w.morphemes), len(w.gloss), len(w.translation))
            lines[0].append(w.wolof.ljust(width))
            lines[1].append(w.morphemes.ljust(width))
            lines[2].append(w.gloss.ljust(width))
            lines[3].append(w.translation.ljust(width))
        
        return '\n'.join('  '.join(line) for line in lines)
    
    def to_html(self) -> str:
        html = '<table class="interlinear" style="border-collapse:collapse;font-family:monospace;">'
        html += '<tr style="font-weight:bold;background:#f0f0f0;">'
        for w in self.words:
            html += f'<td style="padding:4px 8px;border:1px solid #ddd;">{w.wolof}</td>'
        html += '</tr><tr>'
        for w in self.words:
            html += f'<td style="padding:4px 8px;border:1px solid #ddd;color:#666;">{w.morphemes}</td>'
        html += '</tr><tr>'
        for w in self.words:
            html += f'<td style="padding:4px 8px;border:1px solid #ddd;font-style:italic;">{w.gloss}</td>'
        html += '</tr><tr style="background:#f8f8f8;">'
        for w in self.words:
            html += f'<td style="padding:4px 8px;border:1px solid #ddd;">{w.translation}</td>'
        html += '</tr></table>'
        return html


FRENCH_PATTERNS = re.compile(r'.*(tion|ment|eur|eux|oir|age|ais|ait|ez|ence|ance)$', re.IGNORECASE)

FRENCH_COMMON = frozenset([
    'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'le', 'la', 'les',
    'un', 'une', 'des', 'de', 'du', 'et', 'ou', 'mais', 'est', 'sont', 'avec',
    'pour', 'dans', 'sur', 'très', 'trop', 'bien', 'mal', 'vraiment', 'merci',
])

LEIPZIG_GLOSSES = {
    'ROOT': '',
    'TAM': 'TAM',
    'PERFECT': 'PFV',
    'SUBJECT_FOCUS': 'SBJF',
    'VERB_FOCUS': 'VRBF',
    'PRESENTATIVE': 'PRSV',
    'FUTURE': 'FUT',
    'NEGATIVE': 'NEG',
    'NEGATION': 'NEG',
    'IMPERFECTIVE': 'IPFV',
    'SUBJECT': 'SBJ',
    'OBJECT': 'OBJ',
    'PAST': 'PST',
    'CAUSATIVE': 'CAUS',
    'CAUSATIVE_LO': 'CAUS',
    'REFLEXIVE': 'REFL',
    'RECIPROCAL': 'RECP',
    'REPETITIVE': 'REP',
    'NOMINALIZATION': 'NMLZ',
    'DETERMINER': 'DET',
    'BENEFACTIVE': 'BEN',
    'REVERSIVE': 'REV',
    'INTENSIVE': 'INTS',
}

PERSON_MARKERS = {
    'naa': '1SG.PFV',
    'nga': '2SG.PFV',
    'na': '3SG.PFV',
    'nanu': '1PL.PFV',
    'ngeen': '2PL.PFV',
    'nañu': '3PL.PFV',
    'maa': '1SG.SBJF',
    'yaa': '2SG.SBJF',
    'moo': '3SG.SBJF',
    'noo': '1PL.SBJF',
    'yeena': '2PL.SBJF',
    'ñoo': '3PL.SBJF',
    'dama': '1SG.VRBF',
    'danga': '2SG.VRBF',
    'dafa': '3SG.VRBF',
    'danu': '1PL.VRBF',
    'dangeen': '2PL.VRBF',
    'dañu': '3PL.VRBF',
    'dinaa': '1SG.FUT',
    'dinga': '2SG.FUT',
    'dina': '3SG.FUT',
    'dinanu': '1PL.FUT',
    'dingeen': '2PL.FUT',
    'dinañu': '3PL.FUT',
    'duma': '1SG.NEGF',
    'doo': '2SG.NEGF',
    'du': '3SG.NEGF',
    'dunu': '1PL.NEGF',
    'dungeen': '2PL.NEGF',
    'duñu': '3PL.NEGF',
    'maangi': '1SG.PRSV',
    'yaangi': '2SG.PRSV',
    'mungi': '3SG.PRSV',
    'nungi': '1PL.PRSV',
    'yeengi': '2PL.PRSV',
    'ñungi': '3PL.PRSV',
}


class InterlinearGlosser:
    
    def __init__(self):
        self.tokenizer = WolofTokenizer(normalize=True)
        self.analyzer = MorphologyAnalyzer()
        self.dictionary = Dictionary()
    
    def _is_french(self, word: str) -> bool:
        w = word.lower()
        if w in FRENCH_COMMON:
            return True
        if FRENCH_PATTERNS.match(w) and len(w) > 4:
            return True
        return False
    
    def _gloss_morpheme(self, morpheme) -> str:
        if morpheme.type.name in LEIPZIG_GLOSSES:
            gloss = LEIPZIG_GLOSSES[morpheme.type.name]
            if gloss:
                return gloss
        return morpheme.text.upper()
    
    def _get_person_gloss(self, word: str) -> Optional[str]:
        return PERSON_MARKERS.get(word.lower())
    
    def _lookup_translation(self, word: str, morphemes: list) -> str:
        entry = self.dictionary.lookup(word.lower())
        if entry:
            return entry.english
        
        if morphemes:
            root = morphemes[0].text if morphemes else word.lower()
            entry = self.dictionary.lookup(root)
            if entry:
                return entry.english
            
            for length in range(len(root) - 1, 2, -1):
                entry = self.dictionary.lookup(root[:length])
                if entry:
                    return entry.english + '...'
        
        return '?'
    
    def gloss(self, text: str) -> InterlinearGloss:
        tokens = self.tokenizer.tokenize(text)
        words = []
        
        for token in tokens:
            if token.type != TokenType.WORD:
                continue
            
            if self._is_french(token.text):
                words.append(GlossedWord(
                    wolof=token.text,
                    morphemes=token.text,
                    gloss='[FR]',
                    translation=token.text,
                ))
                continue
            
            person_gloss = self._get_person_gloss(token.text)
            if person_gloss:
                words.append(GlossedWord(
                    wolof=token.text,
                    morphemes=token.text,
                    gloss=person_gloss,
                    translation='',
                ))
                continue
            
            morphemes = self.analyzer.analyze(token.text)
            
            if morphemes:
                morph_str = '-'.join(m.text for m in morphemes)
                gloss_str = '-'.join(self._gloss_morpheme(m) for m in morphemes)
            else:
                morph_str = token.text
                gloss_str = token.text.upper()
            
            translation = self._lookup_translation(token.text, morphemes)
            
            words.append(GlossedWord(
                wolof=token.text,
                morphemes=morph_str,
                gloss=gloss_str,
                translation=translation,
            ))
        
        return InterlinearGloss(original=text, words=words)


def gloss(text: str) -> InterlinearGloss:
    return InterlinearGlosser().gloss(text)


def gloss_to_string(text: str) -> str:
    return InterlinearGlosser().gloss(text).to_string()


def gloss_to_html(text: str) -> str:
    return InterlinearGlosser().gloss(text).to_html()
