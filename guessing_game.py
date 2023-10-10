class GuessingGame:
    def __init__(self, number) -> None:
        self.number = number
        self.issolved = False

    def guess(self, guess):
        if guess < self.number:
            print("low")
            self.issolved = False
        elif guess > self.number:
            print("high")
            self.issolved = False
        else:
            print("correct")
            self.issolved = True

    def solved(self):
        print(self.issolved)
        return self.issolved

game = GuessingGame(10)

game.solved() 

game.guess(5)  
game.guess(20)
game.solved()  

game.guess(10) 
game.solved()