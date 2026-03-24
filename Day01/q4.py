#Lab One Course Python ITI
#Q4

#4- Write a program that prints the locations of "i" character in anystring you added.
# (ask the user to enter a word)


word = input("Enter word : ")
counter = 0

for c in word:
    if c == "i":
        print(c,counter)
    counter += 1