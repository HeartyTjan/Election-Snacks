package electionApp;

import org.junit.jupiter.api.Test;

import javax.sound.midi.SoundbankResource;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class RegistrationTest {

    @Test
    public void testThatRegisterVoterAdd_newVoter() {
        Registration reg = new Registration();
        reg.registerVoter("Name one", "Password");
        assertEquals(1,reg.getNumberOfVoters());

    }

    @Test
    public void testThatRegisterCandidateAdd_newCandidate() {
        Registration reg = new Registration();
        reg.registerCandidate("Name one","President");
        assertEquals(1,reg.getNumberOfCandidates());

    }

    @Test
    public void testThatFindVoter_ByID_returnsExpectedVoter() {
        Registration reg = new Registration();
        reg.registerVoter("Name one", "Password");
        reg.registerVoter("Name two", "Password2");
        reg.registerVoter("Name three", "Password3");
        assertEquals(3,reg.getNumberOfVoters());
        Voter voter = Registration.findVoter("v13");
        assertEquals("Name three",voter.getName());
    }

    @Test
    public void testThatFindCandidate_ByID_returnsExpectedCandidate() {
        Registration reg = new Registration();
        reg.registerCandidate("Name one", "President");
        reg.registerCandidate("Name Two", "Governor");
        assertEquals(2,reg.getNumberOfCandidates());
        Candidate candidate = Registration.findCandidate("c11");
        assertEquals("President", candidate.getPosition());
    }

    @Test
    public void testFindCandidate_ByID_throwException_IDNull() {
        Registration reg = new Registration();
        reg.registerCandidate("Name one","President");
        assertThrows(NullPointerException.class,()-> Registration.findCandidate(""));
    }

    @Test
    public void testFindVoter_ByID_throwException_IDNull() {
        Registration reg = new Registration();
        assertThrows(NullPointerException.class,()-> Registration.findVoter(""));
    }
}
