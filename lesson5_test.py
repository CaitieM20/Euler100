import lesson5
def test_input_1():
    assert lesson5.smallest_multiple(1) == 1

def test_input_3():
    assert lesson5.smallest_multiple(3) == 6

def test_input_4():
    assert lesson5.smallest_multiple(4) == 12

def test_input_5():
    assert lesson5.smallest_multiple(5) == 60

# def test_input_7():
#     assert lesson5.smallest_multiple(7) == 420

# def test_input_10():
#     assert lesson5.smallest_multiple(10) == 2520

# def test_input_13():
#     assert lesson5.smallest_multiple(13) == 360360

# def test_input_20():
#     assert lesson5.smallest_multiple(20) == 232792560