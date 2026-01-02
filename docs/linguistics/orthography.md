# Orthography

Wolof uses multiple spelling conventions. This toolkit normalizes to CLAD (Centre de Linguistique Appliquée de Dakar) standard.

## Vowel System

### CLAD Standard

| Short | Long | IPA |
|-------|------|-----|
| a | aa | /a/, /aː/ |
| e | ee | /ɛ/, /ɛː/ |
| ë | ëë | /ə/, /əː/ |
| i | ii | /i/, /iː/ |
| o | oo | /ɔ/, /ɔː/ |
| u | uu | /u/, /uː/ |

### Common Variants Normalized

| Variant | Standard | Notes |
|---------|----------|-------|
| eu, euh | ë | French influence |
| ou | u | French influence |
| oe | ë | Rare |

## Consonants

### CLAD Standard

| Letter | IPA | Notes |
|--------|-----|-------|
| c | /tʃ/ | Not "k" sound |
| j | /dʒ/ | |
| x | /x/ | Voiceless velar fricative |
| ñ | /ɲ/ | Palatal nasal |
| ŋ | /ŋ/ | Velar nasal |

### Common Variants Normalized

| Variant | Standard | Notes |
|---------|----------|-------|
| kh | x | French/Arabic influence |
| gn, ny | ñ | |
| dj | j | French influence |
| tch, ch | c | French influence |

## Word Normalizations

High-frequency mappings from corpus analysis of 40K senegalese YouTube comments:

| Input | Output | Count in corpus |
|-------|--------|-----------------|
| beug, begg | bëgg | 726 |
| nekh, neekh | neex | 684 |
| nek | nekk | 684 |
| wakh | wax | 688 |
| niou, gnou | ñu | 969 |
| machallah | mashallah | 1,031 |
| dieuredieuf | jërëjëf | 243 |

## Implementation

The normalizer applies mappings in two stages:

1. **Word-level**: Complete word replacements
2. **Orthographic**: Character sequence substitutions

French words are detected and excluded from normalization to prevent corruption.

```python
from wolof_nlp import normalize

normalize("Beug naa ko")      # "Bëgg naa ko"
normalize("C'est vraiment")   # "C'est vraiment" (unchanged)
```

## Diacritics

Wolof uses:
- Grave accent: à, ë
- Acute accent: é (in some conventions)
- Tilde: ñ

Input without diacritics is accepted but may reduce analysis accuracy.
