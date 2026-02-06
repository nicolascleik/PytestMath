# PytestMath

> Uma biblioteca de funções matemáticas essenciais desenvolvida para demonstrar práticas de **Testes Unitários** robustos utilizando o framework **Pytest**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)
![Pytest](https://img.shields.io/badge/Test-Pytest-yellow?logo=pytest)
![Status](https://img.shields.io/badge/Status-Educational-orange)

## Objetivo do Projeto

Este projeto serve como um laboratório de estudos para implementação de testes automatizados em Python. O foco não é apenas a lógica matemática, mas sim como garantir que essa lógica funcione em diversos cenários, incluindo casos de erro e limites.

### Conceitos de Testes Aplicados:
* **Happy Path:** Testes de sucesso para somas e divisões simples.
* **Exception Handling:** Verificação de lançamento de erros (ex: `ZeroDivisionError`) usando `pytest.raises`.
* **Parametrização:** Uso de `@pytest.mark.parametrize` para testar múltiplas entradas e saídas (ex: Números Primos) sem repetir código.
* **Edge Cases:** Tratamento de fatoriais de números negativos e zero.

## Estrutura do Projeto

```text
PytestMath/
├── matematica.py        # Módulo com a lógica das funções (soma, divisão, fatorial, primo)
├── test_matematica.py   # Suíte principal de testes unitários
├── test_sample.py       # Arquivo de rascunho para testes simples
└── README.md            # Documentação

```

## Funções Implementadas

O arquivo `matematica.py` contém as seguintes operações:

1. **`somar(n1, n2)`**: Retorna a soma de dois números.
2. **`dividir(n1, n2)`**: Realiza divisão (levanta erro nativo se dividir por zero).
3. **`fatorial(n)`**:
* Retorna `None` para números negativos.
* Calcula o fatorial iterativo para inteiros positivos.


4. **`eh_numero_primo(n)`**: Verifica se um número é primo (retorna `True` ou `False`) com algoritmo otimizado.

## Como Executar

### Pré-requisitos

* Python 3 instalado.
* Biblioteca `pytest`.

### 1. Instalação

Caso não tenha o pytest instalado:

```bash
pip install pytest

```

### 2. Rodando os Testes

Para executar todos os testes e ver o resultado detalhado no terminal:

```bash
# Execução simples
pytest

# Execução verbosa (mostra cada teste individualmente)
pytest -v

```

## Exemplo de Código e Teste

Um dos destaques do projeto é o uso de **Parametrização** para testar números primos de forma limpa:

**Lógica (`matematica.py`):**

```python
def eh_numero_primo(n):
    if n <= 1: return False
    if n == 2: return True
    # ... lógica de verificação ...
    return True

```

**Teste Parametrizado (`test_matematica.py`):**

```python
@pytest.mark.parametrize("entrada, esperado", [
    (2, True),
    (5, True),
    (9, False),
    (25, False),
    (1, False),
    (17, True)
])
def test_primo_varios_casos(self, entrada, esperado):
    assert matematica.eh_numero_primo(entrada) is esperado

```

Isso garante que com uma única função de teste, validamos 6 cenários diferentes!

---

Desenvolvido por **Nicolas Cleik de Andrade** como parte do desafio de estudos "Hard Mode", como exemplo de **Boas Práticas em Python**.

```