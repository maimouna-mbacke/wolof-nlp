"""Wolof Proverbs - Léebu Wolof"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Proverb:
    wolof: str
    french: str
    english: str
    theme: str

PROVERBS = [
    Proverb("Ku am sa bopp du am bopp", "Qui a sa tête n'a pas de tête", "He who has his own head doesn't have a head (stubbornness)", "wisdom"),
    Proverb("Ndank-ndank mooy jàpp golo ci ñaay", "Doucement on attrape le singe dans la brousse", "Slowly slowly catches the monkey", "patience"),
    Proverb("Lu dul sa tanka bopp, bul ko tegee sa bopp", "Ce qui ne concerne pas ta jambe, ne le mets pas sur ta tête", "Don't carry what's not your burden", "wisdom"),
    Proverb("Nit nit ay garabam", "L'homme est le remède de l'homme", "Man is man's remedy", "solidarity"),
    Proverb("Góor lu mu gëna rafet mooy jom", "La plus belle chose d'un homme c'est la dignité", "A man's greatest beauty is dignity", "honor"),
    Proverb("Ku begg ñàkk liggéey du ñàkk wàjj", "Qui veut travailler ne manque pas de prétexte", "Where there's a will there's a way", "work"),
    Proverb("Loxo benn du taar", "Une seule main ne peut applaudir", "One hand cannot clap", "cooperation"),
    Proverb("Bul teg sa tool ci àll", "Ne mets pas ton champ dans la forêt", "Don't put your farm in the forest", "planning"),
    Proverb("Ku am fit, amul njàmbaar", "Qui a peur n'a pas de courage", "Who has fear has no courage", "courage"),
    Proverb("Jëf ja gën wax", "L'action vaut mieux que la parole", "Actions speak louder than words", "action"),
    Proverb("Dëgg dëgg la, waaye ñakk la", "La vérité est vraie, mais elle est pauvre", "Truth is true but it's poor", "truth"),
    Proverb("Ku jël na jox", "Qui prend doit donner", "Who takes must give", "reciprocity"),
    Proverb("Sa bët mooy sa màgg", "Ton oeil est ton aîné", "Your eye is your elder (see for yourself)", "experience"),
    Proverb("Lu la neex bañ ko, lu la metti sopp ko", "Ce qui te plaît, refuse-le; ce qui te fait mal, aime-le", "Refuse pleasure, embrace hardship", "discipline"),
    Proverb("Am na lu gën wax", "Il y a plus important que parler", "There's more than just talking", "action"),
]

class ProverbCollection:
    def __init__(self):
        self.proverbs = PROVERBS
    
    def get_all(self) -> List[Proverb]:
        return self.proverbs
    
    def get_by_theme(self, theme: str) -> List[Proverb]:
        return [p for p in self.proverbs if p.theme == theme.lower()]
    
    def search(self, query: str) -> List[Proverb]:
        q = query.lower()
        return [p for p in self.proverbs if q in p.wolof.lower() or q in p.english.lower()]
    
    def random(self) -> Proverb:
        import random
        return random.choice(self.proverbs)
    
    def themes(self) -> List[str]:
        return list(set(p.theme for p in self.proverbs))

def get_proverbs() -> List[Proverb]:
    return ProverbCollection().get_all()

def search_proverbs(query: str) -> List[Proverb]:
    return ProverbCollection().search(query)