import lesson1

def test_input_10():
    assert lesson1.sum_multiples_of_three_and_five(10) == 23

def test_input_49():
    assert lesson1.sum_multiples_of_three_and_five(49) == 543

def test_input_1000():
    assert lesson1.sum_multiples_of_three_and_five(1000) == 233168

def test_input_8456():
    assert lesson1.sum_multiples_of_three_and_five(8456) == 16687353 

def test_input_19564():
    assert lesson1.sum_multiples_of_three_and_five(19564) == 89301183
