"""
Wolof Noun Class System

Based on McLaughlin (1997) "Noun classification in Wolof: When affixes are not renewed"
and Robert (2024) "Wolof: A grammatical sketch" in Oxford Guide to Atlantic Languages.

CRITICAL INSIGHT: Wolof noun class assignment uses MIXED strategies, NOT pure semantic domains.
The system lacks semantic coherence - there are more exceptions than rules.

Assignment strategies (in order of productivity):
1. DEFAULT: B-class (~40% of lexicon, all modern loanwords)
2. PHONOLOGICAL "copy process": stem-initial consonant → matching class
3. SEMANTIC tendencies: weak correlations with many exceptions
4. MORPHOLOGICAL: derived nouns resist default class
5. SOCIOLINGUISTIC: urban Wolof expands B-class usage

Special cases:
- K-class is QUASI-EMPTY: only "nit" (person) as lexical member
  → Functions as generic human pronoun class (ku "who", ñi "they")
- Plural: ki → ñi ONLY for nit; ALL other classes → yi
"""

from dataclasses import dataclass, field
from typing import Optional, Dict, List
from ..core.constants import NOUN_CLASS_MARKERS, ADVERBIAL_CLASSES, PLURAL_RULES

@dataclass
class NounClassInfo:
    """Information about a Wolof noun class."""
    class_marker: str
    definite: str
    indefinite: str
    plural_marker: str
    relative: str
    demonstrative_proximal: Optional[str] = None
    demonstrative_distal: Optional[str] = None
    assignment_strategy: str = "mixed"
    tendency: str = ""
    copy_initial: Optional[str] = None
    copy_correlation: Optional[float] = None
    examples: List[str] = field(default_factory=list)
    lexicon_percentage: float = 0.0
    note: Optional[str] = None

