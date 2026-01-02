# Lexicon Module

`wolof_nlp.lexicon`

## Dictionary

```python
from wolof_nlp.lexicon import Dictionary, DictionaryEntry, lookup, translate
```

### lookup

```python
lookup(word: str) -> Optional[DictionaryEntry]
```

### translate

```python
translate(word: str, target: str = 'english') -> Optional[str]
```

### DictionaryEntry

```python
@dataclass
class DictionaryEntry:
    wolof: str
    french: str
    english: str
    pos: str
    noun_class: Optional[str] = None
    example: Optional[str] = None
```

### Coverage

The dictionary contains approximately 100 core entries across categories:

| Category | Examples |
|----------|----------|
| Verbs | def, dem, ñëw, wax, gis, xam, bëgg, lekk |
| Body parts | bopp, xol, loxo, bët, tànk |
| Family | yaay, baay, doom, xarit, jabar |
| Time | bés, guddi, suba, démb, tey |
| Places | kër, dëkk, réew, yoon |
| Religious | yàlla, jàmm, barke |

### Example

```python
entry = lookup("dem")
print(entry.english)     # "go"
print(entry.french)      # "aller"
print(entry.pos)         # "verb"
```

---

## Collocations

```python
from wolof_nlp.lexicon import Collocations, VERB_OBJECT_COLLOCATIONS, GREETING_EXPRESSIONS
```

### Categories

**Verb-Object**
```python
[('lekk', 'ceeb', 'eat rice'),
 ('naan', 'ndox', 'drink water'),
 ('jàng', 'téere', 'read a book'), ...]
```

**Greetings**
```python
[('na nga def', 'comment ça va', 'how are you'),
 ('jàmm rekk', 'la paix seulement', 'peace only'), ...]
```

**Religious Expressions**
```python
[('yàlla na yàlla', 'que Dieu fasse', 'may God grant'),
 ('barke yàlla', 'grâce à Dieu', 'by God\'s grace'), ...]
```

### Methods

```python
class Collocations:
    def get_verb_objects(self, verb: str) -> List[Tuple[str, str]]
    def get_greetings(self) -> List[Tuple[str, str, str]]
    def get_religious(self) -> List[Tuple[str, str, str]]
    def is_collocation(self, word1: str, word2: str) -> bool
    def find_expression(self, text: str) -> List[Tuple[str, str, str]]
```

---

## Proverbs

```python
from wolof_nlp.lexicon import ProverbCollection, Proverb, get_proverbs, search_proverbs
```

### Proverb

```python
@dataclass
class Proverb:
    wolof: str
    french: str
    english: str
    theme: str
```

### Available Proverbs

15 proverbs across themes: wisdom, patience, solidarity, honor, courage, action, truth.

| Wolof | English |
|-------|---------|
| Ndank-ndank mooy jàpp golo ci ñaay | Slowly slowly catches the monkey |
| Nit nit ay garabam | Man is man's remedy |
| Loxo benn du taar | One hand cannot clap |
| Jëf ja gën wax | Actions speak louder than words |

### Methods

```python
class ProverbCollection:
    def get_all(self) -> List[Proverb]
    def get_by_theme(self, theme: str) -> List[Proverb]
    def search(self, query: str) -> List[Proverb]
    def random(self) -> Proverb
    def themes(self) -> List[str]
```

### Example

```python
proverbs = search_proverbs("patience")
print(proverbs[0].wolof)   # "Ndank-ndank mooy jàpp golo ci ñaay"
print(proverbs[0].english) # "Slowly slowly catches the monkey"
```

---

## Lexicon Utilities

```python
from wolof_nlp.lexicon import Lexicon, is_wolof_word, detect_noun_class, detect_tam
```

### is_wolof_word

```python
is_wolof_word(word: str) -> bool
```

### detect_noun_class

```python
detect_noun_class(determiner: str) -> Optional[str]
```

### detect_tam

```python
detect_tam(marker: str) -> Optional[str]
```

Returns TAM type: `'subject_focus'`, `'verb_focus'`, `'presentative'`, `'perfect'`, `'future'`, `'negative'`.
