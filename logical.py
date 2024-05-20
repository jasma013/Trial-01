# Example 1 for AND
x = 5
# Both conditions x > 3 and x < 10 are true
print(x > 3 and x < 10)  # Output: True

# Example 2 for AND
y = 12
# Both conditions y > 10 and y % 5 == 0 are true (12 is greater than 10 and divisible by 5)
print(y > 10 and y % 5 == 0)  # Output: False (12 is not divisible by 5)

# Example 1 for OR
x = 5
# At least one condition (x < 3 or x > 10) needs to be true; both are false here
print(x < 3 or x > 10)  # Output: False

# Example 2 for OR
y = 12
# At least one condition (y < 10 or y % 2 == 0) needs to be true; y % 2 == 0 is true
print(y < 10 or y % 2 == 0)  # Output: True

# Example 1 for NOT (reverses the result of the condition)
x = 5
# The condition (x > 3 and x < 10) is true, so not True is False
print(not (x > 3 and x < 10))  # Output: False

# Example 2 for NOT
y = 12
# The condition (y > 10 and y % 5 == 0) is false (12 is not divisible by 5), so not False is True
print(not (y > 10 and y % 5 == 0))  # Output: True
