#ler um arquivo JSON
import json
from pathlib import Path

from .models import Book


class BookRepository:
    """
    Responsável por acessar os dados da biblioteca.
    """

    def __init__(self):
        self.data_file = (
            Path(__file__).parent / "data" / "books.json"
        )

    def get_all_books(self) -> list[Book]:
        """
        Retorna todos os livros da biblioteca.
        """
        with open(self.data_file, "r", encoding="utf-8") as file:
            books_data = json.load(file)

        return [Book(**book) for book in books_data]