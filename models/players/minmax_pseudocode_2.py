

'''
falta atualizar o valor de alpha


def alphaBeta(self, board, rules, alpha, beta, ply, player):
        """ Implements a minimax algorithm with alpha-beta pruning. """
        if ply == 0:
            return self.positionEvaluation(board, rules, player)

        move_list = board.generateMoves(rules, player)
        for move in move_list:
            board.makeMove(move, player)
            current_eval = -self.alphaBeta(board, rules, -beta, -alpha, ply - 1, board.getOtherPlayer(player))
            board.unmakeMove(move, player)

            if current_eval >= beta:
                return beta

            if current_eval > alpha:
                alpha = current_eval

        return alpha

def rootAlphaBeta(self, board, rules, ply, player):
        """ Makes a call to the alphaBeta function. Returns the optimal move for a player at given ply. """
        best_move = None
        max_eval = float('-infinity')

        move_list = board.generateMoves(rules, player)
        for move in move_list:
            board.makeMove(move, player)
            current_eval = -self.alphaBeta(board, rules, float('-infinity'), float('infinity'), ply - 1, board.getOtherPlayer(player))
            board.unmakeMove(move, player)

            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move

        return best_move
'''
