from validate_docbr import CPF

def nome_valido(nome):
    return nome.isalpha()

def cpf_caracteres_valido(cpf):
    return len(cpf) == 11

def cpf_valido(cpf):
    def valida(cpf):
        """Função que valida o CPF com a biblioteca validate_docbr CPF"""
        validador = CPF()
        print(validador.validate(cpf))
        return validador.validate(cpf)
    return valida(cpf)

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    return len(celular) < 11
