# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1.lower() != "q"):
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    if calc1.upper() == "Q":
        break
    else:
        calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2.lower() == "q":
        break
    else:
        calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation.strip() == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation.strip() == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
