factorial = 100
i = 100
while i > 1:
    i -= 1
    factorial *= i
sum_of_digits = 0
while factorial > 0:
    sum_of_digits += factorial % 10
    factorial = factorial/10
print sum_of_digits
