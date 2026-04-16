"""

Task3: 
Write a program that asks the user for their PIN and account balance. Make a function
called withdraw (balance, amount) that checks if the withdrawal is valid, deducts the amount,
and returns the new balance. The program should keep asking for a withdrawal amount until
the user types 0 to exit.
Conditions to implement
• If PIN is wrong, deny access and stop the program
• Amount must be greater than 0 and less than or equal to the current balance
• Amount must be a multiple of 500 (you can only withdraw 500, 1000, 1500...)
• Print the remaining balance after each successful withdrawal



"""


class Acount:
    def __init__(self):
        self.balance = 500
        self.pin = 2345

    def withdraw(self, pin, amount):
        if self.pin != pin:
            return 'Invalid Your Pin'
        elif amount <= self.balance:
            self.balance -= amount
            return f' Transaction completed successfully\nYour Rmaining Acount Balance {self.balance}'
        else:
            return 'Insuficeint Balance '


def programme():
    while True:
        pin = int(input('Enter Your PIN Code: '))
        withdraw_amount = int(input('Enter withdraw amount: '))
        User = Acount()
        result = User.withdraw(pin, withdraw_amount)
        print(result)
        option = int(input("Press 0 to exit or 1 to continue: "))
        if option == 0:
            print('Thank you for using our banking system.')
            break


print(" ----- Welcome to our Banking System -----")
user_account = programme()
