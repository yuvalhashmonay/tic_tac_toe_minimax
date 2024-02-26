from game_file import Game
from game_series_file import GameSeries




def get_number_of_players_input():
    while True:
        number_of_players = input("Enter number of players: ").strip()
        if number_of_players == '1' or number_of_players == '2':
            return int(number_of_players)
        print("Please choose either 1 or 2.")





def main():


    previous_number_of_players = 666  # Arbitrary number to make the statement in the first iteration False and thus create a new game series
    while True:  # main program loop
        number_of_players = get_number_of_players_input()
        if number_of_players != previous_number_of_players:
            game_series = GameSeries(number_of_players)
        game = Game(game_series)
        game.run()
        game_series.add_game_results(game)
        game_series.print_score()
        previous_number_of_players = number_of_players


if __name__ == "__main__":
    main()

