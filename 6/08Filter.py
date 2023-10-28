# spam=['make a lot of money',"buy now",'subscribe this',"click this"]
# cmt=input("Enter Your Comment: ")
# if(cmt in spam):
#     print("Your Comment is Spam")
# else:
#     print("Your comment is Fine.")

comment = input("Enter Your Comment: ")
if("make a lot of money" or "buy now" or "click this" or "subscribe this" in comment):
    print("Your Comment is Spam.")
else: 
    print("Your Comment is Fine")