# Encontro 2 - Partes 2 e 3: Condicional, Laço e input()
idade = 20
# repare nos dois-pontos e no recuo o recuo substitui as chaves do C
if idade >= 18:
    print("maior")
elif idade > 12:
    print("adolescente")
else:
    print("crianca")

# range(10) vai de 0 a 9 nunca inclui o ultimo
for i in range(10):
    print(i, end=" ")
print()

# para ir de 1 a 10, diga onde comeca e onde para
for i in range(1, 11):
    print(i, end=" ")
print()

# A armadilha do input()
# int() converte o texto que veio do input em numero
numero = int(input("Digite um numero: "))
print(numero + 1)
