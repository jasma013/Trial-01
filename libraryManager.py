#initiliaze empty list, set, and dictionary
books_list= []
authers_set=set()
books_dict= {}

# add books
books_list.append("Python programming")
authers_set.add("John Smith")
books_dict["Python programming"]= "John Smith"

books_list.append("Data Structures and Algorithms")
authers_set.add("Jane Doe")
books_dict["Data Structures and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning Basics")
authers_set.add("Alice Johnson")
books_dict["Machine Learning Basics"]= "Alice Johnson"

# Search for a book
search_title= input("Enter the title of book to search:")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found!")

# Display all books
print("List of books:") 
for book in books_list :
    print (book)

# Remove a book
remove_title= input("Enter the title of the book  to remove or else  enter to skip")
if remove_title in books_list:
    remove_auther= books_dict[remove_title]
    books_list.remove(remove_title)
    authers_set.remove(remove_auther)
    del books_dict [remove_title]
    print("Book removed succesfully!")
    print("Books available:", books_list)
else:
    print("Book not found!")

# Function to re-add a book
def readd_book(title, author):
    books_list.append(title)
    authors_set.add(author)
    books_dict[title] = author
    print("Book re-added successfully!")

