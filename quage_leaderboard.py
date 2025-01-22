import random

class QuageLeaderboard:
    def __init__(self, options):
        self.options = options
        self.scores = {}

    def roll_and_score(self, player):
        dice_roll = random.randint(1, 6)
        self.scores[player] = dice_roll
        decision = self.options[dice_roll - 1]
        return dice_roll, decision

    def show_leaderboard(self):
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores

# Example usage
options = ["Option A", "Option B", "Option C", "Option D", "Option E", "Option F"]
leaderboard = QuageLeaderboard(options)

# Players roll the dice
leaderboard.roll_and_score("Player1")
leaderboard.roll_and_score("Player2")
leaderboard.roll_and_score("Player3")

# Show leaderboard
print("Leaderboard:")
for player, score in leaderboard.show_leaderboard():
    print(f"{player}: {score}")
