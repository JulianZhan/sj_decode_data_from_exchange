import logging
from decode_data_utils import *
from fields_structure_data import *

logging.basicConfig(level=logging.ERROR)

def read_file(file_name):
    with open(file_name, "rb") as f:
        file_data = f.read()
    return file_data


def decode_data(data):
    processed_records = []

    start = 0
    start_marker = b"\x1b"
    end_marker = b"\r\n"
    len_end_marker = len(end_marker)

    while True:
        start = data.find(start_marker, start)  
        # if start not found anymore, break
        if start == -1:
            break  

        end = data.find(end_marker, start) 
        # if end not found anymore, break
        if end == -1:
            break  

        end += len_end_marker
        record_data = data[start:end]

        try:
            processed_record = process_stock_data_dynamic(
                record_data, sotck_transaction_structure_6
            )
            processed_records.append(processed_record)
        except Exception as e:
            logging.error(f"Error processing record at {start}-{end}: {e}")

        start = end

    return processed_records


