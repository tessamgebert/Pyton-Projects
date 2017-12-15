power_digit = 2**1000
sum_of_digits = 0
while power_digit > 0:
    sum_of_digits += power_digit%10
    power_digit = power_digit/10
print sum_of_digits
