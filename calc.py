def calculator():
    print("SIMPLE CALCULATOR!!")
    print("Operations: + for addition,- for Subtraction ,* for multiplication,/ for division")

    num1 = float(input("Enter the first number:"))
    operation = input("Enter the operation(+,_,*,/):")
    num2 = float(input("Enter the second number:"))

    if operation == '+':
        result = num1+num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1*num2
    elif operation =='/':
        if num2 == 0:
            print("ERROR: Cannot divide by zero.")
            return
        result = num1/num2
    else:
        print("Invalid operation.")
        return
    
    print(f"the result of {num1}{operation}{num2} is {result}")

#Run the calculator
calculator()
