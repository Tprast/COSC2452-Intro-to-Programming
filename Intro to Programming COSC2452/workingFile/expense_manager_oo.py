import sys
expense_dates=[]
expense_names=[]
expense_amounts=[]

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
    value=get_float(prompt)
    while(value<0):
        value=get_float("Input must be positive. Re-enter:")
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
    while not ["+choice+"] in menu:
        choice=get_str(choice+" was an invalid choice! Re-enter: ").lower()

    return choice

def load_data():
    with open ("expenses.csv","r") as file_object:
        for line in file_object:
            fields=line.split(",")
            expense_date=fields[0]
            expense_name=fields[1]
            expense_amount=float(fields[2])
            add_expense(expense_date,expense_name,expense_amount)

def add_expense(expense_date,expense_name,expense_amount):
    expense_dates.append(expense_date)
    expense_names.append(expense_name)
    expense_amounts.append(expense_amount)

def add_expense_via_menu():
    sys.stdout.write("--------------\n")
    sys.stdout.write("Add an expense\n")
    sys.stdout.write("--------------\n")

    expense_date=get_str("Enter expense date as YYYY-MM-DD: ")
    sys.stdout.write("\n")
    expense_name=get_str("Enter expense name: ")
    expense_amount=get_positive_float("Enter expense amount: ")
    sys.stdout.write("\n")

    add_expense(expense_data,expense_name,expense_amount)

def remove_expense():
    sys.stdout.write("--------------\n")
    sys.stdout.write("Remove an expense\n")
    sys.stdout.write("--------------\n")
    if (len(expense_names)<=0):
        sys.stdout.write("No expenses to remove. Try adding expenses first...\n");
        return

    search_target_date=get_str("Enter expense date: ")
    search_target_name=get_str("Enter expense name: ")

    sys.stdout.write("attempting to remove...\n")

    dates_width=11
    names_width=len(max(expense_names,key=len))+4
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
        if (search_target_date==expense_dates[1] and search_target_name==expense_names[i]):
            row_text=column_format.format(expense_dates[i],expense_names[i],expense_amounts[i])
            del(expense_dates[i])
            del(expense_names[i])
            del(expensea_amounts[i])
            matches+=1
        i+=1
    sys.stdout.write("Removed "+str(matches)+" matches.\n")

def find_expenses():
    sys.stdout.write("--------\n")
    sys.stdout.write("Find expenses\n")
    sys.stdout.write("--------------\n")
    if (len(expense_names)<=0):
        sys.stdout.write("No expenses to find. Try adding expenses first.../n");
        return
    sys.stdout.write("Enter partial expense name to find: ")
    sys.stdout.flush()
    search_target=sys.stdin.readline().strip()
    sys.stdout.write("\n")

    dates_width=11
    names_width=len(max(expense_names,key=len))+4
    amounts_width=10

    colum_format=column_format="{:<"+str(dates_width)+"}{:<"+str(names_width)+"}{:>"+str(amounts_width)+"}\n"

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
        if (search_target_date==expense_dates[1] and search_target_name==expense_names[i]):
            row_text=column_format.format(expense_dates[i],expense_names[i],expense_amounts[i])
            del(expense_dates[i])
            del(expense_names[i])
            del(expensea_amounts[i])
            matches+=1
        i+=1
    sys.stdout.write("Removed "+str(matches)+" matches.\n")

def save_data():
    try:
        file_object=open("expenses.csv","w")
        num_expenses=len(expense_names)
        i=0
        while(i<num_expenses):
            file_object.write(expense_dates[i]+","+expense_names[i]+","+str(expense_amounts[i])+"\n")
            i+=1
        file_object.close()
    except:
        sys.stdout.write("Could not save to file")
        
run_expenses_manager()
        

        

        
        

