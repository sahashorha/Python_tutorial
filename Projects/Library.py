# Add a book -> Title , author , copies
# View all book -> Display stored catalog
# Issue book -> Reduce book count when borrowed
# Return Book -> Increase book count
# Remove a book -> Delete book from library
# Save Data -> Store dertails in file so nothing is lost

# We can store the data in format of list where id, title, author, copies


import json;
import os

FILE = "database.json"

# --------Load Data from File ------------#
def load_data():
      if not os.path.exists(FILE):
            return []
      with open(FILE, "r") as f:
            return json.load(f)
      
# -------- Save Data to File --------------
def save_data(books):
      with open(FILE,"w") as f:
            json.dump(books, f, indent = 4)

#  ----------- Add Book ------------------

def add_book(books):
      title = input("Enter Book Title: ")
      author = input("Enter Author Name: ")
      copies = int(input("Enter Number of Copies: "))
      
      new_book = {
            "id" : len(books) + 1,
            "title" : title,
            "author":author,
            "copies":copies
      }
      books.append(new_book);
      save_data(books);
      print("\n Books Added Successfully \n")

#------------ View Book --------------------

def view_book(books):
      if not books:
            print("\n No Books is Available\n")
            return;
      print("\n Available Books \n");
      for book in books:
            print(f"ID: {book['id']} | Title: {book['title']} by {book['author']} | Copies: {book['copies']}")

# --------------- Issue Book ------------------------

def issue_book(books):
      book_id = int(input("Enter Book ID to Issue: "));
      cnt = 0;
      for book in books:
            if(book["id"] == book_id):
                  if book["copies"] > 0:
                        book["copies"] -=1
                        save_data(books)
                        print("\n Book Issued Successfully \n")
                  else:
                        print("\n No copies are available \n")
                  return;
            else:
                  # print("\n Book Id Not Found \n")
                  cnt+=1;
      if(cnt>=book_id):
               print("\n Book Id Not Found \n")

#------------------- Return book ----------------
def return_book(books):
      book_id = int(input("Enter the Id of the Book which you want to return: "))
      for book in books:
            if book["id"] == book_id:
                  book["copies"] +=1
                  save_data(books)
                  print("\n Book Return Successfully\n")
                  return
            else:
                  print("\n Book Id is not Available \n")
# ------------------ Remove Book ----------------
def remove_book(books):
      book_id = int(input("Enter the book id which you want to remove: "))
      for book in books:
            if book["id"] == book_id:
                  books.remove(book)
                  save_data(books)
                  print("\n Books Removed Successfully \n")
            print("\n Book Id Not Found \n")

#---------------------Main Program ---------------


def menu():
      books = load_data();
      while True:
            print("\n=========Library Management System ==========")
            print("1. Add Books")
            print("2. View Book")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Remove Book")
            print("6. Exit")

            choice = input("\nEnter Your Choice ")
            if(choice == "1"):
                  add_book(books);
            elif choice == "2":
                  view_book(books);
            elif choice == "3":
                  issue_book(books);
            elif choice == "4":
                  return_book(books);
            elif choice == "5":
                  remove_book(books);
            elif choice == "6":
                  print("\n Thank  You for using LMS! @Rahul Poddar \n")
            else:
                  print("\n Invalid Choice .. Try Again \n")
menu()

