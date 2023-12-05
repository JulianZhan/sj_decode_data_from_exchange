import numpy as np


def unpack_bcd(bcd_data, data_type=None):
    """
    Unpacks pack BCD data in hex format to decimal.

    Args:
        bcd_data (bytes): BCD data in hex format, multiple bytes.

    Returns:
        if data_type ends with "V99", return float.
        if data_type starts with "9" but not ends with "V99", return int.
        otherwise, return str.
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

    # if data_type ends with "V99", convert the unpacked string to float
    if isinstance(data_type, str) and data_type.endswith("V99"):
        unpacked = unpacked[:-2] + "." + unpacked[-2:]
        unpacked = float(unpacked)
    # if data_type starts with "9" but not ends with "V99", convert the unpacked string to int
    elif isinstance(data_type, str) and data_type.startswith("9"):
        unpacked = int(unpacked)
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
        hex_data (bytes): Hex data, multiple bytes.

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
        hex_data (int): Hex data, one byte.

    Returns:
        str: Binary string with eight bits.
    """
    # convert hex to binary string
    hex_data = int.from_bytes(hex_data, byteorder="big")
    decoded = np.base_repr(hex_data, base=2)
    # pad with zeros to make sure the string is 8 bits long
    # if input is 0x00, return should be 00000000
    return decoded.zfill(8)


def is_beginning_of_message(hex_data):
    """
    Checks if the data is the beginning of a message.

    Args:
        hex_data (bytes): Hex data, one byte.

    Returns:
        bool: True if the data is the beginning of a message, False otherwise.
    """
    # check if the byte is 0x1B
    return hex_data == b"\x1b"


def is_end_of_message(hex_data):
    """
    Checks if the data is the end of a message.

    Args:
        hex_data (bytes): Hex data, two bytes.

    Returns:
        bool: True if the data is the end of a message, False otherwise.
    """
    # check if these two bytes are 0x0D and 0x0A
    return hex_data[0] == b"\x0d" and hex_data[1] == b"\x0A"


def calculate_xor_checksum(data, skip_the_beginning=1, skip_the_end=-3):
    """
    Calculates the XOR checksum of the data, excluding the first and last three bytes.

    Args:
        data (bytes): Hex data, multiple bytes.

    Returns:
        int: XOR checksum.
    """
    checksum = 0
    for byte in data[skip_the_beginning:skip_the_end]:
        # XOR the checksum with the current byte
        checksum ^= byte
    return checksum


def should_decode_field(field_name, revelation_note):
    if not field_name.startswith("buy_") and not field_name.startswith("sell_"):
        return True

    # trade price and volume (bit 7)
    if revelation_note[0] == "1" and field_name in set(("trade_price", "trade_volume")):
        return True

    # if bit 0 is 1, skip prices and volumes for both buy and sell
    if revelation_note[7] == "1" and (
        field_name.startswith("buy_") or field_name.startswith("sell_")
    ):
        return False

    # buy price and volume (bit 6-4)
    num_buy_levels = int(revelation_note[1:4], 2)  # binary to integer
    if field_name.startswith("buy_") and _get_field_level(field_name) <= num_buy_levels:
        return True

    # sell price and volume (Bit 3-1)
    num_sell_levels = int(revelation_note[4:7], 2)  # binary to integer
    if (
        field_name.startswith("sell_")
        and _get_field_level(field_name) <= num_sell_levels
    ):
        return True

    return False


def _get_field_level(field_name):
    # extract the last number from the field name
    try:
        return int(field_name.split("_")[-1])
    except ValueError:
        return 0


def process_stock_data(stock_data, stock_data_structure):
    """
    Processes stock data based on the given stock data structure.

    Args:
        stock_data (bytes): Hex data, multiple bytes.
        stock_data_structure (StockTransactionStructure): Stock data structure.

    Returns:
        StockTransactionStructure: Stock data structure with values.
    """

    for field in stock_data_structure.fields.values():
        # get the bytes of the field
        field_bytes = stock_data[field.position[0] : field.position[1]]

        # decode the bytes based on the storing type
        if field.storing_type == "ASCII":
            field.value = decode_from_hex_with_ascii(field_bytes)
        elif field.storing_type == "PACK BCD":
            field.value = unpack_bcd(field_bytes, data_type=field.data_type)
        elif field.storing_type == "BIT MAP":
            field.value = decode_from_hex_to_binary_string(field_bytes)
        else:
            field.value = field_bytes

    return stock_data_structure


def process_stock_data_dynamic(stock_data, stock_data_structure):
    revelation_note = decode_from_hex_to_binary_string(stock_data[22:23])
    number_of_position_to_move = 0

    for field_name, field in stock_data_structure.fields.items():
        start_position = field.position[0]
        end_position = field.position[1]
        if should_decode_field(field_name, revelation_note):
            start_position -= number_of_position_to_move
            end_position -= number_of_position_to_move
            # Decode the field
            field_bytes = stock_data[start_position:end_position]
            if field.storing_type == "ASCII":
                field.value = decode_from_hex_with_ascii(field_bytes)
            elif field.storing_type == "PACK BCD":
                field.value = unpack_bcd(field_bytes, data_type=field.data_type)
            elif field.storing_type == "BIT MAP":
                field.value = decode_from_hex_to_binary_string(field_bytes)
            else:
                field.value = field_bytes
        else:
            if field_name == "trade_price":
                number_of_position_to_move += 3
            elif field_name == "trade_volume":
                number_of_position_to_move += 4
            elif field_name.split("_")[1] == "price":
                number_of_position_to_move += 3
            elif field_name.split("_")[1] == "volume":
                number_of_position_to_move += 4

    return stock_data_structure
