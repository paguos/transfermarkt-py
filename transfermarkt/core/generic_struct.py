class GenericStruct:

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def to_dict(self) -> dict:
        return self.__dict__

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, GenericStruct):
            return self.to_dict() == other.to_dict()

        if isinstance(other, dict):
            return self.to_dict() == other

        return False
