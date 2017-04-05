class Number:
    def __init__(self,x,y,number):
   	 self.x = x
   	 self.y = y
   	 self.number = number

    def move(self,x,y):
   	 self.x = x
   	 self.y = y
   	 return(x,y)
    


    def __str__(self):
   	 return ("x="+str(self.x)+",y="+str(self.y))

