### حذف الكتاب

#### الأمر:
```python
from bookshelf.models import Book

# استرجاع الكتاب الذي تم إنشاؤه
new_book = Book.objects.get(title="Nineteen Eighty-Four")

# حذف الكتاب
new_book.delete()

# التأكد من أن الكتاب قد تم حذفه
Book.objects.all()
# resulte
(1, {'bookshelf.Book': 1})
<QuerySet []>