import lesson2

def test_input_10():
    assert lesson2.compute_sum(10) == 10

def test_input_60():
    assert lesson2.compute_sum(60) == 44

def test_input_1000():
    assert lesson2.compute_sum(1000) == 798

def test_input_100000():
    assert lesson2.compute_sum(100000) == 60696

def test_input_4000000():
    assert lesson2.compute_sum(4000000) == 4613732
