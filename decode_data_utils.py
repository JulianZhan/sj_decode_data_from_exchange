import numpy as np


def unpack_bcd(bcd_data):
    """
    Unpacks pack BCD data in hex format to decimal as a string.

    Args:
        bcd_data (bytes): BCD data in hex format.

    Returns:
        str: Decimal string.
    """

    # initialize unpacked string
    unpacked = ""
    # iterate over each byte in the data
    for byte in bcd_data:
        # a byte is 8 bits, a nibble is 4 bits
        # the high nibble is the first 4 bits, the low nibble is the last 4 bits
        # shift the byte 4 bits to the right to get the high nibble
        high_nibble = byte >> 4
        # 0x0F is 00001111 in binary
        # using a bitwise AND will return the low nibble
        low_nibble = byte & 0x0F
        # concatenate the high and low nibbles to the unpacked string
        unpacked += str(high_nibble) + str(low_nibble)
    return unpacked


def remove_starting_zeros(decimal_string):
    """
    After unpacking BCD data, the resulting decimal string may have starting zeros.
    This function removes the starting zeros.

    Args:
        decimal_string (str): Decimal string.

    Returns:
        str: Decimal string without starting zeros.
    """
    # remove starting zeros, if there are no digits left after unpacking, return "0"
    return decimal_string.lstrip("0") or "0"


def decode_from_hex_with_ascii(hex_data):
    """
    Decodes data from hex format with ASCII encoding.

    Args:
        hex_data (bytes): Hex data.

    Returns:
        str: Decoded string.
    """
    # convert each byte to ASCII with chr()
    decoded = [chr(byte) for byte in hex_data]
    # join the list of strings into one string
    return "".join(decoded)


def decode_from_hex_to_binary_string(hex_data):
    """
    decodes data from hex format to binary string.

    Args:
        hex_data (int): Hex data.

    Returns:
        str: Binary string with eight bits.
    """
    # convert hex to binary string
    decoded = np.base_repr(hex_data, base=2)
    # pad with zeros to make sure the string is 8 bits long
    # if input is 0x00, return should be 00000000
    return decoded.zfill(8)
