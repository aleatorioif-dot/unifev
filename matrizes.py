# Encontro 2 - Parte 5: Matriz vira lista de listas
# matriz e uma lista de listas: cada linha e uma lista
matriz = [[1, 2, 3],
          [4, 5, 6]]

print(matriz[1][2]) # linha 1, coluna 2

for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print() # quebra a linha ao terminar cada uma

print("\nPreenchendo nova matriz:")
matriz2 = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"valor [{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha) # a linha pronta entra na matriz
print(matriz2)
