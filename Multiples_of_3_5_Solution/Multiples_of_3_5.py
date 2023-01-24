numbers=[num for num in range(1,1000) ]

soma = 0

for num in numbers:
    if num % 5 == 0 or num % 3 == 0 :
        soma += num
print(str(soma))

# Answer: 233168