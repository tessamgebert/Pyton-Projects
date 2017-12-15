sum_of_squares = 0
total_sum = 0
i = 1
while i <= 100:
    sum_of_squares += i**2
    total_sum += i
    i += 1
square_of_sum = total_sum**2
print (square_of_sum - sum_of_squares)


