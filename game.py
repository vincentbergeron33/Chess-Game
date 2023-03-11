class Game(Piece, Board, Player):

    def set_game(self):
        input_player_name()
        set_board()


    def run_game(self):
        while checkmate() is not True or draw() is not True:
            set_player_turn()
            Print_board()
            piece_to_play = choose_piece()
            print_valid_moves(piece_to_play)
            move_to_play = choose_move()
            set_move(move_to_play)
            check()
        
        print_checkmate()




