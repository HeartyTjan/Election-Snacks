from unittest import TestCase

from project.evoting.registration import Registration
from project.evoting.voter import Voter
from project.evoting.candidate import Candidate


class TestVoter(TestCase):
    def test_cast_vote_add_one_to_canidate(self):
        reg = Registration()
        voter = reg.register_voter("Ahmaed tobiloba",  "password")
        candidate = reg.register_candidate("Ahmaed tobiloba",  "President")
        voter.cast_vote(candidate.get_id_number())
        self.assertEqual(1, candidate.get_vote_count())
