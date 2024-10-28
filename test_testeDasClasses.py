
from funcoes import *
# testes das classes

def test_acordar_cedo():
    assert acordar_cedo(6) == 'Você é um guerreiro'
    assert acordar_cedo(5) == 'Você é um guerreiro'
    assert acordar_cedo(7) == 'Tente novamente amanhã'

def test_tempo_exercicio():
    assert tempo_exercicio(70, 3) == 69 # peso reduzido em 1
    assert tempo_exercicio(70, 1) is None #Deve retornar em none pois ele descansou apenas 1 minuto
    assert tempo_exercicio(60, 2) is None  #Deve retornar em none pois ele descansou apenas 2 minutos

def test_tem_exercicio():
    assert tem_exercicio('Futebol')
    assert not tem_exercicio('Descanso')
    assert tem_exercicio('Vôlei')

