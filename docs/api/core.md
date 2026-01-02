# Core Module

`wolof_nlp.core`

## WolofTokenizer

Tokenizes Wolof text into words, handling contractions, clitics, and punctuation.

```python
from wolof_nlp import WolofTokenizer, Token, TokenType
```

### Constructor

```python
WolofTokenizer(
    normalize: bool = False,
    detect_language: bool = False
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `normalize` | bool | False | Apply orthographic normalization |
| `detect_language` | bool | False | Detect per-token language |

### Methods

#### tokenize

```python
tokenize(text: str) -> List[Token]
```

Returns a list of `Token` objects.

#### tokenize_words

```python
tokenize_words(text: str) -> List[str]
```

Returns word strings only (no punctuation).

### Token

```python
@dataclass
class Token:
    text: str
    type: TokenType
    start: int
    end: int
    language: Optional[Language] = None
```

### TokenType

```python
class TokenType(Enum):
    WORD = auto()
    PUNCTUATION = auto()
    NUMBER = auto()
    WHITESPACE = auto()
    UNKNOWN = auto()
```

### Language

```python
class Language(Enum):
    WOLOF = auto()
    FRENCH = auto()
    ARABIC = auto()
    ENGLISH = auto()
    UNKNOWN = auto()
```

### Example

```python
tokenizer = WolofTokenizer(normalize=True)
tokens = tokenizer.tokenize("Beug naa ko")

for t in tokens:
    print(f"{t.text}: {t.type.name}")
# bëgg: WORD  (normalized from "beug")
# naa: WORD
# ko: WORD
```

---

## WolofNormalizer

Converts variant spellings to CLAD standard orthography.

```python
from wolof_nlp import WolofNormalizer, normalize
```

### Constructor

```python
WolofNormalizer()
```

### Methods

#### normalize

```python
normalize(text: str) -> str
```

### Convenience Function

```python
normalize(text: str) -> str
```

### Mappings

| Input | Output | Notes |
|-------|--------|-------|
| beug, begg | bëgg | "want/love" |
| nekh, neekh | neex | "be good" |
| nek | nekk | "be/exist" |
| wakh | wax | "speak" |
| kham | xam | "know" |
| niou, gnou | ñu | 3PL pronoun |
| machallah | mashallah | Arabic |
| dieuredieuf | jërëjëf | "thank you" |

### Example

```python
from wolof_nlp import normalize

normalize("Beug naa ko")  # "Bëgg naa ko"
normalize("Dieuredieuf")  # "Jërëjëf"
```

---

## Constants

`wolof_nlp.core.constants`

### TAM Markers

```python
SUBJECT_FOCUS = frozenset(['maa', 'yaa', 'moo', 'noo', 'yeena', 'ñoo'])
VERB_FOCUS = frozenset(['dama', 'danga', 'dafa', 'danu', 'dangeen', 'dañu'])
PRESENTATIVE = frozenset(['maangi', 'yaangi', 'mungi', 'nungi', ...])
PERFECT = frozenset(['naa', 'nga', 'na', 'nanu', 'ngeen', 'nañu'])
FUTURE = frozenset(['dinaa', 'dinga', 'dina', 'dinanu', 'dingeen', 'dinañu'])
NEGATIVE_FUTURE = frozenset(['duma', 'doo', 'du', 'dunu', 'dungeen', 'duñu'])
```

### Determiners

```python
NOUN_CLASS_MARKERS = {
    'B': {'def': 'bi', 'indef': 'ab', 'rel': 'bu', ...},
    'G': {'def': 'gi', 'indef': 'ag', 'rel': 'gu', ...},
    ...
}

ALL_DETERMINERS = frozenset(['bi', 'gi', 'ji', 'ki', 'li', 'mi', 'si', 'wi', ...])
```

### Vocabulary

```python
COMMON_VERBS = frozenset(['def', 'dem', 'ñëw', 'wax', 'gis', 'xam', ...])
COMMON_NOUNS = frozenset(['bopp', 'xol', 'loxo', 'doom', 'yaay', ...])
FRENCH_COMMON = frozenset(['mais', 'que', 'pour', 'vraiment', ...])
```
