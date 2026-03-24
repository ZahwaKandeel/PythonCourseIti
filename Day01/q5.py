#Lab One Course Python ITI
#Q5

#5- Write a program that build a Mario pyramid like below:
# 4
#    *
#   **
#  ***
# ****

num = input("Please enter a number: ")
if num.isdigit():
    num = int(num)
    i=1

    while i <= num:
        print(" " * (num - i) + "*" * i)
        i += 1

else:
    print("Please enter numbers only ")