#   codigo que fala se o numero da variavel é maior que 10 ou nao

#   variavel
x = 10

if x > 10:
    print("Maior")

elif x == 10:
    print("Igual")
else:
    print("Menor")

#   if ternario (escrito em apenas uma linha simplificada) vendo se é igual ou nao é
msg = "Ola" if x == 10 else print("Não")

print(msg or "Não é!")
