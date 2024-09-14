class Board:
    def __init__(self):
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, types):
        try:
            if self.board[position - 1] == ' ':
                self.board[position - 1] = types
                return True
            else:
                print('位置已经被选了，请选择其他位置。')
                return False
        except:
            print('你输入的位置不存在，请重新输入。')

    def check_winner(self, types):
        if (self.board[0] == types and self.board[1] == types and self.board[2] == types) or \
                (self.board[3] == types and self.board[4] == types and self.board[5] == types) or \
                (self.board[6] == types and self.board[7] == types and self.board[8] == types) or \
                (self.board[0] == types and self.board[3] == types and self.board[6] == types) or \
                (self.board[1] == types and self.board[4] == types and self.board[7] == types) or \
                (self.board[2] == types and self.board[5] == types and self.board[8] == types) or \
                (self.board[0] == types and self.board[4] == types and self.board[8] == types) or \
                (self.board[2] == types and self.board[4] == types and self.board[6] == types):
            return True
        else:
            return False

    def check_draw(self):
        if ' ' not in self.board:
            return True
        else:
            return False


class Play:
    def __init__(self, types):
        self.types = types
        self.names = self.get_play_name()

    def get_play_name(self):
        if self.types == 'X':
            name = input("选择X的玩家，请输入你的名字：")
        else:
            name = input("选择O的玩家，请输入你的名字：")
        return name


class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Play('X')
        self.player2 = Play('O')
        self.current_player = self.player1

    def play(self):
        try:
            while True:
                position = int(input(f'{self.current_player.names},请输入位置(1-9)：'))
                if self.board.update_board(position, self.current_player.types):
                    self.board.print_board()
                    if self.board.check_winner(self.current_player.types):
                        print(self.current_player.names, 'wins!')
                        break
                    elif self.board.check_draw():
                        print("Game is a draw")
                        break
                    else:
                        if self.current_player == self.player1:
                            self.current_player = self.player2
                        else:
                            self.current_player = self.player1
        except:
            print('请输入数字1-9！')


game = Game()
game.play()
