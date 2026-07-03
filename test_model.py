from mcp_library_server.models import Book

book = Book(
    id=1,
    title="Clean Code",
    author="Robert C. Martin",
    category="Software Engineering",
    year=2008
)

print(book)