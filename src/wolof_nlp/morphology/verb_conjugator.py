"""Wolof Verb Conjugator - Generate verb forms from root"""

from typing import Dict, List
from dataclasses import dataclass

from ..core.constants import (
    SUBJECT_CLITICS, OBJECT_CLITICS, NEGATION_SUFFIXES, PAST_SUFFIXES,
    CAUSATIVE_SUFFIXES, REFLEXIVE_SUFFIXES, RECIPROCAL_SUFFIXES, REPETITIVE_SUFFIXES
)

@dataclass
class ConjugatedForm:
    form: str
    person: int
    number: str
    tam: str
    gloss: str

class VerbConjugator:
    PERFECT_MARKERS = {
        (1, 'sg'): 'naa', (2, 'sg'): 'nga', (3, 'sg'): 'na',
        (1, 'pl'): 'nanu', (2, 'pl'): 'ngeen', (3, 'pl'): 'nañu'
    }
    
    VERB_FOCUS = {
        (1, 'sg'): 'dama', (2, 'sg'): 'danga', (3, 'sg'): 'dafa',
        (1, 'pl'): 'danu', (2, 'pl'): 'dangeen', (3, 'pl'): 'dañu'
    }
    
    SUBJECT_FOCUS = {
        (1, 'sg'): 'maa', (2, 'sg'): 'yaa', (3, 'sg'): 'moo',
        (1, 'pl'): 'noo', (2, 'pl'): 'yeena', (3, 'pl'): 'ñoo'
    }
    
    FUTURE = {
        (1, 'sg'): 'dinaa', (2, 'sg'): 'dinga', (3, 'sg'): 'dina',
        (1, 'pl'): 'dinanu', (2, 'pl'): 'dingeen', (3, 'pl'): 'dinañu'
    }
    
    NEGATIVE = {
        (1, 'sg'): 'duma', (2, 'sg'): 'doo', (3, 'sg'): 'du',
        (1, 'pl'): 'dunu', (2, 'pl'): 'dungeen', (3, 'pl'): 'duñu'
    }
    
    def conjugate(self, root: str, tam: str = 'perfect') -> List[ConjugatedForm]:
        forms = []
        paradigm = self._get_paradigm(tam)
        
        for (person, number), marker in paradigm.items():
            if tam == 'perfect':
                form = f"{root} {marker}"
            elif tam in ['verb_focus', 'future', 'negative']:
                form = f"{marker} {root}"
            elif tam == 'subject_focus':
                form = f"{marker} {root}"
            else:
                form = f"{root} {marker}"
            
            forms.append(ConjugatedForm(
                form=form,
                person=person,
                number=number,
                tam=tam,
                gloss=self._make_gloss(root, person, number, tam)
            ))
        
        return forms
    
    def conjugate_all(self, root: str) -> Dict[str, List[ConjugatedForm]]:
        return {
            'perfect': self.conjugate(root, 'perfect'),
            'verb_focus': self.conjugate(root, 'verb_focus'),
            'subject_focus': self.conjugate(root, 'subject_focus'),
            'future': self.conjugate(root, 'future'),
            'negative': self.conjugate(root, 'negative'),
        }
    
    def _get_paradigm(self, tam: str) -> Dict:
        paradigms = {
            'perfect': self.PERFECT_MARKERS,
            'verb_focus': self.VERB_FOCUS,
            'subject_focus': self.SUBJECT_FOCUS,
            'future': self.FUTURE,
            'negative': self.NEGATIVE,
        }
        return paradigms.get(tam, self.PERFECT_MARKERS)
    
    def _make_gloss(self, root: str, person: int, number: str, tam: str) -> str:
        subj = {(1, 'sg'): 'I', (2, 'sg'): 'you', (3, 'sg'): 'he/she',
                (1, 'pl'): 'we', (2, 'pl'): 'you.PL', (3, 'pl'): 'they'}
        s = subj.get((person, number), '')
        
        if tam == 'perfect':
            return f"{s} {root}-ed"
        elif tam == 'verb_focus':
            return f"{s} DID {root}"
        elif tam == 'subject_focus':
            return f"it's {s} who {root}-ed"
        elif tam == 'future':
            return f"{s} will {root}"
        elif tam == 'negative':
            return f"{s} won't {root}"
        return f"{s} {root}"
    
    def derive(self, root: str, derivation: str) -> str:
        if derivation == 'reflexive':
            return root + ('ku' if root[-1] in 'aeiouëàéóú' else 'u')
        elif derivation == 'reciprocal':
            return root + 'ante'
        elif derivation == 'repetitive':
            return root + ('waat' if root[-1] in 'aeiouëàéóú' else 'aat')
        elif derivation == 'causative':
            return root + 'al'
        elif derivation == 'causative_lo':
            return root + 'lo'
        return root

def conjugate(root: str, tam: str = 'perfect') -> List[ConjugatedForm]:
    return VerbConjugator().conjugate(root, tam)