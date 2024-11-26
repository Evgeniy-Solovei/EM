from database import Database
from book import Book


class Library:
    """
        Класс для управления библиотекой книг.
        :param database (Database): Объект класса Database для работы с БД>.
        :param next_id (int): Следующий id для новой книги.
    """
    def __init__(self):
        self.database = Database()
        self.next_id = len(self.database.books) + 1

    def add_book(self, title: str, author: str, year: int) -> None:
        """
            Добавляет новую книгу в библиотеку.
            :param title: Название книги.
            :param author: Автор книги.
            :param year: Год издания книги.
        """
        new_book = Book(book_id=self.next_id, title=title, author=author, year=year)
        self.database.add_book(new_book)
        self.next_id += 1

    def remove_book(self, book_id: int) -> None:
        """
            Удаляет книгу из БД по id.
            :param book_id: Id книги для удаления.
        """
        try:
            self.database.remove_book(book_id)
            print(f"Книга с ID {book_id} была успешно удалена.")
        except ValueError as e:
            print(e)

    def find_books(self, title: str = None, author: str = None, year: int = None) -> list[Book]:
        """
        Ищет книги по переданным параметрам.
        :param title: Название книги (по умолчанию None).
        :param author: Автор книги (по умолчанию None).
        :param year: Год издания книги (по умолчанию None).
        :return: Список найденных книг.
        """
        results = self.database.books
        if title:
            results = [book for book in results if title.lower() in book.title.lower()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        if year:
            results = [book for book in results if str(book.year).startswith(str(year))]
        return results

    def display_books(self) -> None:
        """
        Отображает все книги из БД.
        """
        if not self.database.books:
            print("Библиотека пуста.")
            return

        print("\nСписок всех книг:\n")
        for book in self.database.books:
            print(book)

    def update_status(self, book_id: int, new_status: str) -> None:
        """
        Изменяет статус книги по ее уникальному идентификатору.
        :param book_id: Уникальный идентификатор книги.
        :param new_status: Новый статус книги ("в наличии" или "выдана").
        """
        while True:
            if new_status in ["в наличии", "выдана"]:
                self.database.update_status(book_id, new_status)
                break
            else:
                print("Неверный статус книги.")
                new_status = input("Введите новый статус (в наличии/выдана) или нажмите 1 для выхода: ")
                if new_status == '1':
                    break
