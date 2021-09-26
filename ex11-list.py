#   de um a 20 de dois em dois
l2 = list(range(0, 20, 2))
print(l2)

#   desempacotando

#   pegando o primeiro, segundo, terceiro e o resto
a, b, c, * resto = l2
print(a, b, c, resto)

#   pegando o ultimo o penultimo e o resto e exibindo
* resto, p, u = l2
print(p, u, resto)

#   penultimo, resto ultimo e penultimo de novo
* resto, p, u = l2
print(p,  resto, u, p)