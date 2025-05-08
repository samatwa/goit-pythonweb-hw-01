from abc import ABC, abstractmethod
import logging
from typing import List

# Налаштування логування
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("library.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


# SRP: Клас, який представляє одну книгу
class Book:
    """Клас для представлення книги."""

    def __init__(self, title: str, author: str, year: str) -> None:
        """Ініціалізація книги з назвою, автором та роком видання."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        """Повертає рядкове представлення книги."""
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP: Інтерфейс для бібліотеки
class LibraryInterface(ABC):
    """Інтерфейс для бібліотеки."""

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """Додати книгу до бібліотеки."""
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """Видалити книгу з бібліотеки за назвою."""
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        """Отримати список книг у бібліотеці."""
        pass


# OCP + LSP: Реалізація інтерфейсу бібліотеки
class Library(LibraryInterface):
    """Клас для бібліотеки, що реалізує інтерфейс LibraryInterface."""

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Додає книгу до бібліотеки."""
        self.books.append(book)
        logger.info("Book '%s' added to the library.", book.title)

    def remove_book(self, title: str) -> None:
        """Видаляє книгу з бібліотеки за назвою."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info("Book '%s' removed from the library.", title)
                return
        logger.info("Book '%s' not found in the library.", title)

    def get_books(self) -> List[Book]:
        """Повертає список книг у бібліотеці."""
        return self.books


# DIP: Менеджер працює через інтерфейс LibraryInterface
class LibraryManager:
    """Клас для управління бібліотекою."""

    def __init__(self, library: LibraryInterface):
        """Ініціалізація менеджера бібліотеки з конкретною бібліотекою."""
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        """Додає книгу до бібліотеки."""
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        """Видаляє книгу з бібліотеки за назвою."""
        self.library.remove_book(title)

    def show_books(self) -> None:
        """Виводить список книг у бібліотеці."""
        books = self.library.get_books()
        if books:
            logger.info("Books in the library:")
            for book in books:
                logger.info(str(book))
        else:
            logger.info("No books in the library.")


# Інтерфейс користувача
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logger.info("Exiting program.")
                break
            case _:
                logger.warning("Invalid command: %s", command)
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
