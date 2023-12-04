from fields_structure_data import sotck_transaction_structure_tsmc
from test_data import tsmc_data
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
