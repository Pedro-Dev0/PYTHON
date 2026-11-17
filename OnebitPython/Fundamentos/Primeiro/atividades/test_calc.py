import pytest
from OnebitPython.Fundamentos.Primeiro.atividades.calc import dobro

def test_dobro():
    assert dobro(5) == 10