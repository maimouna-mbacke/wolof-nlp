# Architecture

## Design Rationale

Wolof is agglutinative: verbs combine with TAM markers, focus particles, clitics, and derivational suffixes to produce dozens of surface forms. A lexicon-only approach fails because:

1. Unknown words cannot be analyzed
2. The lexicon would need to enumerate all possible verb forms
3. Social media text contains misspellings and non-standard forms

This toolkit uses a hybrid approach: morphological rules decompose words into analyzable units, lexicon lookup enriches the analysis when available.

## Processing Layers

```
┌─────────────────────────────────────────┐
│  LAYER 1: RULE-BASED                    │
│  - Morphological decomposition          │
│  - Suffix pattern matching              │
│  - TAM marker detection                 │
│  - French word detection                │
│  Priority: Applied first                │
│  Coverage: Handles unknown words        │
├─────────────────────────────────────────┤
│  LAYER 2: LEXICON                       │
│  - Root translations                    │
│  - Sentiment scores                     │
│  - Named entity gazetteers              │
│  Priority: Enriches rule output         │
│  Coverage: ~100 dictionary entries      │
└─────────────────────────────────────────┘
```

## Module Dependencies

```
core/
├── constants.py      ← All linguistic data
├── tokenizer.py      ← Uses constants
└── normalizer.py     ← Uses constants

morphology/
├── analyzer.py       ← Uses core
├── lemmatizer.py     ← Uses analyzer
└── verb_conjugator.py ← Uses constants

applications/
├── sentiment.py      ← Uses tokenizer, constants
├── ner.py            ← Uses tokenizer
├── pos_tagger.py     ← Uses tokenizer, constants
└── glosser.py        ← Uses tokenizer, morphology, lexicon

semantics/
├── noun_classes.py   ← Uses constants
├── temporal.py       ← Uses tokenizer
└── spatial.py        ← Uses tokenizer

syntax/
├── sentence_parser.py ← Uses tokenizer, constants
└── clause_analyzer.py ← Uses tokenizer, constants

lexicon/
├── dictionary.py     ← Standalone
├── collocations.py   ← Standalone
├── proverbs.py       ← Standalone
└── utils.py          ← Uses constants
```

## Key Implementation Decisions

### Negation Detection

The suffix `-ul/-oul` marks verbal negation. It does not apply to nouns.

```python
# Correct: verb + ul
"demul" → dem + ul → "didn't go"
"neexul" → neex + ul → "not good"

# Incorrect: nouns cannot take -ul
"bindkat" (writer) + ul → NOT VALID WOLOF
```

The sentiment analyzer and POS tagger check morphological class before applying negation rules.

### TAM Classification Priority

TAM markers (dafa, dinaa, moo, etc.) are classified before context rules to prevent misclassification.

```python
# Without priority: "bi dafa jàng"
# Context rule sees "bi" (determiner) and marks next word as NOUN
# Result: dafa → NOUN (wrong)

# With priority: TAM check runs first
# Result: dafa → TAM.VRBF (correct)
```

### Discourse Flipper Handling

Wolof uses `waaye` (and French `mais`) as contrastive markers. Sentiment after the flipper typically represents the speaker's conclusion.

```python
"Metti na waaye baax na"  # It's hard but it's good
# Sentiment: POSITIVE (prioritizes post-waaye content)
```

### French Detection

Code-switching is pervasive (69% of corpus). French words are detected by:

1. Membership in common French word list
2. Suffix patterns: `-tion`, `-ment`, `-eur`, `-eux`, `-ance`, `-ence`

French words receive the `FWORD` POS tag and `[FR]` gloss marker.

## Data Flow

### Sentiment Analysis

```
Input text
    │
    ▼
Tokenize (with normalization)
    │
    ▼
For each word:
    ├── Check verb negation pattern (-ul)
    ├── Check negation context (du + verb)
    ├── Check positive/negative lexicons
    ├── Check Arabic expressions
    ├── Check French sentiment words
    └── Check emoji
    │
    ▼
Apply discourse flipper logic
    │
    ▼
Calculate weighted score
    │
    ▼
Return SentimentResult
```

### POS Tagging

```
Input text
    │
    ▼
Tokenize
    │
    ▼
For each word:
    ├── Check if French → FWORD
    ├── Check morphological patterns → VERB.NEG, NOUN.AGENT, etc.
    ├── Check lexicon (TAM first, then VERB/NOUN) → category
    └── Check context rules → fallback category
    │
    ▼
Return [(word, POS), ...]
```

## Test Coverage

The test suite (`tests/test_tokenizer.py`) validates:

- Tokenization accuracy
- Morphological decomposition
- Sentiment negation handling
- NER entity extraction
- POS tag assignment
- Glosser output

Run tests:

```bash
python tests/test_tokenizer.py
```
