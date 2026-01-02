# Morphology Module

`wolof_nlp.morphology`

## MorphologyAnalyzer

Decomposes words into morphemes.

```python
from wolof_nlp.morphology import MorphologyAnalyzer, analyze_morphology, Morpheme, MorphemeType
```

### analyze_morphology

```python
analyze_morphology(word: str) -> List[Morpheme]
```

### Morpheme

```python
@dataclass
class Morpheme:
    text: str
    type: MorphemeType
    gloss: Optional[str] = None
```

### MorphemeType

```python
class MorphemeType(Enum):
    ROOT = auto()
    NEGATION = auto()           # -ul, -oul
    NOMINALIZATION = auto()     # -kat (agent), -aay (abstract)
    CAUSATIVE = auto()          # -al, -loo
    REFLEXIVE = auto()          # -u, -ku
    RECIPROCAL = auto()         # -ante, -andoo
    REPETITIVE = auto()         # -aat, -waat
    DETERMINER = auto()         # -i, -a (suffixed determiners)
    TAM = auto()
    SUBJECT = auto()
    OBJECT = auto()
```

### Detected Patterns

| Pattern | Type | Example |
|---------|------|---------|
| V + ul/oul | NEGATION | demul → dem + ul |
| V + kat | NOMINALIZATION | bindkat → bind + kat |
| V + aay/waay | NOMINALIZATION | liggéeyaay |
| V + al/loo | CAUSATIVE | demal, defloo |
| V + u/ku | REFLEXIVE | soppiku |
| V + ante/andoo | RECIPROCAL | gisante |
| V + aat/waat | REPETITIVE | defaat |

### Example

```python
morphemes = analyze_morphology("bindkat")
# [Morpheme(text='bind', type=ROOT), Morpheme(text='kat', type=NOMINALIZATION)]

morphemes = analyze_morphology("demul")
# [Morpheme(text='dem', type=ROOT), Morpheme(text='ul', type=NEGATION)]
```

---

## VerbConjugator

Generates verb forms from a root.

```python
from wolof_nlp.morphology import VerbConjugator, conjugate, ConjugatedForm
```

### conjugate

```python
conjugate(root: str, tam: str = 'perfect') -> List[ConjugatedForm]
```

### ConjugatedForm

```python
@dataclass
class ConjugatedForm:
    form: str
    person: int       # 1, 2, 3
    number: str       # 'sg', 'pl'
    tam: str
    gloss: str
```

### TAM Options

| TAM | Description |
|-----|-------------|
| `perfect` | Completed action |
| `verb_focus` | Emphasis on verb |
| `subject_focus` | Emphasis on subject |
| `future` | Future action |
| `negative` | Negated future |

### Example

```python
forms = conjugate("dem", tam="perfect")

for f in forms:
    print(f"{f.form}: {f.gloss}")
# dem naa: I went
# dem nga: you went
# dem na: he/she went
# dem nanu: we went
# dem ngeen: you (pl) went
# dem nañu: they went
```

---

## Lemmatizer

Reduces inflected forms to root.

```python
from wolof_nlp.morphology import Lemmatizer, lemmatize
```

### lemmatize

```python
lemmatize(word: str) -> str
```

### Example

```python
lemmatize("demul")    # "dem"
lemmatize("bindkat")  # "bind"
lemmatize("gisante")  # "gis"
```
