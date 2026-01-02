# Corpus Validation

## Dataset

The toolkit was validated against a corpus of YouTube comments collected from Senegalese series.

| Metric | Value |
|--------|-------|
| Total comments | 40,102 |
| Total videos | 679 |
| Database | `wolof_corpus.db` |

## Language Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| Mixed (Wolof-French) | 27,814 | 69.4% |
| Pure Wolof | 6,203 | 15.5% |
| Pure French | 6,085 | 15.2% |

The high proportion of mixed-language content (69.4%) motivated the French detection features in the POS tagger and glosser.

## TAM Marker Frequency

| Marker Type | Occurrences |
|-------------|-------------|
| Perfect (na/naa/nga) | 5,114 |
| Negative (du/dul/ul) | 4,234 |
| Object focus (la) | 3,312 |
| Imperative | 3,179 |
| Optative (na...na) | 2,743 |
| Verb focus (dafa/dama) | 499 |
| Future (dina/dinaa) | 367 |
| Subject focus (moo/maa) | 123 |
| Presentative (mungi/ngi) | 97 |

## Noun Class Distribution

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

The B and S classes dominate, consistent with B being the default class in modern wolof and for loanwords.

## Named Entities

### Places (LOC)

| Entity | Count |
|--------|-------|
| Touba | 1,281 |
| Sénégal | 960 |
| Dakar | 204 |
| Guinée | 80 |
| France | 64 |
| Mali | 27 |

### Surnames (PER)

| Surname | Count |
|---------|-------|
| Ba | 440 |
| Seck | 420 |
| Mbaye | 398 |
| Fall | 374 |
| Ndiaye | 245 |
| Faye | 194 |
| Sall | 193 |
| Diop | 137 |

### Religious Titles (PER)

| Title | Count |
|-------|-------|
| Serigne | 1,365 |
| Cheikh | 531 |
| Oustaz | 452 |
| Mame | 382 |

### Multi-word Entities

| Entity | Count |
|--------|-------|
| Serigne Touba | 880 |
| Cheikh Ahmadou Bamba | 57 |

## Sentiment Markers

### Positive

| Marker | Count | Type |
|--------|-------|------|
| amine | 1,841 | Arabic |
| mashallah | 1,024 | Arabic |
| neex/nekh | 238 | Wolof |
| jërëjëf | 55 | Wolof |
| magnifique | 207 | French |
| bravo | 220 | French |

### Negative

| Marker | Count |
|--------|-------|
| V-ul (negated verbs) | 2,011 |
| triste | 67 |
| metti | 20 |

### Emoji

| Emoji | Count |
|-------|-------|
| ❤️ | 61,888 |
| 😂 | 9,747 |
| 😭😢 | 3,943 |
| 🙏 | 2,554 |

## Normalization Patterns

High-frequency spelling variants identified:

| Variant | Standard | Count |
|---------|----------|-------|
| machallah | mashallah | 1,031 |
| niou | ñu | 969 |
| beug | bëgg | 726 |
| wakh | wax | 688 |
| nek | nekk | 684 |
| dieuredieuf | jërëjëf | 243 |

These patterns informed the normalizer's mapping table.

## Religious Content

9.4% of comments (3,788) contained religious expressions, reflecting the cultural context of Senegalese social media.

## Implications for Design

1. **Code-switching handling**: French detection is essential, not optional
2. **Arabic expressions**: Must be included in sentiment lexicons
3. **Multi-word NER**: Title + name patterns are frequent
4. **Negation frequency**: The -ul suffix appears 2,011 times, validating its importance
5. **Emoji**: High emoji usage requires emoji sentiment mapping
