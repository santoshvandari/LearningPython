a=100
def function():
    global a
    # if we use global keyword then it will access a global variable which was already created.
    # IF we don't use Global keyword then it will create new local variable
    print(a)
    a=50
    print(a)
function()
print(a)