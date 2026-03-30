#Q6
# Write a program that prints the locations of "i" character in any
# string you added.

arr = ['i','x','y','z','i']

for index, char in enumerate(arr):
    if char == "i":
        print(f'{index} : {char}')

#Q7
# Write a program that generate a multiplication table from 1 to the
# number passed

num = input("Enter a number: ")
result = []

if num.isdigit():
    num = int(num)
    for i in range (1, num + 1):
        row = []
        for j in range (1, i + 1):
            row.append(i * j)
        result.append(row)
else:
    print("Invalid input! Please enter a number")


print(result)

#Q8
#Write a program that build a Mario pyramid like below

num = int(input("Please enter a number: "))

for i in range (1, num + 1):
    print(" " * (num - i) + "*" * i)