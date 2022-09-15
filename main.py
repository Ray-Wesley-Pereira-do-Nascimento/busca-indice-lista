def busca_indice(base, buscado):
    return base.index(buscado)



vetI = [str] * 5
for i in range(5):
    vetI[i] = input('Digite um nome: ')

sBusca = input("\nDigite o nome que quer procurar: ")
print(f"\n{sBusca} está no índice {busca_indice(vetI, sBusca)} da base de dados.")



