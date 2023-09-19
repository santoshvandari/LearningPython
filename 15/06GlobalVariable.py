a=100
def function():
    global a
    print(a)
    a=50
    print(a)
function()
print(a)