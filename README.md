# Wolof NLP Toolkit
[![PyPI version](https://img.shields.io/pypi/v/wolof-nlp.svg)](https://pypi.org/project/wolof-nlp/)
[![PyPI downloads](https://img.shields.io/pypi/dm/wolof-nlp.svg)](https://pypi.org/project/wolof-nlp/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Wolof is a Niger–Congo language spoken by over 18 million people across Senegal, Gambia, and Mauritania, yet it remains largely unsupported by mainstream NLP libraries such as spaCy and NLTK. This toolkit addresses that gap by providing Wolof-aware processing that accounts for the language’s complex tense–aspect–mood (TAM) system, agglutinative morphology, and pervasive code-switching with French and Arabic.
## Features

- **Tokenization** with two modes: word-level and morpheme-level
- **Language detection** for Wolof, French, and Arabic loanwords
- **Orthography normalization** (informal → CLAD standard)
- **Morphological analysis** with derivational suffix recognition
- **POS tagging** with Wolof-specific tagset
- **Named Entity Recognition** with Senegalese gazetteers
- **Sentiment analysis** with negation and intensifier handling
- **Interlinear glossing** following Leipzig conventions

## Installation

```bash
pip install wolof-nlp
```

Or install from source:

```bash
git clone https://github.com/maimouna-mbacke/wolof-nlp.git
cd wolof-nlp
pip install -e .
```

## Quick Start

```python
from wolof_nlp import WolofTokenizer, tokenize, morphemes, normalize, analyze_morphology

# Tokenization with language detection
tokenizer = WolofTokenizer(normalize=True, detect_language=True)
tokens = tokenizer.tokenize("Dafa trop neex")
for tok in tokens:
    print(f"{tok.text}: {tok.language.name}")
# Dafa: WOLOF
# trop: FRENCH
# neex: WOLOF

# Two tokenization modes
tokenize("Damay dem")    # ['Damay', 'dem'] - word level
morphemes("Damay dem")   # ['da', 'ma', 'y', 'dem'] - morpheme level

# Orthography normalization
normalize("dieuradieuf")  # → 'jërëjëf'

# Morphological analysis
analyze_morphology("bindkat")  # → [bind:ROOT, kat:NOMINALIZATION]
```

## Applications

```python
from wolof_nlp.applications import tag, extract_entities, analyze_sentiment, gloss

# POS Tagging
tag("Xale bi dafa lekk")
# [('Xale', 'NOUN'), ('bi', 'DET'), ('dafa', 'TAM'), ('lekk', 'VERB')]

# Named Entity Recognition
extract_entities("Abdou dem na Dakar")
# [NamedEntity('Abdou', 'PER'), NamedEntity('Dakar', 'LOC')]

# Sentiment Analysis (negation-aware)
result = analyze_sentiment("Dafa neex lool")
print(result.sentiment)  # POSITIVE

# Interlinear Glossing
gloss("Xale bi mungi fo").to_string()
```

## Evaluation

Tokenizer performance on 542 annotated sentences:

| System | Precision | Recall | F1 | Exact Match |
|--------|-----------|--------|-----|-------------|
| **Wolof NLP** | 95.9% | 94.9% | **95.4%** | 83.4% |
| Regex baseline | 80.1% | 83.1% | 81.5% | 57.7% |
| Whitespace | 56.6% | 38.8% | 46.0% | 1.5% |

See [evaluation details](docs/evaluation.md).

Validated against a real-world corpus of 40,102 YouTube comments from Senegalese series 
(69.4% Wolof-French code-switching). See [corpus validation](docs/corpus-validation.md).

## Documentation

- **Notebooks**
  - [01_quickstart.ipynb](notebooks/01_quickstart.ipynb) - Core functionality
  - [02_applications.ipynb](notebooks/02_applications.ipynb) - NLP applications
  - [03_evaluation.ipynb](notebooks/03_evaluation.ipynb) - Evaluation on gold standard
- **API Reference**: [docs/api/](docs/api/)
- **Linguistics**: [docs/linguistics/](docs/linguistics/)

## Project Structure

```
wolof-nlp/
├── src/wolof_nlp/
│   ├── core/           # Tokenizer, normalizer
│   ├── morphology/     # Morphological analyzer
│   ├── applications/   # POS, NER, sentiment, glosser
│   ├── lexicon/        # Dictionary, collocations
│   ├── semantics/      # Noun classes, spatial, temporal
│   └── syntax/         # Sentence parser, clause analyzer
├── data/
│   └── gold_standard.json
├── notebooks/
├── tests/
└── docs/
```

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

**Maimouna MBACKE** - [GitHub](https://github.com/maimouna-mbacke)

## Acknowledgments

- Wolof linguistic resources from Ka (1994), McLaughlin, Robert
- CLAD orthography standard
- Senegalese YouTube corpus for gold standard data
