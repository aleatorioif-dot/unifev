# livro.py - Classes e objetos (Encontro 5)
from datetime import date

class Livro:
    def __init__(self, titulo, autor, ano):
        if not titulo:
            raise ValueError("Titulo e obrigatorio")
        if not autor:
            raise ValueError("Autor e obrigatorio")
        if ano < 1450 or ano > date.today().year:
            raise ValueError(f"Ano invalido: {ano}")
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def descricao(self):
        return f"{self.titulo} - {self.autor} ({self.ano})"
    
    def idade(self):
        return date.today().year - self.ano
        
    def e_classico(self):
        return self.idade() > 100

if __name__ == "__main__":
    acervo = [
        Livro("Dom Casmurro", "Machado de Assis", 1899),
        Livro("Iracema", "Jose de Alencar", 1865),
        Livro("O Cortico", "Aluisio Azevedo", 1890)
    ]
    for livro in acervo:
        print(livro.descricao(), "-", livro.idade(), "anos", "- Classico:", livro.e_classico())
