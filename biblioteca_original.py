# biblioteca.py original (antes da refatoração do Encontro 4)
# Contém o código misturado com opções de menu
acervo = []
while True:
    print("\n=== BIBLIOTECA ===")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Listar")
    print("0 - Sair")
    opcao = input("Opcao: ")
    
    if opcao == "1":
        # Cadastrar livro
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        livro = {"titulo": titulo, "autor": autor, "ano": ano}
        acervo.append(livro)
        print("Livro cadastrado.")
    elif opcao == "2":
        # Consultar livro
        titulo = input("Buscar: ")
        achado = False
        for livro in acervo:
            if livro["titulo"] == titulo:
                print(livro["autor"])
                achado = True
                break
        if not achado:
            print("Nao esta no acervo.")
    elif opcao == "3":
        # Listar livros
        if not acervo:
            print("Acervo vazio.")
        else:
            print(f"Total: {len(acervo)}")
            for livro in acervo:
                print(f"{livro['titulo']} - {livro['autor']}")
    elif opcao == "0":
        print("Ate logo.")
        break
    else:
        print("Opcao invalida.")
