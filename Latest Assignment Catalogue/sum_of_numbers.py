def sum_of_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    print(total)
sum_of_numbers(4, 8, 10, 12, 11)
