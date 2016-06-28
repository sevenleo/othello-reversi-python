from controllers.board_controller import BoardController
from models.move                  import Move
from models.board                 import Board

player0=0
player1=0
player2=0

while (player1+player2+player0) < 10 :


  controller = BoardController()
  quemGanhou = controller.init_game()

  if (quemGanhou ==1):
    player1+=1
  elif (quemGanhou ==2):
    player2+=1
  elif (quemGanhou ==1):
    player0+=1

  print ''
  print "-----------PLACAR-TOTAL-------------"
  print 'Player1: ', controller.white_player.name(), player1
  print 'Player2: ', controller.black_player.name(), player2
  print 'Empate: ', player0