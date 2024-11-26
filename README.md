# Библиотека книг (Консольное приложение)


## Описание

Данное приложение предназначено для управления библиотекой книг.
Оно позволяет добавлять, удалять, искать, изменять статус и отображать список книг.

## Функционал

### 1. Добавление книги
- Пользователь вводит название, автора и год издания книги.
- Программа автоматически генерирует уникальный ID и добавляет книгу в библиотеку.

### 2. Удаление книги
- Удаление книги осуществляется по её ID.

### 3. Поиск книги
- Возможен поиск книг по названию, автору или году издания.

### 4. Отображение всех книг
- Программа выводит список всех книг с полями:
  - ID
  - Название
  - Автор
  - Год издания
  - Статус ("в наличии" или "выдана").

### 5. Изменение статуса книги
- Пользователь может изменить статус книги на "в наличии" или "выдана" по её ID.

## Хранение данных
- Все данные о книгах хранятся в формате JSON в файле `db_library.json`.

## Использование

### Установка
1. Убедитесь, что у вас установлен Python 3.12.
2. Скачайте код проекта.
3. Убедитесь, что файл `db_library.json` находится в корне проекта.

### Запуск
Запустите файл `main.py`:

```bash
python main.py