class ValidatorUtil:

    @staticmethod
    def isValidString(val):
        return len(val) != 0

    @staticmethod
    def isValidCode(val):
        return len(val) != 0 and val.isalnum()

    @staticmethod
    def isValidInt(val):
        if isinstance(val, int):
            return True
        if val.isnumeric():
            return True
        return False

    @staticmethod
    def isValidFloat(val):
        try:
            float(val)
            return True
        except ValueError:
            return False