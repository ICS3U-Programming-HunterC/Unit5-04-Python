#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: May 10, 2022
# This program gets 3 parameters, and then calculates the answer
# with the three parameters


def calculate(sign, number1, number2):
    # calculate the answer
    if sign == "-":
        answer = number1 - number2
    elif sign == "+":
        answer = number1 + number2
    elif sign == "*":
        answer = number1 * number2
    elif sign == "/":
        answer = number1 / number2
    elif sign == "%":
        answer = number1 % number2
    else:
        print
    return answer


def main():
    # get the operation sign and numbers
    sign = input("Enter the operation you want to perform (+, -, /, *, %): ")
    number1_as_string = input("Enter the first number: ")
    number2_as_string = input("Enter the second number: ")

    # if the operator sign is valid then it will error check the numbers
    if sign == "+" or sign == "-" or sign == "/" or sign == "*" or sign == "%":
        # error check the numbers
        try:
            number1 = float(number1_as_string)
            number2 = float(number2_as_string)

            # call the function
            answer = calculate(sign, number1, number2)

            # display the answer
            print(
                "The result of {} {} {} is {:.2f}".format(
                    number1, sign, number2, answer
                )
            )
        # if there is invalid input it will display
        except Exception:
            print("Must be a valid number!")
    # if it is an invalid operator it will display invalid
    else:
        print("{} is not a recognized operator".format(sign))
    # call function


if __name__ == "__main__":
    main()
