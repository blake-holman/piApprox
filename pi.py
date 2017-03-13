i = 1.0
pi = 0
while i < 1000000:
    pi = pi + 1.0/i - 1.0/(i + 2)
    i += 4
print(4 * pi)
