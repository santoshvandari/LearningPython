spam=['make a lot of money',"buy now",'subscribe this',"click this"]
cmt=input("Enter Your Comment: ")
if(cmt in spam):
    print("Your Comment is Spam")
else:
    print("Your comment is Fine.")