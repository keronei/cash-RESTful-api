from flask import Flask,request,jsonify
from cashman_.model.expense import Expense,ExpenseSchema
from cashman_.model.income import IncomeSchema,Income
from cashman_.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
    Income('Salo',12000),
    Income('Benefits',5050),
    Expense('Entertainment',1000),
    Expense('Date',1200)
]

#exposed endpoints from here...
@app.route('/incomes')
def get_incomes():
    schema = IncomeSchema(many = True)
    
    incomes = schema.dump(
        
        filter(lambda  t: t.type == TransactionType.INCOME,transactions)
        
        )
    return jsonify(incomes.data)


@app.route('/incomes',methods = ['POST'])
def add_income():
   income = IncomeSchema().load(request.get_json())
   transactions.append(income.data)
   
   return '',204

@app.route('/expenses')
def get_expenses():
    schema = ExpenseSchema(many = True)
    
    expenses = schema.dump(
        
        filter(lambda d: d.type ==TransactionType.EXPENSE,transactions)
    )
   
    return jsonify(expenses.data)

@app.route('/expenses',methods = ['POST'])
def add_expense():
    expense = ExpenseSchema().load(request.get_json())
    
    transactions.append(expense.data)
    
    return '',204


if __name__ == '__main__':
    app.run(debug = True)