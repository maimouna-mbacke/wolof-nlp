"""Wolof Dictionary - Core vocabulary with verified translations"""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class DictionaryEntry:
    wolof: str
    french: str
    english: str
    pos: str
    noun_class: Optional[str] = None
    example: Optional[str] = None


DICTIONARY = {
    'def': DictionaryEntry('def', 'faire', 'do/make', 'verb'),
    'dem': DictionaryEntry('dem', 'aller', 'go', 'verb'),
    'ñëw': DictionaryEntry('ñëw', 'venir', 'come', 'verb'),
    'wax': DictionaryEntry('wax', 'parler/dire', 'speak/say', 'verb'),
    'gis': DictionaryEntry('gis', 'voir', 'see', 'verb'),
    'xam': DictionaryEntry('xam', 'savoir', 'know', 'verb'),
    'bëgg': DictionaryEntry('bëgg', 'aimer/vouloir', 'love/want', 'verb'),
    'lekk': DictionaryEntry('lekk', 'manger', 'eat', 'verb'),
    'naan': DictionaryEntry('naan', 'boire', 'drink', 'verb'),
    'toog': DictionaryEntry('toog', "s'asseoir", 'sit', 'verb'),
    'jàng': DictionaryEntry('jàng', 'étudier/lire', 'study/read', 'verb'),
    'bind': DictionaryEntry('bind', 'écrire', 'write', 'verb'),
    'soppi': DictionaryEntry('soppi', 'changer', 'change', 'verb'),
    'jeggal': DictionaryEntry('jeggal', 'pardonner', 'forgive', 'verb'),
    'nekk': DictionaryEntry('nekk', 'être/exister', 'be/exist', 'verb'),
    'am': DictionaryEntry('am', 'avoir', 'have', 'verb'),
    'mën': DictionaryEntry('mën', 'pouvoir', 'can/be able', 'verb'),
    'war': DictionaryEntry('war', 'devoir', 'must/should', 'verb'),
    'may': DictionaryEntry('may', 'donner', 'give', 'verb'),
    'jël': DictionaryEntry('jël', 'prendre', 'take', 'verb'),
    'jënd': DictionaryEntry('jënd', 'acheter', 'buy', 'verb'),
    'jaay': DictionaryEntry('jaay', 'vendre', 'sell', 'verb'),
    'daw': DictionaryEntry('daw', 'courir', 'run', 'verb'),
    'dox': DictionaryEntry('dox', 'marcher', 'walk', 'verb'),
    'taxaw': DictionaryEntry('taxaw', 'se lever/debout', 'stand', 'verb'),
    'tëdd': DictionaryEntry('tëdd', 'se coucher', 'lie down', 'verb'),
    'neex': DictionaryEntry('neex', 'être bon/agréable', 'be good/pleasant', 'verb'),
    'baax': DictionaryEntry('baax', 'être bon', 'be good', 'verb'),
    'rafet': DictionaryEntry('rafet', 'être beau', 'be beautiful', 'verb'),
    'metti': DictionaryEntry('metti', 'être difficile/douloureux', 'be difficult/painful', 'verb'),
    'sant': DictionaryEntry('sant', 'remercier', 'thank', 'verb'),
    'nangu': DictionaryEntry('nangu', 'accepter', 'accept', 'verb'),
    'bañ': DictionaryEntry('bañ', 'refuser', 'refuse', 'verb'),
    'door': DictionaryEntry('door', 'commencer/frapper', 'start/hit', 'verb'),
    'jooy': DictionaryEntry('jooy', 'pleurer', 'cry', 'verb'),
    'ree': DictionaryEntry('ree', 'rire', 'laugh', 'verb'),
    'feebar': DictionaryEntry('feebar', 'être malade', 'be sick', 'verb'),
    
    'ndox': DictionaryEntry('ndox', 'eau', 'water', 'noun', 'M'),
    'ceeb': DictionaryEntry('ceeb', 'riz', 'rice', 'noun', 'B'),
    'mburu': DictionaryEntry('mburu', 'pain', 'bread', 'noun', 'M'),
    'kër': DictionaryEntry('kër', 'maison', 'house', 'noun', 'G'),
    'xale': DictionaryEntry('xale', 'enfant', 'child', 'noun', 'B'),
    'nit': DictionaryEntry('nit', 'personne', 'person', 'noun', 'K'),
    'jigéen': DictionaryEntry('jigéen', 'femme', 'woman', 'noun', 'J'),
    'góor': DictionaryEntry('góor', 'homme', 'man', 'noun', 'G'),
    'yaay': DictionaryEntry('yaay', 'mère', 'mother', 'noun', 'J'),
    'baay': DictionaryEntry('baay', 'père', 'father', 'noun', 'B'),
    'doom': DictionaryEntry('doom', 'enfant (de)', 'child (of)', 'noun', 'J'),
    'xarit': DictionaryEntry('xarit', 'ami', 'friend', 'noun', 'B'),
    'maam': DictionaryEntry('maam', 'grand-parent', 'grandparent', 'noun', 'B'),
    'mag': DictionaryEntry('mag', 'aîné/grand', 'elder/big', 'noun', 'B'),
    'rakk': DictionaryEntry('rakk', 'cadet', 'younger sibling', 'noun', 'B'),
    'jabar': DictionaryEntry('jabar', 'épouse', 'wife', 'noun', 'J'),
    'jëkkër': DictionaryEntry('jëkkër', 'époux', 'husband', 'noun', 'B'),
    
    'bopp': DictionaryEntry('bopp', 'tête', 'head', 'noun', 'B'),
    'bët': DictionaryEntry('bët', 'œil', 'eye', 'noun', 'B'),
    'nopp': DictionaryEntry('nopp', 'oreille', 'ear', 'noun', 'B'),
    'bakkan': DictionaryEntry('bakkan', 'nez', 'nose', 'noun', 'B'),
    'gémmiñ': DictionaryEntry('gémmiñ', 'bouche', 'mouth', 'noun', 'G'),
    'loxo': DictionaryEntry('loxo', 'main/bras', 'hand/arm', 'noun', 'B'),
    'tànk': DictionaryEntry('tànk', 'pied/jambe', 'foot/leg', 'noun', 'B'),
    'xol': DictionaryEntry('xol', 'cœur', 'heart', 'noun', 'B'),
    'biir': DictionaryEntry('biir', 'ventre', 'stomach', 'noun', 'B'),
    
    'bés': DictionaryEntry('bés', 'jour', 'day', 'noun', 'B'),
    'guddi': DictionaryEntry('guddi', 'nuit', 'night', 'noun', 'G'),
    'suba': DictionaryEntry('suba', 'matin/demain', 'morning/tomorrow', 'noun', 'S'),
    'ngoon': DictionaryEntry('ngoon', 'après-midi', 'afternoon', 'noun', 'B'),
    'démb': DictionaryEntry('démb', 'hier', 'yesterday', 'adv'),
    'tey': DictionaryEntry('tey', "aujourd'hui", 'today', 'adv'),
    'ëllëg': DictionaryEntry('ëllëg', 'demain', 'tomorrow', 'adv'),
    'at': DictionaryEntry('at', 'année', 'year', 'noun', 'B'),
    'weer': DictionaryEntry('weer', 'mois/lune', 'month/moon', 'noun', 'W'),
    
    'dëkk': DictionaryEntry('dëkk', 'ville/village', 'city/village', 'noun', 'B'),
    'réew': DictionaryEntry('réew', 'pays', 'country', 'noun', 'B'),
    'yoon': DictionaryEntry('yoon', 'chemin/route', 'road/path', 'noun', 'W'),
    'garab': DictionaryEntry('garab', 'arbre/médicament', 'tree/medicine', 'noun', 'G'),
    'géej': DictionaryEntry('géej', 'mer/océan', 'sea/ocean', 'noun', 'G'),
    'suuf': DictionaryEntry('suuf', 'sol/terre', 'ground/earth', 'noun', 'S'),
    'asamaan': DictionaryEntry('asamaan', 'ciel', 'sky', 'noun', 'B'),
    'jant': DictionaryEntry('jant', 'soleil', 'sun', 'noun', 'J'),
    
    'yàlla': DictionaryEntry('yàlla', 'Dieu', 'God', 'noun'),
    'jàmm': DictionaryEntry('jàmm', 'paix', 'peace', 'noun', 'J'),
    'barke': DictionaryEntry('barke', 'bénédiction', 'blessing', 'noun', 'B'),
    'diné': DictionaryEntry('diné', 'religion', 'religion', 'noun', 'B'),
    
    'liggéey': DictionaryEntry('liggéey', 'travail', 'work', 'noun', 'L'),
    'xaalis': DictionaryEntry('xaalis', 'argent', 'money', 'noun', 'B'),
    'téere': DictionaryEntry('téere', 'livre', 'book', 'noun', 'B'),
    'ekool': DictionaryEntry('ekool', 'école', 'school', 'noun', 'B'),
    
    'tuuti': DictionaryEntry('tuuti', 'un peu', 'a little', 'adv'),
    'lool': DictionaryEntry('lool', 'beaucoup/très', 'a lot/very', 'adv'),
    'leegi': DictionaryEntry('leegi', 'maintenant', 'now', 'adv'),
    'ndank': DictionaryEntry('ndank', 'doucement', 'slowly', 'adv'),
    'gaaw': DictionaryEntry('gaaw', 'vite', 'fast', 'adv'),
    'rekk': DictionaryEntry('rekk', 'seulement', 'only', 'adv'),
    'itam': DictionaryEntry('itam', 'aussi', 'also', 'adv'),
    
    'ci': DictionaryEntry('ci', 'à/dans', 'at/in', 'prep'),
    'ak': DictionaryEntry('ak', 'avec/et', 'with/and', 'conj'),
    'ngir': DictionaryEntry('ngir', 'pour', 'for', 'prep'),
    'ba': DictionaryEntry('ba', "jusqu'à", 'until', 'prep'),
    'te': DictionaryEntry('te', 'et (clauses)', 'and (clauses)', 'conj'),
    'wala': DictionaryEntry('wala', 'ou', 'or', 'conj'),
    
    'lan': DictionaryEntry('lan', 'quoi', 'what', 'inter'),
    'kan': DictionaryEntry('kan', 'qui', 'who', 'inter'),
    'fan': DictionaryEntry('fan', 'où', 'where', 'inter'),
    'kañ': DictionaryEntry('kañ', 'quand', 'when', 'inter'),
    'naka': DictionaryEntry('naka', 'comment', 'how', 'inter'),
    'ndax': DictionaryEntry('ndax', 'pourquoi/est-ce que', 'why/whether', 'inter'),
    'ñaata': DictionaryEntry('ñaata', 'combien', 'how many', 'inter'),
}


