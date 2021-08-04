class Employee:
   def __init__(self,name, position, gross_salary, children):
       self.name = name
       self.position = position
       self.gross_salary = gross_salary
       self.children = children

   def get_info(self):
       return f"{self.name} pracuje na pozícii {self.position}."
   def get_net_salary(self):
       tax = self.gross_salary * 0.15 - self.children * 1500
       return self.gross_salary - tax

zam1 = Employee("Maria Nova","recepčná",30000,2)
print(zam1.get_info())
print(zam1.get_net_salary())
