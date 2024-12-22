### تحديث عنوان الكتاب

#### الأمر:
```python
from bookshelf.models import Book

# استرجاع الكتاب الذي تم إنشاؤه سابقًا
new_book = Book.objects.get(title="1984")

# تحديث عنوان الكتاب
new_book.title = "Nineteen Eighty-Four"
book.save()

# عرض الكتاب بعد التحديث
new_book
# resulte
<Book: Nineteen Eighty-Four>
