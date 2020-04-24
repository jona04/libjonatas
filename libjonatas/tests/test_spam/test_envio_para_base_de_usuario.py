from unittest.mock import Mock

import pytest

# from libjonatas.spam.enviador_email import Enviador
from libjonatas.spam.main import EnviadorDeSpam
from libjonatas.spam.modelos import Usuario


# class EnviadorMock(Enviador):
#
#     def __init__(self):
#         super().__init__()
#         self.parametros_de_envio = None
#         self.qtd_email_enviados = 0
#
#     def enviar(self, remetente, destinatarios, assunto, corpo):
#         self.parametros_de_envio = (remetente, destinatarios, assunto, corpo)
#         self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jonatas', email='jonatas.iw@gmail.com'),
            Usuario(nome='Silva', email='silva@gmail.com')
        ],
        [
            Usuario(nome='Jonatas', email='jonatas.iw@gmail.com'),
        ]

    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador2 = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador2)
    enviador_de_spam.enviar_emails(
        'jonatas.iw@gmail.com',
        'assum email',
        'corpo email')
    assert len(usuarios) == enviador2.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jonatas', email='jonatas.iw@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'silva@gmail.com',
        'assum email',
        'corpo email')
    enviador.enviar.assert_called_once_with == (
        'silva@gmail.com',
        'jonatas.iw@gmail.com',
        'assum email',
        'corpo email'
    )
