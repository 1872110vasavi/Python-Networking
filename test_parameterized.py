import pytest

@pytest.mark.parametrize("a,b,c", [(1,2,3),(1,8,9)])
def test_functionAdd(a,b,c):
    assert a+b==c

@pytest.mark.parametrize("p,q,r", [(3,2,1),(5,2,3)])
def test_functionSub(p,q,r):
    assert p-q==r

@pytest.mark.parametrize("x,y,z",[(4,2,2),(20,2,10)])
def test_functionMul(x,y,z):
    assert z*y==x


@pytest.mark.parametrize("a,b,c",[("vasu","abhi","vasuabhi")])
def test_functionconc(a,b,c):
    assert a+b==c
