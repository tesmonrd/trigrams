import io


def test_make_trigram():
    from trigrams import make_trigram
    file = io.open(test.txt, encoding='utf-8')
    assert len(make_trigram(file)) >= len(file)


@pytest.mark.parametrize('d, s', ('test.txt', [])
def test_ran_words_0(d, s):
        from trigrams import ran_words
        assert len(ran_words(d, s)) == 3


# def test_make_story():
#     from trigrams import make_story
#     assert make_story()
