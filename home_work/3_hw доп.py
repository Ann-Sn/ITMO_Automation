def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

numbers = [int(input()) for _ in range(5)]  
print(count_positive(numbers))  


def days_count(years, months):
    return years * 365 + months * 29
