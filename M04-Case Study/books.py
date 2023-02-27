class Book:
    def __init__(self, title, author, genre, pub):
        self.title = title
        self.author = author
        self.genre = genre
        self.pub = pub

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title)



