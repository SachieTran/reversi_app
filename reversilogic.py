# reversilogic.py
#
# Created by: Tran Tran
#
#
# This program includes the game logic component allowing two players play the
# Game of Reversi, store and maintain the current state of the game.

from ezarrays import Array2D

# Values representing the color of the chips on the board.
EMPTY = 0
BLACK = 1
WHITE = 2

class ReversiGameLogic :
  
  # Creates an instance of Reversi game logic with the board correctly
  # initialized and the current player set to black.
  def __init__(self) :
     # Use a 2-D array to represent the board.
    self._gameBoard = Array2D(8, 8)
    self._gameBoard.clear(EMPTY)
    
     # Set the initial configuration of the board.
    self._gameBoard[4,3] = BLACK
    self._gameBoard[3,4] = BLACK
    self._gameBoard[3,3] = WHITE
    self._gameBoard[4,4] = WHITE

     # Maintain the number of the current player.
    self._currentPlayer = BLACK
    
     # Keep track of the number of each players chips.
    self._numBlackChips = 2
    self._numWhiteChips = 2
    
     # A flag that is set when the game is over. That is, when there are
     # no empty squares on the board or neither player can make a move.
    self._gameOver = False
    
  # Returns a boolean indicating whether the game is over.
  def isOver(self) :
    return self._gameOver
    
  # Returns the player number of the current player.
  def whoseTurn(self) :
    return self._currentPlayer
    
  # Returns the number of chips on the board for the given player.
  def numChips(self, player) :
    if player == BLACK :
      return self._numBlackChips
    else :
      return self._numWhiteChips
  
  # Returns the number of open squares on the board.
  def numOpenSquares(self) :
    return (64 - self._numBlackChips - self._numWhiteChips)
    
  # Returns the player number of the winner or 0 if it's a draw.
  def getWinner( self ):
    if self.isOver() == True :
      if self._numBlackChips > self._numWhiteChips :
        return 1
      elif self._numBlackChips > self._numWhiteChips :
        return 2
      else :
        return 0
    else :
      return "The returned value is undefined"
      
  # Returns the player number whose chip occupies the given square.
  def occupiedBy(self, row, col):
    if self._gameBoard[row, col] == BLACK :
      return 1
    elif self._gameBoard[row, col] == WHITE :
      return 2
    else :
      return 0
      
  ## ADD THE REMAINING METHODS HERE.
  
  # Returns a Boolean indicating if the current player can place their chip 
  # in the square at position (row, col ).
  def isLegalMove(self, row, col) :
    while row >= 0 and col >= 0 and row < 8 and col < 8 :
      if self._gameBoard[row, col] != EMPTY :
        return False
      else :        
        if self._isALineOfAttack(row, col, 0, 1) or \
           self._isALineOfAttack(row, col, 0, -1) or\
           self._isALineOfAttack(row, col, 1, 0) or\
           self._isALineOfAttack(row, col, 1, 1) or \
           self._isALineOfAttack(row, col, 1, -1) or \
           self._isALineOfAttack(row, col, -1, 0) or \
           self._isALineOfAttack(row, col, -1, 1) or \
           self._isALineOfAttack(row, col, -1, -1) :
          return True
        return False
  
  # Performs an actual move in the game.   
  def makeMove(self, row, col) :
    
    # Flip the chip of the current player. 
    if self.whoseTurn() == BLACK :
      self._gameBoard[row, col] = BLACK
      self._numBlackChips = self._numBlackChips + 1                        
    else :
      self._gameBoard[row, col] = WHITE
      self._numWhiteChips = self._numWhiteChips + 1
    
    # Flip all chips on the board based on the rules of Reversi.
    if self._isALineOfAttack(row, col, 0, 1) :       
      self._flipChips(row, col, 0, 1)
    if self._isALineOfAttack(row, col, 0, -1) :
      self._flipChips(row, col, 0, -1)
    if self._isALineOfAttack(row, col, 1, 0) :
      self._flipChips(row, col, 1, 0)
    if self._isALineOfAttack(row, col, -1, 0) :
      self._flipChips(row, col, -1, 0)
    if self._isALineOfAttack(row, col, 1, 1) :
      self._flipChips(row, col, 1, 1)
    if self._isALineOfAttack(row, col, 1, -1) :
      self._flipChips(row, col, 1, -1)
    if self._isALineOfAttack(row, col, -1, 1) :
      self._flipChips(row, col, -1, 1)
    if self._isALineOfAttack(row, col, -1, -1) :
      self._flipChips(row, col, -1, -1)   
    
    # Determine the game is over or not.  
    if self._numBlackChips + self._numWhiteChips == 64 :
      self._gameOver = True
    else :   
      if self._nextPlayerMakeMove() == False :
        if self._nextPlayerMakeMove() == False :
          self._gameOver = True
          
  # Flip all chips in the line of attack.      
  def _flipChips(self, row, col, rowInc, colInc) :
    row += rowInc
    col += colInc
    if row < 0 or row > 7 or col < 0 or col > 7 :
      return
      
     # The next cell in the line must contain the opponents chip.  
    if self.occupiedBy(row, col) == self._currentPlayer :
      return
    
     # Traverse along the line and flip the chips.
    while row >= 0 and col >= 0 and row < 8 and col < 8 :
      if self.occupiedBy(row, col) == self._currentPlayer :
        return 
      elif self.occupiedBy(row, col) == EMPTY :
        return 
      else :        
        self._gameBoard[row, col] = self._currentPlayer
        if self._currentPlayer == BLACK :
          self._numBlackChips = self._numBlackChips + 1  
          self._numWhiteChips = self._numWhiteChips - 1
        else :
          self._numBlackChips = self._numBlackChips - 1  
          self._numWhiteChips = self._numWhiteChips + 1          
        row += rowInc
        col += colInc
        
    return
  
  # Return a Boolean determines whether the next player can make a move.
  def _nextPlayerMakeMove(self) :
    
    # Switch the player.
    if self._currentPlayer == BLACK :
      self._currentPlayer = WHITE
    else :
      self._currentPlayer = BLACK 
      
    # Determines whether the next player can make a move.  
    for i in range(8) :
      for j in range(8) :
        if self.isLegalMove(i, j) == True :
          return True
    return False
        
   # Helper method that returns a Boolean indicating if there is a line of
   # attack from cell (row, col) in the direction offset given by rowInc
   # and colInc. The direction offsets should be, 0, 1, or -1.
  def _isALineOfAttack(self, row, col, rowInc, colInc) :
    
  
  
  
     # Advance to the adjacent cell, which must be on the board.
    row += rowInc
    col += colInc
    if row < 0 or row > 7 or col < 0 or col > 7 :
      return False
      
     # The next cell in the line must contain the opponents chip.  
    if self.occupiedBy(row, col) == self._currentPlayer :
      return False
    
     # Traverse along the line and determine if it's a line of attack.
    while row >= 0 and col >= 0 and row < 8 and col < 8 :
      if self.occupiedBy(row, col) == self._currentPlayer :
        return True
      elif self.occupiedBy(row, col) == EMPTY :
        return False
      else :
        row += rowInc
        col += colInc
        
    return False
