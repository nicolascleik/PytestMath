def somar(n1, n2):
    return n1 + n2

def dividir(n1, n2):
    return n1 / n2

def fatorial(n):
    if n < 0: return None
    if n == 0 or n == 1: return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado

def eh_numero_primo(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    limite = int(n ** (1 / 2))
    for i in range(3, limite + 1, 2):
        if n % i == 0:
            return False

    return True
