import os
import csv
import sys
from datetime import date

today = date.today()
file = 'budget_log.csv'

def check_yn(n):
    if n == "y" or n == "n":
        return True
    else:
        print("Enter only y or n.")
        return False

current = 0
with open('now.txt') as now: #current money
  for line in now:
      current += int(line)

print(current)

##income
bonus = 800
pay_1 = 1240
pay_2 = 1310
taxret = 413
hst = 88
extra = 80
##expenses
weed = 300
mortg = 280
gas = 193
tax = 110
groceries = 100
hydro = 83
phone = 41
condo = 35
fee = 20
##calculations
calc_1 = pay_2 * 6 + bonus
calc_2 = (extra*2)
calc_3 = (mortg + condo + fee + gas + tax + hydro + phone) * 2
calc_4 = groceries * 16 - 50 - 165 - 134 - 248 - 101#1600
calc_5 = weed * 4 - 175 - 140 - 160 - 160 - 280 - 85 - 95 - 160#1200
final = (calc_1 + calc_2) - (calc_3 + calc_4 + calc_5)
##total possible at end date
print(current+final)

with open('exp_inc.csv', "a", newline='') as exp_inc, open(file, "a",
newline='') as log, open(file, newline='') as log_chk:
    
    exp_inc_writer = csv.writer(exp_inc, delimiter=",")
    logwriter = csv.writer(log, delimiter=",")
    logread = csv.reader(log_chk)

    ##user input beings here
    while True:
        expenses = input("Enter expenses(y/n)? ") 

        if (check_yn(expenses)):
            break
        else:
            continue
        
    ##expenses   
    while expenses == "y": #if yes loops until no
        name = input("Name: ")
        while True:
            try:
                amount = input("Amount: ")
                current -= int(amount)
                break
            except ValueError:
                print("Enter a number")
                continue
        
        xp_out = [str(today), "Expense", name, str(amount)] #written to expenses/income log
        exp_inc_writer.writerow(xp_out)

        while True:
            poutpout = input("Another expense(y/n)? ")
            if (check_yn(poutpout)): 
                break
            else:
                continue
        expenses = poutpout
        
    ##income   
    if expenses == "n":
        while True:
            income = input("Enter income(y/n)? ") ###next input
            if (check_yn(income)):
                break
            else:
                continue
        
        while income == "y": #if yes loops until no
            name = input("Name: ")
            while True:
                try:
                    amount = input("Amount: ")
                    current += int(amount)
                    break
                except ValueError:
                    print("Enter a number")
                    continue
            
            inc_out = [str(today), "Income", name, str(amount)] #written to expenses/income log
            exp_inc_writer.writerow(inc_out)
            
            while True:
                comecome = input("Another icome(y/n)? ")
                if (check_yn(comecome)):
                    break
                else:
                    continue
            income = comecome

        #comments    
        if income == "n":
            print(current)
            print(current+final)
                
            while True:
                inp = input("Add comments(y/n)? ") #add comments, no more user input after this
                if (check_yn(inp)):
                    break
                else:
                    continue
                
            a=[] 
            for line in logread: 
                a.append(line)

            output = [str(current+final), str(current), str(today)] #written to income log
            
            if inp == "y": #if yes to comments
                comments = input("")
                output.append(comments)

            if os.stat(file).st_size == 0: #if file is empty
                logwriter.writerow(str(output))
                sys.exit("write successful")
                                       
            else:
                if a[-1] == output: #if last line of log is same as output
                        sys.exit("already in")
                else:       
                    logwriter.writerow(output)
                    with open('now.txt', "w", newline='') as now_updt: #open here protects file from losing value if terminated before end
                        now_updt.write(str(current))
                    sys.exit("write successful")

