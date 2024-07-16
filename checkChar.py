user_input = input("Enter a character: ")

if len(user_input) == 1:
    if user_input.isalpha():
        print("The character entered is an alphabet letter.")
    elif user_input.isdigit():
        print("The character entered is a digit.")
    elif user_input.isspace():
        print("The character entered is a whitespace character.")
    elif user_input.isalnum():
        print("The character entered is an alphanumeric character (letter or digit).")
    else:
        print("The character entered doesn't fit any of the specified types.")
else:
    print("Please enter only a single character.")
