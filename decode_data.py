import logging
from decode_data_utils import *
from fields_structure_data import *

logging.basicConfig(level=logging.ERROR)

def decode_new_file(file_path):
    processed_records = []

    with open(file_path, "rb") as file:
        file_data = file.read()

    start = 0
    start_marker = b"x1b"
    end_marker = b"\r\n"
    len_end_marker = len(end_marker)

    while True:
        start = file_data.find(start_marker, start)  
        # if start not found anymore, break
        if start == -1:
            break  

        end = file_data.find(end_marker, start) 
        # if end not found anymore, break
        if end == -1:
            break  

        end += len_end_marker
        record_data = file_data[start:end]

        try:
            processed_record = process_stock_data_dynamic(
                record_data, sotck_transaction_structure_6
            )
            processed_records.append(processed_record)
        except Exception as e:
            logging.error(f"Error processing record at {start}-{end}: {e}")

        start = end

    return processed_records

