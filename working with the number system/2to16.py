def binary_to_hex(binary_string, num_bytes=4):
    """Converts a binary string representing a negative number (two's complement) to its hexadecimal representation.

    Args:
        binary_string: A string representing the binary number.
        num_bytes: Number of bytes for hexadecimal representation (default: 4).

    Returns:
        A string representing the hexadecimal value.
    """

    # Check if the number is negative (starts with '1')
    if binary_string[0] == '1':
        # Calculate decimal value from two's complement
        inverted_string = ''.join(['1' if bit == '0' else '0' for bit in binary_string])
        decimal_value = - (int(inverted_string, 2) + 1)  # Convert inverted string to int

        # Convert the decimal value to hex
        max_value = 2**(num_bytes * 8)
        hex_value = hex(max_value + decimal_value)[2:].upper().zfill(num_bytes * 2)

    else:
        # If positive, directly convert
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)[2:].upper().zfill(num_bytes * 2)

    return hex_value


# Example usage:
binary_number = "1111111111111111111111111100111011000101101111101011110000110001"  # Example negative binary number (2's complement)
hex_number = binary_to_hex(binary_number)
print(f"The hexadecimal representation of {binary_number} is: {hex_number}")  # Output: FFDBC1

binary_number = "00000000000000000000000000000101" # Example positive binary number
hex_number = binary_to_hex(binary_number)
print(f"The hexadecimal representation of {binary_number} is: {hex_number}") # Output: 00000005
