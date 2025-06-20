def decimal_to_hex(decimal_number, num_bytes=4):
    """Converts a decimal integer to a hexadecimal string, handling negative numbers using two's complement.

    Args:
        decimal_number: An integer representing the decimal number.
        num_bytes: The number of bytes to represent the hexadecimal number (default: 4).
                   This determines the range of representable numbers.

    Returns:
        A string representing the hexadecimal value of the decimal number.
    """

    if decimal_number < 0:
        # Calculate two's complement
        max_value = 2**(num_bytes * 8)  # Maximum value for the given number of bytes
        hex_value = hex(max_value + decimal_number)[2:].upper().zfill(num_bytes * 2)
    else:
        hex_value = hex(decimal_number)[2:].upper().zfill(num_bytes * 2)  # Convert to hex, uppercase, pad with zeros

    return hex_value

# Example usage:
decimal_number = -3

hex_number = decimal_to_hex(decimal_number, num_bytes=2)
print(f"The hexadecimal representation of {decimal_number} is: {hex_number}")  # Output: FD5A

decimal_number = -2313441
hex_number = decimal_to_hex(decimal_number)
print(f"The hexadecimal representation of {decimal_number} is: {hex_number}") # Output: FFDCB31F
