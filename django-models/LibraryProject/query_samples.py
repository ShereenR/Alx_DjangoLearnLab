from relationship_app.models import Book, Author, Library, Librarian

# استعلامات باستخدام Django ORM

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    books_in_library = Book.objects.filter(library__name=library_name)
    return books_in_library

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        librarian = Library.objects.get(name=library_name).librarian
        return librarian
    except Library.DoesNotExist:
        return None
