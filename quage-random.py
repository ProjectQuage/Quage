import random

class QuageDice:
    def __init__(self, sides=6):
        self.sides = sides  # Default number of dice sides (6 sides)

    def roll(self):
        return random.randint(1, self.sides)

class QuageDecision:
    def __init__(self, options):
        self.options = options  # Options for the decision
        self.dice = QuageDice()  # Dice object

    def make_decision(self):
        dice_roll = self.dice.roll()
        decision = self.options[dice_roll - 1]  # -1 because Python indexes start at 0
        return dice_roll, decision

# Example usage
options = ["Option A", "Option B", "Option C", "Option D", "Option E", "Option F"]  # 6 options
decision_maker = QuageDecision(options)

dice_roll, decision = decision_maker.make_decision()
print(f"Dice roll result: {dice_roll} - The decision: {decision}")
