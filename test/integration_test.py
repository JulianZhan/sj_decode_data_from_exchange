from fields_structure_data import *
from test_data import *
from expected_data import *
from decode_data_utils import *
from decode_data import *


def test_tsmc_stock_data():
    decoded_data = process_stock_data(tsmc_data)

    for key in expected_data_tsmc:
        assert decoded_data.fields[key].value == expected_data_tsmc[key]


def test_2002_stock_data():
    decoded_data = process_stock_data(data_2002)

    for key in expected_data_2002:
        assert decoded_data.fields[key].value == expected_data_2002[key]


def test_1504_stock_data():
    decoded_data = process_stock_data(data_1504)

    for key in expected_data_1504:
        assert decoded_data.fields[key].value == expected_data_1504[key]


def test_1301_stock_data():
    decoded_data = process_stock_data(data_1301)

    for key in expected_data_1301:
        assert decoded_data.fields[key].value == expected_data_1301[key]


def test_decode_data_function():
    decoded_data_tsmc = decode_data(tsmc_data)
    
    for key in expected_data_tsmc:
        assert decoded_data_tsmc[0].fields[key].value == expected_data_tsmc[key]

    decoded_data_2002 = decode_data(data_2002)
    
    for key in expected_data_2002:
        assert decoded_data_2002[0].fields[key].value == expected_data_2002[key]

    decoded_data_1504 = decode_data(data_1504)
    
    for key in expected_data_1504:
        assert decoded_data_1504[0].fields[key].value == expected_data_1504[key]

    decoded_data_1301 = decode_data(data_1301)
    
    for key in expected_data_1301:
        assert decoded_data_1301[0].fields[key].value == expected_data_1301[key]
