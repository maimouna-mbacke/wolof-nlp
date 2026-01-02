# Quickstart

## Installation

```bash
pip install wolof-nlp
```

Or from source:

```bash
git clone https://github.com/maimouna-mbacke/wolof-nlp
cd wolof-nlp
pip install -e .
```

## Two Tokenization Modes

```python
from wolof_nlp import tokenize, morphemes

tokenize("Damay dem.")
morphemes("Damay dem.")
```

Output:
```
['Damay', 'dem']
['da', 'ma', 'y', 'dem']
```

## Tokenization with Language Detection

```python
from wolof_nlp import WolofTokenizer

tokenizer = WolofTokenizer(normalize=True, detect_language=True)
tokens = tokenizer.tokenize("Dafa trop neex Dakar")

for tok in tokens:
    if tok.type.name == 'WORD':
        print(f"{tok.text}: {tok.language.name}")
```

Output:
```
Dafa: WOLOF
trop: FRENCH
neex: WOLOF
Dakar: WOLOF
```

## Orthography Normalization

```python
from wolof_nlp import normalize

normalize("dieuradieuf")
normalize("serigne")
normalize("sokhna")
```

Output:
```
'jërëjëf'
'seriñ'
'soxna'
```

## Morphological Analysis

```python
from wolof_nlp import analyze_morphology

analyze_morphology("bindkat")
analyze_morphology("demul")
analyze_morphology("gisante")
analyze_morphology("soppiku")
```

Output:
```
[bind:ROOT, kat:NOMINALIZATION(agent)]
[dem:ROOT, ul:NEGATION]
[gis:ROOT, ante:RECIPROCAL]
[soppi:ROOT, ku:REFLEXIVE]
```

## POS Tagging

```python
from wolof_nlp.applications import tag

tag("Xale bi dafa lekk")
```

Output:
```
[('Xale', 'NOUN'), ('bi', 'DET'), ('dafa', 'TAM'), ('lekk', 'VERB')]
```

## Named Entity Recognition

```python
from wolof_nlp.applications import extract_entities

entities = extract_entities("Serigne Touba dem na Dakar")

for ent in entities:
    print(f"{ent.text}: {ent.label}")
```

Output:
```
Serigne Touba: PER
Dakar: LOC
```

## Sentiment Analysis

```python
from wolof_nlp.applications import analyze_sentiment

result = analyze_sentiment("Dafa neex lool")
print(result.sentiment)
print(result.positive_words)
```

Output:
```
Sentiment.POSITIVE
['neex']
```

## Interlinear Glossing

```python
from wolof_nlp.applications import gloss

result = gloss("Xale bi dem na")
print(result.to_string())
```

## Verb Conjugation

```python
from wolof_nlp.morphology import conjugate

forms = conjugate("dem", tam="perfect")
for form in forms:
    print(f"{form.form}: {form.gloss}")
```

Output:
```
dem naa: I dem-ed
dem nga: you dem-ed
dem na: he/she dem-ed
```
