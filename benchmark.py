import pytest
from decode_data import decode_data, read_file

def test_decode_new_file_benchmark(benchmark):
    data = read_file("sj_data_from_exchange.new")
    benchmark(decode_data, data)
