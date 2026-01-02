# Wolof NLP Toolkit Documentation

## Overview

This toolkit provides rule-based NLP components for Wolof. The design prioritizes morphological analysis over lexicon lookup, enabling the system to process unknown words by decomposing their structure.

## Contents

### Getting Started

- [Installation](installation.md)
- [Quickstart](quickstart.md)

### Architecture

- [System Architecture](architecture.md) - Hybrid rule-based design
- [Evaluation](evaluation.md) - 95.5% F1 on 542 annotated sentences
- [Corpus Validation](corpus-validation.md) - 40K YouTube comment analysis

### API Reference

- [Core](api/core.md) - Tokenizer, Normalizer
- [Morphology](api/morphology.md) - Analyzer, Conjugator, Lemmatizer
- [Applications](api/applications.md) - Sentiment, NER, POS, Glosser
- [Semantics](api/semantics.md) - Noun classes, Temporal, Spatial
- [Syntax](api/syntax.md) - Sentence parser, Clause analyzer
- [Lexicon](api/lexicon.md) - Dictionary, Collocations, Proverbs

### Linguistic Reference

- [TAM System](linguistics/tam-system.md) - Tense-Aspect-Mood paradigms
- [Noun Classes](linguistics/noun-classes.md) - 10-class system
- [Verbal Derivation](linguistics/verbal-derivation.md) - Suffixes and patterns
- [Orthography](linguistics/orthography.md) - CLAD standard and normalization

### Additional Resources

- [References](references.md) - Academic sources
- [Demo](../notebooks/) - Sample sentences and tool demonstration

## Module Summary

| Module | Purpose | Key Classes |
|--------|---------|-------------|
| `core` | Text preprocessing | `WolofTokenizer`, `WolofNormalizer` |
| `morphology` | Word structure analysis | `MorphologyAnalyzer`, `VerbConjugator` |
| `applications` | NLP tasks | `SentimentAnalyzer`, `NERTagger`, `POSTagger` |
| `semantics` | Meaning analysis | `NounClassSystem`, `TemporalAnalyzer` |
| `syntax` | Sentence structure | `SentenceParser`, `ClauseAnalyzer` |
| `lexicon` | Vocabulary resources | `Dictionary`, `Collocations` |
