from models.players.human_player import HumanPlayer
#from models.players.random_player import RandomPlayer
from models.players.core1_player import Core1Player
from models.players.core2_player import Core2Player
from views.console_board_view import ConsoleBoardView
from models.board import Board

class BoardController:
  def __init__(self):
    self.board = Board(None)
    self.view  = ConsoleBoardView(self.board)

  def init_game(self):
  #  self.white_player = Core1Player(Board.WHITE)
    self.white_player = HumanPlayer(Board.WHITE)
    self.black_player = Core2Player(Board.BLACK)
  #  self.black_player = RandomPlayer(Board.BLACK)
    self.atual_player = self.black_player

    finish_game = 0

    self.view.update_view()
    

    while finish_game != 2:
      #raw_input("")
      atual_color = self.atual_player.color
      print 'Jogador: ' + atual_color +' ('+ self.atual_player.name() +')'

      if self.board.valid_moves(atual_color).__len__() > 0:
        self.board.play(self.atual_player.play(self.board.get_clone()), atual_color)
        self.view.update_view()
        finish_game = 0
      else:
        print 'Sem movimentos para o jogador: ' + atual_color
        finish_game += 1
      self.atual_player = self._opponent(self.atual_player)

    return self._end_game()


  def _end_game(self):
    score = self.board.score()
    print ''
    print'-----------------PLACAR DESTA RODADA---------------------'
    print self.white_player.name() , " = " , score[0]
    print self.black_player.name() , " = " , score[1]
    if score[0] > score[1]:
      print ""
      print 'Jogador ' + self.white_player.name() + ' Ganhou'
      return 1
    elif score[0] < score[1]:
      print ""
      print 'Jogador ' + self.black_player.name() + ' Ganhou'
      return 2
    else:
      print ""
      print 'Jogo terminou empatado'
      return 0
    print'---------------------------------------------'
    
    
  def _opponent(self, player):
    if player.color == Board.WHITE:
      return self.black_player

    return self.white_player
