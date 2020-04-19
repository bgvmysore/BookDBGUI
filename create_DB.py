import sqlite3

MyBookDB=sqlite3.connect('MyBookDB.db')
MyBookCurs=MyBookDB.cursor()
try:
    MyBookCurs.execute("""CREATE TABLE books (
    BookTitle TEXT (50) NOT NULL,
    BookAuth  TEXT (30),
    BookPrice INTEGER NOT NULL);""")
except:
    print("Books Table already exists in DB........")
    print("###############################################################")

dont_exit=True

while dont_exit:
    
    
    try:
        booktitle=input("Enter Book's Title: ")
        if booktitle=='':
            booktitle=None
        bookauth=input("Enter Author's name: ")
        bookprice=int(input("Enter Price of each book: "))
        MyBookCurs.execute("INSERT INTO books (BookTitle,BookAuth,BookPrice) VALUES (?,?,?);",(booktitle,bookauth,bookprice))
        MyBookDB.commit()
    except:
        print("###############################################################\nError Inserting the book into DB")
        MyBookDB.rollback()
    
    print("###############################################################")
    exit_str=input("Press Enter to Continue (or) Type 'x' to Quit :")
    if exit_str=="x":
        dont_exit=False
    print("###############################################################\n")
    
    
MyBookDB.close()
