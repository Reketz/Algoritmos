filmes = [
    {'nome': 'Frozen 1'}, 
    {'nome': 'Tropa de elite'},
    {'nome': '😀 o filme'},
    ]

def buscarFilme(nomeFilme, filmes):
    for filme in filmes:
        if(nomeFilme == filme['nome']):
            return filme
        
    return None

nome = input('Digite o nome do filme: ')
filme = buscarFilme(nome, filmes)

#BUSCAR FILME
if(filme):
    print('Filme:', filme)
else:
    print("Filme não encontrado")
#ADICIONAR
if(filme):
    print('Esse filme já esta cadastrado!')
else:
    print('Iniciado processo de adição')

#ALTERAR
if(filme):
    print('Iniciado processo de alteração')
else:
    print('Filme não encontrado')