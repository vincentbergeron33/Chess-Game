

@dataclass
class Game():
    board: Board
    player_white: Player
    player_black: Player
    currentPlayer: Player


    def run_game(self):
        while checkmate() is not True:
            set_player_turn()
            self.board.printboard()
            piece_to_play = choose_piece()
            print_valid_moves(piece_to_play)
            move_to_play = choose_move()
            set_move(move_to_play, piece_to_play)
            
            board.pieces[piece_to_play.location[0]][piece_to_play.location[1]] = None
            piece_to_play.location = (move_to_play[0], move_to_play[1])
            board.pieces[move_to_play[0]][move_to_play[1]]
            

            check()

        
        print_checkmate()
    
    def set_player_turn():
        if currentPlayer is player_white:
            currentPlayer = player_black
            print('It is black turn')
        else:
            currentPlayer = player_white
            print('It is white turn')





def set_up_board() -> Board:
    board = Board(pieces = [None, None, None, None, None, None])
    return board

board = set_up_board()

def set_up_players() -> Tuple[Player, Player]:
    player_white_name = input("Enter white player name:")
    player_black_name = input("Enter black player name")
    player_white =  Player(player_white_name)
    player_black = Player(player_black_name)

    return (player_white, player_black)
players = set_up_players()

game = Game(board, players[0], players[1], currentPlayer = players[1])

game.run_game()