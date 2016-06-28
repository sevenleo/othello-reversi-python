from models.move import Move

class Core2Player:
  def __init__(self, color):
    self.color = color

  def name(self):
    return "Core2"

  
  def play(self, board):
    
    return self.MinMaxAB(board, 5)

  
    
  def MinMaxAB(self, board, maxdeep, eval_fn = None):
    bestValue, bestMove = None, None  

    for move in  board.valid_moves(self.color):
      boardCloned = board.get_clone()
      boardCloned.play(move, self.color)
            
      if bestValue is not None:
        opp_beta = -1 * bestValue
      else:
        opp_beta = None
    
      val = -1 * self.alphabeta(boardCloned, maxdeep, None, opp_beta, eval_fn)
      
      if bestValue is None or val > bestValue:
        (bestValue, bestMove) = (val, move)

    return bestMove
    
    
    
    
  def alphabeta(self, board, maxdeep, alpha, beta, eval_fn = None):
    '''alpha = None => -inf
    beta = None => +inf'''
    
    if alpha == None:
      alpha= -999999
      
    if beta == None:
      beta= 999999
    
    if maxdeep == 0: 
      return 1
  
    for move in  board.valid_moves(self.color):
      boardCloned = board.get_clone()
      boardCloned.play(move, self.color)

      if beta is not None:
        opp_alpha = -1 * beta
      else:
        opp_alpha = None
      if alpha is not None:
        opp_beta = -1 * alpha
      else:
        opp_beta = None
        
      val = -1 * self.alphabeta(boardCloned, maxdeep-1, opp_alpha, opp_beta, eval_fn)

      if alpha is None or val > alpha:
          alpha = val
   
      if (alpha is not None) and (beta is not None) and alpha >= beta:
        return beta

    return alpha  
