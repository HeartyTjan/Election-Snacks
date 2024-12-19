package electionApp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class VoterTest {

    @Test
    public void testCastVote_increaseTheVoteCount_ofSpecifiedCandidates() {
        Registration reg = new Registration();
        Voter voter = reg.registerVoter("Ahmaed tobiloba","password");
        Candidate candidate = reg.registerCandidate("Tijani Olayinka","President");
        voter.castVote(candidate.getID());
        assertEquals(1, candidate.getVoteCount());
    }
    @Test
    public void testCastVoteThrowExceptionWhenCandidateID_isIncorrect() {
        Registration reg = new Registration();
        Voter voter = reg.registerVoter("Ahmaed tobiloba","password");
        Candidate candidate = reg.registerCandidate("Tijani Olayinka","President");
        assertThrows(IllegalArgumentException.class, () -> voter.castVote("245"));
    }
}
