"""Wolof Linguistic Constants - Based on CLAD orthography and academic sources"""

VOWELS = frozenset('aeëiouàáéóú')
CONSONANTS = frozenset('bcdfghjklmnñŋpqrstvwxy')
PRENASALIZED = frozenset(['mb', 'nd', 'nj', 'ng', 'nc', 'nk', 'nq', 'mp', 'nt'])
GEMINATES = frozenset(['bb', 'cc', 'dd', 'ff', 'gg', 'jj', 'kk', 'll', 'mm', 'nn', 'pp', 'rr', 'ss', 'tt', 'ww', 'yy'])
LONG_VOWELS = frozenset(['aa', 'ee', 'ëë', 'ii', 'oo', 'uu', 'éé', 'àà', 'óó'])

ORTHOGRAPHY_MAP = {
    'kh': 'x', 'eu': 'ë', 'euh': 'ë', 'gn': 'ñ', 'ny': 'ñ',
    'dj': 'j', 'tch': 'c', 'ch': 'c', 'oe': 'ë',
    'ou': 'u', 'oo': 'oo', 'th': 'c', 'ié': 'ee',
}

WORD_NORMALIZATIONS = {
    'beug': 'bëgg', 'begg': 'bëgg', 'bëg': 'bëgg', 'begue': 'bëgg',
    'nekh': 'neex', 'neekh': 'neex', 'nex': 'neex',
    'nek': 'nekk',
    'kham': 'xam', 'khamm': 'xamm', 'khol': 'xol', 'khalis': 'xalis', 'khey': 'xëy',
    'gnou': 'ñu', 'gnaw': 'ñaw', 'ñou': 'ñu', 'niou': 'ñu',
    'diokh': 'jox', 'diang': 'jàng', 'djang': 'jàng', 'diox': 'jox',
    'dioy': 'jooy', 'teud': 'tëdd', 'jeund': 'jënd',
    'deug': 'dëgg', 'deg': 'dëgg', 'dëg': 'dëgg',
    'wakh': 'wax', 'guiss': 'gis',
    'gnaan': 'ñaan', 'gnakh': 'ñàkk',
    'jang': 'jàng', 'djang': 'jàng',
    'keur': 'kër', 'guer': 'gër',
    'thiep': 'ceeb', 'thiép': 'ceeb', 'thiéb': 'ceeb', 'thieb': 'ceeb', 'ceebu': 'ceeb',
    'wathié': 'wacce', 'wathie': 'wacce', 'watié': 'wacce',
    'touti': 'tuuti', 'toute': 'tuuti', 'toutit': 'tuuti',
    'djéggalou': 'jeggalu', 'djégalou': 'jeggalu', 'djeggalu': 'jeggalu',
    'djéggal': 'jeggal', 'djégal': 'jeggal',
    'diégal': 'jéggal', 'diegue': 'jëg',
    'ndeysane': 'ndeysan', 'ndéysan': 'ndeysan',
    'yallah': 'yàlla', 'yalla': 'yàlla',
    'inchallah': 'inshàlla', 'inshallah': 'inshàlla',
    'barké': 'barke', 'baraka': 'barke',
    'machallah': 'mashallah', 'maachallah': 'mashallah',
    'dieuradieuf': 'jërëjëf', 'dieuredieuf': 'jërëjëf', 'dieureudieuf': 'jërëjëf', 
    'jerejef': 'jërëjëf', 'dieredief': 'jërëjëf', 'dieuredjef': 'jërëjëf',
    'alxamdulilah': 'alhamdulillah',
    'serigne': 'seriñ', 'sérigne': 'seriñ', 'serigné': 'seriñ',
    'sokhna': 'soxna', 'sokna': 'soxna',
}

