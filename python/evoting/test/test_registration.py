import unittest

from project.evoting.registration import Registration


class TestRegistration(unittest.TestCase):
    def test_register_candidate_add_one_to_candidate_list(self):
        registration = Registration()
        self.assertEqual(0, len(registration.get_candidates()))
        registration.register_candidate("Name", "President")
        self.assertEqual(1, len(registration.get_candidates()))

    def test_register_candidate_add_two_candidates(self):
        registration = Registration()
        self.assertEqual(0, len(registration.get_candidates()))
        registration.register_candidate("Name", "President")
        registration.register_candidate("Name Two", "President")
        self.assertEqual(2, len(registration.get_candidates()))
