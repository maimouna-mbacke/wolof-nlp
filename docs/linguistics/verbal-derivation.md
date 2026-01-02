# Verbal Derivation

Wolof verbs combine with 30+ derivational suffixes to create new meanings. This toolkit implements detection for the most productive patterns.

## Implemented Patterns

### Negation (-ul/-oul)

Applies **only to verbs**. This is a critical constraint.

| Root | Derived | Meaning |
|------|---------|---------|
| dem | demul | didn't go |
| neex | neexul | not good |
| xam | xamul | doesn't know |
| am | amul | doesn't have |

**Cannot apply to nouns:**
- bindkat (writer) + ul → INVALID
- jàngkat (student) + ul → INVALID

### Agent Nouns (-kat)

Derives nouns meaning "one who V".

| Root | Derived | Meaning |
|------|---------|---------|
| bind | bindkat | writer |
| jàng | jàngkat | student |
| liggéey | liggéeykat | worker |
| ñaw | ñawkat | tailor |

### Abstract Nouns (-aay/-waay/-in)

Derives nouns for the act or result of V.

| Root  | Derived  | Meaning  |
|-------|----------|----------|
| rafet | rafetaay | beauty   |
| baax  | baaxaay  | kindness |

### Causative (-al/-loo/-lu/-andi)

"Make someone V" or "V for someone".

| Root | Derived | Meaning |
|------|---------|---------|
| dem | demal | make go / go for |
| def | defloo | make do |
| lekk | lekkal | feed (make eat) |

### Reflexive (-u/-ku/-iku)

Subject acts on self.

| Root | Derived | Meaning |
|------|---------|---------|
| soppi | soppiku | change oneself |
| faj | faju | heal oneself |
| raxass | raxassu | wash oneself |

### Reciprocal (-ante/-andoo/-aante)

"V each other".

| Root | Derived | Meaning |
|------|---------|---------|
| gis | gisante | see each other |
| bëgg | bëggante | love each other |
| xam | xamante | know each other |

### Repetitive (-aat/-waat)

"V again".

| Root | Derived | Meaning     |
|------|---------|-------------|
| def | defaat | do again    |
| wax | waxaat | say again   |
| jël | jëliwaat | fetch again |

## Detection in Code

The morphology analyzer uses regex patterns:

```python
VERB_NEGATION_PATTERN = re.compile(r'^(.+?)(w?oul|w?ul)$')
AGENT_NOUN_PATTERN = re.compile(r'^(.+?)(kat)$')
RECIPROCAL_PATTERN = re.compile(r'^(.+?)(ante|andoo|aante)$')
# etc.
```

Minimum root length constraints prevent false positives.

## Suffix Stacking

Suffixes can combine:

```
wax + aat + oon + na → waxaatoon na (said again)
gis + ante + woon → gisantewoon (used to see each other)
```

The analyzer processes right-to-left to extract layered morphology.

## Corpus Evidence

From 40K YouTube comments, negated verb forms (-ul) appeared 2,011 times, confirming the pattern's productivity.
