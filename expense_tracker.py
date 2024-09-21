from expenses import Expense
import calendar
import datetime

def main():
    print(f"Welcome to the RupeeBuddy 🤑")
    expense_file_path="expenses.csv"
    budget=3000
    #Ask user to input their expense
    expense=get_user_expenses()

    #Write their expenses in the file
    save_expenses_to_file(expense,expense_file_path)

    #Read the file  and summarize the expenses
    summarize_expenses(expense_file_path,budget)
    

def get_user_expenses():
    print(f"🎯Ready To Enter your Expenses")
    expense_name=input("Enter expense name: ")
    expense_amount=float(input("Enter expense amount: "))
    print(f"You've entered {expense_name},{expense_amount}")

    Expense_categories=["🍛Food","🧳Travel","🎉Fun","📒Stationery","🤷Misc"]
    while True:
        print("Select the Category: ")
        for i,category_name in enumerate(Expense_categories):
            print(f"  {i+1}.{category_name}")
        
        value_range=f"[1-{len(Expense_categories)}]"
        try:
           selected_index=int(input(f"Enter a category number {value_range}: "))-1
           if selected_index in range(len(Expense_categories)):
            selected_category=Expense_categories[selected_index]
            new_expenses=Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expenses 
           else:
            print("Invalid category.Please try again!")
        except ValueError:
           print(f"Please enter the numeric value between 1-{len(Expense_categories )}")


def save_expenses_to_file(expense:Expense,expense_file_path):
    print(f"🎯Saving User Expenses: {expense} to {expense_file_path}")
    with open(expense_file_path,"a",encoding="utf-8") as f:
       f.write(f"{expense.name},{expense.amount},{expense.category}\n")
       




def summarize_expenses(expense_file_path,budget):
    print(f"Summarizing User Expense")
    expenses=[]
    with open(expense_file_path,"r",encoding="utf-8") as f:
       lines=f.readlines()
       for line in lines:
          expense_name,expense_amount,expense_category=line.strip().split(",")#unpacking
          line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
          expenses.append(line_expense)
    
    amount_by_category={}
    for expense in expenses:
       key=expense.category
       if key in amount_by_category:
          amount_by_category[key]+=expense.amount
       else:
          amount_by_category[key]=expense.amount
    print("Expenses By Category📝")
    for key,amount in amount_by_category.items():
       print(f" {key}: ₹{amount:.2f}")

    total_spent=sum([ex.amount for ex in expenses])
    print(f"💰You've spent ₹{total_spent:.2f} this month!")
    remaining_budget=budget-total_spent
    if remaining_budget>=0:
       print(f"🤑Remaining Amount= {remaining_budget:.2f}")

    #Now calculating the number of days left and the daily spending amount 
    now=datetime.datetime.now() #current date
    days_in_month=calendar.monthrange(now.year,now.month)[1]#no of days in current month
    remaining_days=days_in_month-now.day#remaining days in the current month
    print("Remaining days in the current month is : ",remaining_days)
    daily_budget=remaining_budget/remaining_days
    print(green(f"👉 Budget Per Days :₹{daily_budget:.2f}"))

def green(text):
   return f"\033[92m{text}\033[0m"
     
if __name__=="__main__":
    main()