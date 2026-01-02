"""
Wolof NLP - Professional NLP tools for the Wolof language

Two tokenization modes:
- tokenize(): Word-level tokenization for NLP pipelines
- morphemes(): Deep morphological splitting for linguistic analysis
"""

from .core import (
    WolofTokenizer, 
    Token, 
    TokenType, 
    Language,
    tokenize, 
    morphemes,
    WolofNormalizer, 
    normalize
)

from .morphology.analyzer import analyze_morphology, Morpheme, MorphemeType

__version__ = "0.1.0"
__all__ = [
    "WolofTokenizer",
    "Token",
    "TokenType",
    "Language",
    "tokenize",
    "morphemes",
    "WolofNormalizer",
    "normalize",
    "analyze_morphology",
    "Morpheme",
    "MorphemeType",
]