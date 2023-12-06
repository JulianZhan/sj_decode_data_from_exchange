def decode_revelation_note(revelation_note):
    return {
        "trade_available": bool(int(revelation_note[0])),
        "n_bid": int(revelation_note[1:4], 2),
        "n_ask": int(revelation_note[4:7], 2),
        "trade_only": bool(int(revelation_note[7]))
    }

def decode_price_limit_mark(value):
    transaction_type = ["normal", "limit_down", "limit_up"]
    price_trend = ["normal", "downward_trend", "upward_trend", "reserved"]

    return {
        "trade": transaction_type[int(value[0:2], 2)],
        "bid": transaction_type[int(value[2:4], 2)],
        "ask": transaction_type[int(value[4:6], 2)],
        "price_trend": price_trend[int(value[6:8], 2)]
    }


def decode_status_note(value):
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
    return stock_code.strip()