from binomial import array_factorials, factorial


def test_array_factorials():
    n = 2
    result = array_factorials(n)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result == [1]