SUBJECT_FOCUS = frozenset(['maa', 'yaa', 'moo', 'noo', 'yeena', 'ñoo'])
VERB_FOCUS = frozenset(['dama', 'danga', 'dafa', 'danu', 'dangeen', 'dañu'])
PRESENTATIVE = frozenset(['maangi', 'yaangi', 'mungi', 'nungi', 'yeengi', 'ñungi', 'mangi', 'yangi', 'angi', 'ngi'])
PERFECT = frozenset(['naa', 'nga', 'na', 'nanu', 'ngeen', 'nañu'])
FUTURE = frozenset(['dinaa', 'dinga', 'dina', 'dinanu', 'dingeen', 'dinañu'])
NEGATIVE_FUTURE = frozenset(['duma', 'doo', 'du', 'dunu', 'dungeen', 'duñu'])
OPTATIVE = frozenset(['naa', 'nga', 'na', 'nanu', 'ngeen', 'nañu'])
PROHIBITIVE = frozenset(['buma', 'boo', 'bu', 'bunu', 'bungeen', 'buñu', 'bul'])
IMPERFECTIVE = frozenset(['di', 'diy', 'y'])
SEMI_AUXILIARIES = frozenset(['bañ', 'mën', 'war', 'soxla'])

TAM_MARKERS = SUBJECT_FOCUS | VERB_FOCUS | PRESENTATIVE | PERFECT | FUTURE | NEGATIVE_FUTURE | OPTATIVE | PROHIBITIVE | frozenset(['woon', 'doon', 'ngiy'])
FOCUS_MARKERS = frozenset(['la', 'moo', 'maa', 'yaa', 'noo', 'ñoo', 'dafa', 'dama'])

PAST_SUFFIXES = ['woon', 'oon']
NEGATION_SUFFIXES = ['wul', 'ul', 'uma', 'uloo', 'unu', 'uleen', 'uñu']
IMPERATIVE_SUFFIXES = ['al', 'leen', 'aal', 'eel', 'il', 'ul', 'wal']
CAUSATIVE_SUFFIXES = ['al', 'le', 'lu', 'ali', 'andi', 'anti']
CAUSATIVE_LO_SUFFIXES = ['lo', 'loo']
DIRECTIONAL_SUFFIXES = ['i', 'ji']
NUMERAL_CONNECTIVES = frozenset(['fukki', 'juróomi', 'ñenti', 'ñaari', 'ñetti', 'ñeenti'])
SERIAL_VERBS = frozenset(['bëgga', 'soxlaa', 'namma', 'bugga', 'wara', 'mana', 'mëna'])
BENEFACTIVE_SUFFIXES = ['al', 'l', 'el']
REFLEXIVE_SUFFIXES = ['éku', 'iku', 'ku', 'u']
RECIPROCAL_SUFFIXES = ['ante', 'andoo', 'oo', 'aante']
REPETITIVE_SUFFIXES = ['aat', 'waat', 'aate', 'waate']
NOMINALIZATION_SUFFIXES = ['kat', 'aay', 'waay', 'ay', 'in']
INTENSIVE_SUFFIXES = ['at', 'it', 'ut']
REVERSIVE_SUFFIXES = ['adi', 'andi', 'anti', 'i']

SUBJECT_CLITICS = frozenset(['ma', 'nga', 'mu', 'nu', 'ngeen', 'ñu', 'nanu', 'nañu'])
OBJECT_CLITICS = frozenset(['ma', 'la', 'ko', 'nu', 'leen', 'ñu'])

CLITIC_COMBINATIONS = {
    'nako': ['na', 'ko'], 'nala': ['na', 'la'], 'nama': ['na', 'ma'],
    'nanu': ['na', 'nu'], 'naleen': ['na', 'leen'], 'lako': ['la', 'ko'],
    'lama': ['la', 'ma'], 'mako': ['ma', 'ko'], 'kola': ['ko', 'la'],
    'dinako': ['dina', 'ko'], 'dinala': ['dina', 'la'],
}

CONTRACTIONS = {
    'mangui': ['ma', 'ngi'], 'mangi': ['ma', 'ngi'],
    'yangui': ['yaa', 'ngi'], 'yangi': ['yaa', 'ngi'],
    'mungi': ['mu', 'ngi'],
    'mooy': ['moo', 'di'],
    'damay': ['da', 'ma', 'y'],
    'dangay': ['da', 'nga', 'y'],
    'dafay': ['da', 'fa', 'y'],
    'dañuy': ['da', 'ñu', 'y'],
    'lañuy': ['la', 'ñu', 'y'],
    'dinay': ['di', 'na', 'y'],
    'maangi': ['maa', 'ngi'],
    'yaangi': ['yaa', 'ngi'],
    'dinaa': ['di', 'na', 'a'],
    'dinga': ['di', 'nga'],
    'dinanu': ['di', 'na', 'nu'],
    'dingeen': ['di', 'ngeen'],
    'dinañu': ['di', 'na', 'ñu'],
    'naa': ['na', 'a'],
    'nanga': ['na', 'nga'],
    'nañu': ['na', 'ñu'],
    'ngay': ['nga', 'y'],
    'ngaay': ['nga', 'y'],
}

