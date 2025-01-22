### **1. MySQL jadvali yaratish**
#### Funksiya deklaratsiyasi:
```python
def create_books_table(cursor):
    """
    Create a 'books' table in the database if it doesn't exist.
    """
```

#### Nima qilish kerak:
1. MySQL server bilan ulanishni o‘rnating.
2. `books` jadvalini quyidagi ustunlar bilan yarating:
   - `id` - asosiy kalit va avtomatik o‘suvchi.
   - Qolgan ustunlarni yuqoridagi shartlarda berilgan xususiyatlarga muvofiq yarating.
3. Jadval oldindan mavjud bo‘lsa, uni qayta yaratmang.

#### Misol:
```python
def create_books_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            published_year YEAR,
            genre VARCHAR(100),
            price FLOAT,
            available BOOLEAN
        )
    """)
```

---

### **2. Foydalanuvchidan ma'lumot kiritish**
#### Funksiya deklaratsiyasi:
```python
def insert_book(cursor, title, author, published_year, genre, price, available):
    """
    Insert a new book into the 'books' table.
    """
```

#### Nima qilish kerak:
1. Foydalanuvchidan interaktiv tarzda kitob ma’lumotlarini so‘rang.
2. Ma’lumotlarni tekshirib, `books` jadvaliga qo‘shing.

#### Misol:
```python
def insert_book(cursor, title, author, published_year, genre, price, available):
    query = """
    INSERT INTO books (title, author, published_year, genre, price, available)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (title, author, published_year, genre, price, available))
```

---

### **3. Barcha kitoblarni ko'rsatish**
#### Funksiya deklaratsiyasi:
```python
def show_all_books(cursor):
    """
    Retrieve and display all books from the 'books' table.
    """
```

#### Nima qilish kerak:
1. `SELECT * FROM books` so‘rovini bajarib, barcha ma’lumotlarni olib keling.
2. Natijalarni formatlab konsolda chiqaring.

#### Misol:
```python
def show_all_books(cursor):
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    for book in books:
        print(book)
```

---

### **4. Ma'lum bir shart bo'yicha qidiruv**
#### Funksiya deklaratsiyasi:
```python
def search_books_by_author_or_genre(cursor, search_type, search_value):
    """
    Search for books by author or genre.
    """
```

#### Nima qilish kerak:
1. Foydalanuvchidan qidiruv turini (`author` yoki `genre`) va qiymatini so‘rang.
2. Mos keluvchi ma’lumotlarni olib keling va chiqaring.

#### Misol:
```python
def search_books_by_author_or_genre(cursor, search_type, search_value):
    query = f"SELECT * FROM books WHERE {search_type} = %s"
    cursor.execute(query, (search_value,))
    results = cursor.fetchall()
    for book in results:
        print(book)
```

---

### **5. Kitob narxini yangilash**
#### Funksiya deklaratsiyasi:
```python
def update_book_price(cursor, book_id, new_price):
    """
    Update the price of a specific book.
    """
```

#### Nima qilish kerak:
1. Foydalanuvchidan kitob `id`si va yangi narxni so‘rang.
2. Kitob narxini yangilang.

#### Misol:
```python
def update_book_price(cursor, book_id, new_price):
    query = "UPDATE books SET price = %s WHERE id = %s"
    cursor.execute(query, (new_price, book_id))
```

---

### **6. Kitob mavjudligini o'zgartirish**
#### Funksiya deklaratsiyasi:
```python
def update_book_availability(cursor, book_id, available):
    """
    Update the availability of a specific book.
    """
```

#### Nima qilish kerak:
1. Foydalanuvchidan kitob `id`si va mavjudlik holatini (`True/False`) so‘rang.
2. Ma’lumotni jadvalda yangilang.

#### Misol:
```python
def update_book_availability(cursor, book_id, available):
    query = "UPDATE books SET available = %s WHERE id = %s"
    cursor.execute(query, (available, book_id))
```

---

### **7. Kitobni o'chirish**
#### Funksiya deklaratsiyasi:
```python
def delete_book(cursor, book_id):
    """
    Delete a specific book from the 'books' table.
    """
```

#### Nima qilish kerak:
1. Foydalanuvchidan o‘chirilishi kerak bo‘lgan kitob `id`si so‘raladi.
2. Kitob jadvaldan o‘chirib tashlanadi.

#### Misol:
```python
def delete_book(cursor, book_id):
    query = "DELETE FROM books WHERE id = %s"
    cursor.execute(query, (book_id,))
```

---

### **8. Yil bo'yicha saralash**
#### Funksiya deklaratsiyasi:
```python
def sort_books_by_year(cursor, order="ASC"):
    """
    Retrieve books sorted by published year.
    """
```

#### Nima qilish kerak:
1. Foydalanuvchidan tartibni (`ASC` yoki `DESC`) so‘rang.
2. Kitoblarni yil bo‘yicha tartiblang va chiqaring.

#### Misol:
```python
def sort_books_by_year(cursor, order="ASC"):
    query = f"SELECT * FROM books ORDER BY published_year {order}"
    cursor.execute(query)
    books = cursor.fetchall()
    for book in books:
        print(book)
```

---

### **9. Jami kitoblar sonini chiqarish**
#### Funksiya deklaratsiyasi:
```python
def count_books(cursor):
    """
    Count the total number of books in the 'books' table.
    """
```

#### Nima qilish kerak:
1. `COUNT` funksiyasidan foydalanib, kitoblar sonini hisoblang.
2. Natijani foydalanuvchiga ko‘rsating.

#### Misol:
```python
def count_books(cursor):
    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]
    print(f"Total books: {count}")
```

---

### **10. Narx bo'yicha statistikani chiqarish**
#### Funksiya deklaratsiyasi:
```python
def price_statistics(cursor):
    """
    Display min, max, and average price of books.
    """
```

#### Nima qilish kerak:
1. `MIN`, `MAX`, va `AVG` funksiyalaridan foydalanib, statistikani oling.
2. Foydalanuvchiga chiqaring.

#### Misol:
```python
def price_statistics(cursor):
    cursor.execute("SELECT MIN(price), MAX(price), AVG(price) FROM books")
    min_price, max_price, avg_price = cursor.fetchone()
    print(f"Min Price: {min_price}, Max Price: {max_price}, Avg Price: {avg_price:.2f}")
```

---
