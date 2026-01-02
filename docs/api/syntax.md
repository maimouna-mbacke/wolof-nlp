# Syntax Module

`wolof_nlp.syntax`

## Sentence Parser

Analyzes Wolof sentence structure and focus marking.

```python
from wolof_nlp.syntax import parse_sentence, SentenceAnalysis

analysis = parse_sentence("Dafa lekk ceeb")
print(analysis.clause_type)
print(analysis.focus_type)
print(analysis.is_negative)
```

### SentenceAnalysis

| Attribute | Type | Description |
|-----------|------|-------------|
| clause_type | ClauseType | Type of clause |
| focus_type | FocusType | What is focused |
| is_negative | bool | Negation present |
| is_question | bool | Interrogative |
| subject | str | Subject if detected |
| verb | str | Main verb if detected |

### ClauseType

- `SUBJECT_FOCUS` - moo, yaa, etc.
- `VERB_FOCUS` - dafa, danga, etc.
- `PRESENTATIVE` - mungi, yaangi, etc.
- `PERFECT` - na-forms
- `FUTURE` - dina-forms
- `IMPERATIVE` - commands
- `UNKNOWN` - could not determine

### FocusType

- `SUBJECT` - subject is focused
- `VERB` - verb/action is focused
- `OBJECT` - object is focused
- `NONE` - no focus marking

## Clause Analyzer

```python
from wolof_nlp.syntax import analyze_clause, ClauseAnalysis

analysis = analyze_clause("Xale bi dafa lekk")
```

Provides lower-level clause structure analysis.
