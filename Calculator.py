# my calculator


if True:
	print("options:")
	print("enter 'add' to add two nunbers")
	print("enter 'subtract' to subtract two numbers")
	print("enter 'multiply' to multiply two numbers")
	print("enter 'divide' to divide two numbers")
	print("enter 'quit' to end the program")
	user_input = input(":")
	
if user_input == True:
	print('exit')

elif user_input == "add":
	num1 = float(input('enter a number'))
	num2 = float(input('enter another number'))
	result = str(num1 + num2)
	print('the answer is' + result)

elif user_input == "subtract":
	num1 = float(input('enter a number'))
	num2 = float(input('enter another number'))
	result = str(num1 - num2)
	print('the answer is' + result)

elif user_input == "multiply":
	num1 = float(input('enter a number'))
	num2 = float(input('enter another number'))
	result = str(num1 * num2)
	print('the answer is' + result)

elif user_input == "divide":
	num1 = float(input('enter a number'))
	num2 = float(input('enter another number'))
	result = str(num1 / num2)
	print('the answer is' + result)

else:
	print('unknown input')