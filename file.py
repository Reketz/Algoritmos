ingressos = [
    {
        'nome': 'Joao',
        'filmes': [
            {
                'nome': 'Rambo',
                'valor': 50,
                'quantidade': 1
            },
            {
                'nome': 'Filme do Pelé',
                'valor': 24,
                'quantidade': 1
            },
            {
                'nome': 'Rio 2',
                'valor': 59.9,
                'quantidade': 2
            },
        ]
    }
]

f = open("ingressos.txt", "a", encoding="UTF-8")

for ingresso in ingressos:
    f.write(f"Nome do cliente: {ingresso['nome']}\n")
    for filme in ingresso['filmes']:
        f.write(f'\tO filme {filme["nome"]} foi assistido {filme["quantidade"]} vezes\n')

f.close()