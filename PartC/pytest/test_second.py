import pytest

@pytest.mark.dependency(name='a')
def test_six():
    assert 'malayalam' == 'malayalam', "malayalam is not a palindrome"
    print('malayalam is Palindrome string')

@pytest.mark.dependency(name='b')
def test_seven():
    print("Seventh Testcase")


def test_eight():
    print("This is eigth class")


num = 10
def test_nine(num):
    assert num % 2 == 0, "It is not even number"
    print("It is even number")

@pytest.mark.dependency(depends=['a','b'])
def test_ten():
    assert 'Sample' == 'Bye', "both are not same"
    print("We both are same")

