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

    if isinstance(data_type, str):
        # if data_type ends with "V99", convert the unpacked string to float
        if data_type.endswith("V99"):
            unpacked = float(unpacked[:-2] + "." + unpacked[-2:])
        # if data_type starts with "9" but not ends with "V99", convert the unpacked string to int
        elif data_type.startswith("9"):
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
    # convert hex to integer
    hex_data = int.from_bytes(hex_data, byteorder="big")
    # make integer into binary string with 8 bits
    # if input is 0x00, return should be 00000000
    return format(hex_data, "08b")


def should_decode_field(field_name, revelation_note):
    """
    Checks if the field should be decoded.

    Args:
        field_name (str): Field name.
        revelation_note (str): Revelation note as binary string.

    Returns:
        bool: True if the field should be decoded, False otherwise.
    """
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
    """
    Gets the level of the field. Level is the last number in the field name from buy and sell.

    Args:
        field_name (str): Field name.

    Returns:
        int: Level of the field.
    """
    # extract the last number from the field name
    try:
        return int(field_name.split("_")[-1])
    except ValueError:
        return 0


def process_stock_data_dynamic(stock_data, stock_data_structure):
    """
    Processes stock data with the given stock data structure.
    Trade and volume, buy and sell prices and volumes are decoded based on the revelation note dynamically.

    Args:
        stock_data (bytes): Stock data in bytes.
        stock_data_structure (StockDataStructure): Stock data structure.

    Returns:
        StockDataStructure: Processed stock data structure.
    """
    revelation_note = decode_from_hex_to_binary_string(stock_data[22:23])
    number_of_position_to_move = 0

    for field_name, field in stock_data_structure.fields.items():
        start_position = field.position[0]
        end_position = field.position[1]
        if should_decode_field(field_name, revelation_note):
            start_position -= number_of_position_to_move
            end_position -= number_of_position_to_move

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
