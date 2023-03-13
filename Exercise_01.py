# File: Exercise_01.py
# Author: Pham Quang, Pham Duy Quang
# Description :Programming demo

import random

# Task 1
def print_Test():
    print("Hello Word!")

# Task 2
def list_Numbers_Strings():
    list_Num = []
    for i in range(10):
        list_Num.append(int(input("Number "+str(i)+": ")))
    print("--------------------------------------")
    list_Str = []
    for i in range(10):
        list_Str.append(input("String "+str(i)+": "))
    print(list_Num)
    print(list_Str)

# Task 3
def sort_List():
    list_sort = [2, -5, 7 , 9, 11, 0, 445, -100, 4]
    list_sort.sort()
    print(list_sort)

# Task 5
def count_even(list):
    count = 0
    for i in list:
        if(i % 2 == 0):
            count += 1 
    return count

# Task 6
def sum_Positive_Int(list):
    count = 0
    for i in list:
        if(i > 0 and i % 3 == 0):
            count += i 
    return count

# Task 4
def repeated_Read():
    count = 0
    condition = True
    l = []
    while condition:
        num = int(input("Please give an integer: "))
        if(num < 0):
            count += 1
        if(num != 0):
            l.append(num)
        if(num == 0):
            condition = False
    return count, l

# Task 7
def ap():
    num = int(input("Give maximum value: "))
    list_ap = []
    sum_squared = 0
    for i in range(num):
        if (i % 3 == 0 and i != 0):
            list_ap.append(i)

    print("Procession: ", list_ap)
    print("Number of term is: ", len(list_ap))
    for i in list_ap:
        sum_squared += i*i
    print("Sum of term is: ", sum(list_ap))
    print("Sum of squared term is: ", sum_squared)

# Task 8
def rock_paper_scissors():
    count_p_point = 0
    count_c_point = 0
    while True:
        player_choice = input("Give your choice(R, P, S): ")
        list_choice = ["P", "R", "S"]
        computer_choice = random.choice(list_choice)
        print("Computer's choice is: ", computer_choice)
        if (player_choice == "R" and computer_choice == "P"):
            print("Paper covers Rock.")
            count_c_point +=1
        elif (player_choice == "R" and computer_choice == "S"):
            print("Rock crushes Scissors.")
            count_p_point +=1
        elif (player_choice == "P" and computer_choice == "R"):
            print("Paper covers Rock.")
            count_p_point +=1
        elif (player_choice == "P" and computer_choice == "S"):
            print("Scissors cuts Paper.")
            count_c_point +=1
        elif (player_choice == "S" and computer_choice == "R"):
            print("Rock crushes Scissors.")
            count_c_point +=1
        elif (player_choice == "S" and computer_choice == "P"):
            print("Scissors cuts Paper.")
            count_p_point +=1
        else:
            print("It's a tie.")
        print("Compute", count_c_point, "You", count_p_point)
        if (count_p_point == 3 or count_c_point == 3):
            if (count_c_point == 3):
                print("You lost!")
            else:
                print("You win!")
            break

# Task 9
def random_number():
    return random.randint(1,6)

def main():
    print("Task 1:")
    print_Test()
    print("=========================================================")

    print("Task 2:")
    list_Numbers_Strings()
    print("=========================================================")

    print("Task 3:")
    sort_List()
    print("=========================================================")

    print("Task 4:")
    result = repeated_Read()
    count = result[0]
    print()
    print("Number of negative integers is:", count)
    print("=========================================================")

    print("Task 5:")
    result5 = repeated_Read()[1]
    print()
    print("Number of  even integers is:", count_even(result5))
    print("=========================================================")

    print("Task 6:")
    result6 = repeated_Read()[1]
    print()
    print("Sum of positive integers divisible by three is:",sum_Positive_Int(result6))
    print("=========================================================")

    print("Task 7:")
    ap()
    print("=========================================================")

    print("Task 8:")
    rock_paper_scissors()
    print("=========================================================")

    print("Task 9:") 
    print("Random number is:",random_number())

main()