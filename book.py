class Book:
    """
        Класс для представления книги в библиотеке.
        :param book_id: Уникальный идентификатор книги.
        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        :param status: Статус книги
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "В наличии"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self) -> str:
        return f"№{self.book_id}:\n Книга: {self.title}\n Автор: {self.author}\n Год выпуска: ({self.year})\n Статус: {self.status}."

