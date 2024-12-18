<!-- the command line -->
Book.objects.all()
<!-- the resultes -->


### استرجاع بيانات الكتاب

#### الأمر:
```python
from bookshelf.models import Book

# استرجاع الكتاب الذي تم إنشاؤه سابقًا
new_book = Book.objects.get(title="1984")

# عرض جميع الخصائص
new_book.title, new_book.author, new_book.publication_year

# resultes
('1984', 'George Orwell', 1949)

