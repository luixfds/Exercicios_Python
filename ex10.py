#   cria uma lista
nomes = ["João", "José", "Maria", "Fulano"]

#   cria uma variavel e armazena o numero escolhido
id = input("Digite o ID:")

#    procura o valor com o index digitado
for indice, dado in enumerate(nomes):
    #   sempre converter caso for números

    # se o index for igual ao id digitado mostra o tal
    if indice == int(id):
        print(indice, dado)

        #   cria e escreve o tal em um txt
        arquivo = open("arquivo.txt", "w", encoding="UTF-8")
        arquivo.writelines(dado)
        arquivo.close()

    #   caso o index nao corresponder ele exibe a mensagem
    else:
        print ("nao corresponde")