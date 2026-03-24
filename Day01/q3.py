#Lab One Course Python ITI
#Q3

#3- Write a program that remove all vowels from the input word and generate a brief version of it.
# (ask the user to enter a word)
# noha  ===> nh

name = input("Enter your name : ")
briefVersion = ""

for char in name:
    if char not in "aeiou":
        briefVersion += char

print(briefVersion)