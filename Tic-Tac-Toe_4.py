# -*- coding: utf-8 -*-

# Import libraries
import numpy as np
from copy import deepcopy
import time

def execution_time(function):
  """
  Decorator for calculation of minimax computing time.

  Parameters
  ----------
  fonction : function

  Returns
  -------
  function
  """
  def inner(*param, **param2):
    """
    Determine execution time of the function

    Returns
    -------
    Time execution.
    """  
    t = time.perf_counter()
    function(*param, **param2)
    print("Time execution:", time.perf_counter()-t,"seconds")
    return function(*param, **param2)
  return inner



# I- Board definition
class Board:
  """
  Class representing the board game by a grid (2D numpy array).
  """

  def __init__(self,n=12):
    """
    Init method for the Board class.

    Parameters
    ----------
    n : int
        grid length
    """
    self.grid = np.full((n, n), "_", dtype=str)

  def __str__(self):
    """
    Display the board.

    Returns
    -------
    string
          grid description.
    """
    grid_string = "   "
    for k in range(1,len(self.grid)+1):
        grid_string += f"  {k} " if k < 10 else f" {k} "
    for i,k in zip(range(len(self.grid)), range(1,len(self.grid)+1)):
      grid_string += f"\n{k}  |" if k<10 else f"\n{k} |"
      for j in range(len(self.grid)):
        grid_string += f" {self.grid[i,j]} |"
      grid_string += "\n"
    return grid_string

  def actions(self):
    """
    List of all possible actions on the current board.

    Returns
    -------
    list
        list of coordinates of all possible actions.
    """
    list_actions = list()
    for i in range(len(self.grid)):
      for j in range(len(self.grid[i])):
        if self.grid[i,j] == "_":
          list_actions.append([i,j])
    return list_actions

  def place_marker(self, coord, player):
    """
    Place a marker on the grid board.

    Parameters
    ----------
    coord : list
          Coordinates of the marker.
    player : Player
          The player.
    """
    self.grid[coord[0],coord[1]] = player.val
    print(f"[{coord[0]+1},{coord[1]+1}]","\n")

  def board_limitations(self, case_number=3):
    """
    Sets the coordinates of a new grid that will be used by the minimax algorithm.
    The objective is to reduce the tree search by width.
    In fact, we made the hypothesis that a player has no interest to place a marker
    at more than 3/4 cases from the cases already placed.

    Parameters
    ----------
    case_number : int
        Length of  of additional cells to be added around  to narrow the basic grid

    Returns
    -------
    min_column : int
        représente le minimum de la colonne de tous les jetons 
    min_raw : int 
        représente le minimum de la ligne de tous les jetons
    max_column : int 
        représente le maximum de la colonne de tous les jetons
    max_raw : int 
        represent the max number  le maximum de la ligne de tous les jetons
    """
    min_column=100
    min_raw=100
    max_column=-1
    max_raw=-1
    
    for i in range (12):
        for j in range (12):
            if self.grid[i,j]!="_":
                if(i<min_raw):
                    min_raw=i
                if(j<min_column):
                    min_column=j
                if i>max_raw:
                    max_raw=i
                if j>max_column:
                    max_column=j
    if min_column<case_number:
        min_column=0
    else:
        min_column-=case_number
        
    if min_raw<case_number:
        min_raw=0
    else:
        min_raw-=case_number
    if max_column>11-case_number:
        max_column=11
    else:
        max_column+=case_number
    if max_raw>11-case_number:
        max_raw=11
    else:
        max_raw+=case_number
    return min_column,min_raw,max_column,max_raw
 


