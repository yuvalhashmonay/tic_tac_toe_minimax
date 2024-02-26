import random



class Player:

    def __init__(self, name=None, number=1):
        if name is None:
            name = "player" + str(number)
        self.name = name
        self.number = number
        self.wins = 0
        self.mark = 'X' if number == 1 else 'O'


class HumanPlayer(Player):

    def choose_square(self, game):
        return self.get_square_input(game)

    def get_square_input(self, game):

        while True:
            square_input = input("Enter number of row followed by number of column or enter the letter 's' to print the score so far:")
            if square_input.lower() == 's':
                game.game_series.print_score()
                game.print_turn_info()
                continue
            if not game.square_input_format_is_correct(square_input):
                print(game.square_input_instructions)
                continue
            row = int(square_input[0])
            column = int(square_input[1])
            if game.square_is_available(row, column):
                break
            print("The chosen square is unavailable.")
        return row, column

class RobotPlayer(Player):

    def choose_square(self, game):

        if game.turns_played == 0:  # if this is the first turn of the game
            return [random.randint(0,2), random.randint(0,2)]  # forcing the computer choose a random square if the first turn of the game is its.
        player_index = 1  # 1 is fot current player (computer) and -1 is for the other human/computer player
        if game.current_player.number == 1:
            self.players_dict = {1: game.player1, -1: game.player2}
        else:
            self.players_dict = {1: game.player2, -1: game.player1}

        player = self.players_dict[player_index]
        board = game.board
        best_score = float('-inf')  # when maximizing
        level = 1
        self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window = float('inf')
        best_square = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == game.available_mark:
                    board[i][j] = player.mark # it's ok to change the original board and just cancel the marking in this iteration because we're not continuing to the next round of the loop until all the recursion windows close.

                    if game.player_won(board, player, do_prints=False) or game.ended_in_tie(board, do_prints=False):
                        return [i, j]

                    score, number_of_levels_took_to_end_game = self.minimax(game, board, -player_index, level=level+1) # this was player_index without minus in the version that worked
                    board[i][j] = game.available_mark

                    # if score > best_score : # shouldn't this if statement be true at least once? no, because sometimes we return -infinity
                    if score > best_score or best_square is None: # shouldn't this if statement be true at least once? no, because sometimes we return -infinity
                        best_score = score
                        best_square = [i, j]  # where is the default chosen_square though?

                        if score == 1:
                            self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window = number_of_levels_took_to_end_game
                        # lowest_potentially_possible_number_of_levels_for_win = number_of_levels_took_to_end_game

                    elif score == best_score and number_of_levels_took_to_end_game < self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window:
                        best_square = [i, j]
                        if score == 1:
                            self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window = number_of_levels_took_to_end_game
        return best_square


    def minimax(self, game, board, player_index, level):

        player = self.players_dict[player_index]
        best_score = float('-inf') * player_index
        minimum_levels_took_for_player_in_current_recursion_call_to_get_current_best_score = float('inf')
        # print(f" level = {level}   self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window = {self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window}")
        # if level < self.minimum_levels_took_for_the_player_to_find_a_win_from_the_first_window: # the call count is the same even without this statement
        for i in range(3):
            for j in range(3):
                if board[i][j] == game.available_mark:
                    board[i][j] = player.mark  # it's ok to change the original board and just cancel the marking in this round because we're not continuing to the next round of the loop until all the recursion windows close.

                    if game.player_won(board, player, do_prints=False):
                        board[i][j] = game.available_mark  # erasing the change made to the board
                        return player_index, level  # we return 1 and -1 depending on the player and we also used these numbers to choose the correct player each time so we can just return the index.

                    elif game.ended_in_tie(board, do_prints=False):
                        score, number_of_levels_took_to_end_game = 0, level
                        board[i][j] = game.available_mark

                    else:
                        score, number_of_levels_took_to_end_game = self.minimax(game, board, -player_index, level=level+1)
                        board[i][j] = game.available_mark


                    if score * player_index > best_score * player_index:
                        best_score = score
                        minimum_levels_took_for_player_in_current_recursion_call_to_get_current_best_score = number_of_levels_took_to_end_game

                    elif score == best_score and number_of_levels_took_to_end_game < minimum_levels_took_for_player_in_current_recursion_call_to_get_current_best_score:
                        minimum_levels_took_for_player_in_current_recursion_call_to_get_current_best_score = number_of_levels_took_to_end_game

        return best_score, minimum_levels_took_for_player_in_current_recursion_call_to_get_current_best_score



 