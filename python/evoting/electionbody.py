import sys

from project.evoting.registration import Registration


class ElectionBody:
    VALID_POSITION = ["president", "vice-president", "governor", "senator"]

    def __init__(self, election_category):
        self.registration = Registration()
        self.election_category = election_category
        self.logged_in_voter = None

    def validate_position(self, position):
        if position not in self.VALID_POSITION:
            return False
        return True

    def display_registration_menu(self):

        print("""
              Registration  Menu
        ====================================
        1 -> Voter Registration
        2 -> Candidate Registration
        3 -> Login
      =======================================
        
        """)
        option = input("Enter preferred option : ")
        match option:
            case "1":
                self.register_voter()

            case "2":
                self.register_candidate()

            case "3":
                self.login()

            case _:
                print("Invalid option")
                self.display_registration_menu()

    def register_voter(self):
        name = input("Enter your full name : ")
        pin = input("Enter your pin : ")

        try:
            voter = self.registration.register_voter(name, pin)
            print("Your Id is : ", voter.get_id_number())

        except ValueError as err:
            print(err)
        finally:
            self.display_registration_menu()

    def register_candidate(self):
        name = input("Enter your full name : ")
        position = input("Enter your position : ").lower()

        if not self.validate_position(position):
            print("Invalid position. Please enter a valid position")
            return self.register_candidate()

        try:
            candidate = self.registration.register_candidate(name, position)
            print("Your id is : ", candidate.get_id_number())

        except ValueError as err:
            print(err)
        finally:
            self.display_registration_menu()

    def login(self):

        voter_id = input("Enter your id :").lower()
        pin = input("Enter your pin :")
        try:
            voter = self.registration.find_voter_by_id(voter_id)

            is_successful = voter.login(voter_id, pin)
            if is_successful:
                self.logged_in_voter = voter

                print("==============================================")
                print(f"Welcome back {voter.get_name().upper()}")
                print("==============================================")

                self.display_election_menu()
            else:
                print("Invalid credentials")
                self.display_registration_menu()

        except ValueError as err:
            print(err)

        except Exception as err:
            print(err)

        finally:
            self.display_registration_menu()

    def display_election_menu(self):
        print("""
                Election Menu
        =====================================
           1 -> Cast Vote for Candidate
           2 -> Display Result
           3 -> Exit/ Logout
       =======================================    
        """)

        choice = input("Enter your choice : ")
        match choice:
            case "1":
                self.display_candidate_per_position()

            case "2":
                self.display_result_per_position()

            case "3":
                self.exit()

    def display_candidate_per_position(self):
        self.display_position()
        option = input("Enter your preferred option : ")

        match option:
            case "1":
                self.vote_for_each_position("president")

            case "2":
                self.vote_for_each_position("vice-President")

            case "3":
                self.vote_for_each_position("governor")

            case "4":
                self.vote_for_each_position("senator")

            case "5":
                self.display_election_menu()

            case _:
                print("Invalid Option")
                self.display_candidate_per_position()

    def display_result_per_position(self):
        self.display_position()

        option = input("Enter your preferred option : ")
        match option:
            case "1":
                self.show_vote_count_per_position("president")

            case "2":
                self.show_vote_count_per_position("vice-president")

            case "3":
                self.show_vote_count_per_position("governor")

            case "4":
                self.show_vote_count_per_position("senator")

            case "5":
                self.display_election_menu()

            case _:
                print("Invalid option")
                self.display_result_per_position()

    def show_vote_count_per_position(self, position):
        self.election_category = position
        self.display_result()

        option = input("Enter 1 for previous menu or 0 for main menu : ")
        if option == "1":
            self.display_result_per_position()
        elif option == "0":
            self.display_election_menu()

        else:
            print("Invalid option")
            self.display_result_per_position()

    def vote_for_each_position(self, position):

        self.election_category = position
        self.display_candidates()
        option = input("Enter your 1 to cast vote or 0 to return to previous menu : ")
        if option == "1":
            self.cast_vote()
        elif option == "0":
            self.display_candidate_per_position()
        else:
            print("Invalid option")
            self.display_election_menu()

    def cast_vote(self):

        candidate_id = input("Enter candidate id : ")
        try:

            if self.logged_in_voter.has_voted_for_positions(self.election_category):
                raise Exception("Already voted for this category")

            candidate = self.registration.find_candidate_by_id(candidate_id)

            candidate.add_vote()
            self.logged_in_voter.get_voted_positions().add(self.election_category)
            print("Vote casted successfully")

        except ValueError as err:
            print(err)

        except Exception as err:
            print(err)

        finally:
            self.display_candidate_per_position()

    def display_candidates(self):
        candidates = self.registration.get_candidates()
        try:
            if len(candidates) == 0:
                print("There is no registered candidate")

            else:
                print("Candidate ID\t Candidate Name    \t Candidate Position :")
                candidate_found = False
                for candidate in candidates:
                    if self.election_category == candidate.get_position():
                        candidate.display_candidate()
                        candidate_found = True

                if not candidate_found:
                    print("There is no candidate for this category")
                    self.display_candidate_per_position()

        except Exception as err:
            print(err)

    def display_result(self):
        candidates = self.registration.get_candidates()
        try:
            if len(candidates) == 0:
                print("There is no registered candidate")

            else:
                print("Candidate ID\t Candidate Name    \t Candidate Position \t Candidate Vote")
                candidate_found = False
                for candidate in candidates:
                    if self.election_category == candidate.get_position():
                        print(
                            f"{candidate.get_id_number():^10} {candidate.get_name():^25}  {candidate.get_position():>13} {candidate.get_vote_count():>14}")
                        candidate_found = True

                if not candidate_found:
                    print("There is no candidate for this category")
                    self.display_result_per_position()

        except Exception as err:
            print(err)

    def display_position(self):

        print("""
                Positions
       ===========================
       1 -> President Position
       2 -> Vice President Position
       3 -> Governor Position
       4 -> Senator Position
       5 -> Main Menu
      =============================
       """)

    def exit(self):
        self.logout()
        sys.exit("Thank you for your Vote")

    def logout(self):

        self.logged_in_voter = None
        print("==============================================")
        print("Logout successful")
        print("==============================================")


election = ElectionBody("election")
election.display_registration_menu()
