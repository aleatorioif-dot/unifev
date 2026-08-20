# principal.py - Só o que conversa com o usuário (Encontro 4)
from acervo import cadastrar, buscar

livros = []
while True:
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("0 - Sair")
    opcao = input("Opcao: ")
    
    if opcao == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        while True:
            try:
                ano = int(input("Ano: "))
                break
            except ValueError:
                print("O ano precisa ser um numero. Tente de novo.")
        cadastrar(livros, titulo, autor, ano)
        print("Livro cadastrado.")
    elif opcao == "2":
        achado = buscar(livros, input("Buscar: "))
        if achado:
            print(achado["autor"])
        else:
            print("Nao esta no acervo.")
    elif opcao == "0":
        print("Ate logo.")
        break
    else:
        print("Opcao invalida.")
