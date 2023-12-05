class Account:
    def __init__(self,holder_name):
        self.holder_name=holder_name
        self.current_balance=0
        self.total_loan=0
        self.transactions_history=[]
    def deposit(self,amount):
        if amount>=100:
            self.current_balance+=amount
            self.transactions_history.append(f'Total amount:{amount} taka has been deposit of your bank account.')
            print(f'Total {amount} taka has been deposit of your bank account.Now your new balance is:{self.current_balance}')
        else:
            print('Bank can not access deposit less than 100 taka.')
    def withdarw(self,amount):
        if  amount>0 and amount<self.current_balance and self.current_balance-amount>=500:
            self.current_balance-=amount
            self.transactions_history.append(f'{amount} taka withdraw from your bank account')
            print(f'Congretes!{amount} taka withdraw from your bank account successfully done.Now your new balance is:{self.current_balance}')
        else:
            print('Your account have not sufficient money for withdaw.Your account balance remains at least 500 taka.')    
    def get_balance(self):
        return self.current_balance
    def transfer_balance(self,amount,client):
        if amount>0 and amount<self.current_balance and self.current_balance-amount>=500:
            self.current_balance-=amount
            self.transactions_history.append(f'{amount} taka has been transfered to {client.holder_name}')
            print(f'Now,new balance of your bank account is:{self.current_balance}')
            client.current_balance+=amount
            client.transactions_history.append(f'{amount} taka is added on your bank account from {self.holder_name}')
        else:
            print('You have not suffcient balance to transfer balance')
    def get_loan(self,amount):
         maximum_loan=2*self.current_balance
         if  amount<=maximum_loan:
             self.total_loan=amount
             self.current_balance+=amount
             self.transactions_history.append(f'You have taken {amount} taka loan successfully.Now,your new balance of your account is:{self.current_balance} and you need pay load is:{self.total_loan}')
         else:
             print(f'You can take loan atmost {maximum_loan} taka')
    def payment_loan(self,amount):
        if amount>0:
            self.total_loan-=amount
            self.current_balance-=amount
            self.transactions_history.append(f'You have paid {amount} taka.Now,you have ramain loan is:{self.total_loan}')
        else:
            print('Please enter a valid amount for pay loan.') 
    def check_transations_history(self):
        return self.transactions_history
    def get_holder_info_details(self):
        bank_info=[]
        bank_info.append(f'Account Holder Name:{self.holder_name}')
        bank_info.append(f'Account balance:{self.current_balance}')
        bank_info.append(f'Total loan:{self.total_loan}')
        return bank_info
    
    
           
    
                          
       
    