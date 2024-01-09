class BankAccount():
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    def deposit(self,x):
        self.balance=self.balance+x
        print(self.balance)
    def withdraw(self,y):
        if self.balance-y>=0:
            self.balance=self.balance-y
            print(self.balance)
        else:
            print('your withdrawl amount exceeds your total bank balance')
            print('withdrawl failed')
    def view(self):
        print('your name:',self.name)
        print('your account number:',self.number)
        print('your account balance:',self.balance)
while(1):
    try:
        name=input('Enter your name: ')
        number=int(input('Enter your account number: '))
        balance=int(input('enter the balance: '))
        if balance <0:
            print("balance should be greater than or equal to zero")
        else:
            break
    except:
        print("INVALID INPUT TRY AGAIN")
ac=BankAccount(name,number,balance)
val=0
s=''
while(1):
    choice=input('----press 1 to deposit----press 2 to withdraw----press 3 to view your account----type "logout" to logout----: ')
    if choice=='1':
        val=int(input('enter the amount u want to deposit: '))
        ac.deposit(val)
    elif choice=='2':
        val=int(input('enter the amount u want to withdraw: '))
        ac.withdraw(val)
    elif choice=='3':
        ac.view()
    elif choice=='logout':
        print('logging out')
        exit()
    else:
        print('INVALID INPUT')
            