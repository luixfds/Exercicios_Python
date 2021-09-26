#   criando lista com nome
v = ['luis', 'felipe', 'dos', 'santos']

#   exibindo lista cmopleta
print (v)
#   exibindo lista por index
print (v[0])
#   acrescenta mais um na lista
v.append('souza')
print (v)

#   exibindo dado por dado da lista
for dados in v:
    print (dados)

#   exibindo dado por dado da lista com o index de cada
for dados in enumerate(v):
    print (dados)

#   exibindo dado por dado da lista com o index de cada corretamente (compactando e descompactando)
for indice, dados in enumerate(v):
    print (indice, dados)
