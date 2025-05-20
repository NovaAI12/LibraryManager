import os 
import libraryClass as lb
os.chdir("libraryManager")
with open("library.txt","a") as file:
    pass
try:
    while True:
        print("""What would you like to do?:
              1- add book
              2- remove book
              3- show all books
              4- search for specific book
              5 - exit""")
        lbchoise = int(input("Enter yuor input(1,2,3,4,5): "))
        if lbchoise == 1:
            btitle = input("Enter the book title: ")
            bauthor = input("Enter the author name: ")
            book = lb.Book(bauthor,btitle)
            lb.library(name = btitle).add_book(book)
            print("Complete")
        elif lbchoise == 2:
            btitle = input("Enter the book title: ")
            lb.library(name=btitle).remove_book()
            print("Complete")
        elif lbchoise == 3:
            print(lb.library().showBooks())
        elif lbchoise == 4:
            btitle = input("Enter the book title: ")
            print(lb.library(name= btitle).sBook())
        elif lbchoise == 5:
            break
        else:
            print("Invalid input, please enter a correct input")
except ValueError:
    print("Invalid input, please enter a correct input")
finally:
    print("-----------------------------------------------")