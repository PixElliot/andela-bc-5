def my_sum(x, y):
	return x + y

def diff_sum():
	#Asking user for numbers to perfrom sum on
	x = int(raw_input("Enter the first number: "))
	y = int(raw_input("Enter the first number: "))
    #Returning the sum of x and y
	return (x + y)

def my_sol(num):
	ls = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	for i in str(num):
		for j in range(len(ls)): 
			if i == str(j):
				print ls[j],
