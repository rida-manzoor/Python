# Faulty calculator
# 45 * 3 =555, 56+9= 77, 56/6 = 4

print("Enter a first number:")
z = int(input())
print("Enter second number:")
x = int(input())
print("Enter operator:")
n = input()
if z == 46 and x == 3 and n == '*':
    print("555")
elif z == 56 and x == 9 and n == '+':
    print("77")
elif z == 56 and x == 6 and n == '/':
    print("4")
elif n == '-':
    m = z - x
    print(m)
elif n == '*':
    b = z * x
    print(b)
elif n == '+':
    c = z + x
    print(c)
elif n == '/':
    v = z / x
    print(v)
elif n == '%':
    l = z % x
    print(l)
else:
    print("Opps! Check your input.")

