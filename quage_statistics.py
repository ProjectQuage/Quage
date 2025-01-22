import random

class QuageStatistics:
    def __init__(self, options):
        self.options = options
        self.rolls = []
        self.decisions = {option: 0 for option in options}

    def roll_and_decide(self):
        dice_roll = random.randint(1, 6)
        decision = self.options[dice_roll - 1]
        self.rolls.append(dice_roll)
        self.decisions[decision] += 1
        return dice_roll, decision

    def show_statistics(self):
        return self.decisions

# Example usage
options = ["Option A", "Option B", "Option C", "Option D", "Option E", "Option F"]
statistics = QuageStatistics(options)

# Players roll the dice
for _ in range(100):
    statistics.roll_and_decide()

# Show statistics
print("Dice Roll Statistics:")
for option, count in statistics.show_statistics().items():
    print(f"{option}: {count} times selected")
