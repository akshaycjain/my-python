def input_number():
	n1 = int(input("Enter the first number: "))
	n2 = int(input("Enter the second number: "))
	return n1, n2

def add(a, b):
	return a+b

def display(a, b, c):
	print('{0} + {1} = {2}'.format(a,b,c))


def main():
	num1, num2 = input_number()
	sum_of_2_num = add(num1, num2)
	display(num1, num2, sum_of_2_num)
main()
