from django.test import TestCase 

from models.account import Account

class AccountClassTest(TestCase): 

    # Account Fields 
    #

    def setUp(self) -> None:

        self.account_data = {
            'id': 1, 
            'currency_id': 1, 
            'balance':  0.0, 
            'locked': False, 

        }
        user_account = Account.objects.create(self.account_data)
        return super().setUp()  
        

    # We don't need this method
    def test_return_json_object(self): 
        account_data = self.account_data 


    def test_add_balance(self): 
        user_data = {
            'id': 1, 
            'currency_id': 1, 
            'balance': 0.0, 
            'locked': 0.0
        }
        amount = 100.0 
        current_balance = Account.objects.get(id=user_data['id']).balance 
        new_balance = current_balance + amount 
        Account.objects.get(id=user_data['id']).balance = new_balance
        Account.save()  
        updated_balance = Account.objects.get(id=user_data['id']).balance
        self.assertEqual(updated_balance, amount)

    def test_attributes_after_add_funds(self): 
        user_data = {
            'id': 1, 
            'currency_id': 1, 
            'balance': 0.0, 
            'locked': 0.0
        }
        amount = 100.0  
        expected_locked = 100.0
        current_locked = Account.objects.get(id=user_data['id']).locked 
        new_locked = amount + current_locked 
        Account.objects.get(id=user_data['id']).locked = new_locked 
        Account.save() 
        updated_locked = Account.objects.get(id=user_data['id']).locked 
        self.assertEqual(updated_locked, expected_locked)

    def test_plus_locked_funds(self): 
        pass 