class StringReverser:

    def reverse_words(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


if __name__ == '__main__':
    reverser = StringReverser()
    input_string = input("Please enter a string: ")
    reversed_string = reverser.reverse_words(input_string)
    print(f"Original string: {input_string}")
    print(f"Reversed string: {reversed_string}")
