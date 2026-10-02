from abc import ABC, abstractmethod


class MediaItem(ABC):
    def __init__(self, title: str, year: int):
        self.__title = title
        self.__year = year

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if year < 0:
            raise ValueError("Year cannot be negative")
        self.__year = year

    @abstractmethod
    def get_description(self):
        pass


class Book(MediaItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.__author = author

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_description(self):
        return f"Book: {self.get_title()}, Year: {self.get_year()}, Author: {self.__author}"


class Movie(MediaItem):
    def __init__(self, title, year, director):
        super().__init__(title, year)
        self.__director = director

    def get_director(self):
        return self.__director

    def set_director(self, director):
        self.__director = director

    def get_description(self):
        return f"Movie: {self.get_title()}, Year: {self.get_year()}, Director: {self.__director}"


class Song(MediaItem):
    def __init__(self, title, year, artist):
        super().__init__(title, year)
        self.__artist = artist

    def get_artist(self):
        return self.__artist

    def set_artist(self, artist):
        self.__artist = artist

    def get_description(self):
        return f"Song: {self.get_title()}, Year: {self.get_year()}, Artist: {self.__artist}"


class MediaLibrary:
    def print_all_descriptions(self, items):
        for item in items:
            print(item.get_description())


items = [
    Book("Python Basics", 2024, "James"),
    Movie("Inception", 2010, "Christopher Nolan"),
    Song("Imagine", 1971, "John Lennon")
]

library = MediaLibrary()
library.print_all_descriptions(items)