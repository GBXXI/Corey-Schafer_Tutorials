
# IDEPMPOTENCE: The property of certain operations that can be applied
# multiple times without changing the result beyond the initial application

# f(x)
# add_ten(num)
def add_ten(num):
    return num + 10

# f(f(x)) = f(x)

print(add_ten(10))  # Output: 20
                    # So by the definition this is not an idempontent operation

# Idempotent operation example
print(abs(-10))
print((abs(abs(-10))) == 10) # Output: True
print((abs((abs(abs(-10))))) == 10)  # Output: True
print((abs(abs(10))) == 10)  # Output: True
