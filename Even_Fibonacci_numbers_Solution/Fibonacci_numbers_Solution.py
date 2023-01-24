lim = 4e6
a = 0
b = 1
c = 0

total = 0
while b < lim :
    c = b + a
    b = a
    a = c
    if b % 2 == 0:
        total += b
    else:
        pass 

print(total)

# Answer = 4613732
