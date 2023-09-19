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
            print(f"The {BookName} Book is Available and issued to You.")

class Student:
    pass

if __name__=="__main__":
    pass