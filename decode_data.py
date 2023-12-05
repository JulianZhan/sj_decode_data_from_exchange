import time
from decode_data_utils import *
from fields_structure_data import *

def timing_decorator(repetitions):
    def func_parser(func):
        def wrapper(*args, **kwargs):
            total_time = 0
            result = None 
            for _ in range(repetitions):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)  
                end_time = time.perf_counter()
                total_time += end_time - start_time
            avg_time = total_time / repetitions
            print(f"Average time per execution over {repetitions} repetitions: {avg_time} seconds")
            return result  
        return wrapper  
    return func_parser  


@timing_decorator(100)
def decode_new_file(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()

    processed_records = []

    start = 0
    end = 0

    while end < len(file_data):
        if is_beginning_of_message(file_data[end : end + 1]):
            start = end

        if is_end_of_message(file_data[end : end + 2]):
            end += 2
            record_data = file_data[start:end]
            if len(record_data) <= 20:
                continue

            processed_record = process_stock_data_dynamic(
                record_data, sotck_transaction_structure_6
            )

            processed_records.append(processed_record)

            start = end

        end += 1

    return processed_records

decoded_file = decode_new_file("sj_data_from_exchange.new")