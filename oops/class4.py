class customer:
    def __init__(self, custID, custName):
        self.custID = custID
        self.__custName = custName
    def display(self):
        print(f"customer Id {self.custID} customer name is {self.__custName}") #custname is a private attribute 
c1 = customer(101,"IBM")
c1.display()
#print(c1.__custName) #Accessing private variable encounters a error