def decode_revelation_note(value):
    """
    Format revelation note to make it more readable

    Args:
        revelation_note (str): Revelation note in binary string.

    Returns:
        dict: Decoded revelation note.
    """
    return {
        "trade_available": bool(int(value[0])),
        "n_bid": int(value[1:4], 2),
        "n_ask": int(value[4:7], 2),
        "trade_only": bool(int(value[7]))
    }

def decode_price_limit_mark(value):
    """
    Format price limit mark to make it more readable

    Args:
        value (str): Price limit mark in binary string.

    Returns:
        dict: Decoded price limit mark.
    """
    transaction_type = ["normal", "limit_down", "limit_up"]
    price_trend = ["normal", "downward_trend", "upward_trend", "reserved"]

    return {
        "trade": transaction_type[int(value[0:2], 2)],
        "bid": transaction_type[int(value[2:4], 2)],
        "ask": transaction_type[int(value[4:6], 2)],
        "price_trend": price_trend[int(value[6:8], 2)]
    }


def decode_status_note(value):
    """
    Format status note to make it more readable

    Args:
        value (str): Status note in binary string.

    Returns:
        dict: Decoded status note.
    """
    trial_calc_status = ["normal", "trial"]
    delayed = [False, True]
    matching_method = ["aggregate", "individual"]

    return {
        "trial_calc_status": trial_calc_status[int(value[0])],
        "delayed_opening": delayed[int(value[1])],
        "delayed_closing": delayed[int(value[2])],
        "matching_method": matching_method[int(value[3])]
    }

def decode_match_time(unpacked_time):
    """
    Format match time to make it more readable

    Args:
        unpacked_time (int): Match time in unpacked BCD format.

    Returns:
        dict: Decoded match time.
    """
    unpacked_time = str(unpacked_time)
    if len(unpacked_time) == 12:
        return {
            "hours": int(unpacked_time[0:2]),
            "Minutes": int(unpacked_time[2:4]),
            "Seconds": int(unpacked_time[4:6]),
            "Milliseconds": int(unpacked_time[6:9]),
            "Microseconds": int(unpacked_time[9:12])
        }
    else:
        return {
            "hours": int(unpacked_time[0:1]),
            "Minutes": int(unpacked_time[1:3]),
            "Seconds": int(unpacked_time[3:5]),
            "Milliseconds": int(unpacked_time[5:8]),
            "Microseconds": int(unpacked_time[8:11])
        }

def decode_stcok_code(stock_code):
    """
    Remove leading and trailing spaces from stock code

    Args:
        stock_code (str): Stock code.

    Returns:
        str: Stock code without leading and trailing spaces.
    """
    return stock_code.strip()