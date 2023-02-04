


operator = input("Enter math operation you want to perform: 1 for add, 2 for subtract, 3 for multiply, 4 for divide  " )
print(int(operator))
if(int(operator) > 4 or int(operator) < 4):
    print("Invalid option")

first_number = input("Enter firt number: ")
second_number = input("Enter second number: ")



def switch(math_operation, first_number, second_number):
    if math_operation == "1":
        return int(first_number) + int(second_number)
    elif math_operation == "2":
        return int(first_number) - int(second_number)
    elif math_operation == "3":
        return int(first_number) * int(second_number)
    elif math_operation == "4":
        return float(first_number) / float(second_number) 


print(switch(operator,first_number,second_number))
