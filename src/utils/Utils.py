

class Utils:

    @staticmethod
    def get_int_value_from_string(string_value):
        value = None
        try:
            value = int(string_value)
        except Exception:
            pass
        
        return value