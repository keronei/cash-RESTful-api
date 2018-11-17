from marshmallow import post_load
from .transaction import Transaction,TransactionSchema
from .transaction_type import TransactionType

class Expense(Transaction):
    def __init__(self,desc,amount):
        super(Expense,self).__init__(desc,-abs(amount),TransactionType.EXPENSE)
        
    def __repr__(self):
        return 'Expense( name = {self.desc!r})>'.format(self = self)
    
class ExpenseSchema(TransactionSchema):
    @post_load
    def make_expense(self,data):
        return Expense(**data)