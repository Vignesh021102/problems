class Category:
    def __init__(self,name):
        self.ledger = []
        self.balance = 0
        self.category_name = name
        self.totalSpent = 0
    def check_funds(self,amount):
        if (amount != 0)&(amount <= self.balance):
            return True
        return False
    def deposit(self,amount,description= ""):
        if amount == 0:
            return False
        self.balance += amount
        self.ledger.append({"amount":amount,"description":description})

    def withdraw(self,amount,description= "withdraw"):
        if self.check_funds(amount):
            self.balance -= amount
            self.totalSpent+=amount
            self.ledger.append({"amount":(amount*-1),"description":description})

            return True
        return False
    def get_balance(self):
        return self.balance
    def transfer(self,amount,transTo):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {transTo.category_name}")
            transTo.deposit(amount,f"Transfer from {self.category_name}")
            return True
        return False
    def __repr__(self):
        text = []
        str = "*"*(30-len(self.category_name))
        text.append(str[:int(len(str)/2)]+self.category_name+str[int(len(str)/2):])
        for i in self.ledger:
            i['description'] = i['description'][:23]
            n = 30-(len("{:.2f}".format(i['amount']))+len(i['description']))
            text.append(f"{i['description']}{' '*n}"+"{:.2f}".format(i['amount']))
        text.append(f"Total: "+"{:0.2f}".format(self.balance))
        return "\n".join(text)
      
##
def create_spend_chart(categories):
    totalBudget = 0
    maxStrLen = 0
    text = []
    result = "Percentage spent by category"
    for i in categories:
        totalBudget += i.totalSpent
        maxStrLen = len(i.category_name) if maxStrLen < len(i.category_name) else maxStrLen

    for i in categories:
        n = int(i.totalSpent/(0.1*totalBudget))+1
        text.append(" "*(11-n)+"o"*n)

    for i in range(100,-10,-10):
        string = f"{' '*(3-len(str(i)))}{i}|"
        for j in text:
            string+=" "+j[10-int(i/10)]+" "
        result+= " \n"+string
    result += "\n"+" "*4+"-"*(3*len(categories)+1)
    for i in range(maxStrLen):
        string = " "*4
        for j in categories:
            j = j.category_name
            if i < len(j):
                string+=" "+j[i]+" "
            else:
                string+="   "
        result+="\n"+string+" "
    return result

entertainment = Category('Entertainment')
food = Category('Food')
business = Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(business, food, entertainment)
a = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
b = create_spend_chart([business,food,entertainment])
print(a)
print(b)
