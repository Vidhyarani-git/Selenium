import pytest

@pytest.mark.xfail
def test_one():
    print("First test case.")

@pytest.mark.xfail
def test_two():
    assert 10 == 10.3, "Both are not equal"
    print("Both are same")

@pytest.mark.skipif(10==10,reason='result already exist')
def test_three():
    print("Third Testcase.")

def test_fourth():
    assert 'Subhash' == 'Subhash', "It is not correct"
    print("This is correct")

@pytest.mark.skip(reason='result already exist')
def test_five():
    print("Fifth testcase")
