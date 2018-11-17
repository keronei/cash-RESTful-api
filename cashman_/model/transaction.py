import datetime as dt
from marshmallow import Schema,fields

class Transaction():
    def __init__(self,desc,amount,type):
        self.desc = desc
        self.amount = amount
        self.created_at = dt.datetime.now(tz = None)
        self.type = type
        
        
    def __repr__(self):
        return '<Transaction(name={self.desc!r})>'.format(self = self)
    
    
class TransactionSchema(Schema):
    desc = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()