# II- Game functions
class Tic_tac_toe_4:
  """
  Class representing the tic-tac-toe 4 game.
  """
  def __init__(self, player1, player2):
    """
    Init method for the Tic_tac_toe_4 game class.

    Parameters
    ----------
    player1 : Player
        The first player.
    player2 : Player
        The second player.
    """
    self.player1 = player1
    self.player2 = player2
  
  def winning_move(self, player):
    """
    Indicate weather the player has won.

    Parameters
    ----------
    player : Player
        A player playing the game.

    Returns
    -------
    bool
        True if the player won.
    """
    column = 12
    raw = 12
    # Horizontal
    for c in range(column-3):
    	for r in range(raw):
    		if self.board.grid[r,c] == player and self.board.grid[r,c+1] == player and self.board.grid[r,c+2] == player and self.board.grid[r,c+3] == player:
    			return True
	  # Vertical 
    for c in range(column):
    	for r in range(raw-3):
    		if self.board.grid[r,c] == player and self.board.grid[r+1,c] == player and self.board.grid[r+2,c] == player and self.board.grid[r+3,c] == player:
    			return True          

    # Diagonals
    for c in range(column-3):
        for r in range(raw-3):
            if self.board.grid[r,c] == player and self.board.grid[r+1,c+1] == player and self.board.grid[r+2,c+2] == player and self.board.grid[r+3,c+3] == player:
                return True
    for c in range(column-3):
        for r in range(3, raw):
            if self.board.grid[r,c] == player and self.board.grid[r-1,c+1] == player and self.board.grid[r-2,c+2] == player and self.board.grid[r-3,c+3] == player:
                return True   
    return False

  def result(self):
    """
    Indicate the game state.

    Returns
    -------
    bool or Player
        The winner or a boolean value if there is a draw or it's not an ending/terminal state.
    """
    if self.winning_move(self.player1.val):
      return self.player1
    if self.winning_move(self.player2.val):
      return self.player2
    for i in self.board.grid:
      for j in i:
        if j == "_":
          return False
    return True

  def game(self):
    """
    Represent the game.
    """
    self.board = Board()
    current_player = self.player1
    if isinstance(current_player,AI):
      self.board.place_marker([5,5], current_player)
      current_player = self.player2
    while self.result() == False:
      print("AI" if isinstance(current_player,AI) else "human", f":[{current_player.val}]", "Turn")
      print(self.board)
      # We make the player play.
      if current_player == self.player1:
        self.board.place_marker(self.player1.play(self.board), self.player1)
        current_player = self.player2
      else:
        self.board.place_marker(self.player2.play(self.board), self.player2)
        current_player = self.player1

    print("End of the game: ")
    print(self.board)
    res = self.result()
    if res == True:
      print("Draw")
    else:
      print(f"{res.name} won")



# III- Player functions
class Player:
  """
  Represent a human player
  """
  def __init__(self,val,name = "Player"):
    """
    Init method for the Player class.

    Parameters
    ----------
    val : string
        Symbol that will represent the player on the grid.
    name : string
        Player name.
    """
    self.name = name
    self.val = val

  def play(self,board):
    """
    Make the player play.

    Parameters
    ----------
    board : Boad
        The board game.

    Returns
    -------
    list
        Coordinates chosen by the player.
    """
    coord = list()
    index = 0
    while coord not in board.actions():
      if index > 0:
        print("Input values are incorrect")
      try:
        j = eval(input("Enter the column number:"))-1
        i = eval(input("Enter the raw number:"))-1
      except ValueError:
        print("You didn't type a number")
        i=-1
        j=-1
      except:
        print("Error, try again")
        i=-1
        j=-1
      coord = [i,j]
      index +=1
    return coord

class AI(Player):
  """
  Represent an AI player.
  """
  def __init__(self,val,method,name = "AI"):
    """
    Init method for the AI class.

    Parameters
    ----------
    val : string
        Symbol that will represent the player on the grid.
    method : function
        Method to use for AI (Minimax,alpha-beta pruning)
    name : string
        Player name.
    """
    Player.__init__(self,name,val)
    self.val = val
    self.method = method(self.val)
  
  @execution_time
  def play(self, board):
    """
    Make the AI player play.

    Parameters
    ----------
    board : Boad
        The board game.

    Returns
    -------
    list
        Coordinates chosen by the AI algorithm.
    """
    self.method.__init__(self.val)
    coord_new_board = board.board_limitations(2) # We compute the new board
    # coord_new_board contains the following values:
    # [minColumn, minRaw, maxColumn, maxRaw]
    # We check if it's necessary to create this new board (maybe the new coordinates corresponds to the current board
    # so there is no modification to do)
    if coord_new_board[0] == 0 and coord_new_board[1] == 0 and coord_new_board[2] == 11 and coord_new_board[3] == 11:
      return self.method.minimax_decision(deepcopy(board.grid))
    else:
      new_board=deepcopy(board.grid[coord_new_board[1]:coord_new_board[3]+1,
                                            coord_new_board[0]:coord_new_board[2]+1])
      decision = self.method.minimax_decision(new_board)
      return [decision[0]+coord_new_board[1],decision[1]+coord_new_board[0]]



