"""
Write a program that takes a student's name and marks in 5 subjects as input, calculates the 
total and percentage, then prints the grade (A/B/C/D/F) using if-elif-else logic. 
Conditions to implement 
• 90% and above → A 
• 80–89% → B 
• 70–79% → C 
• 60–69% → D 
• Below 60% → F

"""


def student_percentage(name, sub_1, sub_2, sub_3, sub_4, sub_5):
    total = sub_1+sub_2+sub_3+sub_4+sub_5
    prcnt = total / 500 * 100
    if prcnt >= 95:
        print(f'Name: {name}\nPercentage: {prcnt} \nGrade: A++')
    elif prcnt >= 90 and prcnt <= 94:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: A+')
    elif prcnt >= 85 and prcnt <= 89:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: A')
    elif prcnt >= 80 and prcnt <= 84:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: B++')
    elif prcnt >= 75 and prcnt <= 79:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: B+')
    elif prcnt >= 70 and prcnt <= 74:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: B')
    elif prcnt >= 60 and prcnt <= 69:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: C')
    elif prcnt >= 50 and prcnt <= 59:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: D')
    elif prcnt >= 40 and prcnt <= 49:
        print(f'Name: {name}\nPerncentage: {prcnt}\nGrade: E')
    else:
        print('Fail')


def result_programme():
    name = input("Enter  name here: ")
    numb1 = int(input("Enter  Marks subject_1: "))
    numb2 = int(input("Enter  Marks subject_2: "))
    numb3 = int(input("Enter  Marks subject_3: "))
    numb4 = int(input("Enter  Marks subject_4: "))
    numb5 = int(input("Enter  Marks subject_5: "))
    result = student_percentage(name, numb1, numb2, numb3, numb4, numb5)

#  main funtion of programme call here..

# result_programme()

"""
Task2: 
Write a program that takes 10 numbers from the user and stores them in a list. Make three 
functions — get_odds(), get_evens(), and get_primes() — each takes the list and returns only 
the numbers that match that category. Print all three results at the end. 
Conditions to implement 
• A prime number is only divisible by 1 and itself — implement this check manually using a 
loop 
• 1 is not a prime number 
• Each function must use a loop and return a new list — do not print inside the function 
• If a category is empty, print "None found" for that category

"""


def get_odd(lst):
    odd_list = []
    for num in range(len(lst)):
        if lst[num] % 3 == 0:
            odd_list.append(lst[num])
    if not odd_list:
        return 'Not Found Odd Number'
    else:
        return odd_list


def get_even(lst):
    even_lst = []
    for num in range(len(lst)):
        if lst[num] % 2 == 0:
            even_lst.append(lst[num])
    if not even_lst:
        return 'Not Found Even Number'
    else:
        return even_lst


def get_prime(lst):
    prime_lst = []
    for item in range(len(lst)):
        not_prime = 0
        for num in range(2, lst[item]):
            if lst[item] % num == 0:
                not_prime = lst[item]
                break
        if not_prime == 0:
            prime_lst.append(lst[item])
    if not prime_lst:
        return 'Prime Number Not Found'
    else:
        return prime_lst


def programme_type_of_number():
    print('Enter 10 Numbers')
    list_of_number = []
    for num in range(1, 11):
        num_1 = int(input(f'Press Number_{num}: '))
        list_of_number.append(num_1)
    option = int(input('For Odd Number Press 1\nFor Even Number Press 2: \nFor Prime Number Press 3:  '))
    if option == 1:
        odd = get_odd(list_of_number)
        print(f'Odd Number: {odd}')
    elif option == 2:
        even = get_even(list_of_number)
        print(f'Even Number: {even}')
    elif option == 3:
        prime = get_prime(list_of_number)
        print(f'Prime Number: {prime}')
    else:
        ('Invalid Number')


# print('--- This Programme only for Getting Prime, Odd and Even Number ---')

# programme_type_of_number()



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


# print(" ----- Welcome to our Banking System -----")
# user_account = programme()
