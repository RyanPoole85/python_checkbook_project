import os

# Function to load the ledger from a file
def load_ledger(filename):
    ledger = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                ledger.append(float(line))
    return ledger

# Function to save the ledger to a file
def save_ledger(filename, ledger):
    with open(filename, 'w') as file:
        for item in ledger:
            file.write(f"{item:.2f}\n")

# Function to view the current balance
def view_balance(ledger):
    return sum(ledger)

# Function to record a debit (withdrawal)
def record_debit(ledger):
    while True:
        try:
            debit = float(input("\nHow much would you like to withdraw? $"))
            ledger.append(-debit)
            print(f"\nDebit of ${debit:.2f} recorded.")
            break
        except ValueError:
            print("\nNot a valid number. Please enter a valid number for the debit.")

# Function to record a credit (deposit)
def record_credit(ledger):
    while True:
        try:
            credit = float(input("\nHow much would you like to deposit? $"))
            ledger.append(credit)
            print(f"\nCredit of ${credit:.2f} recorded.")
            break
        except ValueError:
            print("\nNot a valid number. Please enter a valid number for the credit.")

# Main function to run the checkbook application
def main():
    ledger_file = 'ledger.txt'
    ledger = load_ledger(ledger_file)
    
    print("\n~~~ Welcome to your terminal checkbook! ~~~")

    while True:
        print("\nWhat would you like to do?\n")
        print("1) view current balance")
        print("2) record a debit (withdraw)")
        print("3) record a credit (deposit)")
        print("4) exit")

        choice = input("\nYour choice? ")

        if choice == '1':
            balance = view_balance(ledger)
            print(f"\nYour current balance is ${balance:.2f}.")
        elif choice == '2':
            record_debit(ledger)
        elif choice == '3':
            record_credit(ledger)
        elif choice == '4':
            save_ledger(ledger_file, ledger)
            print("\nThanks, have a great day!\n")
            break
        else:
            print("\nInvalid choice:", choice)

if __name__ == "__main__":
    main()

