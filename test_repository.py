from mcp_library_server.repository import BookRepository

repository = BookRepository()

books = repository.get_all_books()

for book in books:
    print(book)