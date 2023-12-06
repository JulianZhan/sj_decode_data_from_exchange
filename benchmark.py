import pytest
from decode_data import decode_new_file 

def test_decode_new_file_benchmark(benchmark):
    result = benchmark(decode_new_file, "sj_data_from_exchange.new")
