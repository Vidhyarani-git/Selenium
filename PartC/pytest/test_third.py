import pytest

@pytest.mark.fun
def test_eleven():
    print("Eleventh Test case")

a1 = ['Sample', 'Sam', '0810',123,True]
@pytest.mark.happy
@pytest.mark.fun
@pytest.mark.parametrize('a',a1)
def test_twelve(a):
    assert type(a) == str, "The datatype is not a str"
    for i in a:
        print(i)

@pytest.mark.fun
def test_thirteen():
    print("Thirteenth testcase")

@pytest.mark.happy
def test_fourteen():
    assert "Sample".count('a')>2, "The result is fail"
    print("The result is pass")
    
@pytest.mark.fun
def test_fifteen():
    print("Fifteenth testcase")

#multiple arguments
data=[(10,20),(100,100),(10,-20),('sample','test'),([1,2],[3,4])]
@pytest.mark.parametrize("a,b",data)
def test_add(a,b):
    assert a!=b,"Both are not equal"
    print(a+b)


# Username is correct and password is correct --> Login Successfull
# Username is correct and password is incorrect --> Incorrect Password
# Username is incorrect and password is correct --> Invalid Username
# Username is incorrect and password is incorrect --> Invalid Username
# Check for different values.
args="user,pwd"
data=[('admin','admin123'),('Admin','Admin123'),('Test','Test123'),('Demo','admin123')]
@pytest.mark.parametrize(args,data)
def test_login(user,pwd):
    assert user == 'Admin' ,"Username incorrect"
    assert pwd == 'admin123', "Password incorrect"
    print("Login successfully")





