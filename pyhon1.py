class calculator:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def addition (self):
        result=self.x+self.y
        print(result)
    def multiplication (self):
        result=self.x*self.y
        print(result)
    def subtraction (self):
        result=self.x-self.y
        print(result)
    def division (self):
        result=self.x/self.y
        print(result)
c=calculator(500,1000)
c.addition()
c.multiplication()
c.subtraction()
c.division()
