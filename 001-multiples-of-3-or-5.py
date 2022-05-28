import math

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# i will do this without inclusion-exclusion or any knowledge of mathematics really
total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


# better solution
print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))

# note: do not use sum, list, str as variable names otherwise you can get ListError

