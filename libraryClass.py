class Book:
    def __init__(self,author,title):
        self.author = author
        self.title = title
    def display_info(self):
        return f"Book name: {self.title} and the author: {self.author}\n"
class library:
    def __init__(self,name = ""):
        self.name =name
    def add_book(self,book):
        with open("library.txt","a") as file:
            file.write(book.display_info())
    def remove_book(self):
        with open("library.txt","r") as file:
            data = file.readlines()
            ndata = [x for x in data if self.name not in x]
        with open("library.txt","w") as file:
            file.writelines(ndata)
    def sBook(self):
        with open("library.txt","r") as file:
            data = file.readlines()
            name = "".join([x for x in data if self.name in x])
            return name
    def showBooks(self):
        with open("library.txt","r") as file:
            return file.read()