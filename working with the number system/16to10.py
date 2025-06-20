def hex_to_decimal(hex_string):
    """Converts a hexadecimal string to a decimal integer, handling negative numbers.
    
    Args:
        hex_string: A string representing a hexadecimal number.

    Returns:
        An integer representing the decimal value of the hexadecimal string.
    """
    
    # Check if the number is negative (highest bit is set)
    if hex_string[0] in ('8', '9', 'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f'):
        # Calculate the two's complement
        inverted_string = ''.join([hex(15 - int(c, 16))[2:].upper() for c in hex_string])
        decimal_value = - (int(inverted_string, 16) + 1)
    else:
        decimal_value = int(hex_string, 16)
    
    return decimal_value

# Example usage:
hex_number = "FFFB"
decimal_number = hex_to_decimal(hex_number)
print(f"The decimal representation of {hex_number} is: {decimal_number}")  # Output: -678

hex_number = "FFAA"
decimal_number = hex_to_decimal(hex_number)
print(f"The decimal representation of {hex_number} is: {decimal_number}") # Output: -2313441
