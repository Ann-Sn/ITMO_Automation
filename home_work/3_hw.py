def max_num(a, b):
if a > b:
return a
else:
return b

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print(max_num(num1, num2))


def check_difference(num1, num2):
    if (num1 - num2) == 135 or (num2 - num1) == 135:
        return "yes"
    else:
        return "No"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = check_difference(num1, num2)
print(result)


