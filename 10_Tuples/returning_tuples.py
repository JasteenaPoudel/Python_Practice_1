def http_status():
    return 200, "Ok"

code, message = http_status()

# Exercises
# Create calculator function
# def calculate(a, b):

# Return:

# sum
# differenc
# e

def calculate ():
    a = input("Enter the first number:")
    b = input("Enter the second number:")
    c = input("Enter the operator:")
    
    if c == "+":
       print("sum=",a + b)

    elif c == "-":
        print("Difference =", a - b)

    else:
        print("Invalid Operator")

calculate()


def calculate_sum_diff():
    return 10 , 5

sum , diff = calculate_sum_diff()

print (sum)
print (diff)

x = 1,2,3
print(type(x))