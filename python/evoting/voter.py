class Voter:
    def __init__(self, name, id_number, pin):
        self.__name = name
        self.__id_number = id_number
        self.__pin = self.validate_pin(pin)
        self.__voted_position = set()

    def get_id_number(self):
        return self.__id_number

    def has_voted_for_positions(self, position):
        return position in self.__voted_position

    def get_voted_positions(self):
        return self.__voted_position

    def get_name(self):
        return self.__name

    def validate_pin(self, pin):
        pin_pattern = "^.{4}$"
        if not pin.match(pin_pattern):
            raise ValueError("Enter a valid pin. Must contain at least 4 characters.")

    def login(self, voter_id, pin):
        login_unsuccessfully = self.__id_number != voter_id or self.__pin != pin
        if login_unsuccessfully:
            raise Exception("Incorrect details. Please try again.")
        else:
            return True
