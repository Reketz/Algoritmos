def registrarUsuario(nome, senha, acesso = False):
    usuario = dict()
    usuario['nome'] = nome
    usuario['senha'] = senha
    usuario['acesso'] = acesso
    return usuario


def validarDados(**dados):
    nome = dados['nome']
    senha = dados['senha']
    messagemErro = ''
    if(nome == ''):
        messagemErro += ('* O campo nome é obrigatório\n')
    if(senha == ''):
        messagemErro +=('* O campo senha é obrigatório\n')
    
    return messagemErro

nomeUsuario = input('Digite o nome do usuário: ')
senhaUsuario = input('Digite o senha do usuário: ')
acesso = input('Digite o acesso do usuário: [A - Admin, U - Usuario]')

validado = validarDados(nome=nomeUsuario, senha=senhaUsuario)

if(validado == ''):
    novoUsuario = registrarUsuario(nomeUsuario, senhaUsuario, acesso == 'A')
    print(novoUsuario)
    
else:
    print(validado)