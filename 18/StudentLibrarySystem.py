class Student:
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
    pass

if __name__=="__main__":
    pass