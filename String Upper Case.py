class IOString():
    # Constructor to set default value
    def __init__(self):
        self.str1 = "" 
    # Function to get input from user
    def get_string(self):
        self.str1 = str(input("Please enter a word: "))
    # Function to print the string in uppercase
    def print_string(self):
        print("The result is: ", self.str1.upper())
str1 = IOString()
str1.get_string()
str1.print_string()
