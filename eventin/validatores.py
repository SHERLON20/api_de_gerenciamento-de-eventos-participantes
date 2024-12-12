import re

def nome_invalido(nome):
    return len(nome)<3 or not all(char.isalpha() or char.isspace() for char in nome)
def email_invalido(email):
    return '@'not in email or '.' not in email.split('@')[-1]
def telefone_invalido(telefone):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(modelo,telefone)
    return not response