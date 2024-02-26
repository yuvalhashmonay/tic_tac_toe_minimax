from player_file import HumanPlayer, RobotPlayer




class GameSeries:

    def __init__(self, number_of_players):
        self.player1 = HumanPlayer(self.get_player_name(1))
        if number_of_players == 2:
            self.player2 = HumanPlayer(self.get_player_name(2), number=2)
        else:
            self.player2 = RobotPlayer("Computer", number=2)
        self.total_number_of_games = 0
        self.ties = 0

    def get_player_name(self, player_number):
        min_name_length = 2
        max_name_length = 15
        while True:
            name = input(f"Enter name for player {player_number}: ")
            if min_name_length <= len(name) <= max_name_length:
                return name
            print(f"Name length has to be {min_name_length}-{max_name_length} characters long.")



    def add_game_results(self, game):
        if game.winner:
            game.winner.wins += 1
        else:
            self.ties += 1
        self.total_number_of_games += 1


    def print_score(self):
        print()
        print(f"{self.player1.name}\t({self.player1.mark}):\tWins = {self.player1.wins} TOTAL SCORE = {self.player1.wins*2 + self.ties}")
        print(f"{self.player2.name}\t({self.player2.mark}):\tWins = {self.player2.wins} TOTAL SCORE = {self.player2.wins*2 + self.ties}")
        print(f"Ties = {self.ties}")
        print(f"Total games = {self.total_number_of_games}\n")