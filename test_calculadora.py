import pytest
from Calculadora import Calculadora  

def calc():

    return Calculadora()

def test_adicao():
    calc = Calculadora()
    assert calc.adicao(5, 3) == 8
    assert calc.adicao(0, 0) == 0
    assert calc.adicao(-1, 1) == 0
    assert calc.adicao(-5, -3) == -8

def test_subtracao():
    calc = Calculadora()
    assert calc.subtracao(5, 3) == 2
    assert calc.subtracao(5, 5) == 0
    assert calc.subtracao(3, 5) == -2
    assert calc.subtracao(-5, -3) == -2

def test_multiplicacao():
    calc = Calculadora()
    assert calc.multiplicacao(5, 3) == 15
    assert calc.multiplicacao(0, 5) == 0
    assert calc.multiplicacao(-2, 3) == -6
    assert calc.multiplicacao(-2, -3) == 6

def test_divisao():
    calc = Calculadora()
    assert calc.divisao(5, 2) == 2.5
    assert calc.divisao(5, 0) == "Erro: Divisão por zero não é permitida."        
    assert calc.divisao(6, 3) == 2
    assert calc.divisao(-6, 3) == -2
    assert calc.divisao(-6, -3) == 2

def test_fatorial():
    calc = Calculadora()
    assert calc.fatorial(5) == 120
    assert calc.fatorial(0) == 1
    assert calc.fatorial(1) == 1
    assert calc.fatorial(-5) == "Erro: Fatorial de número negativo não é definido."
    assert calc.fatorial(10) == 3628800

def test_potencia():
    calc = Calculadora()
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(2, -2) == 0.25
    assert calc.potencia(-2, 3) == -8
    assert calc.potencia(-2, 2) == 4