# IV- AI methods
class alpha_beta:
  """
  Implement a variant of alpha-beta pruning algorithm
  """
  def __init__(self,player):
    """
    Init method for the alpha_beta class.

    Parameters
    ----------
    player : Player
        Current AI player.
    """
    self.player = player
    self.opponent = "X" if player == "O" else "O"

  def actions(self,s):
    """
    List of possible actions.

    Parameters
      ----------
      s : numpy.ndarray
        Represent the grid of the game.
    Returns
    -------
    list
        list of coordinates of all possible actions.
    """
    list_actions = list()
    for i in range(s.shape[0]):
      for j in range(s.shape[1]):
        if s[i,j] == "_":
          list_actions.append([i,j])
    return list_actions

  def result(self,s,a, current_player):
    """
    Place a marker on the grid board.

    Parameters
    ----------
    s : numpy.ndarray
        Represent the grid of the game.
    a : liste
        Coordinates of the marker to place.  
    current_player : Player
        Current player.

    Returns
    -------
    numpy.ndarray
        The modified grid
    """
    state = deepcopy(s)
    state[a[0],a[1]] = current_player
    return state

  def winning_move(self, grid, player):
    """
    Indicate weather the player has won.

    Parameters
    ----------
    player : Player
        A player playing the game.

    Returns
    -------
    bool
        True if the player won.
    """
    column = grid.shape[1]
    raw = grid.shape[0]
    # Horizontal
    for c in range(column-3):
    	for r in range(raw):
    		if grid[r,c] == player and grid[r,c+1] == player and grid[r,c+2] == player and grid[r,c+3] == player:
    			return True
	  # Vertical 
    for c in range(column):
    	for r in range(raw-3):
    		if grid[r,c] == player and grid[r+1,c] == player and grid[r+2,c] == player and grid[r+3,c] == player:
    			return True          

    # Diagonals
    for c in range(column-3):
        for r in range(raw-3):
            if grid[r,c] == player and grid[r+1,c+1] == player and grid[r+2,c+2] == player and grid[r+3,c+3] == player:
                return True
    for c in range(column-3):
        for r in range(3, raw):
            if grid[r,c] == player and grid[r-1,c+1] == player and grid[r-2,c+2] == player and grid[r-3,c+3] == player:
                return True   
    return False

  def terminal_test(self,s):
    """
    Indicate the game state.

    Returns
    -------
    bool or Player
        The winner or a boolean value if there is a draw or it's not an ending/terminal state.
    """
    if self.winning_move(s,self.player) or self.winning_move(s,self.opponent):
      return True
    for i in range(s.shape[0]):
      for j in range(s.shape[1]):
        if s[i,j] == "_":
          return False
    return True

  def utility(self,s):
    """
    Return the heuristic value of the input terminal state.

    Parameters
    ----------
    s : numpy.ndarray
        Represent the grid of the game.

    Returns
    -------
    int
        Heurisitic value.

    """
    quadruplets = []
    raw = s.shape[0]-1
    column = s.shape[1]-1
    # Storage of all quadruplets of the grid 
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            # Vertical
            if (i+3<=raw):
                q = ([s[i,j],s[i+1,j],s[i+2,j],s[i+3,j]],0)
                quadruplets.append(q)
        
            # Horizontal    
            if (j+3<=column):
                q = ([s[i,j],s[i,j+1],s[i,j+2],s[i,j+3]],0)
                quadruplets.append(q)
        
            # Diagonal
            if (i+3<=raw and j+3<=column):
                q = ([s[i,j],s[i+1,j+1],s[i+2,j+2],s[i+3,j+3]],1)
                quadruplets.append(q)
                
            if (i-3>=0 and j+3<=column):
                q = ([s[i,j],s[i-1,j+1],s[i-2,j+2],s[i-3,j+3]],1)
                quadruplets.append(q)
    
    # Computation of the total score 
    score = 0
    for q in quadruplets:
       PlayerMarkerNumber = q[0].count(self.player)
       OpponentMarkerNumber = q[0].count(self.opponent)
       EmptyCaseNumber = q[0].count("_")
       
       if Player in q[0] is True:
           score+=0
       if EmptyCaseNumber == 4:
           score+=0
       if PlayerMarkerNumber > 0 and OpponentMarkerNumber == 0:
           if PlayerMarkerNumber == 1:
               score+=10 if q[1] == 1 else 5
           if PlayerMarkerNumber == 2:
               score+=120 if q[1] == 1 else 60
           if PlayerMarkerNumber == 3:
               score+=500 if q[1] == 1 else 250
           if PlayerMarkerNumber == 4:
               score+=100000 if q[1] == 1 else 100000
       if PlayerMarkerNumber == 0 and OpponentMarkerNumber > 0:
           if OpponentMarkerNumber == 1:
               score-=2 if q[1] == 1 else 1
           if OpponentMarkerNumber == 2:
               score-=20 if q[1] == 1 else 10
           if OpponentMarkerNumber == 3:
               score-=2000 if q[1] == 1 else 800
           if OpponentMarkerNumber == 4:
               score-=15000 if q[1] == 1 else 7000  
    return score
  
  def minimax_decision(self,state):
    """
    Best coordinates calculated by the AI agent.

    Parameters
    ----------
    state : numpy.ndarray
        Represent the grid of the game.
    Returns
    -------
    list
        Predicted coordinate.
    """
    depth = 0
    child = self.max_value(state, -np.inf,np.inf, depth+1)
    return child[0]

  def max_value(self,state,alpha,beta, depth):
    """
    Simulate the AI player.

    Parameters
    ----------
    state : numpy.ndarray
        Represent the grid of the game.
    alpha : int
        alpha parameter.
    beta : int
        beta parameter.
    depth : int
        Number of moves the AI will simulate.
    Returns
    -------
    tuple
        Best coordinates chosen for the AI player and the associated heuristic.
    """
    if self.terminal_test(state) or depth == 3:
      return (None,self.utility(state))
    max_child = None
    max_utility = -np.inf
    for child in self.actions(state):
      utility = self.min_value(self.result(state,child, self.player),alpha,beta, depth+1)[1]
      if utility > max_utility:
        max_child = child
        max_utility = utility
      if max_utility > alpha:
        alpha = max_utility
      if max_utility >= beta:
        break
    return (max_child, max_utility)

  def min_value(self,state,alpha,beta, depth):
    """
    Simulate the opponent player.

    Parameters
    ----------
    state : numpy.ndarray
        Represent the grid of the game.
    alpha : int
        alpha parameter.
    beta : int
        beta parameter.
    depth : int
        Number of moves the AI will simulate.
    Returns
    -------
    tuple
        Best coordinates chosen for the opponent player and the associated heuristic.
    """
    if self.terminal_test(state) or depth == 3:
      return (None,self.utility(state))
    min_child = None
    min_utility = np.inf
    for child in self.actions(state):
      utility = self.max_value(self.result(state,child, self.opponent),alpha,beta, depth+1)[1]
      if utility < min_utility:
        min_child = child
        min_utility = utility
      if min_utility <= alpha:
        break
      if min_utility < beta:
        beta = min_utility
    return (min_child, min_utility)



## V- Play
def main():
  """
    Main function for the Tic-tac-toe 4
  """
  print("-----------------------Tic Tac Toe 4-----------------------")
  play_again = True
  game_number = 1
  while play_again:
    print(f"\n                       Game n°{game_number}                       \n")
    result = input("First to begin? (y/n) > ")
    if result.lower() == "y":
      j1 = Player("X")
      j2 = AI("O",alpha_beta)
    else:
      j1 = AI("X",alpha_beta)
      j2 = Player("O")

    m = Tic_tac_toe_4(j1,j2)
    m.game()

    play_again = True if input("Play again? (y/n) > ").lower() == "y" else False
    game_number += 1

if __name__ == "__main__":
    main()