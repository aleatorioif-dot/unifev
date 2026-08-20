# acervo.py - Só o que mexe nos dados (Encontro 4)
def cadastrar(acervo, titulo, autor, ano):
    livro = {"titulo": titulo, "autor": autor, "ano": ano}
    acervo.append(livro)

def buscar(acervo, titulo):
    for livro in acervo:
        if livro["titulo"] == titulo:
            return livro
    return None

def remover(acervo, titulo):
    for livro in acervo:
        if livro["titulo"] == titulo:
            acervo.remove(livro)
            return True
    return False

def mais_antigo(acervo):
    if not acervo:
        return None
    antigo = acervo[0]
    for livro in acervo:
        if livro["ano"] < antigo["ano"]:
            antigo = livro
    return antigo

if __name__ == "__main__":
    teste = []
    cadastrar(teste, "Dom Casmurro", "Machado de Assis", 1899)
    print(buscar(teste, "Dom Casmurro"))
    print(buscar(teste, "Nao existe"))
