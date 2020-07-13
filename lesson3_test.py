import lesson3

def test_input_2():
    assert lesson3.largest_prime_factor(2) == 2

def test_input_3():
    assert lesson3.largest_prime_factor(3) == 3

def test_input_5():
    assert lesson3.largest_prime_factor(5) == 5
    
def test_input_7():
    assert lesson3.largest_prime_factor(7) == 7

def test_input_8():
    assert lesson3.largest_prime_factor(8) == 2

def test_input_12():
    assert lesson3.largest_prime_factor(12) == 3

def test_input_13195():
    assert lesson3.largest_prime_factor(13195) == 29

