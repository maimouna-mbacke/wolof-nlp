import pytest
from wolof_nlp import WolofTokenizer, TokenType, normalize, analyze_morphology
from wolof_nlp.applications import analyze_sentiment, Sentiment, extract_entities, tag, gloss


class TestTokenizer:
    
    def test_basic_tokenization(self):
        tokenizer = WolofTokenizer()
        tokens = tokenizer.tokenize("Xale bi")
        words = [t.text for t in tokens if t.type == TokenType.WORD]
        assert "Xale" in words
        assert "bi" in words
    
    def test_language_detection(self):
        tokenizer = WolofTokenizer(detect_language=True)
        tokens = tokenizer.tokenize("Dafa trop neex")
        words = [t for t in tokens if t.type == TokenType.WORD]
        languages = [t.language.name for t in words if t.language]
        assert "WOLOF" in languages
        assert "FRENCH" in languages
    
    def test_normalization(self):
        result = normalize("dieuradieuf")
        assert "jërëjëf" in result.lower() or "diëradiëf" in result.lower()


class TestMorphology:
    
    def test_agent_noun(self):
        morphemes = analyze_morphology("bindkat")
        types = [m.type.name for m in morphemes]
        assert "ROOT" in types
        assert "NOMINALIZATION" in types
    
    def test_negation(self):
        morphemes = analyze_morphology("demul")
        types = [m.type.name for m in morphemes]
        assert "NEGATION" in types
    
    def test_reciprocal(self):
        morphemes = analyze_morphology("gisante")
        types = [m.type.name for m in morphemes]
        assert "RECIPROCAL" in types
    
    def test_reflexive(self):
        morphemes = analyze_morphology("soppiku")
        types = [m.type.name for m in morphemes]
        assert "REFLEXIVE" in types


class TestSentiment:
    
    def test_positive(self):
        result = analyze_sentiment("Dafa neex lool")
        assert result.sentiment == Sentiment.POSITIVE
    
    def test_negative(self):
        result = analyze_sentiment("Dafa metti")
        assert result.sentiment == Sentiment.NEGATIVE
    
    def test_negation_flips_sentiment(self):
        result = analyze_sentiment("Neexul")
        assert result.sentiment == Sentiment.NEGATIVE
        assert "neexul" in result.negated_words
    
    def test_intensifier(self):
        result = analyze_sentiment("Dafa neex lool")
        assert result.intensified == True
    
    def test_arabic_positive(self):
        result = analyze_sentiment("Mashallah")
        assert result.sentiment == Sentiment.POSITIVE
    
    def test_french_positive(self):
        result = analyze_sentiment("C'est magnifique")
        assert result.sentiment == Sentiment.POSITIVE


class TestNER:
    
    def test_place_detection(self):
        entities = extract_entities("Dem naa Dakar")
        labels = [e.label for e in entities]
        assert "LOC" in labels
    
    def test_person_with_title(self):
        entities = extract_entities("Serigne Touba")
        assert any(e.label == "PER" for e in entities)
    
    def test_multi_word_entity(self):
        entities = extract_entities("Cheikh Ahmadou Bamba")
        texts = [e.text for e in entities]
        assert "Cheikh Ahmadou Bamba" in texts
    
    def test_surname_detection(self):
        entities = extract_entities("Mamadou Ndiaye")
        labels = [e.label for e in entities]
        assert "PER" in labels


class TestPOSTagger:
    
    def test_noun_detection(self):
        tags = tag("Xale bi")
        pos_dict = dict(tags)
        assert pos_dict.get("Xale") == "NOUN"
    
    def test_determiner_detection(self):
        tags = tag("Xale bi")
        pos_dict = dict(tags)
        assert pos_dict.get("bi") == "DET"
    
    def test_tam_detection(self):
        tags = tag("Dafa lekk")
        words = [w for w, p in tags]
        pos = [p for w, p in tags]
        assert "TAM" in pos or "TAM.VRBF" in pos
    
    def test_french_detection(self):
        tags = tag("Vraiment magnifique")
        pos_dict = dict(tags)
        assert all(pos == "FWORD" for pos in pos_dict.values())


class TestGlosser:
    
    def test_basic_gloss(self):
        result = gloss("Dinaa dem")
        assert len(result.words) > 0
    
    def test_gloss_structure(self):
        result = gloss("dem")
        for word in result.words:
            assert hasattr(word, 'wolof')
            assert hasattr(word, 'gloss')
            assert hasattr(word, 'translation')
