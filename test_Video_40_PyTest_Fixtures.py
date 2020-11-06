import pytest

@pytest.fixture()
def setup():
    print("Once before every method")

def Method1(setup):
    print("This is Method 1")

def Method2(setup):
    print("This is Method 2")


@pytest.yield_fixture()
def setupnew():
    print("New Setup before every function")
    yield 
    print("After every method")

def Method3(setupnew):
    print("This is Method 3")

def Method4(setupnew):
    print("This is Method 4")