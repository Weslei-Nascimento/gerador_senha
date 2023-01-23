import secrets
import string


def gerador_senha(tamanho, caracteres):
    # Gera a senha com o tamanho especificado
    senha = ''.join([secrets.choice(caracteres) for x in range(tamanho)])
    return senha


# Gera os caracteres que poderão ser usados na senha
caracteres = string.ascii_letters + string.digits + string.punctuation

# Especifique o tamanho da senha
tamanho = int(input("Por favor, informe o tamanho da senha: "))

# Chama a senha
senha = gerador_senha(tamanho, caracteres)

# print a senha
print("A sua nova senha é: " + senha)
