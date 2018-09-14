# Python Calculator v.1



print("Enter 'add' to add two numbers")
print("Enter 'subtract' to subtract two numbers")
print("Enter 'multiply' to multiply' two numbers")
print("Enter 'divide' to divide two numbers")
user_input = input("Enter your option: ")

print("What two number:")
num1 = float(input("Number 1:"));
num2 = float(input("Number 2:"));

#Addition 
if user_input == "add":
	result = str(num1 + num2)
	print('The answer is ' + result)

#Subtraction
elif user_input == "subtract":
	result = str(num1 - num2)
	print('The answer is ' + result)

#Multiplication
elif user_input == "multiply":
	result = str(num1 * num2)
	print('The answer is ' + result)

#Division
elif user_input == "division":
	if num1 == 0 or num2 == 0:
		print("undefined")
	result = str(num1 / num2)
	print('The answer is ' + result)

# Everything else
else:
	print("Unknown error")