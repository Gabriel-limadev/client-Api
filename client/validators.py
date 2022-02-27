import re
from validate_docbr import CPF

def valid_name(name):
    name = name.replace(" ", "")
    return name.isalpha()
    
def valid_cpf_characters(cpf):
    return len(cpf) == 11

def valid_cpf(cpf):
        document = CPF()
        return document.validate(cpf)

def valid_rg(rg):
    return len(rg) == 9

def valid_smartphone(smartphone):
    """Verifica se o celular é válido (11 95946-1782)"""
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    answer = re.findall(model, smartphone)
    
    return answer