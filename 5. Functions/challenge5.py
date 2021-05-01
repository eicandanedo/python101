def sum(*args):
    result = 0
    for i in args:
        result += i
    return result


hours_worked = sum(40, 41, 39, 40, 40)
print(hours_worked)
