# Evaluation

## Gold Standard Corpus

542 manually annotated Wolof sentences from YouTube comments on Senegalese series.

## Results

### Overall Performance

| Metric | Score |
|--------|-------|
| Precision | 95.9% |
| Recall | 94.9% |
| **F1 Score** | **95.4%** |
| Exact Match | 83.4% (452/542) |

### Baseline Comparison

| System | Precision | Recall | F1 | Exact Match |
|--------|-----------|--------|-----|-------------|
| **Wolof NLP (ours)** | 95.9% | 94.9% | **95.4%** | 83.4% |
| NLTK RegexpTokenizer | 80.1% | 83.1% | 81.5% | 57.7% |
| Python regex | 80.1% | 83.1% | 81.5% | 57.7% |
| Whitespace split | 56.6% | 38.8% | 46.0% | 1.5% |

### By Category

| Category | Accuracy |
|----------|----------|
| standard | 91.7% (253/276) |
| compound | 91.5% (65/71) |
| code_switch | 77.5% (100/129) |
| punctuation | 51.5% (34/66) |

### Error Analysis (90 errors, 16.6% error rate)

| Error Type | Count | Percentage |
|------------|-------|------------|
| Code-switching boundaries | 26 | 29% |
| Verbal suffixes (-oo/-loo) | 11 | 12% |
| Punctuation handling | 9 | 10% |
| Other edge cases | 44 | 49% |

## Reproduce

```python
import json
from wolof_nlp import WolofTokenizer

with open('data/gold_standard.json') as f:
    gold = json.load(f)

tokenizer = WolofTokenizer(segment_attached=True)
for sent in gold:
    expected = [t.lower() for t in sent['tokens'] if t.strip()]
    predicted = [t.text.lower() for t in tokenizer.tokenize(sent['text']) 
                 if t.type.name in ('WORD', 'PUNCTUATION')]
    # Compare expected vs predicted
```

## Notes

- All numbers verified by running evaluation code on actual gold_standard.json
- NLTK/regex perform similarly because both use word boundary patterns
- Whitespace fails on Wolof because punctuation is not separated
- Lower code-switch accuracy due to French/Arabic boundary detection challenges
