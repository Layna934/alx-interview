#!/usr/bin/python3
"""UTF-8 validation module.
"""
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    expected_bytes = 0

    for num in data:
        byte = num & 0xFF

        if expected_bytes == 0:
            # Determine the number of expected bytes based on the leading bits
            if (byte & 0b10000000) == 0:  # 1-byte character (0xxxxxxx)
                expected_bytes = 0  # No additional bytes expected
            elif (byte & 0b11100000) == 0b11000000:  # 2-byte character (110xxxxx)
                expected_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:  # 3-byte character (1110xxxx)
                expected_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:  # 4-byte character (11110xxx)
                expected_bytes = 3
            else:
                return False  # Invalid leading byte
        else:
            # For continuation bytes, they must start with '10'
            if (byte & 0b11000000) != 0b10000000:
                return False

        expected_bytes -= 1

    return expected_bytes == 0

