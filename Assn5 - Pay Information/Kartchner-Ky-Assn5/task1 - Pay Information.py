"""
Ky Kartchner
CS 1400-1
Assignment 5

task1: Prompts the user for their name, hours worked, hourly pay rate, and tax withholding information, then calculates
and prints their gross pay, tax withholding amounts and total deductions, and net pay.
"""
name = input("Enter employee's name: ").upper()                                # Get employee name
hours_worked = eval(input("Enter number of hours worked in a week: "))         # Get hrs worked in a week
pay_rate = eval(input("Enter hourly pay rate: "))                              # Get hourly pay rate
federal_rate = eval(input("Enter federal tax withholding rate (ex. 0.12): "))  # Get federal tax withholding rate
state_rate = eval(input("Enter state tax withholding rate (ex. 0.06): "))      # Get state tax withholding rate

gross_pay = round(pay_rate * hours_worked, 2)             # Gross Pay = hourly rate times hrs worked
federal_taxes = round(gross_pay * federal_rate, 2)        # Federal taxes = gross pay times federal tax withholding rate
state_taxes = round(gross_pay * state_rate, 2)            # State taxes = gross pay times state tax withholding rate
total_deductions = round(federal_taxes + state_taxes, 2)  # Total deductions = federal taxes plus state taxes
net_pay = gross_pay - total_deductions                    # Net pay = gross pay minus total deductions

# Print results
print(format(name + " PAY INFORMATION", ">33"), "\n\n" + format("Pay", ">22"),
      "\n" + format("Hours Worked:  ", ">31"), format(hours_worked, ">9"),
      "\n" + format("Pay Rate: $", ">31"), format(pay_rate, ">9.2f"),
      "\n" + format("Gross Pay: $", ">31"), format(gross_pay, ">9.2f"),
      "\n\n" + format("Deductions", ">25"),
      "\n" + format("Federal Withholding (" + format(federal_rate, ".2%") + "): $", ">31"), format(federal_taxes, "9.2f"),
      "\n" + format("State Withholding (" + format(state_rate, ".2%") + "): $", ">31"), format(state_taxes, "9.2f"),
      "\n" + format("Total Deduction: $", ">31"), format(total_deductions, "9.2f"),
      "\n\n" + format("Net Pay: $", ">31"), format(net_pay, "9.2f"))
	 
input("\nPress any key to exit")

