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


result_programme()