AK_CONTRACTIONS = {
    'kafék': ['kafé', 'ak'], 'manak': ['mane', 'ak'], 'moomak': ['moom', 'ak'],
    'àndag': ['ànd', 'ak'], 'andak': ['ànd', 'ak'],
}

AY_CONTRACTIONS = {
    'suniy': ['sunu', 'ay'], 'seeniy': ['seen', 'ay'], 'samay': ['sama', 'ay'], 'say': ['sa', 'ay'],
}

POSSESSIVE_CONTRACTIONS = {'sam': 'sama', 'sun': 'sunu'}

NOUN_CLASS_MARKERS = {
    'B': {
        'def': 'bi', 'indef': 'ab', 'pl': 'yi', 'rel': 'bu',
        'dem_prox': 'bii', 'dem_dist': 'boobu',
        'assignment': 'default',
        'tendency': 'Default class (~40% lexicon), loanwords from French/English/Arabic',
        'copy_initial': 'b',
        'examples': ['xale', 'téere', 'ceeb', 'buy'],
        'lexicon_pct': 40
    },
    'G': {
        'def': 'gi', 'indef': 'ag', 'pl': 'yi', 'rel': 'gu',
        'dem_prox': 'gii', 'dem_dist': 'googu',
        'assignment': 'mixed',
        'tendency': 'Trees (guy), g-initial nouns (copy), large objects, toponyms',
        'copy_initial': 'g',
        'copy_correlation': 0.535,
        'examples': ['garab', 'guy', 'gaal', 'Senegaal'],
        'lexicon_pct': 21
    },
    'J': {
        'def': 'ji', 'indef': 'aj', 'pl': 'yi', 'rel': 'ju',
        'dem_prox': 'jii', 'dem_dist': 'jooju',
        'assignment': 'mixed',
        'tendency': 'Arabic/religious loans, some kinship (yaay, doom), j-initial nouns',
        'copy_initial': 'j',
        'copy_correlation': 0.36,
        'examples': ['jigéen', 'jumaa', 'jinne', 'jabar', 'yaay', 'doom'],
        'lexicon_pct': 10
    },
    'K': {
        'def': 'ki', 'indef': 'ak', 'pl': 'ñi', 'rel': 'ku',
        'dem_prox': 'kii', 'dem_dist': 'kooku',
        'assignment': 'lexical',
        'tendency': 'QUASI SINGLE MEMBER: nit (person). Generic human pronoun class.',
        'copy_initial': None,
        'examples': ['nit'],
        'lexicon_pct': 0.1,
        'note': 'Only plural that uses ñi instead of yi'
    },
    'L': {
        'def': 'li', 'indef': 'al', 'pl': 'yi', 'rel': 'lu',
        'dem_prox': 'lii', 'dem_dist': 'loolu',
        'assignment': 'derived',
        'tendency': 'Deverbal nouns, abstract reference, generic inanimate pronouns (lu=what)',
        'copy_initial': 'l',
        'examples': ['liggéey', 'lëf'],
        'lexicon_pct': 5
    },
    'M': {
        'def': 'mi', 'indef': 'am', 'pl': 'yi', 'rel': 'mu',
        'dem_prox': 'mii', 'dem_dist': 'moomu',
        'assignment': 'semantic',
        'tendency': 'Liquids (ndox, meew), masses, m-initial nouns. MOST semantically coherent.',
        'copy_initial': 'm',
        'copy_correlation': 0.45,
        'examples': ['ndox', 'meew', 'mburu', 'màngó'],
        'lexicon_pct': 13
    },
    'S': {
        'def': 'si', 'indef': 'as', 'pl': 'yi', 'rel': 'su',
        'dem_prox': 'sii', 'dem_dist': 'soosu',
        'assignment': 'derived',
        'tendency': 'Diminutives (productive), time words (saa), s-initial nouns, manner',
        'copy_initial': 's',
        'copy_correlation': 0.175,
        'examples': ['suuf', 'saa', 'suba', 'seytaane'],
        'lexicon_pct': 3
    },
    'W': {
        'def': 'wi', 'indef': 'aw', 'pl': 'yi', 'rel': 'wu',
        'dem_prox': 'wii', 'dem_dist': 'woowu',
        'assignment': 'mixed',
        'tendency': 'Some animals, time periods, w-initial nouns, collectives',
        'copy_initial': 'w',
        'copy_correlation': 0.52,
        'examples': ['fas', 'weer', 'waxtu', 'wago'],
        'lexicon_pct': 12
    },
}

