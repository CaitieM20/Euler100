import lesson4

def test_input_2():
    result = lesson4.larget_palindrome_product(2)
    assert result is int
    assert result == 9009

def test_input_3():
    assert lesson4.larget_palindrome_product(3) == 906609

