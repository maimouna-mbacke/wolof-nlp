# Applications Module

`wolof_nlp.applications`

## Sentiment Analysis

```python
from wolof_nlp.applications import SentimentAnalyzer, analyze_sentiment, Sentiment, SentimentResult
```

### analyze_sentiment

```python
analyze_sentiment(text: str) -> SentimentResult
```

### SentimentResult

```python
@dataclass
class SentimentResult:
    sentiment: Sentiment
    score: float
    positive_words: List[str]
    negative_words: List[str]
    negated_words: List[str]
    intensified: bool
```

### Sentiment

```python
class Sentiment(Enum):
    POSITIVE = auto()
    NEGATIVE = auto()
    NEUTRAL = auto()
```

### Detection Features

| Feature | Implementation |
|---------|----------------|
| Negation | V + ul/oul suffix on verbs |
| Negation context | du/duma/doo + verb |
| Intensifiers | lool, trop, vraiment, très |
| Discourse flip | waaye, mais prioritize post-flip |
| Arabic positive | amine, mashallah, barke, alhamdulillah |
| French | magnifique, bravo, triste, nul |
| Emoji | ❤️😂🙏 positive, 😭😢💔 negative |

### Example

```python
result = analyze_sentiment("Neexul waaye dafa baax")
print(result.sentiment)      # Sentiment.POSITIVE
print(result.negated_words)  # ['neexul']
print(result.positive_words) # ['baax']
```

---

## Named Entity Recognition

```python
from wolof_nlp.applications import NERTagger, extract_entities, NamedEntity
```

### extract_entities

```python
extract_entities(text: str) -> List[NamedEntity]
```

### NamedEntity

```python
@dataclass
class NamedEntity:
    text: str
    label: str
    start: int
    end: int
    confidence: float
```

### Labels

| Label | Description |
|-------|-------------|
| PER | Person (including religious titles) |
| LOC | Location |
| ORG | Organization |
| WORK | Creative works (TV shows) |

### Detection Methods

1. **Multi-word patterns**: "Serigne Touba", "Cheikh Ahmadou Bamba"
2. **Title + Name**: (Serigne|Oustaz|Cheikh|Mame) + Capitalized
3. **Gazetteers**: Places, surnames, organizations

### Example

```python
entities = extract_entities("Oustaz Alioune Fall dem na Touba")
# [NamedEntity(text='Oustaz Alioune', label='PER', confidence=0.92),
#  NamedEntity(text='Fall', label='PER', confidence=0.85),
#  NamedEntity(text='Touba', label='LOC', confidence=0.95)]
```

---

## POS Tagging

```python
from wolof_nlp.applications import POSTagger, tag, POSToken
```

### tag

```python
tag(text: str) -> List[Tuple[str, str]]
```

### POSToken

```python
@dataclass
class POSToken:
    text: str
    pos: str
    confidence: float
    morphology: Optional[str]
```

### POS Tags

| Tag | Description |
|-----|-------------|
| NOUN | Noun |
| VERB | Verb |
| ADJ | Adjective |
| ADV | Adverb |
| DET | Determiner |
| PREP | Preposition |
| CONJ | Conjunction |
| PRON | Pronoun |
| NUM | Number |
| TAM | TAM marker (general) |
| TAM.SBJF | Subject focus |
| TAM.VRBF | Verb focus |
| TAM.PRSV | Presentative |
| TAM.PFV | Perfect |
| TAM.FUT | Future |
| TAM.NEGF | Negative future |
| VERB.NEG | Negated verb |
| VERB.RECIP | Reciprocal verb |
| NOUN.AGENT | Agent noun (-kat) |
| NOUN.ABSTRACT | Abstract noun (-aay) |
| FWORD | French word |
| DISC | Discourse marker |
| UNK | Unknown |

### Classification Order

1. French detection (pattern/lexicon)
2. Morphological patterns (-ul, -kat, -ante, etc.)
3. Lexicon lookup (TAM first, then content words)
4. Context rules (after determiner → NOUN)

### Example

```python
tag("Xale bi dafa jàng téere")
# [('Xale', 'NOUN'), ('bi', 'DET'), ('dafa', 'TAM'), 
#  ('jàng', 'VERB'), ('téere', 'NOUN')]
```

---

## Interlinear Glosser

```python
from wolof_nlp.applications import (
    InterlinearGlosser, gloss, gloss_to_string, gloss_to_html,
    InterlinearGloss, GlossedWord
)
```

### gloss

```python
gloss(text: str) -> InterlinearGloss
```

### gloss_to_string

```python
gloss_to_string(text: str) -> str
```

### gloss_to_html

```python
gloss_to_html(text: str) -> str
```

### InterlinearGloss

```python
@dataclass
class InterlinearGloss:
    original: str
    words: List[GlossedWord]
    
    def to_string(self) -> str
    def to_html(self) -> str
```

### GlossedWord

```python
@dataclass
class GlossedWord:
    wolof: str
    morphemes: str
    gloss: str
    translation: str
```

### Leipzig Glossing Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| 1SG, 2SG, 3SG | Person singular |
| 1PL, 2PL, 3PL | Person plural |
| PFV | Perfective |
| FUT | Future |
| NEG | Negation |
| SBJF | Subject focus |
| VRBF | Verb focus |
| PRSV | Presentative |
| CAUS | Causative |
| REFL | Reflexive |
| RECP | Reciprocal |
| [FR] | French word |

### Example

```python
print(gloss_to_string("Dinaa dem"))
# Dinaa      dem
# Dinaa      dem
# 1SG.FUT    DEM
#            go
```
