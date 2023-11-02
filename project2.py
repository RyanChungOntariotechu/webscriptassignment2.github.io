#Ryan Chung #100867856

class BankAccount():
    def __init__(self):#init method
        self.__balance=0
        self.__transaction_history=[]
    
    def get_balance(self):#getting balance
        return self.__balance
    
    def set_balance(self,balance):#setting balance
        if not isinstance(balance,float) or balance <=0:
            raise ValueError('Error: Not greater than 0')
        else:
            self.__balance=balance
            
    def get_transaction_history(self):# getting transaction history
        return self.__transaction_history
    
    def set_transaction_history(self,amount):#setting transaction history
        self.__transaction_history.append(amount)
        
    def get_avg_transaction(self):#getting average transaction method
        if len(self.__transaction_history)==0:
            raise ValueError('Error: No transactions have been made')
        total=sum(self.__transaction_history)
        return total/len(self.__transaction_history)
    
    def deposit(self,amount):#Deposit method
        if(not isinstance(amount,float) and not isinstance (amount,int)) or amount <=0:
            raise ValueError('Error: Not greater than 0')
        else:
            self.__balance+=amount
            self.set_transaction_history(amount)
            
    def withdraw(self,amount): #Withdrawing method
        if (not isinstance(amount,float) and not isinstance(amount,int)) or amount <=0:
            raise ValueError('Error: Not greater than 0')
        else:
            self.__balance-=amount
            self.set_transaction_history(-amount)
            
def main():
    account = BankAccount()
    print("Creating bank account:")
    
    print("\nGetting average transaction(first time)")
    account.deposit(200)
    account.withdraw(100)
    print(account.get_avg_transaction())
    try:
        account.get_avg_transaction()

    except ValueError as v:
        print(v)
    try:
        print('\nDepositing money')
        account.deposit(-100)
    except ValueError as v:
        print(v)
    account.deposit(100)
    account.withdraw(50)
                    
    print("\nGetting the average transactions(second time)")
    print(account.get_avg_transaction())
    print("\nBalance:",account.get_balance())
    
main()

#End