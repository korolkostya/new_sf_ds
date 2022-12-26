
class SalesReport():  
    def __init__(self, employee_name):  
        self.deals = []  
        self.employee_name = employee_name  
      
    def add_deal(self, company, amount):   
        self.deals.append({'company': company, 'amount': amount})  
          
    def total_amount(self):  
        return sum([deal['amount'] for deal in self.deals])  
      
    def average_deal(self):  
        return self.total_amount()/len(self.deals)  
      
    def all_companies(self):  
        return list(set([deal['company'] for deal in self.deals]))  
      
    def print_report(self):  
        print("Employee: ", self.employee_name)  
        print("Total sales:", self.total_amount())  
        print("Average sales:", self.average_deal())  
        print("Companies:", self.all_companies())  
      
      
report = SalesReport("Ivan Semenov")  
  
report.add_deal("PepsiCo", 120_000)  
report.add_deal("SkyEng", 250_000)  
report.add_deal("PepsiCo", 20_000)  
  
report.print_report()  
# => Employee:  Ivan Semenov  
# Total sales: 390000  
# Average sales: 130000.0  
# Companies: ['PepsiCo', 'SkyEng'] 

#Задание 5.1
class User():
    def __init__(self, email, password, balance=0):
        self.email = email
        self.password = password
        self.balance = balance
    
    def login(self, email, password):
        if self.email == email and self.password == password:
            return True
        else:
            return False
    def update_balance(self, amount):
        self.balance += amount

#Задание 5.2
class IntDataFrame():
    def __init__(self, column):
        self.column=column
        self.to_int()
        
    def to_int(self):
        self.column=[int(value) for value in self.column]
    
    def count(self):
        j=0
        for i, value in enumerate(self.column):
            if value>0:
                j+=1
        return j
    
    def unique(self):
        uniq=[]
        for i, value in enumerate(self.column):
            if value in uniq:
                continue
            else:
                uniq.append(value)
        return len(uniq)

#Задание 5.3
