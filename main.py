from library import Library


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите номер действие: ")

        if choice == '1':
            title = input("\nВведите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            library.add_book(title, author, year)

        elif choice == '2':
            book_id = int(input("\nВведите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == '3':
            while True:
                print("\nИскать по:")
                print("1. Названию (title)")
                print("2. Автору (author)")
                print("3. Году издания (year)")
                print("4. Вернуться в главное меню")

                search_choice = input("Введите номер для выбора критерия поиска: ")
                if search_choice == '1':
                    search_type = 'title'
                elif search_choice == '2':
                    search_type = 'author'
                elif search_choice == '3':
                    search_type = 'year'
                elif search_choice == '4':
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")
                    continue
                search_value = input(f"Введите значение для поиска по {search_type}: ")
                results = library.find_books(**{search_type: search_value})
                if results:
                    for book in results:
                        print(book)
                else:
                    print("Книги не найдены.")

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            while True:
                try:
                    book_id = int(input("\nВведите ID книги для изменения статуса: "))
                    break
                except ValueError:
                    print("Пожалуйста, введите целое число.")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, new_status)

        elif choice == '6':
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

        continue_choice = input("\nХотите продолжить? (да/нет): ").strip().lower()
        if continue_choice != 'да':
            print("До свидания, возвращайтесь в нашу библиотеку!!!")
            break


if __name__ == "__main__":
    main()
