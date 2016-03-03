import io


def test_make_trigram():
    from trigrams import make_trigram
    file = io.open(test.txt, encoding='utf-8')
    assert len(make_trigram(file)) >= len(file)

# def test_make_story():
#     from trigrams import make_story
#     assert make_story()
