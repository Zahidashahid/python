print("Day 1 - String Manipulation")
print("String Concatenation is done with the \+ " + " sign.")
print('e.g. print("Hello " + "world")')
print("Hello " + "world")
print("New lines can be created with a backslash and n.\n Here in new line ")

"""
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
"""

num = 35
num = int(input("Enter a number to print its digits sum:"))
sumOfDigits = 0
while num > 0:
    sumOfDigits += num % 10
    num = num // 10

print(sumOfDigits)

"""
3:Write a program that prints the number of characters in a user's name.
"""
name = input("Enter Your name:")
count = 0
for i in name:
    if (i == " "):
        pass
    else:
        count += 1;

print("Number of characters in a your name are:", count)

"""
4:Write a program that switches the values stored in the variables a and b.
"""
a = 2
b = 4
print("Before switch Value of a is {} value of b is {}".format(a, b))
temp = a
a = b
b = temp

print("After switch Value of a is {} value of b is {}".format(a, b))
