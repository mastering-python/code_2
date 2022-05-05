def test_dict_merge():
    a = dict(a=123)
    b = dict(b=456)
    assert a | b
