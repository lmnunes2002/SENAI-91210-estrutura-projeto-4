import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Marta", 22, Sexo.FEMININO)
    return pessoa

def test_pessoa_mudar_nome_valido(pessoa_valida):
    pessoa_valida._nome = "José"
    return pessoa_valida._nome == "José"

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida._nome == "Marta"

def test_pessoa_idade_valido(pessoa_valida):
    assert pessoa_valida._idade == 22

def test_pessoa_idade_negativo(pessoa_valida):
    pessoa_valida.set_idade(-1)
    assert pessoa_valida._idade == 0