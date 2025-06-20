def hex_xor(hex_num1, hex_num2):
    """
    Calculates the XOR of two hexadecimal numbers.

    Args:
        hex_num1: The first hexadecimal number as a string.
        hex_num2: The second hexadecimal number as a string.

    Returns:
        The XOR of the two numbers in hexadecimal format (string).
    """
    # Convert hexadecimal strings to integers (base 16)
    num1 = int(hex_num1, 16)
    num2 = int(hex_num2, 16)

    # Calculate the XOR
    xor_result = num1 ^ num2

    # Convert the result back to hexadecimal
    hex_result = hex(xor_result)[2:].upper()  # [2:] removes the "0x" prefix, upper() for uppercase

    return hex_result

# Example usage
hex_number1 = "FFFFFFCEC5BEB9C0"
hex_number2 = "05F1"
xor_result = hex_xor(hex_number1, hex_number2)
print(f"The XOR of {hex_number1} and {hex_number2} is: {xor_result}")
