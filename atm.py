class ATM:
    def __init__(self,account_no,pin,balance=0):
        self.account_no= account_no
        self.pin=pin
        self.balance=balance

    def credentials(self,account_no,pin):
        return self.account_no == account_no and self.pin == pin

    def check_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance= self.balance+amount
            print("The amount deposited is ",amount,"The updated balance is ",self.balance) 
        else:
            print("Enter valid amount")

    def withdraw(self,amount):
        if amount <= 0:
            print("Enter valid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else :
            self.balance = self.balance-amount
            print("Balance remaining is ",self.balance)

def main():
    atm = ATM(1234,4321,1000)
    account_no = int(input("Enter the account no: "))
    pin = int(input("Enter the pin: "))
    if atm.credentials(account_no,pin):
        print("Valid credentials")
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                print("The balance is: ",atm.check_balance())
            elif choice == '2':
                amount = float(input("Enter the amount to be deposited: "))
                atm.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter the amount to be withdrawn: "))
                atm.withdraw(amount)
            elif choice == '4':
                print("Thank you for banking with us")
                break
            else:
                print("Invalid choice. Try again!")

    else:
        print("Incorrect credatials")

main()
    



        

