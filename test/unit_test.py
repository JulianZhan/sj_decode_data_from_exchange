from decode_data_utils import unpack_bcd, remove_starting_zeros
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
    assert remove_starting_zeros("") == "0"
