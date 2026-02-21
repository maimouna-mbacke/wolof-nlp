# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-01-01

### Added

- **Core**
  - `WolofTokenizer` with two modes: word-level and morpheme-level
  - `WolofNormalizer` for orthography normalization (informal → CLAD)
  - Language detection for Wolof, French, Arabic loanwords
  - `tokenize()` and `morphemes()` convenience functions

- **Morphology**
  - `analyze_morphology()` for derivational analysis
  - Detection of: negation (-ul), causative (-al, -loo), reflexive (-u, -ku), 
    reciprocal (-ante), repetitive (-aat), agent nouns (-kat)

- **Applications**
  - `tag()` - POS tagging with Wolof-specific tagset
  - `extract_entities()` - NER with Senegalese gazetteers
  - `analyze_sentiment()` - Sentiment with negation handling
  - `gloss()` - Interlinear glossing (Leipzig conventions)

- **Data**
  - Gold standard corpus: 542 annotated sentences
  - Evaluation: 95.4% F1 on tokenization

### Technical

- Python 3.8+ support
- Zero external dependencies for core functionality
- Comprehensive test suite

  ## [0.1.1] - 2026-02-21
### Documentation
- Added corpus validation reference in README
- Corpus: 40,102 YouTube comments, 69.4% code-switching