ADVERBIAL_CLASSES = {
    'F': {'rel': 'fu', 'prox': 'fi', 'dist': 'fa', 'function': 'Place (where)'},
    'N': {'rel': 'nu', 'prox': 'ni', 'dist': 'na', 'function': 'Manner (how)'},
}

PLURAL_RULES = {
    'K': 'Ñ',
    'B': 'Y', 'G': 'Y', 'J': 'Y', 'L': 'Y', 'M': 'Y', 'S': 'Y', 'W': 'Y'
}

ALL_DETERMINERS = frozenset(['bi', 'gi', 'ji', 'ki', 'li', 'mi', 'si', 'wi', 'yi', 'ñi', 'ab', 'ag', 'aj', 'ak', 'al', 'am', 'as', 'aw', 'ay'])
RELATIVE_PRONOUNS = frozenset(['bu', 'gu', 'ju', 'ku', 'lu', 'mu', 'su', 'wu', 'nu', 'fu'])
DEMONSTRATIVES = frozenset(['bii', 'gii', 'jii', 'kii', 'sii', 'boobu', 'googu', 'jooju', 'kooku', 'loolu', 'noonu'])

DISCOURSE_MARKERS = frozenset(['rek', 'rekk', 'nak', 'dé', 'deh', 'waay', 'way', 'waw', 'waaw', 'xanaa', 'xana', 'ndax', 'kone', 'kon', 'nag', 'naka', 'kay', 'de', 'ba', 'sax', 'dara', 'amul', 'wiri', 'solo', 'ana', 'war', 'koy', 'dangay', 'fii', 'fee', 'dégg', 'degg', 'wér', 'waw', 'waaye', 'leegi'])
CONJUNCTIONS = frozenset(['ak', 'te', 'wala', 'walla', 'mbaa', 'ndax', 'su', 'bu', 'bi', 'ba', 'ci', 'fi', 'fa', 'ni', 'na', 'ndeke', 'waaye', 'mais', 'motax', 'moytax', 'loolu', 'xanaa', 'donte', 'danke', 'ndaxte', 'ngir'])
PREPOSITIONS = frozenset(['ci', 'fi', 'fa', 'ca', 'ak', 'ngir', 'ba', 'bi', 'ginnaaw', 'kanam', 'digg', 'biir', 'biti', 'kow', 'suuf', 'wetu'])
INTERROGATIVES = frozenset(['kan', 'lan', 'fan', 'kañ', 'naka', 'nan', 'ndax', 'ñaata', 'ban', 'lu', 'ku', 'fu', 'nu', 'yan', 'ñan'])

TEMPORAL_SPATIAL = {
    'gannaaw': {'spatial': 'back/behind', 'temporal': 'past', 'metaphor': 'MOVING_EGO'},
    'kanam': {'spatial': 'face/front/ahead', 'temporal': 'future', 'metaphor': 'MOVING_EGO'},
    'paase': {'spatial': 'go beyond', 'temporal': 'pass (time)', 'metaphor': 'MOVING_EGO'},
    'tollu': {'spatial': 'reach a point', 'temporal': 'arrive at time', 'metaphor': 'MOVING_EGO'},
    'fekk': {'spatial': 'become co-located', 'temporal': 'find/be at time', 'metaphor': 'MOVING_TIME'},
    'jot': {'spatial': 'reach/catch', 'temporal': 'occur/arrive', 'metaphor': 'MOVING_TIME'},
    'ñów': {'spatial': 'come', 'temporal': 'approach (future)', 'metaphor': 'MOVING_TIME'},
    'jiitu': {'spatial': 'go ahead of', 'temporal': 'precede', 'metaphor': 'SEQUENCE'},
    'topp': {'spatial': 'follow', 'temporal': 'come after', 'metaphor': 'SEQUENCE'},
    'tegu': {'spatial': 'be put on', 'temporal': 'be next in sequence', 'metaphor': 'SEQUENCE'},
}

