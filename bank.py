from user import Account
class Bank:
    def __init__(self):
        self.available_accounts=[]
        self.loan_feature_available=True
    def create_new_bank_account(self,holder_name):
        account_name=Account(holder_name)
        self.available_accounts.append(account_name)
    def visible_all_available_account(self):
        for account in self.available_accounts:
            print(account)
    def visible_individual_account(self,holder_name):

        for account in self.available_accounts:
            
            if account.holder_name==holder_name:
                return account
           
        return None

    


