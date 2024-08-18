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


def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return "зима"
    elif month >= 3 and month <= 5:
        return "весна"
    elif month >= 6 and month <= 8:
        return "лето"
    else:
        return "осень"

month = int(input("Введите номер месяца (от 1 до 12): "))
print(get_season(month))
```

def check_numbers(num1, num2, num3):
if num1 > 10 and num2 > 10 and num3 > 10:
return "yes"
else:
return "no"

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

print(check_numbers(num1, num2, num3))


