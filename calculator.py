num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("Select an operation to perform: ")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

operation = input()

if operation == "1":
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    print("The sum is " + str(int(num1) - int(num2)))
elif operation == "3":
    print("The sum is " + str(int(num1) * int(num2)))
elif operation == "4":
    if int(num1) // int(num2) == int(num1) / int(num2) :
        print("The sum is " + str(int(num1) // int(num2)))
    elif int(num1) // int(num2) != int(num1) / int(num2) :
        print("The sum is " + str(int(num1) / int(num2)))
    
else:
    print("Invalid entry")
