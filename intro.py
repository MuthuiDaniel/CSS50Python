# String
print("hello world")
# variable is container to store a value
name = input("what's your name?").strip().title()
# remove whitespace from str and capitalize user name
name = name.strip().title()
# capitalize user name
name = name.title()
# split username into first name and last name
first, last = name.split(" ")
print(f"hello, {first} nice to meet you")
age = input("what is your age\n")
print(f"your age is {age}")

# ----------------------------------------------------------------
# integer
# +, - , *, /, %
x = int(input("what's X?"))
y = int(input("what's Y?"))
print(x + y)
# float - number with a decimal point
x = float(input("what's X?"))
y = float(input("what's Y?"))
print(round(x + y))
# division
x = float(input("what's X?"))
y = float(input("what's Y?"))
z = round(x / y, 2)
print(f"{z:.2f}")
# ---------------------------------------------------------------------
# def - functions/ define
def main():
    name = input("what's your name?")
    return name
main()

def main():
    x = int(input("what's x?"))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()

def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "i'm not sure what you mean"

greeting = greet("hello, computer")
print(greeting)

def get_guess():
    guess = input("Enter a guess:")
    return  guess

print(get_guess())

