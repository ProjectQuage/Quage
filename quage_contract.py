import random

class QuageContract:
    def __init__(self, options, min_stake=1):
        self.options = options  # Options for the decision
        self.min_stake = min_stake  # Minimum stake to participate in the decision
        self.stakes = {}  # Players and their stakes

    def stake(self, player, amount):
        if amount < self.min_stake:
            return "Stake is too low."
        self.stakes[player] = amount
        return f"{player} has staked {amount}."

    def roll_and_decide(self):
        if len(self.stakes) == 0:
            return "No stakes, no decision possible."
        
        dice_roll = random.randint(1, 6)
        decision = self.options[dice_roll - 1]
        return dice_roll, decision, self.stakes

# Example usage
options = ["Option A", "Option B", "Option C", "Option D", "Option E", "Option F"]
contract = QuageContract(options)

print(contract.stake("Player1", 5))
print(contract.stake("Player2", 10))
dice_roll, decision, stakes = contract.roll_and_decide()
print(f"Dice Roll: {dice_roll} - The decision: {decision}")
