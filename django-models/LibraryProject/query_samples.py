from relationship_app.models import Book, Author, Library, Librarian


books = Author.objects.filter(author_name="author")
all_books= Book.objects.all()
librarian =Library.objects.all()
