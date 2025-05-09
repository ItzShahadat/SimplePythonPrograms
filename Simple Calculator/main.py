
# A Simple calculator
# Author : @ItzShahadat

# This calculator only calculates two number, in future that will be updated.

import math

x = input("Enter first number : ")
y = input("Enter second number : ")

operation = input('''Operations available:

A. Addition 
B. Subtraction 
C. Multiplication 
D. Division 
E. Modulus 
F. Exponent 
G. Floor Division

Select an operation to calculate: ''')

if operation.upper() == 'A':
    result = int(x) + int(y)
        print("Addition of two numbers is:", result)
        elif operation.upper() == 'B':
            result = int(x) - int(y)
                print("Subtraction of two numbers is:", result)
                elif operation.upper() == 'C':
                    result = int(x) * int(y)
                        print("Multiplication of two numbers is:", result)
                        elif operation.upper() == 'D':
                            result = int(x) / int(y)
                                print("Division of two numbers is:", result)
                                elif operation.upper() == 'E':
                                    result = int(x) % int(y)
                                        print("Modulus of two numbers is:", result)
                                        elif operation.upper() == 'F':
                                            result = int(x) ** int(y)
                                                print("Exponent of two numbers is:", result)
                                                elif operation.upper() == 'G':
                                                    result = int(x) // int(y)
                                                        print("Floor Division of two numbers is:", result)
                                                        else:
                                                            print("Invalid operation selected!")

                                                            # Thanks for using this calculator
                                                            