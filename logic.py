class VotingSystem:
    def __init__(self):
        self.candidates = {1: "Cameron", 2: "Allison", 3: "Diego"}
        self.vote_count = {1: 0, 2: 0, 3: 0}
        self.candidates_name = set(self.candidates.values())

    def is_valid_candidate(self, candidate_name):
        return candidate_name in self.candidates_name

    def vote_for_candidate(self, candidate):
        if candidate in self.candidates:
            self.vote_count[candidate] += 1

    def get_candidates(self):
        return self.candidates

    def get_vote_count(self):
        return self.vote_count

    def get_total_votes(self):
        return sum(self.vote_count.values())
