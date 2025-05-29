import hello
import pytest

def test_greet():
    assert hello.greet() == "Hello, World!"
    assert hello.greet("Alice") == "Hello, Alice!"