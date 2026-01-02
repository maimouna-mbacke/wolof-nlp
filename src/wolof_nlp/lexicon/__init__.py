from .utils import Lexicon, is_wolof_word, detect_noun_class, detect_tam, word_frequency
from .dictionary import Dictionary, DictionaryEntry, lookup, translate
from .collocations import Collocations, VERB_OBJECT_COLLOCATIONS, GREETING_EXPRESSIONS
from .proverbs import ProverbCollection, Proverb, get_proverbs, search_proverbs

__all__ = [
    'Lexicon', 'is_wolof_word', 'detect_noun_class', 'detect_tam', 'word_frequency',
    'Dictionary', 'DictionaryEntry', 'lookup', 'translate',
    'Collocations', 'VERB_OBJECT_COLLOCATIONS', 'GREETING_EXPRESSIONS',
    'ProverbCollection', 'Proverb', 'get_proverbs', 'search_proverbs',
]