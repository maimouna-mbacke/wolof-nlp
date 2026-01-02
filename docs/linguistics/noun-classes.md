# Noun Classes

Wolof has 10 noun classes: 8 singular and 2 plural. Assignment uses mixed strategies with many exceptions.

## Noun Class Reference Table

| Class | Singular | Plural | Example      | Meaning      | Assignment Rule                        | %   | Definite | Indefinite | Relative |
|-------|----------|--------|-------------|-------------|----------------------------------------|-----|----------|------------|----------|
| b-    | bi       | yi     | xale bi     | the child    | default, many loanwords                 | 40% | bi       | ab         | bu       |
| g-    | gi       | yi     | garab gi    | the tree     | trees, big things, g-initial           | 21% | gi       | ag         | gu       |
| j-    | ji       | yi/ñi  | jigéen ji   | the woman    | Arabic loans, kinship, j-words         | 10% | ji       | ab/ak      | ju       |
| k-    | ki       | ñi     | nit ki      | the person   | ONLY this word!                         | <1% | ki       | ak         | ku       |
| m-    | mi       | yi     | ndox mi     | the water    | liquids, m-initial                      | 13% | mi       | am         | mu       |
| w-    | wi       | yi     | fas wi      | the horse    | animals, time words, w-initial          | 12% | wi       | aw         | wu       |
| s-    | si       | yi     | suuf si     | the ground   | diminutives + time words                | 3%  | si       | as         | su       |
| l-    | li       | yi     | ndab li     | the utensil  | abstract, deverbal nouns                | 5%  | li       | ab         | lu       |


# Assignment Strategies
Wolof noun classes are assigned based on a combination of **default rules, phonological patterns, and semantic tendencies**:

### 1. Default (B-class)
  B-class accounts for ~40% of the lexicon. All modern loanwords default to B.

```
téléphone bi (the phone)
ordinateur bi (the computer)
```

### 2. Phonological Copy
Some nouns follow the **stem-initial consonant**:

| Initial | Class | Example                     |
|---------|-------|-----------------------------|
| g-      | G     | garab gi (the tree)         |
| w-      | w     | waxtaan wi (the discussion) |
| m-      | M     | meew mi (the milk)          |

> Note: This correlation is partial, not absolute.

### 3. Semantic Tendencies
Class assignment often reflects **meaning or category**:

| Class | Tendency           | Example                               |
|-------|------------------|---------------------------------------|
| K     | Humans only       | nit ki (the person)                   |
| G     | Round, large objects | garab gi (the tree)                   |
| M     | Liquids           | ndox mi (the water)                   |
| S     | Small items       | ndoom si (the little child)           |
| L     | Abstracts / deverbal nouns | ndam li (the success)                 |
| W     | Animals, time periods | jën wi (the fish), weer wi (the month) |

### 4. K-Class Special Status  
K-class is quasi-empty: only **nit** (person) is a lexical member.  
K/Ñ forms also serve as **generic human pronouns**:

```
ku ñëw (whoever comes)
ñi ñëw ñépp (all who came)
```

## Corpus Distribution

From 40K YouTube comments:

| Class | Occurrences |
|-------|-------------|
| S | 1,486 |
| B | 1,429 |
| L | 460 |
| K | 357 |
| M | 132 |
| W | 43 |
| J | 17 |
| G | 3 |

B and S dominate, consistent with B as default and S for common small items.

## Implementation

`NounClassSystem` in `semantics/noun_classes.py` provides:

- Class information lookup
- Determiner-to-class mapping
- Agreement marker generation

```python
from wolof_nlp.semantics import get_noun_class

info = get_noun_class("xale")
print(info.definite)  # "bi"
```
