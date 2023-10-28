'''
Print the FOllowing Patterns

  *
 ***
*****

'''
for i in range(3):
    print(" " *(2-i),end="")
    print("*" *(2*i+1),end="")
    print(" " *(2-i))