SENTENCE_PARTICLES = {
    'na': {'type': 'perfect', 'clause': 'neutral_affirmative'},
    'la': {'type': 'complement_focus', 'clause': 'wh_raising'},
    'a': {'type': 'subject_focus', 'clause': 'wh_raising'},
    'dafa': {'type': 'verb_focus', 'clause': 'v_raising'},
    'ngi': {'type': 'presentative', 'clause': 'v_raising'},
    'dina': {'type': 'future', 'clause': 'v_raising'},
    'du': {'type': 'negative_future', 'clause': 'v_raising'},
    'bu': {'type': 'conditional/prohibitive', 'clause': 'conditional'},
    'su': {'type': 'conditional', 'clause': 'conditional'},
}

COMMON_VERBS = frozenset([
    'def', 'dem', 'ñëw', 'wax', 'gis', 'xam', 'bëgg', 'lekk', 'toog', 'taxaw', 'dox',
    'jël', 'jënd', 'jàng', 'bind', 'jàpp', 'wut', 'seet', 'dégg', 'faj', 'sol', 'sang',
    'may', 'tari', 'soppi', 'fattali', 'báyyi', 'xammé', 'raxass', 'sonal',
    'jëli', 'jày', 'fay', 'réer', 'tollu', 'yàgg', 'gaaw', 'nekk', 'am', 'mën',
    'ànd', 'joté', 'mér', 'bég', 'réetaan', 'sant', 'jeggal', 'jégge', 'wacce', 'yégle',
    'gisante', 'soppiku', 'defaat', 'jëliwaat', 'jëndal', 'jàyal', 'jëllo',
    'fattaliku', 'fattaléku', 'báyyiku', 'jàyu', 'faju', 'solu', 'sangu', 'raxassu',
    'takk', 'door', 'tëj', 'ubbi',
    'lay', 'nako', 'nala', 'ko', 'lo', 'mo', 'ya', 'wa', 'melni', 'mane',
    'war', 'daw', 'nangu', 'yobbu', 'génne', 'duggu', 'génn', 'daanu', 'tànn',
    'jooy', 'ree', 'naan', 'roof', 'seeti', 'wàcce', 'yéeg', 'tukki',
])

COMMON_NOUNS = frozenset([
    'bopp', 'xol', 'loxo', 'bët', 'tànk', 'baat', 'nopp', 'bakkan', 'gémmiñ',
    'doom', 'yaay', 'baay', 'maam', 'mag', 'ndaw', 'jëkër', 'jabar', 'xarit', 'mbokk',
    'ndox', 'suuf', 'asamaan', 'jant', 'weer', 'garab', 'géej',
    'ceeb', 'mburu', 'méew', 'kafé', 'naan',
    'bés', 'guddi', 'suba', 'ngoon', 'at', 'ayubés',
    'kër', 'ekool', 'dëkk', 'réew', 'yoon',
    'téere', 'bindukaay', 'dàll', 'yéré', 'këyit',
    'xam-xam', 'njàng', 'liggeey', 'mbir', 'jafe-jafe',
    'ñawkat', 'jàngalekat', 'bindkat', 'jàngkat',
    'xale', 'nit', 'jigéen', 'góor', 'buur', 'ndoomu',
    'waa', 'diné', 'yàlla', 'yalla', 'serigne', 'cheikh',
    'borom', 'diam', 'pod', 'maricu', 'tut',
    'yaw', 'yu', 'té', 'di', 'say', 'umu', 'ray', 'tuba', 'touba',
])

