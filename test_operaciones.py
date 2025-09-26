import pytest
import calculadora


def test_sumar():
    assert calculadora.sumar(2,1) == 3




def test_division_por_cero():
     with pytest.raises(ValueError):
         calculadora.dividir(10,0)


@pytest.mark.parametrize("a,b,esperado",[
    (2,5,7), #numeros positivos
    (-4,-2,-6), #numeros negativos
    (0,0,0) #numeros ceros
])
def test_sumar_varios(a,b,esperado):
    assert calculadora.sumar(a,b) == esperado

@pytest.mark.listo


def test_restar_com_fixture(numeros):
    a,b = numeros
    assert calculadora.restar(a,b) == 0

def test_sumar_com_fixture(numeros):
    a,b = numeros
    assert calculadora.sumar(a,b) == 10

@pytest.mark.listo
def test_sumar_listo():
    assert calculadora.sumar(1,3) == 4



    