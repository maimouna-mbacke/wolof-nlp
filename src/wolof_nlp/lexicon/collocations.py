"""Wolof Collocations - Common expressions and word combinations"""

from typing import List, Tuple


VERB_OBJECT_COLLOCATIONS = [
    ('lekk', 'ceeb', 'eat rice'),
    ('naan', 'ndox', 'drink water'),
    ('naan', 'kafé', 'drink coffee'),
    ('jàng', 'wolof', 'study Wolof'),
    ('jàng', 'téere', 'read a book'),
    ('bind', 'bataaxal', 'write a letter'),
    ('def', 'liggéey', 'do work'),
    ('wax', 'dëgg', 'speak truth'),
    ('am', 'xarit', 'have a friend'),
    ('am', 'doom', 'have a child'),
    ('dem', 'ekool', 'go to school'),
    ('dem', 'liggéey', 'go to work'),
    ('gis', 'xale', 'see a child'),
    ('bëgg', 'nit', 'love someone'),
]

NOUN_ADJECTIVE_COLLOCATIONS = [
    ('ceeb', 'bu neex', 'delicious rice'),
    ('ndox', 'bu sedd', 'cold water'),
    ('kër', 'bu mag', 'big house'),
    ('xale', 'bu ndaw', 'small child'),
    ('jigéen', 'bu rafet', 'beautiful woman'),
    ('nit', 'bu baax', 'good person'),
    ('bés', 'bu baax', 'good day'),
    ('liggéey', 'bu metti', 'hard work'),
]

GREETING_EXPRESSIONS = [
    ('na nga def', 'comment ça va', 'how are you'),
    ('jàmm rekk', 'la paix seulement', 'peace only'),
    ('jàmm nga am', 'que tu aies la paix', 'may you have peace'),
    ('fan nga nekk', 'où es-tu', 'where are you'),
    ('ana waa kër gi', 'comment va la famille', 'how is the family'),
    ('ñu ngi fi', 'nous sommes là', 'we are here'),
    ('mangi fi rekk', 'je suis là seulement', 'I am fine'),
    ('alhamdulillah', 'grâce à Dieu', 'praise God'),
    ('ba beneen', 'à la prochaine', 'until next time'),
]

RELIGIOUS_EXPRESSIONS = [
    ('yàlla na yàlla', 'que Dieu fasse', 'may God grant'),
    ('yàlla nako yàlla', 'que Dieu lui accorde', 'may God grant him/her'),
    ('barke yàlla', 'grâce à Dieu', 'by God\'s grace'),
    ('inshàlla', 'si Dieu le veut', 'God willing'),
    ('mashallah', 'ce que Dieu veut', 'as God wills'),
    ('jërëjëf yàlla', 'merci Dieu', 'thank God'),
    ('yàlla nanu', 'que Dieu nous', 'may God for us'),
    ('na yàlla def', 'que Dieu fasse', 'may God do'),
]

SOCIAL_EXPRESSIONS = [
    ('dafa neex', "c'est bon", 'it is good'),
    ('dafa baax', "c'est bien", 'it is well'),
    ('am na solo', "c'est important", 'it is important'),
    ('amul dara', 'pas de problème', 'no problem'),
    ('baax na', "c'est bon", 'it is good'),
    ('neex na', "c'est agréable", 'it is pleasant'),
    ('dëgg la', "c'est vrai", 'it is true'),
    ('ndank ndank', 'doucement', 'slowly slowly'),
]

DISCOURSE_COLLOCATIONS = [
    ('dafa', 'am', 'there is'),
    ('amul', 'dara', 'no problem'),
    ('baax', 'na', 'it is good'),
    ('neex', 'na', 'it is pleasant'),
    ('dëgg', 'la', 'it is true'),
    ('metti', 'na', 'it is hard'),
    ('yomb', 'na', 'it is easy'),
]


class Collocations:
    
    def get_verb_objects(self, verb: str) -> List[Tuple[str, str]]:
        return [(obj, gloss) for v, obj, gloss in VERB_OBJECT_COLLOCATIONS if v == verb.lower()]
    
    def get_noun_modifiers(self, noun: str) -> List[Tuple[str, str]]:
        return [(mod, gloss) for n, mod, gloss in NOUN_ADJECTIVE_COLLOCATIONS if n == noun.lower()]
    
    def get_greetings(self) -> List[Tuple[str, str, str]]:
        return GREETING_EXPRESSIONS
    
    def get_religious(self) -> List[Tuple[str, str, str]]:
        return RELIGIOUS_EXPRESSIONS
    
    def get_social(self) -> List[Tuple[str, str, str]]:
        return SOCIAL_EXPRESSIONS
    
    def is_collocation(self, word1: str, word2: str) -> bool:
        w1, w2 = word1.lower(), word2.lower()
        for v, obj, _ in VERB_OBJECT_COLLOCATIONS:
            if v == w1 and obj == w2:
                return True
        for d1, d2, _ in DISCOURSE_COLLOCATIONS:
            if d1 == w1 and d2 == w2:
                return True
        return False
    
    def find_expression(self, text: str) -> List[Tuple[str, str, str]]:
        text_lower = text.lower()
        results = []
        
        for wolof, french, english in GREETING_EXPRESSIONS + RELIGIOUS_EXPRESSIONS + SOCIAL_EXPRESSIONS:
            if wolof in text_lower:
                results.append((wolof, french, english))
        
        return results


def get_collocations() -> Collocations:
    return Collocations()
