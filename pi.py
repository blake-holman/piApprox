i = 1.0
pi = 0
# Lebniz equation calculates pi/4 using an infinite series
limit = int(input("please input an upper limit(eg. 10000)"))
while i < limit: # user input for upper limit
    pi = pi + 1.0/i - 1.0/(i + 2)
    if (i - 1) % (limit/5) == 0: # reminds user that the program is still running five times per calculation
        print("calculating. . .")
    i += 4
pi = 4 * pi # since we found pi/4 we must multiply the result by  4
piReal = 3.1415926535897932
percError = 100 * (piReal - pi) / piReal

if percError < 0: # in the event that pi is less than the actual value of pi
    percError *= -1

print(pi)
print("pi is actually %s" %piReal)
print("The percent error is %s" %percError)
