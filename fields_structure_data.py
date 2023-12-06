from fields_structure_template import Field, StockTransactionStructure

sotck_transaction_structure = StockTransactionStructure(
    {
        "stock_code": Field("stock_code", (10, 16), "X(06)", "ASCII"),
        "match_time": Field("match_time", (16, 22), "9(12)", "PACK BCD"),
        "revelation_note": Field("revelation_note", (22, 23), "X(01)", "BIT MAP"),
        "price_limit_mark": Field("price_limit_mark", (23, 24), "X(01)", "BIT MAP"),
        "status_note": Field("status_note", (24, 25), "X(01)", "BIT MAP"),
        "cumulative_volume": Field("cumulative_volume", (25, 29), "9(08)", "PACK BCD"),
        "trade_price": Field("trade_price", (29, 32), "9(4)V99", "PACK BCD"),
        "trade_volume": Field("trade_volume", (32, 36), "9(08)", "PACK BCD"),
        "buy_price_1": Field("buy_price_1", (36, 39), "9(4)V99", "PACK BCD"),
        "buy_volume_1": Field("buy_volume_1", (39, 43), "9(08)", "PACK BCD"),
        "buy_price_2": Field("buy_price_2", (43, 46), "9(4)V99", "PACK BCD"),
        "buy_volume_2": Field("buy_volume_2", (46, 50), "9(08)", "PACK BCD"),
        "buy_price_3": Field("buy_price_3", (50, 53), "9(4)V99", "PACK BCD"),
        "buy_volume_3": Field("buy_volume_3", (53, 57), "9(08)", "PACK BCD"),
        "buy_price_4": Field("buy_price_4", (57, 60), "9(4)V99", "PACK BCD"),
        "buy_volume_4": Field("buy_volume_4", (60, 64), "9(08)", "PACK BCD"),
        "buy_price_5": Field("buy_price_5", (64, 67), "9(4)V99", "PACK BCD"),
        "buy_volume_5": Field("buy_volume_5", (67, 71), "9(08)", "PACK BCD"),
        "sell_price_1": Field("sell_price_1", (71, 74), "9(4)V99", "PACK BCD"),
        "sell_volume_1": Field("sell_volume_1", (74, 78), "9(08)", "PACK BCD"),
        "sell_price_2": Field("sell_price_2", (78, 81), "9(4)V99", "PACK BCD"),
        "sell_volume_2": Field("sell_volume_2", (81, 85), "9(08)", "PACK BCD"),
        "sell_price_3": Field("sell_price_3", (85, 88), "9(4)V99", "PACK BCD"),
        "sell_volume_3": Field("sell_volume_3", (88, 92), "9(08)", "PACK BCD"),
        "sell_price_4": Field("sell_price_4", (92, 95), "9(4)V99", "PACK BCD"),
        "sell_volume_4": Field("sell_volume_4", (95, 99), "9(08)", "PACK BCD"),
        "sell_price_5": Field("sell_price_5", (99, 102), "9(4)V99", "PACK BCD"),
        "sell_volume_5": Field("sell_volume_5", (102, 106), "9(08)", "PACK BCD"),
    }
)
