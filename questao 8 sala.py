fib1=1
fib2=0
fib3=0
print(fib1)
for x in range (14):
    fib3=fib1+fib2
    fib2=fib1
    fib1=fib3
    print(fib1)