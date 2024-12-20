from project.evoting.candidate import Candidate
from project.evoting.voter import Voter


class Registration:

    voters = []

    def __init__(self):
        self.candidates = []
        self.number_of_voter = 0
        self.number_of_candidate = 0

    def register_candidate(self, name, position):
        id_number = self.generate_candidate_id()
        candidate = Candidate(name, id_number, position)
        self.candidates.append(candidate)
        return candidate

    def register_voter(self, name, pin):
        id_number = self.generate_voter_id()
        voter = Voter(name, id_number, pin)
        self.voters.append(voter)
        return voter

    def generate_voter_id(self):
        self.number_of_voter += 1
        return "v" + str(self.number_of_voter + 10)

    def generate_candidate_id(self):
        self.number_of_candidate += 1
        return "c" + str(self.number_of_candidate + 10)

    def find_candidate_by_id(self, id_number):
        for candidate in self.candidates:
            if candidate.get_id_number() == id_number:
                return candidate

        raise Exception("Candidate not found", id_number)

    def find_voter_by_id(self, id_number):
        for voter in self.voters:
            if voter.get_id_number() == id_number:
                return voter

        raise Exception("Voter not found")

    def display_candidate(self):
        for candidate in self.candidates:
            print(candidate.get_name())

    def get_candidates(self):
        return self.candidates


