from bank import Bank
class Admin:
    def __init__(self,bank):
        self.admin_bank=bank
    def check_account(self,holder_name):
        account = self.admin_bank.visible_individual_account(holder_name)
        if account:
            return account.get_holder_info_details()
        else:
            return f"Account not found."
    def check_all_account(self):
        self.admin_bank.visible_all_available_account()

    def check_total_loan_given(self):
        total=0
        for account in self.admin_bank.visible_all_available_account:
            total+= account.total_loan
        return total
    def check_bank_balance(self):
        total_balance=0
        for account in self.admin_bank.visible_all_available_account:
            total_balance+=account.current_balance
        return total_balance
    
    def feature_loan(self):
        if self.admin_bank.loan_feature_available==True:
            self.admin_bank.loan_feature_available=False
        else:
            self.admin_bank.loan_feature_available=True

        return self.admin_bank.loan_feature_available