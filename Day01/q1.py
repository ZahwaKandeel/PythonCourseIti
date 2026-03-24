#Lab One Course Python ITI
#Q1

#1- Write a program that counts up the number of vowels "aeiou" contained in the string.
#example noha  ---> 2

name = "zahwa"
count = 0

for char in name:
    if char in "aeiou":
        count += 1

print(count)