class NounClassSystem:
    """
    Wolof noun class system manager.
    
    10 classes total: 8 singular (B, G, J, K, L, M, S, W) + 2 plural (Y, Ñ)
    Plus 2 adverbial/defective classes: F (place), N (manner)
    """
    
    def __init__(self):
        self.classes = self._build_classes()
        self.adverbial = ADVERBIAL_CLASSES
        self.plural_rules = PLURAL_RULES
    
    def _build_classes(self) -> Dict[str, NounClassInfo]:
        result = {}
        for cls, markers in NOUN_CLASS_MARKERS.items():
            result[cls] = NounClassInfo(
                class_marker=cls.lower(),
                definite=markers['def'],
                indefinite=markers['indef'],
                plural_marker=markers.get('pl', 'yi'),
                relative=markers['rel'],
                demonstrative_proximal=markers.get('dem_prox'),
                demonstrative_distal=markers.get('dem_dist'),
                assignment_strategy=markers.get('assignment', 'mixed'),
                tendency=markers.get('tendency', ''),
                copy_initial=markers.get('copy_initial'),
                copy_correlation=markers.get('copy_correlation'),
                examples=markers.get('examples', []),
                lexicon_percentage=markers.get('lexicon_pct', 0),
                note=markers.get('note')
            )
        return result
    
    def get_class(self, marker: str) -> Optional[NounClassInfo]:
        """Get class info from any marker (definite, indefinite, relative, etc.)"""
        marker = marker.lower()
        for cls, info in self.classes.items():
            if marker in [info.definite, info.indefinite, info.relative,
                         info.demonstrative_proximal, info.demonstrative_distal]:
                return info
        return None
    
    def detect_class(self, determiner: str) -> Optional[str]:
        """Detect class name from a determiner."""
        info = self.get_class(determiner)
        return info.class_marker.upper() if info else None
    
    def get_plural(self, singular_class: str) -> str:
        """Get plural marker for a singular class."""
        return self.plural_rules.get(singular_class.upper(), 'Y')
    
    def get_plural_determiner(self, singular_class: str) -> str:
        """Get plural definite article for a class."""
        plural_class = self.get_plural(singular_class)
        return 'ñi' if plural_class == 'Ñ' else 'yi'
    
    def predict_class_from_initial(self, word: str) -> Optional[str]:
        """
        Predict likely class using phonological copy process.
        
        Based on McLaughlin (1997) correlations:
        - g-initial → G-class (53.5%)
        - w-initial → W-class (52%)
        - m-initial → M-class (45%)
        - j-initial → J-class (36%)
        - s-initial → S-class (17.5%)
        """
        if not word:
            return None
        
        initial = word[0].lower()
        copy_classes = {
            'g': ('G', 0.535),
            'w': ('W', 0.52),
            'm': ('M', 0.45),
            'j': ('J', 0.36),
            's': ('S', 0.175),
            'b': ('B', 0.40),
            'l': ('L', 0.20),
        }
        
        if initial in copy_classes:
            return copy_classes[initial][0]
        
        return 'B'
    
    def get_agreement_forms(self, noun_class: str) -> Dict[str, str]:
        """Get all agreement forms for a class."""
        info = self.classes.get(noun_class.upper())
        if not info:
            return {}
        return {
            'definite_proximal': info.definite,
            'definite_distal': info.definite[0] + 'a',
            'indefinite': info.indefinite,
            'relative': info.relative,
            'plural': info.plural_marker,
            'demonstrative_proximal': info.demonstrative_proximal,
            'demonstrative_distal': info.demonstrative_distal,
        }
    
    def list_classes(self) -> List[str]:
        return list(self.classes.keys())
    
    def get_summary(self) -> str:
        """Get a linguistic summary of the noun class system."""
        return """
WOLOF NOUN CLASS SYSTEM (10 classes)

Singular classes: B, G, J, K, L, M, S, W
Plural classes: Y (general), Ñ (human only, for 'nit')

ASSIGNMENT IS MIXED (not purely semantic):
├─ DEFAULT: B-class (~40% of lexicon)
├─ PHONOLOGICAL: copy process (initial consonant → class)
├─ SEMANTIC: weak tendencies only
├─ DERIVED: morphologically derived nouns resist default
└─ SOCIOLINGUISTIC: urban Wolof expands B-class

PLURAL RULES:
├─ ki → ñi  (ONLY for 'nit' = person)
└─ bi/gi/ji/li/mi/si/wi → yi  (ALL other classes)

SPECIAL: K-class has only ONE lexical member ('nit')
         → Functions as generic human pronoun class
"""

EXAMPLE_NOUNS = {
    'B': ['xale', 'téere', 'ceeb', 'buy', 'waliis'],
    'G': ['garab', 'guy', 'gaal', 'Senegaal'],
    'J': ['jigéen', 'jumaa', 'yaay', 'doom', 'jabar'],
    'K': ['nit'],
    'L': ['liggéey', 'lëf'],
    'M': ['ndox', 'meew', 'mburu', 'màngó'],
    'S': ['suuf', 'saa', 'suba', 'seytaane'],
    'W': ['fas', 'weer', 'waxtu'],
}

PLURAL_EXAMPLES = {
    'nit ki → nit ñi': 'the person → the people (UNIQUE: ki→ñi)',
    'xale bi → xale yi': 'the child → the children',
    'garab gi → garab yi': 'the tree → the trees',
    'jigéen ji → jigéen yi': 'the woman → the women',
    'ndox mi → ndox yi': 'the water → the waters',
    'fas wi → fas yi': 'the horse → the horses',
}

def get_noun_class(determiner: str) -> Optional[str]:
    """Get class name from determiner."""
    return NounClassSystem().detect_class(determiner)

def get_class_info(class_name: str) -> Optional[NounClassInfo]:
    """Get full info for a class."""
    system = NounClassSystem()
    return system.classes.get(class_name.upper())

def get_plural_for(noun: str, singular_class: str) -> str:
    """Get plural form with correct determiner."""
    system = NounClassSystem()
    pl_det = system.get_plural_determiner(singular_class)
    return f"{noun} {pl_det}"