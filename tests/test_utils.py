from ..code.utils import (
    cleanspaces,
    cleanduplicated_words,
    cleanduplicated_sentences,
    onlyalphabetic,
    onlyalphanumeric,
    lowercase,
    nums2words,
    removestopwords,
    lemmatizer,
    stemmer
    )


def test_cleanspaces():
    fixture = "Text   with multiple   spaces"
    t = cleanspaces(fixture)
    assert t == "Text with multiple spaces"


def test_cleanduplicated_words():
    fixture = "duplicated Text Text"
    fixture_two = "this sentence. this sentence."
    t = cleanduplicated_words(fixture)
    u = cleanduplicated_words(fixture_two)
    assert t == "duplicated Text"
    assert u == "this sentence. this sentence."


def test_cleanduplicated_sentences():
    fixture = "duplicated Text Text"
    fixture_two = "this sentence. this sentence."
    t = cleanduplicated_sentences(fixture)
    u = cleanduplicated_sentences(fixture_two)
    assert t == "duplicated Text Text"
    assert u == "this sentence."


def test_onlyalphabetic():
    fixture = "t.e_!x-4t"
    t = onlyalphabetic(fixture)
    u = onlyalphabetic(fixture, False)
    assert t == "t e  x  t"
    assert u == "text"


def test_onlyalphanumeric():
    fixture = "t.e_!x-4t"
    t = onlyalphanumeric(fixture)
    u = onlyalphanumeric(fixture, False)
    assert t == "t e  x 4t"
    assert u == "tex4t"


def test_lowercase():
    fixture = "TeXt!"
    t = lowercase(fixture)
    assert t == "text!"


def test_nums2words():
    fixture = "23 and 1 and 2s 5!"
    t = nums2words(fixture)
    assert t == " twenty-three and one and 2s five!"


def test_removestopwords():
    fixture = "this is a sentence"
    t = removestopwords(fixture.split())
    assert t == ["sentence"]


def test_lemmatizer():
    fixture = "The cats are running quickly."
    t = lemmatizer(fixture.split())
    assert t == ['The', 'cat', 'be', 'run', 'quickly.']


def test_stemmer():
    fixture = "this is a running sentence"
    t = stemmer(fixture.split())
    assert t == ['thi', 'is', 'a', 'run', 'sentenc']
