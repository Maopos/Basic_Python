print('======================')
print()

def calcular_factorial(num):
    if num == 0  or num == 1:
        return 1
    else:
        return num * calcular_factorial(num - 1)

print(calcular_factorial(5))


print()
print('======================')
