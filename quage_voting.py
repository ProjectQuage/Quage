import random

class QuageVoting:
    def __init__(self, options):
        self.options = options  # Options for voting
        self.votes = []  # Votes from participants

    def vote(self, player, option):
        if option in self.options:
            self.votes.append((player, option))
            return f"{player} voted for {option}."
        else:
            return "Invalid option."

    def roll_and_decide(self):
        if len(self.votes) == 0:
            return "No votes have been cast."

        # Random decision based on the votes
        vote_roll = random.randint(1, len(self.votes))
        selected_vote = self.votes[vote_roll - 1]  # -1 due to zero-indexing
        return selected_vote

# Example usage
options = ["Option A", "Option B", "Option C", "Option D"]
voting_system = QuageVoting(options)

# Players vote
voting_system.vote("Player1", "Option A")
voting_system.vote("Player2", "Option C")
voting_system.vote("Player3", "Option B")

# Decision based on voting
selected_vote = voting_system.roll_and_decide()
print(f"Random Vote Decision: {selected_vote}")
