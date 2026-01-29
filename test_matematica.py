import pytest
import matematica

class TestClass:
    def test_somar(self):
        assert matematica.somar(2, 3) == 5
        assert matematica.somar(0, 2) == 2

    def test_dividir(self):
        assert matematica.dividir(10,2) == 5
        with pytest.raises(ZeroDivisionError):
            assert matematica.dividir(10, 0)

    def test_fatorial(self):
        assert matematica.fatorial(5) == 120
        assert matematica.fatorial(-2) is None
        assert matematica.fatorial(0) == 1

    #def test_primo(self):
    #    assert matematica.eh_numero_primo(2) == True
    #    assert matematica.eh_numero_primo(5)
    #    assert matematica.eh_numero_primo(9) == False
    #    assert not matematica.eh_numero_primo(25)
    #    assert not matematica.eh_numero_primo(1)
    #    assert matematica.eh_numero_primo(17)

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