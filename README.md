# python_checkbook_project
Command line checkbook application that allows users to track their finances with a command line interface. 

Build a .py file that will be run from the command line.

If the ledger file does not exist prior to running the .py file, it should be created.

When run, the application should welcome the user and prompt them for an action to take:

-view current balance

-add a debit (withdrawal)

-add a credit (deposit)

-exit

The application should notify the user if the input is invalid and prompt for another choice.

The application should persist between times that it is run.

Example, if you run the application, add some credits, exit the application and run it again, you should still see the balance that you previously created. In order to do this, your application will need to store its data in a text file. Consider creating a file where each line in the file represents a single transaction.
Utilize functions to call the balance, debit, credit, and exit.