COMMON_ADJECTIVES = frozenset([
    'baax', 'bon', 'rafet', 'mag', 'ndaw', 'bees', 'yàgg', 'gaaw', 'sedd', 'tàng',
    'xonq', 'weex', 'ñuul', 'rey', 'tuuti', 'gudd', 'gàtt', 'diis', 'woyof',
    'sonnu', 'sonn', 'xiif', 'mar', 'feebar', 'tang', 'sedd', 'neex', 'metti',
    'doy', 'yomb', 'jafe', 'xew', 'fees', 'sell', 'saafara', 'set',
])

PRONOUNS = {
    'man': {'person': 1, 'number': 'sg', 'type': 'emphatic'},
    'yow': {'person': 2, 'number': 'sg', 'type': 'emphatic'},
    'moom': {'person': 3, 'number': 'sg', 'type': 'emphatic'},
    'nun': {'person': 1, 'number': 'pl', 'type': 'emphatic'},
    'yeen': {'person': 2, 'number': 'pl', 'type': 'emphatic'},
    'ñoom': {'person': 3, 'number': 'pl', 'type': 'emphatic'},
    'sama': {'person': 1, 'number': 'sg', 'type': 'possessive'},
    'sa': {'person': 2, 'number': 'sg', 'type': 'possessive'},
    'am': {'person': 3, 'number': 'sg', 'type': 'possessive'},
    'sunu': {'person': 1, 'number': 'pl', 'type': 'possessive'},
    'seen': {'person': 2, 'number': 'pl', 'type': 'possessive'},
    'seen': {'person': 3, 'number': 'pl', 'type': 'possessive'},
}

NUMBERS = {
    'benn': 1, 'ñaar': 2, 'ñett': 3, 'ñeent': 4, 'juróom': 5,
    'juróom-benn': 6, 'juróom-ñaar': 7, 'juróom-ñett': 8, 'juróom-ñeent': 9,
    'juróom-benni': 6, 'juróom-ñaari': 7, 'juróom-ñetti': 8, 'juróom-ñeenti': 9,
    'fukk': 10, 'fukki': 10, 'ñaar-fukk': 20, 'ñaar-fukki': 20,
    'ñett-fukk': 30, 'ñeent-fukk': 40, 'juróom-fukk': 50,
    'téeméer': 100, 'teemeer': 100, 'teemeeri': 100,
    'junni': 1000, 'juni': 1000,
    'fanweer': 30,
}

COMMON_ADVERBS = frozenset([
    'lool', 'ndank', 'ndànk-ndànk', 'leegi', 'tey', 'démb', 'suba', 'ëllëg',
    'fii', 'foofu', 'fee', 'fale', 'rekk', 'nak', 'sax', 'ba', 'noonu',
    'bénn-bénn', 'yépp', 'ñépp', 'lu', 'ni', 'naka',
])

COMMON_WORDS = (
    COMMON_VERBS | COMMON_NOUNS | COMMON_ADJECTIVES | set(PRONOUNS.keys()) | 
    set(NUMBERS.keys()) | COMMON_ADVERBS | TAM_MARKERS | ALL_DETERMINERS | 
    DISCOURSE_MARKERS | CONJUNCTIONS | PREPOSITIONS | INTERROGATIVES
)

ARABIC_LOANWORDS = frozenset([
    'yàlla', 'yalla', 'allah', 'amine', 'machallah', 'inchallah', 'inshallah',
    'inshàlla', 'inshalla',
    'wallahi', 'billahi', 'bismillah', 'alhamdulillah', 'subhanallah',
    'aldiana', 'aljanna', 'firdaws', 'firdawsi', 'barke', 'barké', 'baraka',
    'tawfékh', 'tawfex', 'ziar', 'ziyaar', 'ziyara',
    'seydina', 'serigne', 'seriñ', 'oustaz', 'imam', 'xaliifa',
    'altine', 'talaata', 'àllarba', 'alxames', 'àjjuma',
    'ajar', 'aduna', 'dunya', 'kitaab', 'xarala', 'junub', 'sàkk', 'bor', 'sabab', 'waxtu',
])

