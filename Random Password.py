import random
import time


def greeting():
  global name
  name = input(
      "Hello! I will make a random password for you. What is your name? ")
  print(
      f"Alright, {name}! I'll be asking you some questions and then I will generate a random password for you!"
  )
  a = input("Should we start? (yes/no) ")
  if a.lower() == "no":
    print("Goodbye then.")

  else:
    default = input("Would you like to use the default format? (yes/no) ")
    if default.lower() == "yes":
      length = 12
      spaces = "no"
      numbers = "yes"
      upper_letters = "yes"
      lower_letters = "yes"
      special_characters = "yes"
      make_password(length, spaces, numbers, upper_letters, lower_letters,
                    special_characters)
    else:
      questions()


def questions():
  global length
  global spaces
  global numbers
  global upper_letters
  global lower_letters
  global special_characters
  print(f"Alright {name}, let's get started.")
  print("Please answer each question with yes or no.")
  while True:
    try:
      length = int(input("How long would you like your password to be? "))
      if length <= 0:
        print("Password length must be greater than 0.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")
  spaces = input("Will your password include spaces? (yes/no) ")
  numbers = input("Will your password include numbers? (yes/no) ")
  upper_letters = input(
      "Will your password include capital letters? (yes/no) ")
  lower_letters = input(
      "Will your password include lowercase letters? (yes/no) ")
  special_characters = input(
      "Will your password include special characters? (yes/no) ")
  make_password(length, spaces, numbers, upper_letters, lower_letters,
                special_characters)


def make_password(length, spaces, numbers, upper_letters, lower_letters,
                  special_characters):
  print(f"Your password will be ready soon, {name}!")
  if numbers.lower() == "no" and upper_letters.lower(
  ) == "no" and lower_letters.lower() == "no" and special_characters.lower(
  ) == "no":
    print(
        f"Sorry, {name}, I can't make that password. You must include at least one character type."
    )
    questions()
    return

  characters = ""
  if spaces.lower() == "yes":
    characters += " "
  if numbers.lower() == "yes":
    characters += "0123456789"
  if upper_letters.lower() == "yes":
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if lower_letters.lower() == "yes":
    characters += "abcdefghijklmnopqrstuvwxyz"
  if special_characters.lower() == "yes":
    characters += "~`!@#$%^&*()_-+=|{}[]:;<>,.?/"

  time.sleep(1)
  
  if characters:
    password = "".join(random.choice(characters) for i in range(length))
    print(f"Your password is: {password}")
  else:
    print(
        f"Sorry, {name}, I can't make that password. No character types were selected.")
    questions()
    return




greeting()
