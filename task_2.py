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


print('--- This Programme only for Getting Prime, Odd and Even Number ---')

programme_type_of_number()
