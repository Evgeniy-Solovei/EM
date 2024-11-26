import json
import os
from book import Book


class Database:
    """
        Класс для работы с базой данных книг.
        :param filename: Имя базы данных.
        :param books: Список книг.
    """
    def __init__(self, filename: str = 'db_library.json'):
        self.filename = filename
        self.books = []
        if os.path.exists(self.filename):
            self.load()

    def load(self) -> None:
        """
            Загружает данные из БД и создаёт список объектов книг.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.books = [Book(**data) for data in json.load(file)]

    def save(self) -> None:
        """
            Сохраняет данные в БД.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False)

    def add_book(self, book: Book) -> None:
        """
            Добавляет книгу в БД.
            :param book: Объект книги.
        """
        self.books.append(book)
        self.save()

    def remove_book(self, book_id: int) -> None:
        """
            Удаляет книгу из БД по ее id.
            :param book_id: Id книги для удаления.
            :raises ValueError: Если книга с данным id не найдена.
        """
        book_to_remove = next((book for book in self.books if book.book_id == book_id), None)
        if book_to_remove is None:
            raise ValueError(f"Книга с ID {book_id} не найдена.")
        self.books.remove(book_to_remove)
        self.save()

    def find_books(self, title: str = None, author: str = None, year: int = None) -> list[Book]:
        """
            Ищет книги по переданным параметрам.
            :param title: Название книги.
            :param author: Автор книги.
            :param year: Год издания книги.
            :return: Список найденных книг.
        """
        results = self.books
        for book in results:
            print(f"'{book.title}'")

        if title:
            title_words = title.lower().split()
            results = [book for book in results if any(word in book.title.lower() for word in title_words)]

        if author:
            author_words = author.lower().split()
            results = [book for book in results if any(word in book.author.lower() for word in author_words)]
        if year:
            year_str = str(year)
            results = [book for book in results if year_str in str(book.year)]
        return results

    def update_status(self, book_id: int, new_status: str) -> None:
        """
            Обновляет статус книги по ID.
             :param book_id: ID книги.
             :param new_status: Новый статус книги.
         """
        for book in self.books:
            if book.book_id == book_id:
                book.status = new_status
                break
        self.save()

