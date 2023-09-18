# Define the base class Player
class Player:
    def play(self):
        print("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(Player):
    def play(self):
        print('The batsman is batting.')

# Define the derived class Bowler
class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler Classes
batsman = Batsman()
bowler = Bowler()
# Call the play() method for ech other
batsman.play()
bowler.play()
