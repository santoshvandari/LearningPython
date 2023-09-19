class Library:
    def __init__(self,books):
        self.books=books
    def DisplayAvailableBooks(self):
        print("The Available Books are: ")
        for i in self.books:
            print("\t - ",i)
    def IssueBook(self,BookName):
        if(BookName in self.books):
            self.books.remove(BookName)
            print(f"The {BookName} Book is Available and issued to You. Please Returned it in 30 Days.")
        else:
            print("Sorry!! The Book is Not Available. Please Try Again When it is available.")
    def ReturnBook(self,Bookname):
        self.books.append(Bookname)
        print("Thank You for Returning the Book. Hope You Enjoy the Books.")
class Student:
    def RequestBook(self):
        bookname=input("Enter a Book You want to Read: ")
        return bookname
    def ReturnBook(self):
        bookName=input("Enter a Book You want to Return: ")
        return bookName

if __name__=="__main__":
    bookList=["Python","Django","C","C++","Java","Rust"]
    library=Library(bookList)
    student=Student()
    while(True):
        welcomeMessage='''
        ====== Welcome to Library ======
        1. List all the Books
        2. Request a Book
        3. Add/Return a Book
        4. Exit
    '''
        print(welcomeMessage)
        try: 
            choice=int(input("Enter Your Choice(1,2,3,4): "))
            if choice==1:
                library.DisplayAvailableBooks()
            elif choice==2:
                library.IssueBook(student.RequestBook)
            elif choice==3:
                library.ReturnBook(student.ReturnBook)
            elif choice==4:
                print("Thank you For Using Library System.")
                exit()
            else:
                print("Invalid Entry!!")   
        except Exception as e:
            print("Invalid Entry: Error: ",e)
