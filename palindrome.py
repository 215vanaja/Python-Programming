text = input("Enter a number or word: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
