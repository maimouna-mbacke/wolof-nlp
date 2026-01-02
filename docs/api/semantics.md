# Semantics Module

`wolof_nlp.semantics`

## Noun Class System

Wolof has 10 noun classes (8 singular + 2 plural). This module provides tools for working with the class agreement system.

```python
from wolof_nlp.semantics import NounClassSystem, get_class_info
```

### NounClassSystem

```python
system = NounClassSystem()

system.get_class("bi")
system.detect_class("gi")
system.get_plural("B")
system.get_plural_determiner("K")
system.predict_class_from_initial("garab")
```

### get_class_info

```python
info = get_class_info("B")
print(info.definite)
print(info.plural_marker)
```

### Noun Classes

| Class | Definite | Plural | Tendency |
|-------|----------|--------|----------|
| B | bi | yi | Default, loanwords |
| G | gi | yi | Trees, round objects |
| J | ji | yi | Some humans, Arabic loans |
| K | ki | ñi | Only 'nit' (person) |
| L | li | yi | Abstracts |
| M | mi | yi | Liquids, m-initial |
| S | si | yi | Small items, time |
| W | wi | yi | Animals, time |

### Plural Rules

- K-class: ki → ñi (only for 'nit')
- All others: → yi

## Temporal Analyzer

```python
from wolof_nlp.semantics import TemporalAnalyzer, analyze_temporal
```

Detects temporal expressions in Wolof text.

| Wolof | English | Type |
|-------|---------|------|
| tey | today | PRESENT |
| démb | yesterday | PAST |
| ëllëg | tomorrow | FUTURE |
| suba | morning | FUTURE |
| leegi | now | PRESENT |

## Spatial Analyzer

```python
from wolof_nlp.semantics import SpatialAnalyzer, analyze_spatial
```

Detects spatial expressions.

| Wolof | English | Region |
|-------|---------|--------|
| fii | here | PROXIMAL |
| foofu | there | DISTAL |
| ci | in/at | LOCATIVE |
| biir | inside | INTERIOR |
