sum_of_evens = 0
i = 1
u = 1
while i <= 4000000 and u <= 4000000:
    u += i
    i += u
    if i%2 == 0:
        sum_of_evens += i
    if u%2 == 0:
        sum_of_evens += u
print sum_of_evens
