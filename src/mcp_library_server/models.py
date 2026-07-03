from dataclasses import dataclass

# Essa classe representa um livro na biblioteca, com atributos como id, título, autor, categoria e ano de publicação.
# Modelos reduzem a chance de inconsistências.
@dataclass
class Book:
    """
    Representa um livro da biblioteca.
    """
    id: int
    title: str
    author: str
    category: str
    year: int