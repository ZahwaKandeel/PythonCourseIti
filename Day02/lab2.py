#Q1
# Write a function that accepts two arguments (length, start) to
# generate an array of a specific length filled with integer numbers
# increased by one from start.

def generate_arr(length,start):
    arr = []
    for i in range(start, start + length):
        arr.append(i)
    return arr

print(generate_arr(5,2))
print(generate_arr(2,3))

#Q2
# write a function that takes a number as an argument and if the
# number divisible by 3 return "Fizz" and if it is divisible by 5 return
# "buzz" and if it is divisible by both return "FizzBuzz"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return ("FizzBuzz")
    elif num % 5 == 0 :
        return ("Buzz")
    elif num % 3 == 0 :
        return ("Fizz")
    else:
        return ("Not FizzBuzz")


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(2))

#Q3
# Write a function which has an input of a string from user then it will return the same string reversed.

def reversed(message):
    return message[::-1]

message="We love python"
print(reversed(message))

#Q4
# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email or not

name = input("Enter your name: ")
while not name.strip() or name.isdigit():
    print("Invalid name")
    name = input("Enter your name: ")

email = input("Please enter your email: ")
while "@" not in email or "." not in email.split("@")[-1]:
    print("Invalid email. Please enter a valid email address.")
    email = input("Please enter your email: ")

print(name , email)

#Q5
# Write a function that takes a string and prints the longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu

def longest_alphabetic(message):
    longest = message[0]
    curent = message[0]

    for i in range(1,len(message)):
        if message[i] >= message[i-1]:
            curent += message[i]
        else:
            if len(curent) > len(longest):
                longest = curent
            curent = message[i]

    if len(curent) > len(longest):
        longest = curent

    return longest
message = "abdulrahman"
print(longest_alphabetic(message))

#Q6
# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake, print an error message and skip to the next number.

total = 0
count = 0
while True:
    numbers = input("Please enter number or done to stop:")
    if numbers.lower() == "done":
        break

    numbers = int(numbers)
    total += numbers
    count += 1

average = total / count
print(total, average)

#Q7
# Word guessing game (hangman)
# ○ A list of words will be hardcoded in your program, out of which the interpreter will
# ○ choose 1 random word.
# ○ The user first must input their names
# ○ Ask the user to guess any alphabet. If the random word contains that alphabet, it
# ○ will be shown as the output(with correct placement)
# ○ Else the program will ask you to guess another alphabet.
# ○ Give 7 turns maximum to guess the complete word.

words = ['python','java','html','css']
set_words  = set(words)
word = set_words.pop()

name = input("Enter your name: ")
print(f"The word have {len(word)} letters.")

guessed_letters = []
turns = 7

while turns > 0:
    show = ""
    for letter in word:
        if letter in guessed_letters:
            show += letter
        else:
            show += "_"
    print(show)

    if show == word:
        print("Correct")
        break

    guess = input("Enter your guess: ")

    if guess in guessed_letters:
        print("You guessed this letter before")
        continue

    guessed_letters.append(guess)

    if (guess) in word:
        print("Correct")
    else:
        print("Wrong")
        turns -=1

    print(f"{turns} turns left")

if turns == 0:
    print("You loss")
    print("The word was", word)
