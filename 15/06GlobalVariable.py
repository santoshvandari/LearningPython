a=100
b=50
def function():
    global a
    # if we use global keyword then it will access a global variable which was already created.
    # IF we don't use Global keyword then it will create new local variable
    print(a)
    a=50
    b=10
    print(a)
    print(b)
function()
print(a)
print(b)