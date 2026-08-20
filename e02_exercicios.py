# Encontro 2 - Parte 6: Entregavel
print("=== Exercício 1 ===")
soma = 0
for i in range(5):
    num = int(input(f"Digite o numero {i+1}: "))
    soma += num
print(f"Soma: {soma}")
print(f"Media: {soma/5}")

print("\n=== Exercício 2 ===")
notas = []
for i in range(6):
    notas.append(float(input(f"Digite a nota {i+1}: ")))
media_turma = sum(notas) / len(notas)
acima_media = sum(1 for n in notas if n > media_turma)
print(f"Maior nota: {max(notas)}")
print(f"Menor nota: {min(notas)}")
print(f"Média da turma: {media_turma}")
print(f"Notas acima da média: {acima_media}")

print("\n=== Exercício 3 ===")
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

soma_total = 0
for i, linha in enumerate(matriz):
    soma_linha = sum(linha)
    soma_total += soma_linha
    print(f"Soma da linha {i}: {soma_linha}")

print(f"Soma total da matriz: {soma_total}")
