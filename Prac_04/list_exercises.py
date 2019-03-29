"""
CP1404 Prac
Basic List Operations and Woefully Inadequate Security Checker
"""

# 1) Basic List Operations
numbers = []
for i in range(5):
    number = int(input("Please insert number: "))
    numbers.append(number)

print("The first number is ", numbers[0])
print("The last number is ", numbers[-1])
print("The smallest number is ", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the numbers is ", sum(numbers) / len(numbers))

# 2) Woefully Inadequate Security Checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("please enter an username: ")
if username in usernames:
    print("welcome ", username)
else:
    print("access denied, you are not welcome", username)
