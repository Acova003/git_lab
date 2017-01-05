from arithmetic import *

while True:
# grab user input raw_input  assign to variable
# take user input variable .split() at space to parse return list
    user_input = raw_input("> ")
    split_action = user_input.split(" ")

    if "q" in split_action:
        print "You are exiting the program!"
        break

    if len(split_action) < 2:
        print "Not enough input"
        continue

        num1 = split_action[1]

        if len(split_action) < 3:
            num2 = 0

        else:
            num2 = split_action[2]

    elif split_action[0] == "+":
        print add(float(num1), float(num2))

    elif split_action[0] == "-":
        print subtract(float(num1, float(num2))

    elif split_action[0] == "/":
        print divide(float(num1, float(num2))

    elif split_action[0] == "*":
        print multiple(float(num1, float(num2))

    elif split_action[0] == "square":
        print square(float(num1))

    elif split_action[0] == "cube":
        print cube(float(num1))

    elif split_action[0] == "pow":
        print power(float(num1, float(num2))

    elif split_action[0] == "mod":
        print mod(float(num1, float(num2))

    else:
        print "Please print an operator followed by two integer."
