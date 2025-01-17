def calculate_even_numbers(n):
    """
    This function returns a list of even numbers from 0 to n (inclusive).
    
    :param n: The upper limit of the range.
    :return: A list of even numbers from 0 to n.
    """
    even_numbers = [num for num in range(n + 1) if num % 2 == 0]
    return even_numbers

# Example usage:
upper_limit = 10
even_numbers_list = calculate_even_numbers(upper_limit)
print(f"Even numbers from 0 to {upper_limit}: {even_numbers_list}")
