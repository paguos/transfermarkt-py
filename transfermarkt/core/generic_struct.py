class GenericStruct:

    def __init__(self, **entries):
        self.__dict__.update(entries)

    def to_dict(self) -> dict:
        return self.__dict__

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, GenericStruct):
            print("struct!")
            return self.to_dict() == other.to_dict()

        if isinstance(other, dict):
            print("dict!")
            return self.to_dict() == other

        print("something else!")
        return False
