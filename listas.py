# Encontro 2 - Parte 4: Vetor vira lista
notas = [] # nasce vazia, sem tamanho definido
notas.append(7) # e cresce conforme voce coloca
notas.append(8.5)
notas.append(6)

print(notas)
print("quantas:", len(notas))
print("primeira:", notas[0])
print("ultima:", notas[-1]) # -1 e o ultimo, sem precisar do tamanho

print("soma:", sum(notas))
print("media:", sum(notas) / len(notas))
print("maior:", max(notas))

# voce pede o item direto: o indice nao interessa
for nota in notas:
    print(nota)
