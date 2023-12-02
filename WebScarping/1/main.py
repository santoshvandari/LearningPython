class Hello:
    def __init__(self,msg):
        print(msg)
        self.name = msg
    def Greet(self):
        print(self.name)

msg=Hello("Hello Santosh")
msg.Greet()