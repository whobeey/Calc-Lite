# Initializing a "private" class for managing CTk item dimensions (size)
class _Size:
    # Dunder Method, to initialize attributes of the class
    def __init__(self, width, height) -> None:
        object.__setattr__(self, "WIDTH", width)    
        object.__setattr__(self, "HEIGHT", height)

    # Method Purpose: return a suitable argument for geometry size
    def geometry(self) -> str: 
        return f"\"{self.WIDTH}x{self.HEIGHT}\""

    # "self.attribute = value" raises the following method, preventing attribute modification
    def __setattr__(self, attribute, value) -> None:
        raise TypeError("Error. Unable to modify information")

    # "del self.attribute" raises the following method, preventing attribute deletion
    def __delattr__(self, attribute) -> None:
        raise TypeError("Error. Unable to delete information")

# Dictionary, a directory-style approach to getting
item_size = {
    "XSS": _Size(32, 32),
    "XS": _Size(64, 64),
    "S": _Size(96, 96),
    "M": _Size(128, 128),
    "L": _Size(194, 194),
    "XL": _Size(256, 256),
    "XXL": _Size(512, 512),
    
    "DOT" : _Size(0, 0),
    "BTN" : _Size(0, 0),
    "SQR" : _Size(0, 0),
} 