FRENCH_COMMON = frozenset([
    'mais', 'que', 'pour', 'vraiment', 'trop', 'très', 'bien', 'comme', 'avec',
    'dans', 'sur', 'quand', 'aussi', 'même', 'alors', 'donc', 'car', 'parce',
    'je', 'tu', 'il', 'elle', 'nous', 'vous', 'ils', 'elles', 'on', 'qui',
    'est', 'sont', 'suis', 'fait', 'faire', 'dit', 'dire', 'vais', 'va', 'aller',
    'vont', 'avoir', 'être', 'peut', 'veut', 'doit',
    'série', 'famille', 'problème', 'chose', 'temps', 'monde', 'vie', 'jour',
    'travail', 'argent', 'maison', 'école', 'voiture', 'téléphone',
    'bon', 'petit', 'grand', 'beau', 'nouveau', 'vieux', 'jeune',
    'la', 'le', 'les', 'un', 'une', 'des', 'du', 'de', 'en', 'et', 'ou', 'a', 'au',
    'ce', 'cette', 'ces', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses',
    'ici', 'là', 'où', 'oui', 'non', 'pas', 'plus', 'moins', 'tout', 'tous', 'toute',
    'moi', 'toi', 'lui', 'eux', 'leur', 'se', 'ne', 'si', 'ni', 'sans', 'sous',
    'saison', 'serie', 'épisode', 'episode', 'film', 'acteur', 'actrice',
    'pur', 'super', 'génial', 'genial', 'top', 'love', 'adore', 'aime',
    'quoi', 'comment', 'pourquoi', 'combien', 'quel', 'quelle',
    'regarde', 'regarder', 'voir', 'vois', 'vu', 'vus', 'vue',
    'préférée', 'preferee', 'meilleur', 'meilleure', 'pire',
    'début', 'fin', 'suite', 'prochain', 'dernier', 'premier',
    'plaisir', 'joie', 'bonheur', 'amour', 'coeur', 'cœur',
    'jamais', 'toujours', 'souvent', 'parfois', 'encore', 'déjà',
    'faut', 'falloir', 'pouvoir', 'vouloir', 'savoir', 'croire',
    'rien', 'personne', 'quelque', 'autre', 'chaque', 'certain',
    'à', 'paix', 'âme', 'bébé', 'merci', 'bravo', 'fort', 'forte',
    'repose', 'repos', 'paradis', 'courage', 'rôle', 'vidéo', 'vidéos',
    'pro', 'tus', 'nus', 'devez', 'pose', 'rip', 'team', 'belle', 'belles',
    'toujours', 'tujours', 'purquoi', 'juste', 'vrai', 'vraie', 'faux',
    'mort', 'morte', 'triste', 'heureux', 'heureuse', 'content', 'contente',
    'femme', 'homme', 'enfant', 'fille', 'garçon', 'mère', 'père',
    'seul', 'seule', 'ensemble', 'entre', 'après', 'avant', 'pendant',
    'tué', 'force', 'curage', 'livre', 'jure', 'soit', 'puce', 'été',
    'jue', 'depuis', 'grave', 'pensé', 'héros', 'visage', 'beaucup',
    'beaucoup', 'me', 'te', 'ui', 'ha', 'es',
    'tv', 'ame', 'tujurs', 'céleste', 'parle', 'fois', 'prophète',
    'venez', 'ai', 'votre', 'était', 'role', 'juer', 'avez', 'dernière',
    'titre', 'ok', 'tres', 'vite', 'deja', 'vraiment',
])

FRENCH_CONTRACTIONS = frozenset([
    "c'est", "j'ai", "l'homme", "l'eau", "d'accord", "n'est", "qu'il", "qu'elle",
    "s'il", "m'a", "t'a", "l'a", "j'aime", "d'abord", "jusqu'à", "aujourd'hui",
    "n'a", "n'ai", "n'ont", "n'avait", "qu'on", "qu'est", "l'autre", "d'autres",
])

ENGLISH_COMMON = frozenset([
    'ok', 'okay', 'yes', 'no', 'please', 'sorry', 'thanks', 'thank',
    'hello', 'bye', 'hi', 'cool', 'nice', 'good', 'bad',
    'phone', 'car', 'money', 'time', 'work', 'school', 'house',
    'facebook', 'whatsapp', 'instagram', 'internet', 'computer',
    'business', 'meeting', 'problem', 'issue',
])

