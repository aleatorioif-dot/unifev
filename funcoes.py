# Encontro 4 - Parte 1: Prática com funções
# def da NOME a um pedaco de programa. notas e o parametro que entra
def media(notas):
    return sum(notas) / len(notas) # return entrega o resultado

# corte = 7.0 e um valor padrao: quem chamar pode omitir
def situacao(nota, corte=7.0):
    if nota >= corte:
        return "aprovado"
    return "recuperacao"

# a virgula devolve DOIS valores de uma vez
def min_max(notas):
    return min(notas), max(notas)

notas = [7, 9, 5]
print(media(notas))
print(situacao(8))        # usa o corte padrao, 7.0
print(situacao(8, 8.5))   # passa outro corte
menor, maior = min_max(notas)
print(menor, maior)
