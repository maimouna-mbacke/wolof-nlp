# Installation

## Requirements

- Python 3.9+
- No external dependencies for core functionality

## From PyPI

```bash
pip install wolof-nlp
```

## From Source

```bash
git clone https://github.com/maimouna-mbacke/wolof-nlp.git
cd wolof-nlp
pip install -e .
```

## Development Setup

```bash
git clone https://github.com/maimouna-mbacke/wolof-nlp.git
cd wolof-nlp
pip install -e ".[dev]"
python -m pytest tests/
```

## Verify Installation

```python
from wolof_nlp import WolofTokenizer
tokenizer = WolofTokenizer()
tokens = tokenizer.tokenize("Na nga def")
print([t.text for t in tokens])
# ['Na', 'nga', 'def']
```
