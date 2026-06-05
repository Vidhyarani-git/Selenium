start=1
end=20
def test_factorial(start,end):
    out={}
    for num in range(start, end + 1):
        fact=fact*num
        out[num]=fact
    return out