class Dictionary:
    
    def __init__(self):
        self.entries = DICTIONARY
    
    def lookup(self, word: str) -> Optional[DictionaryEntry]:
        return self.entries.get(word.lower())
    
    def translate(self, word: str, target: str = 'english') -> Optional[str]:
        entry = self.lookup(word)
        if not entry:
            return None
        return entry.english if target == 'english' else entry.french
    
    def search(self, query: str, field: str = 'all') -> List[DictionaryEntry]:
        results = []
        query = query.lower()
        for entry in self.entries.values():
            if field == 'all':
                if query in entry.wolof or query in entry.french.lower() or query in entry.english.lower():
                    results.append(entry)
            elif field == 'wolof' and query in entry.wolof:
                results.append(entry)
            elif field == 'french' and query in entry.french.lower():
                results.append(entry)
            elif field == 'english' and query in entry.english.lower():
                results.append(entry)
        return results
    
    def get_by_pos(self, pos: str) -> List[DictionaryEntry]:
        return [e for e in self.entries.values() if e.pos == pos]
    
    def get_by_noun_class(self, noun_class: str) -> List[DictionaryEntry]:
        return [e for e in self.entries.values() if e.noun_class == noun_class]


def lookup(word: str) -> Optional[DictionaryEntry]:
    return Dictionary().lookup(word)


def translate(word: str, target: str = 'english') -> Optional[str]:
    return Dictionary().translate(word, target)
