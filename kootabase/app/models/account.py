import _thread


from django.db import models 
from django.core.serializers import serialize


class AccountError(Exception): 
    pass 

class Account(models.Model): 
    member_id = models.ForeignKey('Member', null=False, on_delete=models.CASCADE) 
    currency_id = models.ForeignKey('Currency', null=False, on_delete=models.DO_NOTHING) 
    balance = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False)
    locked = models.DecimalField(max_digits=32, decimal_places=16, default=0.0, null=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)


    def as_json_for_event_api(self): 
        """
        Returns a json object with the 
        account info"""
        data = serialize('json', self.objects.all(), fields=('member_id', 'currency_id',
        'balance', 'locked', 'created_at', 'updated_at')) 
        return data
        

    def add_funds(self, amount): 
        """
        Add amount to the account balance"""
        self._add_funds(self, amount)

    def _add_funds(self, amount): 
        # select the current usr account then 
        # add fund to it 
        #current_user = self.member_id
        lock = _thread.allocate_lock() 
        with lock: 
            self.attributes_after_add_funds(amount)
        

    def attributes_after_add_funds(self, amount : float) -> dict: 
        if amount <= 0: 
            raise AccountError(f"Cannot add funds (account id: {self.id}, amount: {amount}, balance {self.balance}).") 
        self.balance = self.balance + amount 
        self.save() 
    


    

    def add_locked_funds(self, amount): 
        self._add_locked_funds(amount)

    def _add_locked_funds(self, amount): 
        # make sure that the accounts are locked 
        # when updating the fields  
        # How to implement a lock in python 
        lock = _thread.allocate_lock()

        with lock: 
            self.attributes_after_add_funds(amount)


    def attributes_after_locked_funds(self, amount): 
        if amount <= 0: 
            raise AccountError(f"Cannot add funds to (account id: {self.member_id}, amount: {amount}, locked: {self.locked}).")

        self.locked = self.locked + amount 
        self.save()

    def sub_funds(self, amount): 
        lock = _thread.allocate_lock()  

        with lock: 
            self.attributes_after_sub_funds(amount) 

    def attributes_after_sub_funds(self, amount): 
        if amount <= 0 or amount > self.balance: 
            raise AccountError(f"Cannot subtract funds (account id: {self.id}, amount: {amount}, balance : {self.balance}).") 

        self.balance = self.balance - amount 
        self.save() 

    def lock_funds(self, amount): 
        lock = _thread.allocate_lock()
        with lock: 
            self.attributes_after_lock_funds(amount) 

    def attributes_after_lock_funds(self, amount): 
        if amount < 0 or amount > self.balance: 
            raise AccountError(f"cannot lock funds (account id: {self.id}, amount {amount}, balance {self.balance})., locked: {self.locked}") 
        
        self.balance = self.balance - amount 
        self.locked = self.locked + amount 
        self.save()

    def unlock_funds(self, amount): 
        lock = _thread.allocate_lock() 

        with lock: 
            self.attributes_after_unlock_funds(amount) 

    def attributes_after_unlock_funds(self, amount): 
        if amount < 0 or amount > self.locked: 
            raise AccountError(f"Cannot unlock funds (account id: {self.id}, amount: {amount}, balance: {self.balance}). locked: {self.locked}")

    def unlock_and_sub_funds(self, amount): 
        lock = _thread.allocate_lock() 

        with lock: 
            self.attributes_after_unlock_and_sub_funds(amount) 

    def attributes_after_unlock_and_sub_funds(self, amount): 
        if amount < 0 or amount > self.locked: 
            raise AccountError(f"Cannot unlock and sub funds (account id: {self.id}, amount: {amount}, balance: {self.balance}, locked: {self.locked}")
        
        self.locked = self.locked - amount 
        self.save()

    def amount(self): 
        total_balance = self.balance + self.locked 
        return total_balance