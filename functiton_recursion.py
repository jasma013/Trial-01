def sum_of_digits(n):
    """
    Calculate the sum of the digits of a given number n recursively.
    
    :param n: int, the number whose digits will be summed
    :return: int, the sum of the digits
    """
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_of_digits(remaining_digits)

# Example usage
print(sum_of_digits(123))  # Output: 6
