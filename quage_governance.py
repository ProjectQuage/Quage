import random

class QuageGovernance:
    def __init__(self, options):
        self.options = options
        self.votes = {}

    def vote(self, player, option):
        if option not in self.options:
            return "Invalid option."
        self.votes[player] = option
        return f"{player} voted for {option}."

    def roll_and_decide(self):
        if len(self.votes) == 0:
            return "No votes have been cast."

        vote_counts = {option: 0 for option in self.options}
        for vote in self.votes.values():
            vote_counts[vote] += 1

        # Random decision based on the votes
        decision_roll = random.choices(self.options, weights=vote_counts.values(), k=1)
        return decision_roll[0]

# Example usage
options = ["Option A", "Option B", "Option C", "Option D"]
governance_system = QuageGovernance(options)

# Players vote
governance_system.vote("Player1", "Option A")
governance_system.vote("Player2", "Option B")
governance_system.vote("Player3", "Option A")

# Final decision based on the voting
final_decision = governance_system.roll_and_decide()
print(f"Final Decision: {final_decision}")
