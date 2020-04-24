import pytest

from libjonatas.spam.enviador_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente',
                         ['jonatas.iw@gmail.com', 'teste@teste.com'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(remetente,
                                'silva@gmail.com.br',
                                'Olha aqui teste email',
                                'Corpo mensagem')
    assert remetente in resultado


@pytest.mark.parametrize('remetente',
                         ['jonatas.iwgmail.com', ''])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente,
                        'silva@gmail.com.br',
                        'Olha aqui teste email',
                        'Corpo mensagem')
