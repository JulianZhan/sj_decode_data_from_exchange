class Field:
    def __init__(self, name, position, data_type, storing_type, value=None):
        self.name = name
        self.position = position
        self.data_type = data_type
        self.storing_type = storing_type
        self.value = value

    def __repr__(self):
        return f"Field({self.name}, {self.position}, {self.data_type}, {self.storing_type}, {self.value})"


class StockTransactionStructure:
    def __init__(self, fields):
        self.fields = fields

    def get_field(self, field_name):
        return self.fields.get(field_name)
