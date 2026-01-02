# TAM System

Wolof uses sentence-initial markers to encode tense, aspect, mood, and focus. These markers combine with person/number agreement.

## Paradigms Implemented

### Subject Focus

Emphasizes the subject. Marker precedes verb.

| Person | Marker | Example | Gloss |
|--------|--------|---------|-------|
| 1SG | maa | Maa ko def | I did it |
| 2SG | yaa | Yaa ko def | You did it |
| 3SG | moo | Moo ko def | He/she did it |
| 1PL | noo | Noo ko def | We did it |
| 2PL | yeena | Yeena ko def | You (pl) did it |
| 3PL | ñoo | Ñoo ko def | They did it |

### Verb Focus

Emphasizes the action or verb phrase.

| Person | Marker | Example | Gloss |
|--------|-------|---------|-------|
| 1SG | dama | Dama dem | I went (emphasis) |
| 2SG | danga | Danga dem | You went |
| 3SG | dafa | Dafa dem | He/she went |
| 1PL | dañu | Dañu dem | We went |
| 2PL | dangeen | Dangeen dem | You (pl) went |
| 3PL | dañu | Dañu dem | They went |

### Presentative

Indicates ongoing action, often with locative sense.

| Person | Marker | Example    | Gloss |
|--------|-------|------------|-------|
| 1SG | maangi/mangi | Mangi jàng | I am reading |
| 2SG | yaangi/yangi | Yangi jàng | You are reading |
| 3SG | mungi | mungi jàng | He/she is reading |
| 1PL | ñungi | ñungi jàng | We are reading |
| 2PL | yeengi | yeengi jàng | You (pl) are reading |
| 3PL | ñungi | ñungi jàng  | They are reading |

### Perfect

Completed action. Marker follows verb.

| Person | Marker | Example | Gloss |
|--------|-------|---------|-------|
| 1SG | naa | Dem naa | I went |
| 2SG | nga | Dem nga | You went |
| 3SG | na | Dem na | He/she went |
| 1PL | nañu | Dem nañu | We went |
| 2PL | ngeen | Dem ngeen | You (pl) went |
| 3PL | nañu | Dem nañu | They went |

### Future

| Person | Marker | Example | Gloss |
|--------|-------|---------|-------|
| 1SG | dinaa | Dinaa dem | I will go |
| 2SG | dinga | Dinga dem | You will go |
| 3SG | dina | Dina dem | He/she will go |
| 1PL | dinañu | Dinañu dem | We will go |
| 2PL | dingeen | Dingeen dem | You (pl) will go |
| 3PL | dinañu | Dinañu dem | They will go |

### Negative Future

| Person | Marker | Example | Gloss |
|--------|-------|---------|-------|
| 1SG | duma | Duma dem | I won't go |
| 2SG | doo | Doo dem | You won't go |
| 3SG | du | Du dem | He/she won't go |
| 1PL | duñu | Duñu dem | We won't go |
| 2PL | dungeen | Dungeen dem | You (pl) won't go |
| 3PL | duñu | Duñu dem | They won't go |

### Optative

Expresses wishes, blessings, or desirable outcomes.  
Formally uses the same preverbal markers as perfect, but with **optative semantics**.

| Example | Gloss                                 |
|---------|---------------------------------------|
| **Na dem** | May he/she go                         |
| **Nañu dem** | May we go / Let’s go (hortative use)                            |
| **Nañu dem** | May they go |

## Imperative

In Wolof, true imperatives only exist for **2nd person singular** and **2nd person plural**.  
Morphologically, an imperative requires a suffix: **-al** (2SG) or **-leen** (2PL).

###  Positive Imperative

| Person | Form | Example | Meaning |
|--------|------|---------|--------|
| 2SG | **Verb + -al** | **demal** | Go! (you) |
| 2PL | **Verb + -leen** | **demleen** | You all go! |

### Prohibitive

Negative imperative.

| Person | Marker | Example | Gloss |
|--------|--------|---------|-------|
| 2SG | bul | Bul dem | Don't go |
| 2PL | buleen | Buleen dem | Don't (pl) go |

## Corpus Distribution

From 40K YouTube comments:

| Paradigm | Count |
|----------|-------|
| Perfect | 5,114 |
| Negative | 4,234 |
| Object focus (la) | 3,312 |
| Imperative | 3,179 |
| Optative | 2,743 |
| Verb focus | 499 |
| Future | 367 |
| Subject focus | 123 |
| Presentative | 97 |

## Implementation Notes

TAM markers are checked before context rules in POS tagging to prevent misclassification. The `TAM_MARKERS` set in `constants.py` includes all paradigm markers.
