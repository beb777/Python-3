#factorial n! = n*(n-1)(n-2)..........*1
number = int(input("Enter a number to find factorial: "))
factorial = 1;
if number < 0:
    print("Factorial does not defined for negative integer");
elif (number == 0):
    print("The factorial of 0 is 1");
else:

    while (number > 0):
        factorial = factorial * number

        number = number - 1

    print("factorial of the given number is: ")
    print(factorial)