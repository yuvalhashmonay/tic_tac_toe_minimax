import random

class Game:
    def __init__(self, game_series):
        self.available_mark = '_'
        self.board = [[self.available_mark, self.available_mark, self.available_mark] for _ in range(3)]
        self.game_series = game_series
        self.player1 = game_series.player1
        self.player2 = game_series.player2
        self.players = [self.player2, self.player1]
        self.players_index = random.randint(0,1)
        self.current_player = self.players[self.players_index]
        self.square_input_instructions = "To place your mark in a square, enter the number of row followed by the number of column. examples of possible input: 01, 02, 21, 00..."
        self.turns_played = 0




    def __switch_current_player(self):
        self.players_index = not self.players_index
        self.current_player = self.players[self.players_index]


    def print_turn_info(self):
        print(f"\n\t***  {self.current_player.name} ({self.current_player.mark}) Turn ***")
        self.print_board()

    def execute_turn(self):
        self.print_turn_info()
        row, column = self.current_player.choose_square(self)
        self.board[row][column] = self.current_player.mark


    def run(self):

        self.print_instructions()
        while True:
            self.execute_turn()
            self.turns_played += 1
            if self.is_over():
                self.print_board()
                break
            self.__switch_current_player()



    def player_won(self, board, player, do_prints=True):

        def completed_row_or_column():
            for i in range(3):
                if board[i][i] != self.available_mark: # in this loop, self.board[i][i] is always the shared square between a row and a column.
                    if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
                        return True
            return False

        def completed_diagonal():
            if board[1][1] != self.available_mark:  # the center square of the board is shared by the two possible diagonals.
                if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
                    return True
            return False

        if completed_row_or_column() or completed_diagonal():
            if do_prints:
                print(f"\n!!!!!!!!!\t{player.mark} wins\t!!!!!!!!!")
            self.winner = player
            return True
        return False

    def ended_in_tie(self, board, do_prints=True):

        """"temporary function, it doesn't check if a game is obligated to end in tie when the board is still not completely full."""
        for row in board:
            if self.available_mark in row:
                return False
        if do_prints:
            print(f"- - - - - - - - -\tGAME TIED\t- - - - - - - - -")
        self.winner = None
        return True


    def is_over(self):
        return self.player_won(self.board, self.current_player) or self.ended_in_tie(self.board)


    def print_instructions(self):
        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§\tINSTRUCTIONS START\t§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")
        print("To place your mark in a square, enter the number of row followed by the number of column. For example, putting an X at input '01' will give us:")
        print("     0   1   2\n    ___ ___ ___\n0  |___|_X_|___|\n1  |___|___|___|\n2  |___|___|___|\n\n\n")
        print("§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§\tINSTRUCTIONS END\t§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§")



    def square_is_available(self, row, column):
        return self.board[row][column] == self.available_mark


    def square_input_format_is_correct(self, square_input):
        return len(square_input) == 2 and square_input[0] in '012' and square_input[1] in '012'



    def print_board(self):
        print("     0   1   2\n    ___ ___ ___")
        for i, line in enumerate(self.board):
            print(f"{i}  |_{line[0]}_|_{line[1]}_|_{line[2]}_|")