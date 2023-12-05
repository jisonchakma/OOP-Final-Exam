from bank import Bank
from admin import Admin
def main():
    b=Bank()
    admin=Admin(b)
    #create a bank account
    b.create_new_bank_account('Karim')
    account1=b.visible_individual_account('Karim')
    #deposit money to account1
    account1.deposit(200000)
    # print(account1.get_balance())
    account1.withdarw(300)
    # print(account1.get_balance())
    # print(account1.get_holder_info_details())
    account1.get_loan(3000)
    # print(account1.get_balance())
    # print(account1.get_holder_info_details())
    # print(account1.check_transations_history())
    account1.payment_loan(2000)
    print(account1.get_holder_info_details())
    
    #create another holder account
    b.create_new_bank_account('Rahim')
    #check number of user accounts
    print(len(b.available_accounts))
    account2=b.visible_individual_account('Rahim')
    print(account2)
    #deposit money from account2
    account2.deposit(10000)
    #check balance in the account
    print(account2.get_balance())
    print(account2.get_holder_info_details())
    #transfer money from account1 to account2
    server_account=b.visible_individual_account('Rahim')
    client_account=b.visible_individual_account('Karim')
    client_account.transfer_balance(1000,server_account)
    print(account1.get_balance())
    print(account2.get_balance())
__name__=='__main__'
main()