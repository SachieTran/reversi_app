# reversi.py 
#
# 
#
# A text-based front end for playing the game of Reversi. This driver module
# needs a correct implementation of the ReversiGameLogic ADT.
#
# The grading version prints out the user entered moves that are extracted
# from a file using redirected standard input.
#

from reversilogic import ReversiGameLogic

PLAYERS = [None, "Black (o)", "White (x)"]
THE_CHIPS = [".", "o", "x"]

def main():
  theGame = ReversiGameLogic()
  showBoard( theGame )
  
  while not theGame.isOver() :
    player = theGame.whoseTurn()    
    row, col = getMove( player )
    if theGame.isLegalMove( row, col ) :
      theGame.makeMove( row, col )
      player = theGame.whoseTurn()
      showBoard( theGame )
    else :
      print( "\nError!! not a legal move." )    
  
  if theGame.getWinner() == 0 :
    print( "The game is a draw." )
  else :
    print( PLAYERS[theGame.getWinner()] + " is the Winner!!!" )
    
def getMove( player ):
  while True :
    print( PLAYERS[ player ] + ": select the cell for your move." )    
    temp = input("   row (1-8) => ")
    row = ord(temp[0]) - 49    
    if row < 0 or row > 7 :
      print( "Error!! invalid row number." )
    else :
      temp = input("   col (a-h) => ")
      col = ord(temp[0]) - 97
      if col < 0 or col > 7 :
        print( "Error!! invalid column letter." )
      else :
        return row, col
  
def showBoard( game ):
  blackChips = game.numChips( 1 )
  whiteChips = game.numChips( 2 )
  print( "" )
  print( "Score: Black (o): %d, White (x): %d" % (blackChips, whiteChips) )
  print( "    a  b  c  d  e  f  g  h" )
  for row in range(8) :
    print( row+1, " ", end="" )
    for col in range(8) :
      chip = game.occupiedBy( row, col )
      if chip is None :
        chip = 0
      print( " " + THE_CHIPS[chip] + " ", end="" )
    print( "" )
  print( "" )

main()
