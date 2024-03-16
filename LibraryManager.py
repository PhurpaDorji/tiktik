#Initialize empty lists, set, and dictionary
books_list = []
author_set = set()
books_dict = {}

#add books
books_list.append("Python Programming")
author_set.add("John Smith")
books_dict["Python Programming"] = "John Smith"

books_list.append("Data structures and Algorithums")
author_set.add("Jane Doe")
books_dict["Data structure and Algorithms"] = "Jone Doe"

books_list.append("Machines Learning Basics")
author_set.add("Alice Johnson")
books_dict["Machine Learning Basics"] = "Alice Johnson"

#search for a book
search_title = input("Enter the title of the books to search")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found")

#Display all books
print("list of books:")
for bok in books_list:
    print(Book)

#remove a book
remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove  (remove_title)
    author_set.remove(remove_author)
    del books_dict[remove_tilte]
    print("Books removed successfully!")
    print("Books available: ",books_list)
else:
    print("Book not found!")
