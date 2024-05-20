def cadastrarFilme(nome, genero, valor_ingresso):
    filme = dict()
    filme['genero'] = genero
    filme['valor'] = valor_ingresso
    filme['nome'] = nome

filme1 = cadastrarFilme(nome="Tropa de elite", 
                       valor_ingresso=50, 
                       genero="Ação")

filme2 = cadastrarFilme('Frozen', 'Fantasia', 10)
if(not filme1):
    print('Filme não cadastrado!')