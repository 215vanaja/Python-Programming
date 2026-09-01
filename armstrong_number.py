number = int(input("Enter a number: "))
original = number
total = 0
digits = len(str(number))

while number > 0:
    digit = number % 10
    total += digit ** digits
    number //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
