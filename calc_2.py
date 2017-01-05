from new_arithmetic import *

print "If you want to quit, enter 'q': "

while True:

    user_input = raw_input("> ")
    split_action = user_input.split(" ")

    if "q" in split_action:
        print "You are exiting the program!"
        break

    if len(split_action) == 2:
        operator_check = split_action[0]
        num1 = split_action[1]

        if operator_check == "cube":
            print cube(float(num1))

        elif operator_check == "square":
            print square(float(num1))

        else:
            print "invalid input"

    elif len(split_action) == 3:
        operator_check = split_action[0]
        num2 = split_action[2]
        num1 = split_action[1]

        if operator_check == "+":
            print add(float(num1), float(num2))

        elif operator_check == "-":
            print subtract(float(num1), float(num2))

        elif operator_check == "/":
            print divide(float(num1), float(num2))

        elif operator_check == "*":
            print multiply(float(num1), float(num2))

        elif operator_check == "pow":
            print power(float(num1), float(num2))

        elif operator_check == "mod":
            print mod(float(num1), float(num2))

        else:
            print "invalid number"

    # elif len(split_action) == 3:

    # else:

    # if len(split_action) < 2:
    #     print "Not enough input"
    #     continue

    # num1 = split_action[1]

    # if len(split_action) < 4:

    #     num2 = split_action[2]

    # elif num2 == split_action[2]:

    # elif split_action[0] == "+":
    #     print add(float(num1), float(num2))

    # elif split_action[0] == "-":
    #     print subtract(float(num1), float(num2))

    # elif split_action[0] == "/":
    #     print divide(float(num1), float(num2))

    # elif split_action[0] == "*":
    #     print multiple(float(num1), float(num2))

    # elif split_action[0] == "square":
    #     print square(float(num1))

    # elif split_action[0] == "cube":
    #     print cube(float(num1))

    # elif split_action[0] == "pow":
    #     print power(float(num1), float(num2))

    # elif split_action[0] == "mod":
    #     print mod(float(num1), float(num2))

    # else:
    #     print "Please print an operator followed by two integer."
