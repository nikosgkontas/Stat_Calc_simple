def stat_calc(numbers):
    """
    Calculates and returns the maximum, minimum, mean, and variance of a list of numbers.

    Args:
        numbers (list): A list of numerical values.

    Returns:
        tuple: A tuple containing (maximum, minimum, mean, variance).
    """
    # Ensure the input list is not empty to avoid errors
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    # Calculate maximum and minimum
    max_val = max(numbers)
    min_val = min(numbers)

    # Calculate mean using a standard function instead of a lambda expression for clarity
    mean_val = sum(numbers) / len(numbers)

    # Calculate variance using a standard function instead of a lambda expression for clarity
    variance_val = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)

    return max_val, min_val, mean_val, variance_val

# Example usage:
numbers_list = [10, 20, 15, 30, 25]
max_val, min_val, mean_val, variance_val = stat_calc(numbers_list)
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")
print(f"Mean: {mean_val:.2f}")
print(f"Variance: {variance_val:.2f}")
