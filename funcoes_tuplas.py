def pontenciaSomaAdicionais(base, expoente, *adicionais):
    resultado = base ** expoente

    for valor in adicionais:
        resultado += valor
    return resultado

print(pontenciaSomaAdicionais(10, 2, 2*3))