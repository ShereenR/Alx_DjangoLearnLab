<!-- creation  -->

#### الأمر:
```python
from bookshelf.models import Book
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
new_book
# resulte
<Book: 1984>

# retrieve

#### الأمر:

from bookshelf.models import Book

# استرجاع الكتاب الذي تم إنشاؤه سابقًا
new_book = Book.objects.get(title="1984")

# عرض جميع الخصائص
new_book.title, new_book.author, new_book.publication_year

# resultes
('1984', 'George Orwell', 1949)

# update
#### الأمر:

from bookshelf.models import Book

# استرجاع الكتاب الذي تم إنشاؤه سابقًا
new_book = Book.objects.get(title="1984")

# تحديث عنوان الكتاب
new_book.title = "Nineteen Eighty-Four"
new_book.save()

# عرض الكتاب بعد التحديث
new_book
# resulte
<Book: Nineteen Eighty-Four>

# delete

