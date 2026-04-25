# 1st Phase Logic only
n = int(input("Enter Last Number Here:  "))
answer = n * (n + 1) // 2
print(f"The Sum of Natural Number 1+2+3..{n} is {answer}")

# 2nd Phase
n = int(input("Enter Last Number Here:  "))
value = []
for i in range(1, n+1):
    value.append(i)
answer = sum(value)
print(f"The Sum of Natural Number 1+2+3..{n} is {answer}")

# 3rd Phase
n = int(input("Enter Last Number Here:  "))
value = [i for i in range(1, n+1)]
answer = sum(value)
print(f"The Sum of Natural Number 1+2+3..{n} is {answer}")