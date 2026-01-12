class Book:
    def __init__(self,title, author):
        self.title=title
        self.author=author

library = []
for i in range(500):
    author_1=Book(f"название_{i}", f"автор_{i}")
    library.append(author_1)
print(library)