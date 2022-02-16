import re
from validate_docbr import CPF

def nome_valido(nome):
    return nome.isdigit()
    
def cpf_caracteres_valido(cpf):
    return len(cpf) == 11

def cpf_valido(cpf):
        documento = CPF()
        return documento.validate(cpf)

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """Verifica se o celular é válido (11 95946-1782)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    
    return resposta