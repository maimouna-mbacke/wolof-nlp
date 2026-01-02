"""Wolof Lemmatizer - Extract dictionary forms from inflected words"""

from typing import Optional, Tuple
from .analyzer import MorphologyAnalyzer, MorphemeType

class Lemmatizer:
    def __init__(self):
        self.analyzer = MorphologyAnalyzer()
    
    def lemmatize(self, word: str) -> Tuple[str, str]:
        """Returns (lemma, morphological_info)"""
        morphemes = self.analyzer.analyze(word)
        
        if len(morphemes) == 1 and morphemes[0].type == MorphemeType.ROOT:
            return word.lower(), "root"
        
        root = None
        suffixes = []
        
        for m in morphemes:
            if m.type == MorphemeType.ROOT:
                root = m.text
            elif m.type not in [MorphemeType.TAM, MorphemeType.OBJECT, MorphemeType.SUBJECT]:
                suffixes.append(m.type.name.lower())
        
        if root:
            info = "+".join(suffixes) if suffixes else "root"
            return root, info
        
        return word.lower(), "unknown"
    
    def get_lemma(self, word: str) -> str:
        return self.lemmatize(word)[0]

def lemmatize(word: str) -> str:
    return Lemmatizer().get_lemma(word)