from fields_structure_data import *
from test_data import *
from decode_data_utils import *


def test_tsmc_stock_data():
    # TSMC stock data
    expected_data = {
        "esc_code": b"\x1b",
        "message_length": 95,
        "business_type": 1,
        "transmission_format_code": 6,
        "transmission_format_version": 3,
        "transmission_number": 4567,
        "stock_code": "2330  ",
        "match_time": 90415061278,
        "revelation_note": "11010110",
        "price_limit_mark": "00000000",
        "status_note": "00000000",
        "cumulative_volume": 16423,
        "trade_price": 99.50,
        "trade_volume": 1234,
        "buy_price_1": 99.50,
        "buy_volume_1": 250,
        "buy_price_2": 99.00,
        "buy_volume_2": 175,
        "buy_price_3": 98.50,
        "buy_volume_3": 477,
        "buy_price_4": 97.50,
        "buy_volume_4": 669,
        "buy_price_5": 97.00,
        "buy_volume_5": 125,
        "sell_price_1": 100.00,
        "sell_volume_1": 80,
        "sell_price_2": 100.50,
        "sell_volume_2": 675,
        "sell_price_3": 101.50,
        "sell_volume_3": 460,
        "check_sum": b"\xfb",
        "terminal_code": b"\x0d\x0a",
    }

    decoded_data = process_stock_data(tsmc_data, sotck_transaction_structure_tsmc)

    for key in expected_data:
        assert decoded_data.fields[key].value == expected_data[key]


def test_2002_stock_data():
    expected_data = {
        "esc_code": b"\x1b",
        "message_length": 73,
        "business_type": 1,
        "transmission_format_code": 6,
        "transmission_format_version": 3,
        "transmission_number": 64323,
        "stock_code": "2002  ",
        "match_time": 102733165041,
        "revelation_note": "11010000",
        "price_limit_mark": "10100000",
        "status_note": "00000000",
        "cumulative_volume": 11921,
        "trade_price": 13.85,
        "trade_volume": 1921,
        "buy_price_1": 13.85,
        "buy_volume_1": 540,
        "buy_price_2": 13.80,
        "buy_volume_2": 230,
        "buy_price_3": 13.75,
        "buy_volume_3": 72,
        "buy_price_4": 13.70,
        "buy_volume_4": 69,
        "buy_price_5": 13.65,
        "buy_volume_5": 81,
        "check_sum": b"\x6e",
        "terminal_code": b"\x0d\x0a",
    }
    decoded_data = process_stock_data(data_2002, sotck_transaction_structure_2002)

    for key in expected_data:
        assert decoded_data.fields[key].value == expected_data[key]


def test_1504_stock_data():
    expected_data = {
        "esc_code": b"\x1b",
        "message_length": 65,
        "business_type": 1,
        "transmission_format_code": 6,
        "transmission_format_version": 3,
        "transmission_number": 41234,
        "stock_code": "1504  ",
        "match_time": 95023271534,  # This is a placeholder, adjust as needed
        "revelation_note": "10001010",
        "price_limit_mark": "01000100",
        "status_note": "00000000",
        "cumulative_volume": 650,
        "trade_price": 11.50,
        "trade_volume": 17,
        "sell_price_1": 11.50,
        "sell_volume_1": 70,
        "sell_price_2": 11.55,
        "sell_volume_2": 35,
        "sell_price_3": 11.60,
        "sell_volume_3": 46,
        "sell_price_4": 11.65,
        "sell_volume_4": 28,
        "sell_price_5": 11.70,
        "sell_volume_5": 19,
        "check_sum": b"\xa2",
        "terminal_code": b"\x0d\x0a",
    }

    decoded_data = process_stock_data(data_1504, sotck_transaction_structure_1504)

    for key in expected_data:
        assert decoded_data.fields[key].value == expected_data[key]
