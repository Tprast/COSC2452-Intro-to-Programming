import sys

class Expense():
    date="YYYY-MM-DD"
    name=None
    Amount=0

expenses=[]

def add_expense(expense_date,expense_name,expense_amount):
    expense=Expense()
    expense.date=expense_date
    expense.name=expense_name
    expense.amount=expense_amount
    expenses.append(expense)

def save_data():
    try:
        file_object=open("expenses.csv","w")
        num_expenses=len(expenses)
        i=0
        while(i<num_expenses):
            file_object.write(expenses[i].date+","+expenses[i].name+","+str(expenses[i].amount)+"\n")
            i+=1
        file_object.close()
    except:
        sys.stdout.write("Could not save to file")
    
def find_expenses():
    sys.stdout.write("-------------\n")
    sys.stdout.write("Find expenses\n")
    sys.stdout.write("-------------\n")
    if (len(expenses)<=0):
        sys.stdout.write("No expenses to find. Try adding expenses first...\n");
        return

    sys.stdout.write("Enter Partial expense name to find: ")
    sys.stdout.flush()
    search_target=sys.stdin.readline().strip()
    sys.stdout.write("\n")

    dates_width=11
    names_width=20
    amounts_width=10

    column_format="{:<"+str(dates_width)+"}{:<"+str(names_width)+"}{:>"+str(amounts_width)+"}\n"

    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)
    row_text=column_format.format("Date","Name","Amount $")
    sys.stdout.write(row_text)
    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)

    matches=0
    total_amount=0
    num_expenses=len(expenses)
    i=0
    while(i<num_expenses):
        if (search_target in expenses[i].name):
            row_text=column_format.format(expenses[i].date,expenses[i].name,expenses[i].amount)
            total_amount+=expenses[i].amount
            matches+=1;
            sys.stdout.write(row_text)
        i+=1

    sys.stdout.write("\nYou've spent $"+str(total_amount)+" on "+str(matches)+" matches\n")
        

#------------------------------------------------------------------------------
#The code below this point remains unchanged from expense_manager.pdf
#from week 5.

#expense_dates=[]
#expense_names=[]
#expense_amounts=[]

def run_expenses_manager():
    load_data()
    choice=get_menu_choice()
    while(choice!='X'):
        sys.stdout.write("\n")
        if choice=="a":
            add_expense_via_menu()
        elif choice=="r":
            remove_expense()
        elif choice=="f":
            find_expenses()
        choice=get_menu_choice()
    save_data()

def get_str(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    value=sys.stdin.readline().strip()
    while(len(value)==0):
        sys.stdout.write("Input cannot be blank. Re-enter:")
        sys.stdout.flush()
        value_sys.stdin.readline().strip()

    return value

def get_float(prompt):
    value=None
    while(value==None):
        try:
            value=float(get_str(prompt))
        except:
            prompt="That wasn't right. Re-Enter: "    
    return value

def get_positive_float(prompt):
    value=get_float(prompt)
    while(value<0):
        value=get_float("Input must be positive. Re-enter: ")
    return value

def get_menu_choice():
    menu="\n========================\n"
    menu+="Expenses Manager v1.0\n"
    menu+="=========================\n"
    menu+="[A]dd an expense\n"
    menu+="[R]emove an expense\n"
    menu+="[F]ind expenses\n"
    menu+="E[X]it\n"

    sys.stdout.write(menu)

    menu=menu.lower()
    choice=get_str("Enter Choice: ").lower()
    while not "["+choice+"]" in menu:
        choice=get_str(choice+" was an invalid choice! Re-enter: ").lower()

    return choice

def load_data():
    with open ("expenses.csv","r") as file_object:
        for line in file_object:
            fields=line.split(",")
            expenses_date=fields[0]
            expenses_name=fields[1]
            expenses_amount=float(fields[2])
            add_expense(expenses_date,expenses_name,expenses_amount)



def add_expense_via_menu():
    sys.stdout.write("--------------\n")
    sys.stdout.write("Add an expense\n")
    sys.stdout.write("--------------\n")

    expenses_date=get_str("Enter expense date as YYYY-MM-DD: ")
    sys.stdout.write("\n")
    expense_name=get_str("Enter expense name: ")
    expense_amount=get_positive_float("Enter expense amount: ")
    sys.stdout.write("\n")

    add_expense(expenses_date,expense_name,expense_amount)

def remove_expense():
    sys.stdout.write("--------------\n")
    sys.stdout.write("Remove an expense\n")
    sys.stdout.write("--------------\n")
    if (len(expense.names)<=0):
        sys.stdout.write("No expenses to remove. Try adding expenses first...\n");
        return

    search_target_date=get_str("Enter expense date: ")
    search_target_name=get_str("Enter expense name: ")

    sys.stdout.write("attempting to remove...\n")

    dates_width=11
    names_width=len(max(expense_names,key=len))+20
    amouunts_width=10
    column_format="{:<"+str(dates_width)+"}{:<"+str(names_width)+"}{:>"+str(amounts_width)+"}\n"

    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)
    row_text=column_format.format("Date","Name","Amount $")
    sys.stdout.write(row_text)
    row_text=column_format.format("----","----","--------")
    sys.stdout.write(row_text)

    matches=0
    num_expenses=len(expense_names)
    i=0
    while(i<num_expenses):
        if (search_target_date==expense[i].dates and search_target_name==expense[i].names):
            row_text=column_format.format(expense[i].dates,expense[i].names,expense[i].amounts)
            del(expenses[i].dates)
            del(expenses[i].names)
            del(expenses[i].amounts)
            matches+=1
        i+=1
    sys.stdout.write("Removed "+str(matches)+" matches.\n")



        
run_expenses_manager()
        

        

        
        

