#program to ask for a number and check if it is even or odd
def check(num):
    if num%2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

num = int(input("Enter a number"))
result = check(num)
print(result
)