SENEGAL_PLACES = frozenset([
    'dakar', 'thiès', 'thies', 'kaolack', 'ziguinchor', 'saint-louis', 'ndar',
    'touba', 'mbour', 'rufisque', 'diourbel', 'louga', 'tambacounda', 'kolda',
    'matam', 'fatick', 'kaffrine', 'kédougou', 'kedougou', 'sédhiou', 'sedhiou',
    'sénégal', 'senegal', 'gambie', 'gambia', 'casamance', 'sine', 'saloum',
    'fouta', 'walo', 'cayor', 'baol', 'djolof', 'jolof',
    'gorée', 'goree', 'almadies', 'yoff', 'ngor', 'ouakam', 'pikine', 'guédiawaye',
    'tivaouane', 'mbacké', 'mbacke', 'bambey', 'gossas', 'nioro', 'foundiougne',
    'sokone', 'guinguinéo', 'linguère', 'linguere', 'dahra', 'kébémer', 'kebemer',
    'ranérou', 'ranerou', 'podor', 'dagana', 'richard-toll', 'kanel',
    'vélingara', 'velingara', 'médina-yoro-foulah', 'saraya', 'salémata',
    'goudomp', 'bounkiling', 'bignona', 'oussouye', 'diouloulou',
    'birkelane', 'koungheul', 'malem-hodar', 'mbirkilane',
    'bakel', 'goudiry', 'koumpentoum', 'kidira',
    'thiaroye', 'parcelles', 'médina', 'medina', 'plateau', 'fann',
    'sicap', 'liberté', 'liberte', 'sacré-coeur', 'mermoz', 'mamelles',
    'diamniadio', 'saly', 'somone', 'ngaparou', 'popenguine', 'joal', 'fadiouth',
    'kayar', 'lac-rose', 'lac rose', 'petite-côte', 'cap-skirring',
])

WOLOF_NAMES = frozenset([
    'samba', 'demba', 'fatou', 'fatu', 'awa', 'moussa', 'musa', 
    'ibrahima', 'amadou', 'amadu', 'ousmane', 'usmane',
    'mariama', 'aissatou', 'aisatu', 'aminata', 'modou', 'modu',
    'mamadou', 'mamadu', 'abdoulaye', 'abdulaye', 'aliou', 'aliu',
    'oumar', 'umar', 'binta', 'coumba', 'kumba', 'ndeye', 'ndey',
    'pape', 'cheikh', 'sokhna', 'soxna',
    'adja', 'mor', 'mbaye', 'lamine', 'malick', 'youssou', 'yusu',
    'babacar', 'babakar', 'abdou', 'abdu',
    'alassane', 'alasan', 'khady', 'xadi', 'mame', 'biram', 
    'thierno', 'cerno', 'assane', 'asan', 'djibril', 'jibril',
    'seydou', 'seydu', 'boubacar', 'bubakar', 'aida', 'astou', 'astu',
    'yacine', 'yasin', 'rokhaya', 'roxaya', 'seynabou',
    'dieynaba', 'jeynaba', 'nogaye', 'aby', 'adama', 'bamba', 
    'fallou', 'falu', 'serigne', 'seriñ',
    'diop', 'ndiaye', 'fall', 'gueye', 'geye', 'seck', 'ba', 'sy', 
    'thiam', 'ciam', 'diallo', 'jalo',
    'faye', 'sall', 'cisse', 'cissé', 'diouf', 'juf', 'wade', 
    'diagne', 'jañ', 'sarr', 'niang', 'ñang',
    'kane', 'dia', 'ja', 'tall', 'samb', 'lo', 'ndoye', 'ndoy',
    'sene', 'bodian', 'bojan', 'diatta', 'jata', 'sonko', 'sow', 'so', 'camara', 'kamara',
])

POS_CATEGORIES = {
    'VERB': COMMON_VERBS,
    'NOUN': COMMON_NOUNS,
    'ADJ': COMMON_ADJECTIVES,
    'PRON': set(PRONOUNS.keys()),
    'NUM': set(NUMBERS.keys()),
    'ADV': COMMON_ADVERBS,
    'DET': ALL_DETERMINERS,
    'TAM': TAM_MARKERS,
    'DISC': DISCOURSE_MARKERS,
    'CONJ': CONJUNCTIONS,
    'PREP': PREPOSITIONS,
    'INTER': INTERROGATIVES,
}