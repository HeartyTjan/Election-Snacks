class Candidate:

    def __init__(self, name, id_number, position):
        self.__name = name
        self.__id_number = id_number
        self.__position = position
        self.__vote_count = 0

    def get_id_number(self):
        return self.__id_number

    def get_position(self):
        return self.__position

    def get_vote_count(self):
        return self.__vote_count

    def add_vote(self):
        self.__vote_count += 1

    def get_name(self):
        return self.__name

    def display_candidate(self):
        print(f"{self.__id_number:^10} {self.__name:^25}  {self.__position:>13}")
