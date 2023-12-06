from decode_data_utils import *
from fields_structure_data import *
from fields_specifc_decode_utils import *


def should_decode_field(field_name, revelation_note):
    """
    Checks if the field should be decoded.

    Args:
        field_name (str): Field name.
        revelation_note (str): Revelation note as binary string.

    Returns:
        bool: True if the field should be decoded, False otherwise.
    """
    first_word = field_name.split("_")[0]
    if first_word == "cumulative":
        return True
    elif first_word == "trade" and revelation_note["trade_available"]:
        return True
    elif first_word == "buy" and get_field_level(field_name) <= revelation_note["n_bid"]:
        return True
    elif first_word == "sell" and get_field_level(field_name) <= revelation_note["n_ask"]:
        return True
    else:
        return False
    
def process_stock_data(stock_data):
    """
    Processes stock data with the given stock data structure.
    Trade and volume, buy and sell prices and volumes are decoded based on the revelation note dynamically.

    Args:
        stock_data (bytes): Stock data in bytes.
        sotck_transaction_structure (StockDataStructure): Stock data structure.

    Returns:
        StockDataStructure: Processed stock data structure.
    """
    stock_code_start, stock_code_end = sotck_transaction_structure.fields[
        "stock_code"
    ].position
    match_time_start, match_time_end = sotck_transaction_structure.fields[
        "match_time"
    ].position
    revelation_note_start, revelation_note_end = sotck_transaction_structure.fields[
        "revelation_note"
    ].position
    price_limit_mark_start, price_limit_mark_end = sotck_transaction_structure.fields[
        "price_limit_mark"
    ].position
    status_note_start, status_note_end = sotck_transaction_structure.fields[
        "status_note"
    ].position

    stock_code = decode_from_hex_with_ascii(stock_data[stock_code_start:stock_code_end])
    revelation_note = decode_from_hex_to_binary_string(
        stock_data[revelation_note_start:revelation_note_end]
    )
    match_time = unpack_bcd(
        stock_data[match_time_start:match_time_end], data_type="9(12)"
    )
    price_limit_mark = decode_from_hex_to_binary_string(
        stock_data[price_limit_mark_start:price_limit_mark_end]
    )
    status_note = decode_from_hex_to_binary_string(
        stock_data[status_note_start:status_note_end]
    )

    sotck_transaction_structure.fields["stock_code"].value = decode_stcok_code(stock_code)
    sotck_transaction_structure.fields["revelation_note"].value = decode_revelation_note(
        revelation_note
    )
    sotck_transaction_structure.fields["match_time"].value = decode_match_time(match_time)
    sotck_transaction_structure.fields["price_limit_mark"].value = decode_price_limit_mark(
        price_limit_mark
    )
    sotck_transaction_structure.fields["status_note"].value = decode_status_note(status_note)

    number_of_position_to_move = 0

    for field_name, field in sotck_transaction_structure.fields.items():
        start_position = field.position[0]
        end_position = field.position[1]
        if should_decode_field(field_name, sotck_transaction_structure.fields["revelation_note"].value):
            start_position -= number_of_position_to_move
            end_position -= number_of_position_to_move

            field_bytes = stock_data[start_position:end_position]
            if field.storing_type == "PACK BCD":
                field.value = unpack_bcd(field_bytes, data_type=field.data_type)
            elif field.storing_type == "BIT MAP":
                field.value = decode_from_hex_to_binary_string(field_bytes)
            elif field.storing_type == "ASCII":
                field.value = decode_from_hex_with_ascii(field_bytes)
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

    return sotck_transaction_structure
