from src.utils.decode_data_utils import *
import pytest


def test_unpack_bcd_with_message_length():
    # test case from documentation
    # TSMC message length
    bcd_encoded_data = bytes([0x00, 0x95])
    decimal_string = unpack_bcd(bcd_encoded_data)
    assert decimal_string == "0095"
    assert remove_starting_zeros(decimal_string) == "95"


def test_unpack_bcd_with_cumulative_volume():
    # TSMC cumulative volume
    bcd_encoded_data = bytes([0x00, 0x01, 0x64, 0x23])
    decimal_string = unpack_bcd(bcd_encoded_data)
    assert decimal_string == "00016423"
    assert remove_starting_zeros(decimal_string) == "16423"


def test_remove_starting_zeros():
    assert remove_starting_zeros("00000000") == "0"
    assert remove_starting_zeros("00000001") == "1"
    assert remove_starting_zeros("00001000") == "1000"


def test_decode_from_hex_with_ascii():
    # TSMC code
    hex_data = bytes([0x32, 0x33, 0x33, 0x30, 0x20, 0x20])
    assert decode_from_hex_with_ascii(hex_data) == "2330  "


def test_decode_from_hex_to_binary_string():
    assert decode_from_hex_to_binary_string(bytes([0xD6])) == "11010110"
    assert decode_from_hex_to_binary_string(bytes([0x00])) == "00000000"
    assert decode_from_hex_to_binary_string(bytes([0xFF])) == "11111111"


def test_unpakc_bcd_with_data_type():
    # TSMC trade price
    bcd_encoded_data = bytes([0x00, 0x99, 0x50])
    decimal_string = unpack_bcd(bcd_encoded_data)
    assert decimal_string == "009950"
    assert remove_starting_zeros(decimal_string) == "9950"
    decimal_string = unpack_bcd(bcd_encoded_data, "9(4)V99")
    assert decimal_string == 99.50