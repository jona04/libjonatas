from libjonatas.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Jonatas', email='jonatas.iw@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Jonatas', email='jonatas.iw@gmail.com'), Usuario(nome='Silva', email='silva@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
