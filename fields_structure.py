FIELDS_STRUCTURE_6 = {
    "esc_code": {"position": (0, 1), "length": 1, "type": "ASCII"},
    "message_length": {"position": (1, 3), "length": 2, "type": "PACK BCD"},
    "business_type": {"position": (3, 4), "length": 1, "type": "PACK BCD"},
    "transmission_format_code": {"position": (4, 5), "length": 1, "type": "PACK BCD"},
    "transmission_format_version": {
        "position": (5, 6),
        "length": 1,
        "type": "PACK BCD",
    },
    "transmission_number": {"position": (6, 10), "length": 4, "type": "PACK BCD"},
    "stock_code": {"position": (10, 16), "length": 6, "type": "ASCII"},
    "match_time": {"position": (16, 22), "length": 6, "type": "PACK BCD"},
    "revelation_note": {"position": (22, 23), "length": 1, "type": "BIT MAP"},
    "price_limit_mark": {"position": (23, 24), "length": 1, "type": "BIT MAP"},
    "status_note": {"position": (24, 25), "length": 1, "type": "BIT MAP"},
    "cumulative_volume": {
        "position": (25, 29),
        "length": 4,
        "type": "PACK BCD",
    },
    # other fileds here
    "check_sum": {"position": "dynamic", "length": 1, "type": "XOR"},
    "terminal-code": {"position": "dynamic", "length": 2, "type": "HEXACODE"},
}
